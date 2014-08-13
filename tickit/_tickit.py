from ctypes import *

STRING = c_char_p
_libraries = {}
_libraries['libtickit.so'] = CDLL('libtickit.so')


TICKIT_LINECAP_END = 2
TICKIT_MOD_SHIFT = 1
TICKIT_MOUSEWHEEL_DOWN = 2
TICKIT_MOUSEWHEEL_UP = 1
TICKIT_MOUSEEV_WHEEL = 4
TICKIT_MOUSEEV_DRAG = 2
TICKIT_TERMCTL_CURSORBLINK = 4
TICKIT_MOD_ALT = 2
TICKIT_PENTYPE_INT = 1
TICKIT_TERM_MOUSEMODE_OFF = 0
TICKIT_PENTYPE_BOOL = 0
TICKIT_MOUSEEV_PRESS = 1
TICKIT_TERMCTL_ALTSCREEN = 1
TICKIT_PENTYPE_COLOUR = 2
TICKIT_EV_UNBIND = -2147483648
TICKIT_EV_CHANGE = 8
TICKIT_EV_MOUSE = 4
TICKIT_LINECAP_START = 1
TICKIT_EV_KEY = 2
TICKIT_EV_RESIZE = 1
TICKIT_TERM_MOUSEMODE_MOVE = 3
TICKIT_KEYEV_KEY = 1
TICKIT_PEN_ALTFONT = 7
TICKIT_TERMCTL_COLORS = 10
TICKIT_TERMCTL_KEYPAD_APP = 9
TICKIT_LINE_THICK = 3
TICKIT_TERMCTL_TITLE_TEXT = 7
TICKIT_TERMCTL_ICON_TEXT = 6
TICKIT_TERMCTL_CURSORSHAPE = 5
TICKIT_TERMCTL_MOUSE = 3
TICKIT_LINECAP_BOTH = 3
TICKIT_LINE_DOUBLE = 2
TICKIT_LINE_SINGLE = 1
TICKIT_TERM_CURSORSHAPE_LEFT_BAR = 3
TICKIT_TERMCTL_ICONTITLE_TEXT = 8
TICKIT_KEYEV_TEXT = 2
TICKIT_TERM_CURSORSHAPE_UNDER = 2
TICKIT_TERMCTL_CURSORVIS = 2
TICKIT_PEN_FG = 0
TICKIT_TERM_CURSORSHAPE_BLOCK = 1
TICKIT_N_PEN_ATTRS = 8
TICKIT_MOUSEEV_RELEASE = 3
TICKIT_PEN_STRIKE = 6
TICKIT_PEN_REVERSE = 5
TICKIT_PEN_ITALIC = 4
TICKIT_PEN_UNDER = 3
TICKIT_PEN_BOLD = 2
TICKIT_PEN_BG = 1
TICKIT_TERM_MOUSEMODE_DRAG = 2
TICKIT_TERM_MOUSEMODE_CLICK = 1
TICKIT_MOD_CTRL = 4

# values for enumeration 'TickitEventType'
TickitEventType = c_int # enum

# values for enumeration 'TickitKeyEventType'
TickitKeyEventType = c_int # enum

# values for enumeration 'TickitMouseEventType'
TickitMouseEventType = c_int # enum
class TickitEvent(Structure):
    pass
TickitEvent._fields_ = [
    ('lines', c_int),
    ('cols', c_int),
    ('type', c_int),
    ('str', STRING),
    ('button', c_int),
    ('line', c_int),
    ('col', c_int),
    ('mod', c_int),
]
class TickitPen(Structure):
    pass
TickitPen._fields_ = [
]

# values for enumeration 'TickitPenAttr'
TickitPenAttr = c_int # enum

