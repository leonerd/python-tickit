
import sys

from ctypes import *
from ctypes.util import find_library
import tickit._tickit as tickit

if sys.platform.startswith('linux'):
    ctickit = CDLL('libtickit.so.0')

ctickit.tickit_pen_attrname.restype = c_char_p
ctickit.tickit_pen_attrname.argtypes = (tickit.TickitPenAttr,)

ctickit.tickit_pen_lookup_attr.restype = tickit.TickitPenAttr
ctickit.tickit_pen_lookup_attr.argtypes = (c_char_p,)

ctickit.tickit_pen_bind_event.restype = c_int
ctickit.tickit_pen_bind_event.argtypes = (
    POINTER(tickit.TickitPen),
    tickit.TickitEventType,
    tickit.TickitPenEventFn,
    py_object
)

ctickit.tickit_pen_unbind_event_id.restype = None
ctickit.tickit_pen_unbind_event_id.argtypes = (
    POINTER(tickit.TickitPen),
    c_int
)

ctickit.tickit_pen_clear_attr.restype = None
ctickit.tickit_pen_clear_attr.argtypes = (
    POINTER(tickit.TickitPen),
    tickit.TickitPenAttr
)

ctickit.tickit_pen_copy.restype = None
ctickit.tickit_pen_copy.argtypes = (
    POINTER(tickit.TickitPen),
    POINTER(tickit.TickitPen),
    c_int
)

ctickit.tickit_pen_copy_attr.restype = None
ctickit.tickit_pen_copy_attr.argtypes = (
    POINTER(tickit.TickitPen),
    POINTER(tickit.TickitPen),
    tickit.TickitPenAttr
)

ctickit.tickit_pen_destroy.restype = None
ctickit.tickit_pen_destroy.argtypes = (POINTER(tickit.TickitPen),)

ctickit.tickit_pen_new.restype = POINTER(tickit.TickitPen)
ctickit.tickit_pen_new.argtypes = ()

ctickit.tickit_pen_equiv_attr.restype = c_int
ctickit.tickit_pen_equiv_attr.argtypes = (
    POINTER(tickit.TickitPen),
    POINTER(tickit.TickitPen),
    tickit.TickitPenAttr
)

ctickit.tickit_pen_get_bool_attr.restype = c_bool
ctickit.tickit_pen_get_bool_attr.argtypes = (
    POINTER(tickit.TickitPen),
    tickit.TickitPenAttr
)

ctickit.tickit_pen_set_bool_attr.restype = None
ctickit.tickit_pen_set_bool_attr.argtypes = (
    POINTER(tickit.TickitPen),
    tickit.TickitPenAttr,
    c_bool
)

ctickit.tickit_pen_get_colour_attr.restype = c_int
ctickit.tickit_pen_get_colour_attr.argtypes = (
    POINTER(tickit.TickitPen),
    tickit.TickitPenAttr
)

ctickit.tickit_pen_set_colour_attr.restype = None
ctickit.tickit_pen_set_colour_attr.argtypes = (
    POINTER(tickit.TickitPen),
    tickit.TickitPenAttr,
    c_int
)

ctickit.tickit_pen_set_colour_attr_desc.restype = None
ctickit.tickit_pen_set_colour_attr_desc.argtypes = (
    POINTER(tickit.TickitPen),
    tickit.TickitPenAttr,
    c_char_p
)

ctickit.tickit_pen_get_int_attr.restype = c_int
ctickit.tickit_pen_get_int_attr.argtypes = (
    POINTER(tickit.TickitPen),
    tickit.TickitPenAttr
)

ctickit.tickit_pen_set_int_attr.restype = None
ctickit.tickit_pen_set_int_attr.argtypes = (
    POINTER(tickit.TickitPen),
    tickit.TickitPenAttr,
    c_int
)

ctickit.tickit_pen_has_attr.restype = c_bool
ctickit.tickit_pen_has_attr.argtypes = (
    POINTER(tickit.TickitPen),
    tickit.TickitPenAttr
)

ctickit.tickit_pen_is_nondefault.restype = c_bool
ctickit.tickit_pen_is_nondefault.argtypes = (POINTER(tickit.TickitPen),)

ctickit.tickit_pen_is_nonempty.restype = c_bool
ctickit.tickit_pen_is_nonempty.argtypes = (POINTER(tickit.TickitPen),)

ctickit.tickit_pen_attrname.restype = c_char_p
ctickit.tickit_pen_attrname.argtypes = (tickit.TickitPenAttr,)

ctickit.tickit_pen_lookup_attr.restype = tickit.TickitPenAttr
ctickit.tickit_pen_lookup_attr.argtypes = (c_char_p,)

ctickit.tickit_pen_new.restype = POINTER(tickit.TickitPen)
ctickit.tickit_pen_new.argtypes = ()

ctickit.tickit_pen_destroy.restype = None
ctickit.tickit_pen_destroy.argtypes = (POINTER(tickit.TickitPen),)

ctickit.tickit_string_count.restype = c_size_t
ctickit.tickit_string_count.argtypes = (
    c_char_p, POINTER(tickit.TickitStringPos), POINTER(tickit.TickitStringPos)
)

