
import tickit._tickit as tickit

try:
    from collections.abc import MutableMapping
except ImportError:
    from collections import MutableMapping

def lookup_attr(name):
    attr = bytes(name, 'ascii')
    return tickit.tickit_pen_lookup_attr(attr)

class Pen(MutableMapping):
    """An object for storing terminal attributes.

    Pens are used by Terminal objects to alter how output is formatted and may
    be assigned to such via their chpen() and setpen() methods.

    This API mirrors the Tickit::Pen API and additionally implements Pythonic
    methods (the usual Mapping methods are available).
    """
    def __init__(self, **kwargs):
        self._pen = tickit.tickit_pen_new()
        self._attrs = {}

        self._events = {}

        self.setattrs(kwargs)

    def __len__(self):
        return len(self._attrs)

    def __iter__(self):
        return iter(self._attrs)

    def __contains__(self, name):
        return self.hasattr(name)

    def hasattr(self, name):
        """Returns True if the pen has the requested attribute.

        Raises KeyError for invalid attributes.
        """
        attr = lookup_attr(name)
        if attr == -1:
            raise KeyError('invalid attribute')

        return tickit.tickit_pen_has_attr(self._pen, attr)

    def getattrs(self):
        """Returns a dict of the currently-set attributes."""
        return dict(self._attrs)

    def __getitem__(self, name):
        return self.getattr(name)

    def getattr(self, name):
        """Returns the requested attribute value.

        Raises KeyError for invalid attributes.
        """
        attr = lookup_attr(name)
        if attr == -1:
            raise KeyError('invalid attribute')
        type = tickit.tickit_pen_attrtype(attr)
        if type == AttributeType.color:
            func = tickit.tickit_pen_get_colour_attr
        elif type == AttributeType.bool:
            func = tickit.tickit_pen_get_bool_attr
        elif type == AttributeType.int:
            func = tickit.tickit_pen_get_int_attr

        return func(self._pen, attr)

    def setattrs(self, attrs):
        """Sets attributes against the given dict."""
        for k, v in attrs:
            self.setattr(k, v)

    def __setitem__(self, name, value):
        self.setattr(name, value)

    def setattr(self, name, value):
        """Sets an attribute with the given value.

        Raises KeyError for invalid attributes.
        """
        attr = lookup_attr(name)
        if attr == -1:
            raise KeyError('invalid attribute')
        type = tickit.tickit_pen_attrtype(attr)
        if type == AttributeType.color:
            func = tickit.tickit_pen_set_colour_attr
        elif type == AttributeType.bool:
            func = tickit.tickit_pen_set_bool_attr
        elif type == AttributeType.int:
            func = tickit.tickit_pen_set_int_attr

        self._attrs[name] = value

        return func(self._pen, attr, value)

    def __delitem__(self, name):
        self.delattr(name)

    def delattr(self, name):
        """Deletes the specified attribute."""
        attr = lookup_attr(name)
        if attr == -1:
            raise KeyError('invalid attribute')

        del self._attrs[name]

        tickit.tickit_pen_clear_attr(self._pen, attr)

    def chattrs(self, attrs):
        """Changes attributes from the given dict."""
        for k, v in attrs:
            self.chattr(k, v)

    def chattr(self, name, value=None):
        """Changes an attribute to the given value.

        If no value is given or if the given value is None, deletes the
        attribute instead.

        Raises KeyError on invalid attributes.
        """
        attr = lookup_attr(name)
        if attr == -1:
            raise KeyError('invalid attribute')

        if value is not None:
            self.setattr(name, value)
        else:
            self.delattr(name)

    def _wrap_handler(self, func, data):
        def handler(rawpen, type, event, rawdata):
            args = event.contents

            func(self, type, args, data)

        return tickit.TickitPenEventFn(handler)

    def add_on_changed(self, func, event, data):
        """Adds an event handler for Pen events.

        The provided function must take four arguments: the pen object, the
        event type (as a string), the event arguments (as a TickitEvent
        object), and user data (anything).
        """
        if event not in self._events:
            self._events[event] = []

        func = self._wrap_handler(func, data)
        id = tickit.tickit_bind_event(self._pen, event, func, None)

        self._events[event].append((func, id))

        return id

    def remove_on_changed(self, id):
        """Removes the event handler with the specified id."""
        for event in self._events.keys():
            for handler in self._events[event]:
                if handler[1] == id:
                    tickit.tickit_pen_unbind_event_id(self._pen, id)
                    self._events[event].remove(handler)
                    return

        raise KeyError('unknown handler id')

    def __copy__(self):
        other = Pen()
        tickit.tickit_pen_copy(other._pen, self._pen)
        return other

class Attribute:
    fg     = 'fg'     # tickit.TICKIT_PEN_FG
    bg     = 'bg'     # tickit.TICKIT_PEN_BG
    b      = 'b'      # tickit.TICKIT_PEN_BOLD
    u      = 'u'      # tickit.TICKIT_PEN_UNDER
    i      = 'i'      # tickit.TICKIT_PEN_ITALIC
    rv     = 'rv'     # tickit.TICKIT_PEN_REVERSE
    af     = 'af'     # tickit.TICKIT_PEN_ALTFONT
    strike = 'strike' # tickit.TICKIT_PEN_STRIKE

class AttributeType:
    color = colour = tickit.TICKIT_PENTYPE_COLOUR
    bool  = tickit.TICKIT_PENTYPE_BOOL
    int   = tickit.TICKIT_PENTYPE_INT

__all__ = ['Pen', 'Attribute', 'AttributeType']