# values for enumeration 'TickitPenAttrType'
TickitPenAttrType = c_int # enum
tickit_pen_new = _libraries['libtickit.so'].tickit_pen_new
tickit_pen_new.restype = POINTER(TickitPen)
tickit_pen_new.argtypes = []
tickit_pen_new_attrs = _libraries['libtickit.so'].tickit_pen_new_attrs
tickit_pen_new_attrs.restype = POINTER(TickitPen)
tickit_pen_new_attrs.argtypes = [TickitPenAttr]
tickit_pen_clone = _libraries['libtickit.so'].tickit_pen_clone
tickit_pen_clone.restype = POINTER(TickitPen)
tickit_pen_clone.argtypes = [POINTER(TickitPen)]
tickit_pen_destroy = _libraries['libtickit.so'].tickit_pen_destroy
tickit_pen_destroy.restype = None
tickit_pen_destroy.argtypes = [POINTER(TickitPen)]
tickit_pen_has_attr = _libraries['libtickit.so'].tickit_pen_has_attr
tickit_pen_has_attr.restype = c_int
tickit_pen_has_attr.argtypes = [POINTER(TickitPen), TickitPenAttr]
tickit_pen_is_nonempty = _libraries['libtickit.so'].tickit_pen_is_nonempty
tickit_pen_is_nonempty.restype = c_int
tickit_pen_is_nonempty.argtypes = [POINTER(TickitPen)]
tickit_pen_nondefault_attr = _libraries['libtickit.so'].tickit_pen_nondefault_attr
tickit_pen_nondefault_attr.restype = c_int
tickit_pen_nondefault_attr.argtypes = [POINTER(TickitPen), TickitPenAttr]
tickit_pen_is_nondefault = _libraries['libtickit.so'].tickit_pen_is_nondefault
tickit_pen_is_nondefault.restype = c_int
tickit_pen_is_nondefault.argtypes = [POINTER(TickitPen)]
tickit_pen_get_bool_attr = _libraries['libtickit.so'].tickit_pen_get_bool_attr
tickit_pen_get_bool_attr.restype = c_int
tickit_pen_get_bool_attr.argtypes = [POINTER(TickitPen), TickitPenAttr]
tickit_pen_set_bool_attr = _libraries['libtickit.so'].tickit_pen_set_bool_attr
tickit_pen_set_bool_attr.restype = None
tickit_pen_set_bool_attr.argtypes = [POINTER(TickitPen), TickitPenAttr, c_int]
tickit_pen_get_int_attr = _libraries['libtickit.so'].tickit_pen_get_int_attr
tickit_pen_get_int_attr.restype = c_int
tickit_pen_get_int_attr.argtypes = [POINTER(TickitPen), TickitPenAttr]
tickit_pen_set_int_attr = _libraries['libtickit.so'].tickit_pen_set_int_attr
tickit_pen_set_int_attr.restype = None
tickit_pen_set_int_attr.argtypes = [POINTER(TickitPen), TickitPenAttr, c_int]
tickit_pen_get_colour_attr = _libraries['libtickit.so'].tickit_pen_get_colour_attr
tickit_pen_get_colour_attr.restype = c_int
tickit_pen_get_colour_attr.argtypes = [POINTER(TickitPen), TickitPenAttr]
tickit_pen_set_colour_attr = _libraries['libtickit.so'].tickit_pen_set_colour_attr
tickit_pen_set_colour_attr.restype = None
tickit_pen_set_colour_attr.argtypes = [POINTER(TickitPen), TickitPenAttr, c_int]
tickit_pen_set_colour_attr_desc = _libraries['libtickit.so'].tickit_pen_set_colour_attr_desc
tickit_pen_set_colour_attr_desc.restype = c_int
tickit_pen_set_colour_attr_desc.argtypes = [POINTER(TickitPen), TickitPenAttr, STRING]
tickit_pen_clear_attr = _libraries['libtickit.so'].tickit_pen_clear_attr
tickit_pen_clear_attr.restype = None
tickit_pen_clear_attr.argtypes = [POINTER(TickitPen), TickitPenAttr]
tickit_pen_clear = _libraries['libtickit.so'].tickit_pen_clear
tickit_pen_clear.restype = None
tickit_pen_clear.argtypes = [POINTER(TickitPen)]
tickit_pen_equiv_attr = _libraries['libtickit.so'].tickit_pen_equiv_attr
tickit_pen_equiv_attr.restype = c_int
tickit_pen_equiv_attr.argtypes = [POINTER(TickitPen), POINTER(TickitPen), TickitPenAttr]
tickit_pen_equiv = _libraries['libtickit.so'].tickit_pen_equiv
tickit_pen_equiv.restype = c_int
tickit_pen_equiv.argtypes = [POINTER(TickitPen), POINTER(TickitPen)]
tickit_pen_copy_attr = _libraries['libtickit.so'].tickit_pen_copy_attr
tickit_pen_copy_attr.restype = None
tickit_pen_copy_attr.argtypes = [POINTER(TickitPen), POINTER(TickitPen), TickitPenAttr]
tickit_pen_copy = _libraries['libtickit.so'].tickit_pen_copy
tickit_pen_copy.restype = None
tickit_pen_copy.argtypes = [POINTER(TickitPen), POINTER(TickitPen), c_int]
TickitPenEventFn = CFUNCTYPE(None, POINTER(TickitPen), TickitEventType, POINTER(TickitEvent), c_void_p)
tickit_pen_bind_event = _libraries['libtickit.so'].tickit_pen_bind_event
tickit_pen_bind_event.restype = c_int
tickit_pen_bind_event.argtypes = [POINTER(TickitPen), TickitEventType, POINTER(TickitPenEventFn), c_void_p]
tickit_pen_unbind_event_id = _libraries['libtickit.so'].tickit_pen_unbind_event_id
tickit_pen_unbind_event_id.restype = None
tickit_pen_unbind_event_id.argtypes = [POINTER(TickitPen), c_int]
tickit_pen_attrtype = _libraries['libtickit.so'].tickit_pen_attrtype
tickit_pen_attrtype.restype = TickitPenAttrType
tickit_pen_attrtype.argtypes = [TickitPenAttr]
tickit_pen_attrname = _libraries['libtickit.so'].tickit_pen_attrname
tickit_pen_attrname.restype = STRING
tickit_pen_attrname.argtypes = [TickitPenAttr]
tickit_pen_lookup_attr = _libraries['libtickit.so'].tickit_pen_lookup_attr
tickit_pen_lookup_attr.restype = TickitPenAttr
tickit_pen_lookup_attr.argtypes = [STRING]
class TickitRect(Structure):
    pass
