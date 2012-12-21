from ctypes import *

STRING = c_char_p


TICKIT_EV_MOUSE = 4
TICKIT_PENTYPE_COLOUR = 2
TICKIT_EV_KEY = 2
TICKIT_PENTYPE_INT = 1
TICKIT_PEN_UNDER = 3
TICKIT_MOUSEWHEEL_DOWN = 2
TICKIT_MOUSEWHEEL_UP = 1
TICKIT_MOUSEEV_WHEEL = 4
TICKIT_MOUSEEV_RELEASE = 3
TICKIT_MOUSEEV_PRESS = 1
TICKIT_N_PEN_ATTRS = 8
TICKIT_PEN_STRIKE = 6
TICKIT_PEN_REVERSE = 5
TICKIT_PEN_ITALIC = 4
TICKIT_EV_CHANGE = 8
TICKIT_PEN_BOLD = 2
TICKIT_PEN_BG = 1
TICKIT_TERM_CURSORSHAPE_BLOCK = 1
TICKIT_PEN_FG = 0
TICKIT_TERMCTL_TITLE_TEXT = 7
TICKIT_TERM_CURSORSHAPE_LEFT_BAR = 3
TICKIT_TERM_CURSORSHAPE_UNDER = 2
TICKIT_TERMCTL_MOUSE = 3
TICKIT_TERMCTL_KEYPAD_APP = 9
TICKIT_TERMCTL_ICONTITLE_TEXT = 8
TICKIT_TERMCTL_ICON_TEXT = 6
TICKIT_TERMCTL_CURSORSHAPE = 5
TICKIT_TERMCTL_CURSORBLINK = 4
TICKIT_TERMCTL_CURSORVIS = 2
TICKIT_TERMCTL_ALTSCREEN = 1
TICKIT_MOUSEEV_DRAG = 2
TICKIT_PEN_ALTFONT = 7
TICKIT_EV_UNBIND = -2147483648
TICKIT_EV_RESIZE = 1
TICKIT_KEYEV_TEXT = 2
TICKIT_PENTYPE_BOOL = 0
TICKIT_KEYEV_KEY = 1

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
]
class TickitPen(Structure):
    pass
TickitPen._fields_ = [
]

# values for enumeration 'TickitPenAttr'
TickitPenAttr = c_int # enum

# values for enumeration 'TickitPenAttrType'
TickitPenAttrType = c_int # enum
TickitPenEventFn = CFUNCTYPE(None, POINTER(TickitPen), TickitEventType, POINTER(TickitEvent), c_void_p)
class TickitTerm(Structure):
    pass
TickitTerm._fields_ = [
]
size_t = c_ulong
TickitTermOutputFunc = CFUNCTYPE(None, POINTER(TickitTerm), STRING, size_t, c_void_p)
TickitTermEventFn = CFUNCTYPE(None, POINTER(TickitTerm), TickitEventType, POINTER(TickitEvent), c_void_p)

# values for enumeration 'TickitTermCtl'
TickitTermCtl = c_int # enum

# values for enumeration 'TickitTermCursorShape'
TickitTermCursorShape = c_int # enum
class TickitStringPos(Structure):
    pass
TickitStringPos._fields_ = [
    ('bytes', size_t),
    ('codepoints', c_int),
    ('graphemes', c_int),
    ('columns', c_int),
]
__all__ = ['TICKIT_EV_CHANGE', 'TICKIT_EV_MOUSE',
           'TICKIT_TERM_CURSORSHAPE_UNDER', 'TICKIT_PEN_STRIKE',
           'TICKIT_TERM_CURSORSHAPE_BLOCK', 'TICKIT_PEN_ITALIC',
           'TICKIT_EV_KEY', 'size_t', 'TICKIT_MOUSEEV_PRESS',
           'TickitTermOutputFunc', 'TICKIT_TERMCTL_KEYPAD_APP',
           'TICKIT_PEN_ALTFONT', 'TickitPenAttr',
           'TICKIT_TERMCTL_CURSORBLINK', 'TickitStringPos',
           'TickitMouseEventType', 'TickitEventType',
           'TICKIT_KEYEV_KEY', 'TickitKeyEventType',
           'TICKIT_TERMCTL_CURSORSHAPE', 'TICKIT_TERMCTL_ICON_TEXT',
           'TICKIT_PEN_UNDER', 'TICKIT_PENTYPE_COLOUR',
           'TICKIT_EV_UNBIND', 'TICKIT_MOUSEEV_WHEEL', 'TickitEvent',
           'TICKIT_KEYEV_TEXT', 'TICKIT_PEN_BG', 'TICKIT_PENTYPE_INT',
           'TICKIT_TERMCTL_ALTSCREEN', 'TICKIT_PEN_FG',
           'TICKIT_PEN_REVERSE', 'TickitPenAttrType',
           'TICKIT_MOUSEWHEEL_UP', 'TickitPen',
           'TICKIT_TERM_CURSORSHAPE_LEFT_BAR', 'TickitPenEventFn',
           'TICKIT_N_PEN_ATTRS', 'TICKIT_PEN_BOLD',
           'TICKIT_TERMCTL_CURSORVIS', 'TICKIT_TERMCTL_MOUSE',
           'TickitTermCursorShape', 'TICKIT_PENTYPE_BOOL',
           'TICKIT_MOUSEWHEEL_DOWN', 'TickitTermEventFn',
           'TickitTerm', 'TICKIT_MOUSEEV_DRAG',
           'TICKIT_TERMCTL_TITLE_TEXT', 'TICKIT_MOUSEEV_RELEASE',
           'TickitTermCtl', 'TICKIT_TERMCTL_ICONTITLE_TEXT',
           'TICKIT_EV_RESIZE']
