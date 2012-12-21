
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
        """Return a Term object against the current terminal.

        This class method uses the $TERM environment variabler to discover the
        terminal information it should use.
        """
        self = cls(terminal=bytes(os.environ['TERM'], 'UTF-8'), **kwargs)
        return self

    @property
    def input_handle(self):
        """Returns the input handle."""
        return ctickit.tickit_term_get_input_fd(self._term)

    @input_handle.setter
    def input_handle(self, fd):
        """Sets the input handle to the given file descriptor.

        Such file descriptors may be obtained via the fileno() method on
        io.IOBase subclasses.
        """
        ctickit.tickit_term_set_input_fd(self._term, fd)

    @property
    def output_handle(self):
        """Returns the output handle."""
        return ctickit.tickit_term_get_output_fd(self._term)

    @output_handle.setter
    def output_handle(self, fd):
        """Sets the output handle to the given file descriptor.

        Such file descriptors may be obtained via the fileno() method on
        io.IOBase subclasses.
        """
        ctickit.tickit_term_set_output_fd(self._term, fd)

    def set_output_buffer(self, size):
        """Sets the output buffer size."""
        ctickit.tickit_term_set_output_buffer(self._term, size)

    def flush(self):
        """Flushes the output buffer to the terminal."""
        ctickit.tickit_term_flush(self._term)

    def _wrap_handler(self, func):
        def handler(term, type, event, data):
            args = event.contents

            func(self, type, args, data)

        return tickit.TickitTermEventFn(handler)

    @property
    def on_resize(self):
        """Returns the callback for resize events."""
        return self._on_resize

    @on_resize.setter
    def on_resize(self, on_resize):
        """Sets the callback for resize events.

        The callback must expect four arguments; terminal object, event type
        (as a string), event arguments (as a TickitEvent object), and user data
        (anything, not currently usable).
        """
        if hasattr(self, '_on_resize'):
            ctickit.tickit_term_unbind_event_id(self._on_resize_id)
        self._on_resize = self._wrap_handler(on_resize)
        self._on_resize_id = ctickit.tickit_term_bind_event(
            self._term, tickit.TICKIT_EV_RESIZE, self._on_resize, None
        )

    @property
    def on_key(self):
        """Returns the callback for keyboard input events."""
        return self._on_key

    @on_key.setter
    def on_key(self, on_key):
        """Sets the callback for keyboard input events.

        The callback must expect four arguments: terminal object, event type
        (as a string), event arguments (as a TickitEvent object), and user data
        (anything, not currently usable).
        """
        if hasattr(self, '_on_key'):
            ctickit.tickit_term_unbind_event_id(self._on_key_id)
        self._on_key = self._wrap_handler(on_key)
        self._on_key_id = ctickit.tickit_term_bind_event(
            self._term, tickit.TICKIT_EV_KEY, self._on_key, None
        )

    @property
    def on_mouse(self):
        """Returns the callback for mouse input events."""
        return self._on_mouse

    @on_mouse.setter
    def on_mouse(self, on_mouse):
        """Sets the callback for mouse input events.

        The callback must expect four arguments: terminal object, event type
        (as a string), event arguments (as a TickitEvent object), and user data
        (anything, not currently usable).
        """
        if hasattr(self, '_on_mouse'):
            ctickit.tickit_term_unbind_event_id(self._on_mouse_id)
        self._on_mouse = self._wrap_handler(on_mouse)
        self._on_mouse_id = ctickit.tickit_term_bind_event(
            self._term, tickit.TICKIT_EV_MOUSE, self._on_mouse, None
        )

    def refresh_size(self):
        """Reacquires the terminal size."""
        ctickit.tickit_term_refresh_size(self._term)

    def set_size(self, lines, cols):
        """Set the terminal size to the given number of lines & columns."""
        ctickit.tickit_term_set_size(self._term, lines, cols)

    def get_size(self):
        """Returns the terminal size as a 2-tuple in (lines, columns) order."""
        lines = ctypes.c_int()
        cols  = ctypes.c_int()
        ctickit.tickit_term_get_size(
            self._term, ctypes.byref(lines), ctypes.byref(cols)
        )
        return (lines.value, cols.value)

    @property
    def lines(self):
        """Number of lines in the terminal."""
        return self.get_size()[0]

    @property
    def cols(self):
        """Number of columns in the terminal."""
        return self.get_size()[1]

    def print_(self, text):
        """Print the given string to the terminal.

        This method takes a bytes or, with UTF-8 enabled, str object and prints
        it, a la the print() function.

        Note that under Python 3.x, the underline may be omitted.
        """
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
        """Move the cursor to the absolute coordinates specified."""
        ctickit.tickit_term_goto(self._term, lines, cols)

    def move(self, down, right):
        """Move the cursor relative to its current position."""
        ctickit.tickit_term_move(self._term, down, right)

    def scrollrect(self, top, left, lines, cols, down, right):
        """Move the specified rectangle relative to its current position.

        The first four arguments specify the dimensions of the rectangle; the
        remaining two specify the new position relative to the current one.
        """
        return ctickit.tickit_term_scrollrect(
            self._term, top, left, lines, cols, down, right
        )

    def chpen(self, newpen=None, **kwargs):
        """Change the active pen's attributes according to the pen or arguments
        provided."""
        if newpen is None:
            newpen = pen.Pen(kwargs)
        ctickit.tickit_term_chpen(self._term, newpen._pen)

    def setpen(self, newpen=None, **kwargs):
        """Set the active pen to the given pen or one with the arguments
        provided."""
        if newpen is None:
            newpen = pen.Pen(kwargs)
        ctickit.tickit_term_setpen(self._term, newpen._pen)

    def clear(self):
        """Clear the terminal."""
        ctickit.tickit_term_clear(self._term)

    def erasech(self, count, move=None):
        """Erase forward by the specified number of characters.

        If move is True, the cursor is moved to the end of the erased region;
        if move is False, the cusror will remain where it is. Finally, if move
        is None, the terminal will peform whichever of these behaviors is more
        efficient and the cursor's position will be undefined.
        """
        ctickit.tickit_term_erasech(self._term, count, move)

    def setctl(self, ctl, state=True):
        """Set the requested terminal control variable to the given state."""
        ctickit.tickit_term_setctl_int(
            self._term, ctl, state
        )

    def input_push_bytes(self, seq):
        """Push the given sequence of bytes into input.

        This method may trigger keyboard or mouse input events."""
        if not isinstance(seq, (bytes, bytearray)):
            raise TypeError('not a byte sequence')
        ctickit.tickit_term_push_bytes(self._term, seq, len(seq))

    def input_readable(self):
        """Informs the terminal that the input handle may be readable.

        This method attempts to read more input and may trigger keyboard or
        mouse input events.
        """
        ctickit.tickit_term_input_readable(self._term)

    def input_wait(self):
        """Wait until input is available and process it.

        This method returns after one round of input is processed and may
        trigger keyboard or mouse input events.
        """
        ctickit.tickit_term_input_wait(self._term)

    def input_check_timeout(self):
        """Returns a number, in seconds, indicating the next timeout.

        If nothing is waiting, this function returns None. May trigger keyboard
        input events.
        """
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