TickitRect._fields_ = [
    ('top', c_int),
    ('left', c_int),
    ('lines', c_int),
    ('cols', c_int),
]
tickit_rect_init_sized = _libraries['libtickit.so'].tickit_rect_init_sized
tickit_rect_init_sized.restype = None
tickit_rect_init_sized.argtypes = [POINTER(TickitRect), c_int, c_int, c_int, c_int]
tickit_rect_init_bounded = _libraries['libtickit.so'].tickit_rect_init_bounded
tickit_rect_init_bounded.restype = None
tickit_rect_init_bounded.argtypes = [POINTER(TickitRect), c_int, c_int, c_int, c_int]
tickit_rect_intersect = _libraries['libtickit.so'].tickit_rect_intersect
tickit_rect_intersect.restype = c_int
tickit_rect_intersect.argtypes = [POINTER(TickitRect), POINTER(TickitRect), POINTER(TickitRect)]
tickit_rect_intersects = _libraries['libtickit.so'].tickit_rect_intersects
tickit_rect_intersects.restype = c_int
tickit_rect_intersects.argtypes = [POINTER(TickitRect), POINTER(TickitRect)]
tickit_rect_contains = _libraries['libtickit.so'].tickit_rect_contains
tickit_rect_contains.restype = c_int
tickit_rect_contains.argtypes = [POINTER(TickitRect), POINTER(TickitRect)]
tickit_rect_add = _libraries['libtickit.so'].tickit_rect_add
tickit_rect_add.restype = c_int
tickit_rect_add.argtypes = [POINTER(TickitRect), POINTER(TickitRect), POINTER(TickitRect)]
tickit_rect_subtract = _libraries['libtickit.so'].tickit_rect_subtract
tickit_rect_subtract.restype = c_int
tickit_rect_subtract.argtypes = [POINTER(TickitRect), POINTER(TickitRect), POINTER(TickitRect)]
class TickitRectSet(Structure):
    pass
TickitRectSet._fields_ = [
]
tickit_rectset_new = _libraries['libtickit.so'].tickit_rectset_new
tickit_rectset_new.restype = POINTER(TickitRectSet)
tickit_rectset_new.argtypes = []
tickit_rectset_destroy = _libraries['libtickit.so'].tickit_rectset_destroy
tickit_rectset_destroy.restype = None
tickit_rectset_destroy.argtypes = [POINTER(TickitRectSet)]
tickit_rectset_clear = _libraries['libtickit.so'].tickit_rectset_clear
tickit_rectset_clear.restype = None
tickit_rectset_clear.argtypes = [POINTER(TickitRectSet)]
size_t = c_ulong
tickit_rectset_rects = _libraries['libtickit.so'].tickit_rectset_rects
tickit_rectset_rects.restype = size_t
tickit_rectset_rects.argtypes = [POINTER(TickitRectSet)]
tickit_rectset_get_rects = _libraries['libtickit.so'].tickit_rectset_get_rects
tickit_rectset_get_rects.restype = size_t
tickit_rectset_get_rects.argtypes = [POINTER(TickitRectSet), POINTER(TickitRect), size_t]
tickit_rectset_add = _libraries['libtickit.so'].tickit_rectset_add
tickit_rectset_add.restype = None
tickit_rectset_add.argtypes = [POINTER(TickitRectSet), POINTER(TickitRect)]
tickit_rectset_subtract = _libraries['libtickit.so'].tickit_rectset_subtract
tickit_rectset_subtract.restype = None
tickit_rectset_subtract.argtypes = [POINTER(TickitRectSet), POINTER(TickitRect)]
tickit_rectset_intersects = _libraries['libtickit.so'].tickit_rectset_intersects
tickit_rectset_intersects.restype = c_int
tickit_rectset_intersects.argtypes = [POINTER(TickitRectSet), POINTER(TickitRect)]
tickit_rectset_contains = _libraries['libtickit.so'].tickit_rectset_contains
tickit_rectset_contains.restype = c_int
tickit_rectset_contains.argtypes = [POINTER(TickitRectSet), POINTER(TickitRect)]
class TickitTerm(Structure):
    pass
TickitTerm._fields_ = [
]
TickitTermOutputFunc = CFUNCTYPE(None, POINTER(TickitTerm), STRING, size_t, c_void_p)
tickit_term_new = _libraries['libtickit.so'].tickit_term_new
tickit_term_new.restype = POINTER(TickitTerm)
tickit_term_new.argtypes = []
tickit_term_new_for_termtype = _libraries['libtickit.so'].tickit_term_new_for_termtype
tickit_term_new_for_termtype.restype = POINTER(TickitTerm)
tickit_term_new_for_termtype.argtypes = [STRING]
tickit_term_destroy = _libraries['libtickit.so'].tickit_term_destroy
tickit_term_destroy.restype = None
tickit_term_destroy.argtypes = [POINTER(TickitTerm)]
tickit_term_get_termtype = _libraries['libtickit.so'].tickit_term_get_termtype
tickit_term_get_termtype.restype = STRING
tickit_term_get_termtype.argtypes = [POINTER(TickitTerm)]
tickit_term_set_output_fd = _libraries['libtickit.so'].tickit_term_set_output_fd
tickit_term_set_output_fd.restype = None
tickit_term_set_output_fd.argtypes = [POINTER(TickitTerm), c_int]
tickit_term_get_output_fd = _libraries['libtickit.so'].tickit_term_get_output_fd
tickit_term_get_output_fd.restype = c_int
tickit_term_get_output_fd.argtypes = [POINTER(TickitTerm)]
tickit_term_set_output_func = _libraries['libtickit.so'].tickit_term_set_output_func
tickit_term_set_output_func.restype = None
tickit_term_set_output_func.argtypes = [POINTER(TickitTerm), POINTER(TickitTermOutputFunc), c_void_p]
tickit_term_set_output_buffer = _libraries['libtickit.so'].tickit_term_set_output_buffer
tickit_term_set_output_buffer.restype = None
tickit_term_set_output_buffer.argtypes = [POINTER(TickitTerm), size_t]
class timeval(Structure):
    pass
