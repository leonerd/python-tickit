
try:
    from collections.abc import MutableSequence
except ImportError:
    from collections import MutableSequence

from tickit.ctickit import *

from tickit.rect import Rect

class RectSet(MutableSequence):
    def __init__(self):
        self._set = ctickit.tickit_rectset_new()
        self._rects = []

    def __len__(self):
        return len(self._rects)

    def __contains__(self, value):
        return bool(ctickit.tickit_rectset_contains(self._set, value._rect))

    def __iter__(self):
        return iter(self._rects)

    def discard(self, value):
        self.subtract(self, value)

    def subtract(self, value):
        ctickit.tickit_rectset_subtract(self._set, value._rect)
        self._update()

    @property
    def rects(self):
        return self._rects

    def _update(self):
        count = ctickit.tickit_rectset_rects(self._set)
        rect_arr = tickit.TickitRect * count
        rects = rect_arr()
        newcount = ctickit.tickit_rectset_get_rects(self._set, rects, count)
        self._rects = [Rect(obj=x) for x in rects]

    def add(self, rect):
        ctickit.tickit_rectset_add(self._set, rect._rect)
        self._update()

    def clear(self):
        ctickit.tickit_rectset_clear(self._set)
        self._rects = []

    def intersects(self, rect):
        return bool(ctickit.tickit_rectset_intersects(self._set, rect._rect))

    def contains(self, rect):
        return rect in self

