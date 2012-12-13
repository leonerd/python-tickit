
from tickit.ctickit import *

try:
    from collections.abc import MutableMapping
except ImportError:
    from collections import MutableMapping

def lookup_attr(name):
    attr = bytes(name, 'ascii')
    return ctickit.tickit_pen_lookup_attr(attr)

class Pen(MutableMapping):
    """An object for storing terminal attributes.

    Pens are used by Terminal objects to alter how output is formatted and may
    be assigned to such via their chpen() and setpen() methods.

    This API mirrors the Tickit::Pen API and additionally implements Pythonic
    methods (the usual Mapping methods are available).
    """
    def __init__(self, **kwargs):
        self._pen = ctickit.tickit_pen_new()
        self._attrs = {}

        self._changed = {}

        self.setattrs(kwargs)

    def __len__(self):
        return len(self._attrs)

    def __iter__(self):
        return iter(self._attrs)

    def __contains__(self, name):
        return self.hasattr(name)

    def hasattr(self, name):
        attr = lookup_attr(name)
        if attr == -1:
            raise KeyError('invalid attribute')

        return ctickit.tickit_pen_has_attr(self._pen, attr)

    def getattrs(self):
        return dict(self._attrs)

    def __getitem__(self, name):
        return self.getattr(name)

    def getattr(self, name):
        attr = lookup_attr(name)
        if attr == -1:
            raise KeyError('invalid attribute')
        type = ctickit.tickit_pen_attrtype(attr)
        if type == AttributeType.color:
            func = ctickit.tickit_pen_get_colour_attr
        elif type == AttributeType.bool:
            func = ctickit.tickit_pen_get_bool_attr
        elif type == AttributeType.int:
            func = ctickit.tickit_pen_get_int_attr

        return func(self._pen, attr)

    def setattrs(self, attrs):
        for k, v in attrs:
            self.setattr(k, v)

    def __setitem__(self, name, value):
        self.setattr(name, value)

    def setattr(self, name, value):
        attr = lookup_attr(name)
        if attr == -1:
            raise KeyError('invalid attribute')
        type = ctickit.tickit_pen_attrtype(attr)
        if type == AttributeType.color:
            func = ctickit.tickit_pen_set_colour_attr
        elif type == AttributeType.bool:
            func = ctickit.tickit_pen_set_bool_attr
        elif type == AttributeType.int:
            func = ctickit.tickit_pen_set_int_attr

        self._attrs[name] = value

        return func(self._pen, attr, value)

    def __delitem__(self, name):
        self.delattr(name)

    def delattr(self, name):
        attr = lookup_attr(name)
        if attr == -1:
            raise KeyError('invalid attribute')

        del self._attrs[name]

        ctickit.tickit_pen_clear_attr(self._pen, attr)

    def chattrs(self, attrs):
        for k, v in attrs:
            self.chattr(k, v)

    def chattr(self, name, value=None):
        attr = lookup_attr(name)
        if attr == -1:
            raise KeyError('invalid attribute')

        if value is not None:
            self.setattr(name, value)
        else:
            self.delattr(name)

    def add_on_changed(self, obj, id):
        """Adds an event handler for Pen events.

        Note that the event object must implement the callable interface as a
        function which takes a Pen, an EventType, a list of Event arguments,
        and the ID passed to this method.
        """
        if not hasattr(obj, '__call__'):
            raise TypeError('event handler must be callable')

        self._changed.append((obj, id))

        ctickit.tickit_pen_bind_event(self._pen, obj.event_type, obj, id)

    def remove_on_changed(self, obj):
        for item in self._changed:
            if item[0] is obj:
                self._changed.remove((obj, item[1]))
                id = item[1]
                break

        ctickit.tickit_pen_unbind_event(self._pen, id)

    def __copy__(self):
        other = Pen()
        ctickit.tickit_pen_copy(other._pen, self._pen)
        return other

class Attribute:
    fg     = tickit.TICKIT_PEN_FG
    bg     = tickit.TICKIT_PEN_BG
    b      = tickit.TICKIT_PEN_BOLD
    u      = tickit.TICKIT_PEN_UNDER
    i      = tickit.TICKIT_PEN_ITALIC
    rv     = tickit.TICKIT_PEN_REVERSE
    af     = tickit.TICKIT_PEN_ALTFONT
    strike = tickit.TICKIT_PEN_STRIKE

class AttributeType:
    color = colour = tickit.TICKIT_PENTYPE_COLOUR
    bool  = tickit.TICKIT_PENTYPE_BOOL
    int   = tickit.TICKIT_PENTYPE_INT

__all__ = ['Pen', 'Attribute', 'AttributeType']