__time_t = c_long
__suseconds_t = c_long
timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]
tickit_term_await_started = _libraries['libtickit.so'].tickit_term_await_started
tickit_term_await_started.restype = None
tickit_term_await_started.argtypes = [POINTER(TickitTerm), POINTER(timeval)]
tickit_term_flush = _libraries['libtickit.so'].tickit_term_flush
tickit_term_flush.restype = None
tickit_term_flush.argtypes = [POINTER(TickitTerm)]
tickit_term_set_input_fd = _libraries['libtickit.so'].tickit_term_set_input_fd
tickit_term_set_input_fd.restype = None
tickit_term_set_input_fd.argtypes = [POINTER(TickitTerm), c_int]
tickit_term_get_input_fd = _libraries['libtickit.so'].tickit_term_get_input_fd
tickit_term_get_input_fd.restype = c_int
tickit_term_get_input_fd.argtypes = [POINTER(TickitTerm)]
tickit_term_get_utf8 = _libraries['libtickit.so'].tickit_term_get_utf8
tickit_term_get_utf8.restype = c_int
tickit_term_get_utf8.argtypes = [POINTER(TickitTerm)]
tickit_term_set_utf8 = _libraries['libtickit.so'].tickit_term_set_utf8
tickit_term_set_utf8.restype = None
tickit_term_set_utf8.argtypes = [POINTER(TickitTerm), c_int]
tickit_term_input_push_bytes = _libraries['libtickit.so'].tickit_term_input_push_bytes
tickit_term_input_push_bytes.restype = None
tickit_term_input_push_bytes.argtypes = [POINTER(TickitTerm), STRING, size_t]
tickit_term_input_readable = _libraries['libtickit.so'].tickit_term_input_readable
tickit_term_input_readable.restype = None
tickit_term_input_readable.argtypes = [POINTER(TickitTerm)]
tickit_term_input_check_timeout = _libraries['libtickit.so'].tickit_term_input_check_timeout
tickit_term_input_check_timeout.restype = c_int
tickit_term_input_check_timeout.argtypes = [POINTER(TickitTerm)]
tickit_term_input_wait = _libraries['libtickit.so'].tickit_term_input_wait
tickit_term_input_wait.restype = None
tickit_term_input_wait.argtypes = [POINTER(TickitTerm), POINTER(timeval)]
tickit_term_get_size = _libraries['libtickit.so'].tickit_term_get_size
tickit_term_get_size.restype = None
tickit_term_get_size.argtypes = [POINTER(TickitTerm), POINTER(c_int), POINTER(c_int)]
tickit_term_set_size = _libraries['libtickit.so'].tickit_term_set_size
tickit_term_set_size.restype = None
tickit_term_set_size.argtypes = [POINTER(TickitTerm), c_int, c_int]
tickit_term_refresh_size = _libraries['libtickit.so'].tickit_term_refresh_size
tickit_term_refresh_size.restype = None
tickit_term_refresh_size.argtypes = [POINTER(TickitTerm)]
TickitTermEventFn = CFUNCTYPE(None, POINTER(TickitTerm), TickitEventType, POINTER(TickitEvent), c_void_p)
tickit_term_bind_event = _libraries['libtickit.so'].tickit_term_bind_event
tickit_term_bind_event.restype = c_int
tickit_term_bind_event.argtypes = [POINTER(TickitTerm), TickitEventType, POINTER(TickitTermEventFn), c_void_p]
tickit_term_unbind_event_id = _libraries['libtickit.so'].tickit_term_unbind_event_id
tickit_term_unbind_event_id.restype = None
tickit_term_unbind_event_id.argtypes = [POINTER(TickitTerm), c_int]
tickit_term_print = _libraries['libtickit.so'].tickit_term_print
tickit_term_print.restype = None
tickit_term_print.argtypes = [POINTER(TickitTerm), STRING]
tickit_term_printn = _libraries['libtickit.so'].tickit_term_printn
tickit_term_printn.restype = None
tickit_term_printn.argtypes = [POINTER(TickitTerm), STRING, size_t]
tickit_term_printf = _libraries['libtickit.so'].tickit_term_printf
tickit_term_printf.restype = None
tickit_term_printf.argtypes = [POINTER(TickitTerm), STRING]
class __va_list_tag(Structure):
    pass
tickit_term_vprintf = _libraries['libtickit.so'].tickit_term_vprintf
tickit_term_vprintf.restype = None
tickit_term_vprintf.argtypes = [POINTER(TickitTerm), STRING, POINTER(__va_list_tag)]
tickit_term_goto = _libraries['libtickit.so'].tickit_term_goto
tickit_term_goto.restype = c_int
tickit_term_goto.argtypes = [POINTER(TickitTerm), c_int, c_int]
tickit_term_move = _libraries['libtickit.so'].tickit_term_move
tickit_term_move.restype = None
tickit_term_move.argtypes = [POINTER(TickitTerm), c_int, c_int]
tickit_term_scrollrect = _libraries['libtickit.so'].tickit_term_scrollrect
tickit_term_scrollrect.restype = c_int
tickit_term_scrollrect.argtypes = [POINTER(TickitTerm), c_int, c_int, c_int, c_int, c_int, c_int]
tickit_term_chpen = _libraries['libtickit.so'].tickit_term_chpen
tickit_term_chpen.restype = None
tickit_term_chpen.argtypes = [POINTER(TickitTerm), POINTER(TickitPen)]
tickit_term_setpen = _libraries['libtickit.so'].tickit_term_setpen
tickit_term_setpen.restype = None
tickit_term_setpen.argtypes = [POINTER(TickitTerm), POINTER(TickitPen)]
tickit_term_clear = _libraries['libtickit.so'].tickit_term_clear
tickit_term_clear.restype = None
tickit_term_clear.argtypes = [POINTER(TickitTerm)]
tickit_term_erasech = _libraries['libtickit.so'].tickit_term_erasech
tickit_term_erasech.restype = None
tickit_term_erasech.argtypes = [POINTER(TickitTerm), c_int, c_int]

