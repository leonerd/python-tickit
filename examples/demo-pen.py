
import sys

import tickit

colors = {
    1: 'red',
    2: 'green',
    3: 'yellow',
    4: 'blue'
}

attrs = {
    'bold':          'b',
    'underline':     'u', #tickit.PenAttr.u,
    'italic':        'i', #tickit.PenAttr.i,
    'strikethrough': 'strike', #tickit.PenAttr.strike,
    'reverse video': 'rv', #tickit.PenAttr.rv
}

term   = tickit.Terminal(utf8=True)
defpen = tickit.Pen()
pen    = tickit.Pen()

term.input_handle  = sys.__stdin__.fileno()
term.output_handle = sys.__stdout__.fileno()
term.setctl(tickit.TermControl.altscreen, True)
term.setctl(tickit.TermControl.cursorvis, False)
term.clear()

term.goto(0, 0)
for i in range(4):
    pen.setattr('fg', i)
    term.setpen(pen)
    term.print('fg %s' % (colors[i]))
    term.setpen(defpen)
    term.print('     ')

term.goto(2, 0)
for i in range(4):
    pen.setattr('fg', i+8)
    term.setpen(pen)
    term.print('fg hi-%s' % (colors[i]))
    term.setpen(defpen)
    term.print('     ')

pen.setattr('fg', 0)

term.goto(4, 0)
for i in range(4):
    pen.setattr('bg', i)
    term.setpen(pen)
    term.print('bg %s' % (colors[i]))
    term.setpen(defpen)
    term.print('     ')

term.goto(6, 0)
for i in range(4):
    pen.setattr('bg', i+8)
    term.setpen(pen)
    term.print('bg hi-%s' % (colors[i]))
    term.setpen(defpen)
    term.print('     ')

pen.delattr('fg')
pen.delattr('bg')

i = 0

for k, v in attrs.items():
    term.goto(8 + 2*i, 0)
    pen.setattr(v, True)
    term.setpen(pen)
    term.print(k)
    term.setpen(defpen)
    pen.delattr(v)
    i += 1

term.goto(18, 0)
pen.setattr('af', True)
term.setpen(pen)
term.print('alternate font')
term.input_wait()

