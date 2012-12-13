
import sys

import tickit

def printf(term, fmt, *args):
    term.print(fmt % args)

term = tickit.Terminal.find_for_term(utf8=True)

term.input_handle  = sys.__stdin__.fileno()
term.output_handle = sys.__stdout__.fileno()
term.setctl(tickit.TermControl.altscreen, True)
term.setctl(tickit.TermControl.cursorvis, True)
term.clear()

defpen = tickit.Pen()
pen = tickit.Pen()

term.goto(0, 0)
term.setpen(defpen)
term.print('ANSI')

term.goto(2, 0)

for i in range(16):
    pen.setattr('bg', i)
    term.setpen(pen)
    printf(term, '[%02d]', i)

term.goto(4, 0)
term.setpen(defpen)
term.print('216 RGB cube')

for y in range(6):
    term.goto(6+y, 0)

    for x in range(36):
        pen.setattr('bg', y * 36 + x + 16)
        term.setpen(pen)
        term.print('  ')

term.goto(13, 0)
term.setpen(defpen)
term.print('24 Grayscale ramp')

term.goto(15, 0)
for i in range(24):
    pen.setattr('bg', 232 + i)

    if i > 12:
        pen.setattr('fg', 0)

    term.setpen(pen)
    printf(term, 'g%02d', i)

term.input_wait()