# values for enumeration 'TickitTermCtl'
TickitTermCtl = c_int # enum

# values for enumeration 'TickitTermMouseMode'
TickitTermMouseMode = c_int # enum

# values for enumeration 'TickitTermCursorShape'
TickitTermCursorShape = c_int # enum
tickit_term_getctl_int = _libraries['libtickit.so'].tickit_term_getctl_int
tickit_term_getctl_int.restype = c_int
tickit_term_getctl_int.argtypes = [POINTER(TickitTerm), TickitTermCtl, POINTER(c_int)]
tickit_term_setctl_int = _libraries['libtickit.so'].tickit_term_setctl_int
tickit_term_setctl_int.restype = c_int
tickit_term_setctl_int.argtypes = [POINTER(TickitTerm), TickitTermCtl, c_int]
tickit_term_setctl_str = _libraries['libtickit.so'].tickit_term_setctl_str
tickit_term_setctl_str.restype = c_int
tickit_term_setctl_str.argtypes = [POINTER(TickitTerm), TickitTermCtl, STRING]
tickit_string_seqlen = _libraries['libtickit.so'].tickit_string_seqlen
tickit_string_seqlen.restype = c_int
tickit_string_seqlen.argtypes = [c_long]
tickit_string_putchar = _libraries['libtickit.so'].tickit_string_putchar
tickit_string_putchar.restype = size_t
tickit_string_putchar.argtypes = [STRING, size_t, c_long]
class TickitStringPos(Structure):
    pass
TickitStringPos._fields_ = [
    ('bytes', size_t),
    ('codepoints', c_int),
    ('graphemes', c_int),
    ('columns', c_int),
]
tickit_string_count = _libraries['libtickit.so'].tickit_string_count
tickit_string_count.restype = size_t
tickit_string_count.argtypes = [STRING, POINTER(TickitStringPos), POINTER(TickitStringPos)]
tickit_string_countmore = _libraries['libtickit.so'].tickit_string_countmore
tickit_string_countmore.restype = size_t
tickit_string_countmore.argtypes = [STRING, POINTER(TickitStringPos), POINTER(TickitStringPos)]
tickit_string_ncount = _libraries['libtickit.so'].tickit_string_ncount
tickit_string_ncount.restype = size_t
tickit_string_ncount.argtypes = [STRING, size_t, POINTER(TickitStringPos), POINTER(TickitStringPos)]
tickit_string_ncountmore = _libraries['libtickit.so'].tickit_string_ncountmore
tickit_string_ncountmore.restype = size_t
tickit_string_ncountmore.argtypes = [STRING, size_t, POINTER(TickitStringPos), POINTER(TickitStringPos)]
tickit_string_mbswidth = _libraries['libtickit.so'].tickit_string_mbswidth
tickit_string_mbswidth.restype = c_int
tickit_string_mbswidth.argtypes = [STRING]
tickit_string_byte2col = _libraries['libtickit.so'].tickit_string_byte2col
tickit_string_byte2col.restype = c_int
tickit_string_byte2col.argtypes = [STRING, size_t]
tickit_string_col2byte = _libraries['libtickit.so'].tickit_string_col2byte
tickit_string_col2byte.restype = size_t
tickit_string_col2byte.argtypes = [STRING, c_int]
class TickitRenderBuffer(Structure):
    pass
