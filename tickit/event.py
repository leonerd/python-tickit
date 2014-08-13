
import tickit._tickit as tickit

class EventType:
    resize = tickit.TICKIT_EV_RESIZE
    key    = tickit.TICKIT_EV_KEY
    mouse  = tickit.TICKIT_EV_MOUSE
    change = tickit.TICKIT_EV_CHANGE

class KeyEventType:
    key  = tickit.TICKIT_KEYEV_KEY
    text = tickit.TICKIT_KEYEV_TEXT

class MouseEventType:
    press   = tickit.TICKIT_MOUSEEV_PRESS
    drag    = tickit.TICKIT_MOUSEEV_DRAG
    release = tickit.TICKIT_MOUSEEV_RELEASE
    wheel   = tickit.TICKIT_MOUSEEV_WHEEL

class MouseWheel:
    up   = tickit.TICKIT_MOUSEWHEEL_UP
    down = tickit.TICKIT_MOUSEWHEEL_DOWN

