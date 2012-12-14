
import tickit

class Cell:
    glyph = '.'

    def __init__(self):
        self.player = False
        self.items = []

    def __str__(self):
        if self.player:
            return '@'
        else:
            return self.glyph

class Talon:
    def __init__(self, name, tin, tout):
        self.name = name
        self.term = tickit.Terminal.find_for_term(utf8=True)
        self.term.input_handle = tin
        self.term.output_handle = tout
        self.msg = ''

        self.term.refresh_size()
        self.rows = self.term.lines - 3
        self.cols = self.term.cols

        self.grid = [
            [Cell() for col in range(self.cols)] for row in range(self.rows)
        ]
        self.player_x = int(self.cols / 2)
        self.player_y = int(self.rows / 2)
        self.grid[self.player_y][self.player_x].player = True

        self.term.on_key = self.input()
        self.term.clear()
        self.render()

        while 1:
            self.term.input_wait()
            self.render()

    def render(self):
        self.term.goto(0, 0)
        self.term.print(self.msg)

        for y in range(self.rows):
            self.term.goto(y + 1, 0)
            row = ''.join([str(x) for x in self.grid[y]])
            self.term.print(bytes(row, 'UTF-8'))

        self.term.goto(self.rows + 1, 0)
        self.term.print('Name: %s' % (self.name))

    def input(self):
        def handler(term, type, event, data):
            self.msg = ' ' * self.cols if not self.msg.startswith(' ') else ''

            key = event.str.decode('UTF-8')
            self.grid[self.player_y][self.player_x].player = False

            if key == 'Up':
                if self.player_y == 0:
                    self.msg = 'My, what a marvelous bedrock wall.'
                else:
                    self.player_y -= 1
            elif key == 'Down':
                if self.player_y == self.rows - 1:
                    self.msg = 'My, what a marvelous bedrock wall.'
                else:
                    self.player_y += 1
            elif key == 'Left':
                if self.player_x == 0:
                    self.msg = 'My, what a marvelous bedrock wall.'
                else:
                    self.player_x -= 1
            elif key == 'Right':
                if self.player_x == self.cols:
                    self.msg = 'My, what a marvelous bedrock wall.'
                else:
                    self.player_x += 1

            self.grid[self.player_y][self.player_x].player = True
        return handler

if __name__ == '__main__':
    import sys

    t = Talon(sys.argv[1], sys.__stdin__.fileno(), sys.__stdout__.fileno())