TickitRenderBuffer._fields_ = [
]
tickit_renderbuffer_new = _libraries['libtickit.so'].tickit_renderbuffer_new
tickit_renderbuffer_new.restype = POINTER(TickitRenderBuffer)
tickit_renderbuffer_new.argtypes = [c_int, c_int]
tickit_renderbuffer_destroy = _libraries['libtickit.so'].tickit_renderbuffer_destroy
tickit_renderbuffer_destroy.restype = None
tickit_renderbuffer_destroy.argtypes = [POINTER(TickitRenderBuffer)]
tickit_renderbuffer_get_size = _libraries['libtickit.so'].tickit_renderbuffer_get_size
tickit_renderbuffer_get_size.restype = None
tickit_renderbuffer_get_size.argtypes = [POINTER(TickitRenderBuffer), POINTER(c_int), POINTER(c_int)]
tickit_renderbuffer_translate = _libraries['libtickit.so'].tickit_renderbuffer_translate
tickit_renderbuffer_translate.restype = None
tickit_renderbuffer_translate.argtypes = [POINTER(TickitRenderBuffer), c_int, c_int]
tickit_renderbuffer_clip = _libraries['libtickit.so'].tickit_renderbuffer_clip
tickit_renderbuffer_clip.restype = None
tickit_renderbuffer_clip.argtypes = [POINTER(TickitRenderBuffer), POINTER(TickitRect)]
tickit_renderbuffer_mask = _libraries['libtickit.so'].tickit_renderbuffer_mask
tickit_renderbuffer_mask.restype = None
tickit_renderbuffer_mask.argtypes = [POINTER(TickitRenderBuffer), POINTER(TickitRect)]
tickit_renderbuffer_has_cursorpos = _libraries['libtickit.so'].tickit_renderbuffer_has_cursorpos
tickit_renderbuffer_has_cursorpos.restype = c_int
tickit_renderbuffer_has_cursorpos.argtypes = [POINTER(TickitRenderBuffer)]
tickit_renderbuffer_get_cursorpos = _libraries['libtickit.so'].tickit_renderbuffer_get_cursorpos
tickit_renderbuffer_get_cursorpos.restype = None
tickit_renderbuffer_get_cursorpos.argtypes = [POINTER(TickitRenderBuffer), POINTER(c_int), POINTER(c_int)]
tickit_renderbuffer_goto = _libraries['libtickit.so'].tickit_renderbuffer_goto
tickit_renderbuffer_goto.restype = None
tickit_renderbuffer_goto.argtypes = [POINTER(TickitRenderBuffer), c_int, c_int]
tickit_renderbuffer_ungoto = _libraries['libtickit.so'].tickit_renderbuffer_ungoto
tickit_renderbuffer_ungoto.restype = None
tickit_renderbuffer_ungoto.argtypes = [POINTER(TickitRenderBuffer)]
tickit_renderbuffer_setpen = _libraries['libtickit.so'].tickit_renderbuffer_setpen
tickit_renderbuffer_setpen.restype = None
tickit_renderbuffer_setpen.argtypes = [POINTER(TickitRenderBuffer), POINTER(TickitPen)]
tickit_renderbuffer_reset = _libraries['libtickit.so'].tickit_renderbuffer_reset
tickit_renderbuffer_reset.restype = None
tickit_renderbuffer_reset.argtypes = [POINTER(TickitRenderBuffer)]
tickit_renderbuffer_save = _libraries['libtickit.so'].tickit_renderbuffer_save
tickit_renderbuffer_save.restype = None
tickit_renderbuffer_save.argtypes = [POINTER(TickitRenderBuffer)]
tickit_renderbuffer_savepen = _libraries['libtickit.so'].tickit_renderbuffer_savepen
tickit_renderbuffer_savepen.restype = None
tickit_renderbuffer_savepen.argtypes = [POINTER(TickitRenderBuffer)]
tickit_renderbuffer_restore = _libraries['libtickit.so'].tickit_renderbuffer_restore
tickit_renderbuffer_restore.restype = None
tickit_renderbuffer_restore.argtypes = [POINTER(TickitRenderBuffer)]
tickit_renderbuffer_skip_at = _libraries['libtickit.so'].tickit_renderbuffer_skip_at
tickit_renderbuffer_skip_at.restype = None
tickit_renderbuffer_skip_at.argtypes = [POINTER(TickitRenderBuffer), c_int, c_int, c_int]
tickit_renderbuffer_skip = _libraries['libtickit.so'].tickit_renderbuffer_skip
tickit_renderbuffer_skip.restype = None
tickit_renderbuffer_skip.argtypes = [POINTER(TickitRenderBuffer), c_int]
tickit_renderbuffer_skip_to = _libraries['libtickit.so'].tickit_renderbuffer_skip_to
tickit_renderbuffer_skip_to.restype = None
tickit_renderbuffer_skip_to.argtypes = [POINTER(TickitRenderBuffer), c_int]
tickit_renderbuffer_text_at = _libraries['libtickit.so'].tickit_renderbuffer_text_at
tickit_renderbuffer_text_at.restype = c_int
tickit_renderbuffer_text_at.argtypes = [POINTER(TickitRenderBuffer), c_int, c_int, STRING, POINTER(TickitPen)]
tickit_renderbuffer_text = _libraries['libtickit.so'].tickit_renderbuffer_text
tickit_renderbuffer_text.restype = c_int
tickit_renderbuffer_text.argtypes = [POINTER(TickitRenderBuffer), STRING, POINTER(TickitPen)]
tickit_renderbuffer_erase_at = _libraries['libtickit.so'].tickit_renderbuffer_erase_at
tickit_renderbuffer_erase_at.restype = None
tickit_renderbuffer_erase_at.argtypes = [POINTER(TickitRenderBuffer), c_int, c_int, c_int, POINTER(TickitPen)]
tickit_renderbuffer_erase = _libraries['libtickit.so'].tickit_renderbuffer_erase
tickit_renderbuffer_erase.restype = None
tickit_renderbuffer_erase.argtypes = [POINTER(TickitRenderBuffer), c_int, POINTER(TickitPen)]
tickit_renderbuffer_erase_to = _libraries['libtickit.so'].tickit_renderbuffer_erase_to
tickit_renderbuffer_erase_to.restype = None
tickit_renderbuffer_erase_to.argtypes = [POINTER(TickitRenderBuffer), c_int, POINTER(TickitPen)]
tickit_renderbuffer_eraserect = _libraries['libtickit.so'].tickit_renderbuffer_eraserect
tickit_renderbuffer_eraserect.restype = None
tickit_renderbuffer_eraserect.argtypes = [POINTER(TickitRenderBuffer), POINTER(TickitRect), POINTER(TickitPen)]
tickit_renderbuffer_clear = _libraries['libtickit.so'].tickit_renderbuffer_clear
tickit_renderbuffer_clear.restype = None
tickit_renderbuffer_clear.argtypes = [POINTER(TickitRenderBuffer), POINTER(TickitPen)]
tickit_renderbuffer_char_at = _libraries['libtickit.so'].tickit_renderbuffer_char_at
tickit_renderbuffer_char_at.restype = None
tickit_renderbuffer_char_at.argtypes = [POINTER(TickitRenderBuffer), c_int, c_int, c_long, POINTER(TickitPen)]
tickit_renderbuffer_char = _libraries['libtickit.so'].tickit_renderbuffer_char
tickit_renderbuffer_char.restype = None
tickit_renderbuffer_char.argtypes = [POINTER(TickitRenderBuffer), c_long, POINTER(TickitPen)]

# values for enumeration 'TickitLineStyle'
TickitLineStyle = c_int # enum

