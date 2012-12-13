
from tickit.ctickit import *

class StringPos(tickit.TickitStringPos):
    """String position counters and limits thereunto.
    """
    def __init__(self):
        self.bytes = self.codepoints = self.graphemes = self.columns = 0

    @classmethod
    def zero(cls):
        self = cls()
        return self

    @classmethod
    def limit_bytes(cls, size):
        self = cls()
        self.bytes = size
        self.codepoints = self.graphemes = self.columns = -1
        return self

    @classmethod
    def limit_codepoints(cls, size):
        self = cls()
        self.codepoints = size
        self.bytes = self.graphemes = self.columns = -1
        return self

    @classmethod
    def limit_graphemes(cls, size):
        self = cls()
        self.graphemes = size
        self.bytes = self.codepoints = self.columns = -1
        return self

    @classmethod
    def limit_columns(cls, size):
        self = cls()
        self.columns = size
        self.bytes = self.codepoints = self.graphemes = -1
        return self

    @property
    def bytes(self):
        return self.bytes

    @property
    def codepoints(self):
        return self.codepoints

    @property
    def graphemes(self):
        return self.graphemes

    @property
    def columns(self):
        return self.columns