ctickit.tickit_string_countmore.restype = c_size_t
ctickit.tickit_string_countmore.argtypes = (
    c_char_p, POINTER(tickit.TickitStringPos), POINTER(tickit.TickitStringPos)
)

ctickit.tickit_term_bind_event.restype = c_int
ctickit.tickit_term_bind_event.argtypes = (
    POINTER(tickit.TickitTerm),
    tickit.TickitEventType,
    tickit.TickitTermEventFn,
    c_void_p
)

ctickit.tickit_term_unbind_event_id.restype = None
ctickit.tickit_term_unbind_event_id.argtypes = (
    POINTER(tickit.TickitTerm),
    c_int
)

ctickit.tickit_term_chpen.restype = None
ctickit.tickit_term_chpen.argtypes = (
    POINTER(tickit.TickitTerm),
    POINTER(tickit.TickitPen)
)

ctickit.tickit_term_setpen.restype = None
ctickit.tickit_term_setpen.argtypes = (
    POINTER(tickit.TickitTerm),
    POINTER(tickit.TickitPen)
)

ctickit.tickit_term_clear.restype = None
ctickit.tickit_term_clear.argtypes = (POINTER(tickit.TickitTerm),)

ctickit.tickit_term_new.restype = POINTER(tickit.TickitTerm)
ctickit.tickit_term_new.argtypes = ()

ctickit.tickit_term_new_for_termtype.restype = POINTER(tickit.TickitTerm)
ctickit.tickit_term_new_for_termtype.argtypes = (c_char_p,)

ctickit.tickit_term_destroy.restype = None
ctickit.tickit_term_destroy.argtypes = (POINTER(tickit.TickitTerm),)

ctickit.tickit_term_erasech.restype = None
ctickit.tickit_term_erasech.argtypes = (
    POINTER(tickit.TickitTerm),
    c_int,
    c_int
)

ctickit.tickit_term_flush.restype = None
ctickit.tickit_term_flush.argtypes = (POINTER(tickit.TickitTerm),)

ctickit.tickit_term_get_input_fd.restype = c_int
ctickit.tickit_term_get_input_fd.argtypes = (POINTER(tickit.TickitTerm),)

ctickit.tickit_term_set_input_fd.restype = None
ctickit.tickit_term_set_input_fd.argtypes = (
    POINTER(tickit.TickitTerm),
    c_int
)

ctickit.tickit_term_get_output_fd.restype = c_int
ctickit.tickit_term_get_output_fd.argtypes = (POINTER(tickit.TickitTerm),)

ctickit.tickit_term_set_output_fd.restype = None
ctickit.tickit_term_set_output_fd.argtypes = (
    POINTER(tickit.TickitTerm),
    c_int
)

ctickit.tickit_term_get_size.restype = None
ctickit.tickit_term_get_size.argtypes = (
    POINTER(tickit.TickitTerm),
    POINTER(c_int),
    POINTER(c_int)
)

ctickit.tickit_term_set_size.restype = None
ctickit.tickit_term_set_size.argtypes = (
    POINTER(tickit.TickitTerm),
    c_int,
    c_int
)

ctickit.tickit_term_refresh_size.restype = None
ctickit.tickit_term_refresh_size.argtypes = (POINTER(tickit.TickitTerm),)

ctickit.tickit_term_get_utf8.restype = c_bool
ctickit.tickit_term_get_utf8.argtypes = (POINTER(tickit.TickitTerm),)

ctickit.tickit_term_set_utf8.restype = None
ctickit.tickit_term_set_utf8.argtypes = (
    POINTER(tickit.TickitTerm),
    c_bool
)

ctickit.tickit_term_goto.restype = None
ctickit.tickit_term_goto.argtypes = (
    POINTER(tickit.TickitTerm),
    c_int,
    c_int
)

ctickit.tickit_term_move.restype = None
ctickit.tickit_term_move.argtypes = (
    POINTER(tickit.TickitTerm),
    c_int,
    c_int
)

ctickit.tickit_term_input_check_timeout.restype = c_int
ctickit.tickit_term_input_check_timeout.argtypes = (
    POINTER(tickit.TickitTerm),
)

ctickit.tickit_term_input_push_bytes.restype = None
ctickit.tickit_term_input_push_bytes.argtypes = (
    POINTER(tickit.TickitTerm),
    c_char_p,
    c_size_t
)

ctickit.tickit_term_input_readable.restype = None
ctickit.tickit_term_input_readable.argtypes = (POINTER(tickit.TickitTerm),)

ctickit.tickit_term_input_wait.restype = None
ctickit.tickit_term_input_wait.argtypes = (POINTER(tickit.TickitTerm),)

ctickit.tickit_term_print.restype = None
ctickit.tickit_term_print.argtypes = (POINTER(tickit.TickitTerm), c_char_p)

ctickit.tickit_term_scrollrect.restype = c_int
ctickit.tickit_term_scrollrect.argtypes = (
    POINTER(tickit.TickitTerm), c_int, c_int, c_int, c_int, c_int, c_int
)

ctickit.tickit_term_setctl_int.restype = c_int
ctickit.tickit_term_setctl_int.argtypes = (
    POINTER(tickit.TickitTerm), tickit.TickitTermCtl, c_int
)

__all__ = ['tickit', 'ctickit']