# values for enumeration 'TickitLineCaps'
TickitLineCaps = c_int # enum
tickit_renderbuffer_hline_at = _libraries['libtickit.so'].tickit_renderbuffer_hline_at
tickit_renderbuffer_hline_at.restype = None
tickit_renderbuffer_hline_at.argtypes = [POINTER(TickitRenderBuffer), c_int, c_int, c_int, TickitLineStyle, POINTER(TickitPen), TickitLineCaps]
tickit_renderbuffer_vline_at = _libraries['libtickit.so'].tickit_renderbuffer_vline_at
tickit_renderbuffer_vline_at.restype = None
tickit_renderbuffer_vline_at.argtypes = [POINTER(TickitRenderBuffer), c_int, c_int, c_int, TickitLineStyle, POINTER(TickitPen), TickitLineCaps]
tickit_renderbuffer_flush_to_term = _libraries['libtickit.so'].tickit_renderbuffer_flush_to_term
tickit_renderbuffer_flush_to_term.restype = None
tickit_renderbuffer_flush_to_term.argtypes = [POINTER(TickitRenderBuffer), POINTER(TickitTerm)]
class TickitRenderBufferLineMask(Structure):
    pass
TickitRenderBufferLineMask._fields_ = [
    ('north', c_char),
    ('south', c_char),
    ('east', c_char),
    ('west', c_char),
]
tickit_renderbuffer_get_cell_active = _libraries['libtickit.so'].tickit_renderbuffer_get_cell_active
tickit_renderbuffer_get_cell_active.restype = c_int
tickit_renderbuffer_get_cell_active.argtypes = [POINTER(TickitRenderBuffer), c_int, c_int]
tickit_renderbuffer_get_cell_text = _libraries['libtickit.so'].tickit_renderbuffer_get_cell_text
tickit_renderbuffer_get_cell_text.restype = size_t
tickit_renderbuffer_get_cell_text.argtypes = [POINTER(TickitRenderBuffer), c_int, c_int, STRING, size_t]
tickit_renderbuffer_get_cell_linemask = _libraries['libtickit.so'].tickit_renderbuffer_get_cell_linemask
tickit_renderbuffer_get_cell_linemask.restype = TickitRenderBufferLineMask
tickit_renderbuffer_get_cell_linemask.argtypes = [POINTER(TickitRenderBuffer), c_int, c_int]
tickit_renderbuffer_get_cell_pen = _libraries['libtickit.so'].tickit_renderbuffer_get_cell_pen
tickit_renderbuffer_get_cell_pen.restype = POINTER(TickitPen)
tickit_renderbuffer_get_cell_pen.argtypes = [POINTER(TickitRenderBuffer), c_int, c_int]
class TickitRenderBufferSpanInfo(Structure):
    pass
