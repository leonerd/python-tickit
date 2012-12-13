
import ctypes
import io
import os
import sys

import tickit.pen as pen
from tickit.ctickit import *

class Term:
    """A representation of an interactive terminal.

    This class provides functions for interacting with a terminal in a manner
    similar to the classical 'curses' framework. It mirrors the Tickit::Term
    Perl interface to libtickit's tickit_term_* functions.

    WARNING: The event handlers here may only take three arguments due to how
    they're wrapped for Python callbacks.
    """
    def __init__(self, **kwargs):
        if 'struct' in kwargs:
            self._term = kwargs['struct']

        if 'terminal' in kwargs:
            self._term = ctickit.tickit_term_new_for_termtype(
                kwargs['terminal']
            )
        if getattr(self, '_term', None) is None:
            self._term = ctickit.tickit_term_new()

        if 'utf8' in kwargs:
            self._utf8 = kwargs['utf8']
            ctickit.tickit_term_set_utf8(self._term, self._utf8)

        if 'input_handle' in kwargs:
            fd = kwargs['input_handle']

            if isinstance(fd, io.IOBase):
                fd = fd.fileno()
            elif isinstance(fd, int):
                pass
            else:
                raise TypeError('input handle not io.IOBase subclass or fd')

            ctickit.tickit_term_set_input_fd(self._term, fd)

        if 'output_handle' in kwargs:
            fd = kwargs['output_handle']

            if isinstance(fd, io.IOBase):
                fd = fd.fileno()
            elif isinstance(fd, int):
                pass
            else:
                raise TypeError('output handle not io.IOBase subclass or fd')

        if 'writer' in kwargs:
            ctickit.tickit_set_output_func(self._term, kwargs['writer'], None)

        if 'on_resize' in kwargs:
            self.on_resize = kwargs['on_resize']

        if 'on_key' in kwargs:
            self.on_key = kwargs['on_key']

        if 'on_mouse' in kwargs:
            self.on_mouse = kwargs['on_mouse']

    def destroy(self):
        ctickit.tickit_term_destroy(self._term)
        self._term = None

    def __del__(self):
        self.destroy()

    @classmethod
    def find_for_term(cls, **kwargs):
        self = cls(terminal=bytes(os.environ['TERM'], 'UTF-8'), **kwargs)
        return self

    @classmethod
    def from_struct(cls, term):
        self = cls(struct=term)
        self._utf8 = ctickit.tickit_term_get_utf8(self._term)
        return self

    @property
    def input_handle(self):
        return ctickit.tickit_term_get_input_fd(self._term)

    @input_handle.setter
    def input_handle(self, fd):
        ctickit.tickit_term_set_input_fd(self._term, fd)

    @property
    def output_handle(self):
        return ctickit.tickit_term_get_output_fd(self._term)

    @output_handle.setter
    def output_handle(self, fd):
        ctickit.tickit_term_set_output_fd(self._term, fd)

    def set_output_buffer(self, size):
        ctickit.tickit_term_set_output_buffer(self._term, size)

    def flush(self):
        ctickit.tickit_term_flush(self._term)

    def _wrap_handler(self, func):
        def handler(term, type, event, data):
            args = event.contents

            func(self, type, args, data)

        return tickit.TickitTermEventFn(handler)

    @property
    def on_resize(self):
        return self._on_resize

    @on_resize.setter
    def on_resize(self, on_resize):
        if hasattr(self, '_on_resize'):
            ctickit.tickit_term_unbind_event_id(self._on_resize_id)
        self._on_resize = self._wrap_handler(on_resize)
        self._on_resize_id = ctickit.tickit_term_bind_event(
            self._term, tickit.TICKIT_EV_RESIZE, self._on_resize, None
        )

    @property
    def on_key(self):
        return self._on_key

    @on_key.setter
    def on_key(self, on_key):
        if hasattr(self, '_on_key'):
            ctickit.tickit_term_unbind_event_id(self._on_key_id)
        self._on_key = self._wrap_handler(on_key)
        self._on_key_id = ctickit.tickit_term_bind_event(
            self._term, tickit.TICKIT_EV_KEY, self._on_key, None
        )

    @property
    def on_mouse(self):
        return self._on_mouse

    @on_mouse.setter
    def on_mouse(self, on_mouse):
        if hasattr(self, '_on_mouse'):
            ctickit.tickit_term_unbind_event_id(self._on_mouse_id)
        self._on_mouse = self._wrap_handler(on_mouse)
        self._on_mouse_id = ctickit.tickit_term_bind_event(
            self._term, tickit.TICKIT_EV_MOUSE, self._on_mouse, None
        )

    def refresh_size(self):
        ctickit.tickit_term_refresh_size(self._term)

    def set_size(self, lines, cols):
        ctickit.tickit_term_set_size(self._term, lines, cols)

    def get_size(self):
        lines = c_int()
        cols  = c_int()
        ctickit.tickit_term_get_size(self._term, byref(lines), byref(cols))
        return (lines, cols)

    @property
    def lines(self):
        return self.get_size()[0]

    @property
    def cols(self):
        return self.get_size()[1]

    def print_(self, text):
        if isinstance(text, bytes):
            ctickit.tickit_term_print(self._term, text)
        else:
            if self._utf8 == True:
                ctickit.tickit_term_print(self._term, text.encode('UTF-8'))
            else:
                raise TypeError('Unicode output disabled')

    if sys.version_info.major >= 3:
        print = print_

    def goto(self, lines, cols):
        ctickit.tickit_term_goto(self._term, lines, cols)

    def move(self, down, right):
        ctickit.tickit_term_move(self._term, down, right)

    def scrollrect(self, top, left, lines, cols, down, right):
        return ctickit.tickit_term_scrollrect(
            self._term, top, left, lines, cols, down, right
        )

    def chpen(self, newpen=None, **kwargs):
        if newpen is None:
            newpen = pen.Pen(kwargs)
        ctickit.tickit_term_chpen(self._term, newpen._pen)

    def setpen(self, newpen=None, **kwargs):
        if newpen is None:
            newpen = pen.Pen(kwargs)
        ctickit.tickit_term_setpen(self._term, newpen._pen)

    def clear(self):
        ctickit.tickit_term_clear(self._term)

    def erasech(self, count, move):
        ctickit.tickit_term_erasech(self._term, count, move)

    def setctl(self, ctl, state=True):
        ctickit.tickit_term_setctl_int(
            self._term, ctl, state
        )

    def input_push_bytes(self, seq):
        if not isinstance(seq, (bytes, bytearray)):
            raise TypeError('not a byte sequence')
        ctickit.tickit_term_push_bytes(self._term, seq, len(seq))

    def input_readable(self):
        ctickit.tickit_term_input_readable(self._term)

    def input_wait(self):
        ctickit.tickit_term_input_wait(self._term)

    def input_check_timeout(self):
        return ctickit.tickit_term_input_check_timeout(self._term)

Terminal = Term

class TermControl:
    altscreen      = tickit.TICKIT_TERMCTL_ALTSCREEN
    cursorblink    = tickit.TICKIT_TERMCTL_CURSORBLINK
    cursorshape    = tickit.TICKIT_TERMCTL_CURSORSHAPE
    cursorvis      = tickit.TICKIT_TERMCTL_CURSORVIS
    icon_text      = tickit.TICKIT_TERMCTL_ICON_TEXT
    icontitle_text = tickit.TICKIT_TERMCTL_ICONTITLE_TEXT
    keypad_app     = tickit.TICKIT_TERMCTL_KEYPAD_APP
    mouse          = tickit.TICKIT_TERMCTL_MOUSE
    title_text     = tickit.TICKIT_TERMCTL_TITLE_TEXT

class CursorShape:
    block    = tickit.TICKIT_TERM_CURSORSHAPE_BLOCK
    left_bar = tickit.TICKIT_TERM_CURSORSHAPE_LEFT_BAR
    under    = tickit.TICKIT_TERM_CURSORSHAPE_UNDER

__all__ = ['Terminal', 'Term', 'TermControl']