TickitRenderBufferSpanInfo._fields_ = [
    ('is_active', c_int),
    ('n_columns', c_int),
    ('text', STRING),
    ('len', size_t),
    ('pen', POINTER(TickitPen)),
]
tickit_renderbuffer_get_span = _libraries['libtickit.so'].tickit_renderbuffer_get_span
tickit_renderbuffer_get_span.restype = size_t
tickit_renderbuffer_get_span.argtypes = [POINTER(TickitRenderBuffer), c_int, c_int, POINTER(TickitRenderBufferSpanInfo), STRING, size_t]
__va_list_tag._fields_ = [
]
__all__ = ['tickit_renderbuffer_translate',
           'tickit_renderbuffer_hline_at',
           'tickit_pen_unbind_event_id', 'tickit_term_goto',
           'TickitEvent', 'TICKIT_PEN_STRIKE', 'TICKIT_MOD_CTRL',
           'tickit_pen_nondefault_attr', 'TICKIT_TERM_MOUSEMODE_MOVE',
           'tickit_string_byte2col', 'tickit_term_destroy',
           'TICKIT_PEN_ALTFONT', 'size_t',
           'TICKIT_TERMCTL_KEYPAD_APP', 'tickit_string_mbswidth',
           'tickit_renderbuffer_get_cell_text',
           'tickit_pen_is_nonempty', 'tickit_renderbuffer_ungoto',
           'TICKIT_KEYEV_KEY', 'tickit_renderbuffer_get_size',
           'TICKIT_TERM_MOUSEMODE_OFF', 'TICKIT_PEN_UNDER',
           'tickit_rect_subtract', 'tickit_renderbuffer_setpen',
           'tickit_pen_new_attrs', 'TICKIT_PEN_BG',
           'tickit_term_move', 'tickit_renderbuffer_eraserect',
           'tickit_renderbuffer_get_cell_pen', 'tickit_pen_attrtype',
           'tickit_pen_clear', 'tickit_pen_get_colour_attr',
           'tickit_pen_set_colour_attr_desc',
           'tickit_rectset_get_rects', 'tickit_term_printn',
           'TICKIT_N_PEN_ATTRS', 'tickit_term_vprintf',
           'TICKIT_TERMCTL_CURSORVIS', 'tickit_term_printf',
           '__time_t', 'tickit_pen_clone',
           'tickit_term_unbind_event_id',
           'tickit_term_input_check_timeout',
           'tickit_rectset_subtract', 'TickitRenderBufferSpanInfo',
           'tickit_renderbuffer_clear', 'tickit_string_col2byte',
           'TickitLineStyle', 'tickit_term_setctl_str',
           'tickit_term_set_input_fd', 'tickit_term_chpen',
           'tickit_rect_add', 'TICKIT_MOUSEEV_RELEASE',
           'TICKIT_TERM_MOUSEMODE_CLICK', 'tickit_pen_destroy',
           'tickit_renderbuffer_char_at', '__va_list_tag',
           'TICKIT_TERM_CURSORSHAPE_UNDER',
           'tickit_renderbuffer_skip_to', 'TICKIT_LINECAP_START',
           'tickit_renderbuffer_skip_at', 'tickit_rect_intersect',
           'TickitEventType', 'tickit_term_input_readable',
           'TICKIT_TERMCTL_ICON_TEXT', 'tickit_renderbuffer_reset',
           'tickit_pen_copy', 'TickitRenderBufferLineMask',
           'TickitTermOutputFunc', 'tickit_renderbuffer_restore',
           'tickit_renderbuffer_get_cell_active',
           'tickit_pen_has_attr', 'tickit_renderbuffer_savepen',
           'tickit_term_new', 'TICKIT_EV_CHANGE',
           'tickit_term_set_output_func', 'tickit_renderbuffer_mask',
           'tickit_rectset_add', 'tickit_renderbuffer_has_cursorpos',
           'tickit_renderbuffer_get_cursorpos',
           'tickit_string_ncount', 'tickit_renderbuffer_clip',
           'tickit_renderbuffer_get_span', 'TickitPen',
           'tickit_rect_init_sized', 'TICKIT_EV_RESIZE',
           'tickit_pen_bind_event', 'tickit_term_setctl_int',
           'tickit_pen_new', 'tickit_rectset_rects',
           'tickit_term_get_size', 'TICKIT_MOUSEWHEEL_DOWN',
           'tickit_renderbuffer_vline_at', 'tickit_rectset_contains',
           'TickitRectSet', 'tickit_term_get_output_fd',
           'TickitTermCtl', 'tickit_string_seqlen',
           'tickit_pen_equiv_attr', 'tickit_string_ncountmore',
           'TICKIT_LINE_DOUBLE', 'tickit_renderbuffer_flush_to_term',
           'tickit_term_input_push_bytes', 'TICKIT_EV_MOUSE',
           'TICKIT_TERMCTL_ALTSCREEN', 'tickit_pen_clear_attr',
           'TICKIT_TERMCTL_CURSORSHAPE', 'TICKIT_LINE_THICK',
           'TICKIT_EV_KEY', 'TICKIT_MOUSEEV_PRESS',
           'tickit_term_refresh_size',
           'tickit_term_set_output_buffer', 'tickit_term_erasech',
           'TICKIT_TERMCTL_CURSORBLINK', 'tickit_term_setpen',
           'tickit_rect_contains', 'tickit_rect_intersects',
           'TICKIT_EV_UNBIND', 'tickit_term_get_input_fd',
           'tickit_pen_attrname', 'TICKIT_PENTYPE_COLOUR',
           'tickit_term_new_for_termtype', 'TICKIT_MOUSEEV_WHEEL',
           'tickit_term_flush', 'TICKIT_KEYEV_TEXT',
           'tickit_renderbuffer_erase_to', 'tickit_pen_copy_attr',
           'TickitMouseEventType', 'TICKIT_PENTYPE_INT',
           'tickit_rectset_clear', 'TICKIT_PEN_FG',
           'TickitKeyEventType', 'TICKIT_MOUSEWHEEL_UP',
           'TICKIT_TERM_CURSORSHAPE_LEFT_BAR', 'TickitPenEventFn',
           'tickit_pen_set_colour_attr', 'tickit_rectset_intersects',
           'TICKIT_TERM_MOUSEMODE_DRAG', 'TickitTermCursorShape',
           'tickit_term_scrollrect', 'tickit_renderbuffer_skip',
           '__suseconds_t', 'tickit_pen_lookup_attr',
           'TickitRenderBuffer', 'tickit_rectset_new',
           'TICKIT_MOUSEEV_DRAG', 'TICKIT_TERMCTL_TITLE_TEXT',
           'tickit_term_get_termtype', 'tickit_string_count',
           'tickit_rectset_destroy', 'TICKIT_MOD_SHIFT',
           'tickit_renderbuffer_goto', 'tickit_term_get_utf8',
           'tickit_renderbuffer_get_cell_linemask', 'TickitRect',
           'TICKIT_LINECAP_END', 'TICKIT_TERM_CURSORSHAPE_BLOCK',
           'tickit_renderbuffer_save', 'TICKIT_PEN_ITALIC',
           'tickit_term_clear', 'tickit_string_countmore',
           'tickit_renderbuffer_text', 'tickit_term_getctl_int',
           'tickit_pen_is_nondefault', 'TickitPenAttr',
           'TickitStringPos', 'tickit_renderbuffer_erase_at',
           'timeval', 'tickit_term_set_size',
           'tickit_renderbuffer_char', 'TICKIT_MOD_ALT',
           'tickit_term_print', 'TickitPenAttrType', 'TickitTerm',
           'TICKIT_TERMCTL_COLORS', 'tickit_term_bind_event',
           'tickit_pen_set_bool_attr', 'TickitTermMouseMode',
           'tickit_renderbuffer_destroy', 'TICKIT_PEN_REVERSE',
           'tickit_renderbuffer_text_at', 'tickit_pen_equiv',
           'tickit_term_set_output_fd', 'TICKIT_TERMCTL_MOUSE',
           'TICKIT_PEN_BOLD', 'tickit_pen_get_bool_attr',
           'tickit_term_input_wait', 'tickit_renderbuffer_erase',
           'tickit_term_set_utf8', 'tickit_pen_get_int_attr',
           'TICKIT_LINE_SINGLE', 'TICKIT_PENTYPE_BOOL',
           'TickitTermEventFn', 'tickit_renderbuffer_new',
           'tickit_string_putchar', 'tickit_rect_init_bounded',
           'tickit_term_await_started', 'tickit_pen_set_int_attr',
           'TICKIT_LINECAP_BOTH', 'TICKIT_TERMCTL_ICONTITLE_TEXT',
           'TickitLineCaps']
