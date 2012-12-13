
import sys

import tickit

running = True

def render_key(term, type, str):
    term.goto(2, 2)
    term.print('Key:')
    term.goto(4, 4)
    if type == tickit.KeyEventType.text:
        term.print('text ')
    elif type == tickit.KeyEventType.key:
        term.print('key  ')
    term.print(str)
    term.erasech(16, -1)

def render_mouse(term, type, button, line, col):
    term.goto(8, 2)
    term.print('Mouse:')

    term.goto(10, 4)
    if type == tickit.MouseEventType.press:
        term.print('press   ')
    elif type == tickit.MouseEventType.drag:
        term.print('drag    ')
    elif type == tickit.MouseEventType.release:
        term.print('release ')
    elif type == tickit.MouseEventType.wheel:
        term.print('wheel   ')

    if type == tickit.MouseEventType.wheel:
        wheel = 'down' if button == tickit.MouseWheel.down else 'up'
        term.print('%s at (%d,%d)' % (wheel, line, col))
    else:
        term.print('button %d at (%d, %d)' % (button, line, col))

    term.erasech(8, -1)

def event(term, type, args, user):
    if type == tickit.EventType.resize:
        return
    elif type == tickit.EventType.key:
        if args.type == tickit.KeyEventType.key and args.str == 'Q':
            running = False
            return

        render_key(term, args.type, args.str)
    elif type == tickit.EventType.mouse:
        render_mouse(term, args.type, args.button, args.line, args.col)

def main():
    term = tickit.Terminal.find_for_term(utf8=True)

    term.input_handle  = sys.__stdin__.fileno()
    term.output_handle = sys.__stdout__.fileno()

    term.setctl(tickit.TermControl.altscreen,  True)
    term.setctl(tickit.TermControl.cursorvis,  False)
    term.setctl(tickit.TermControl.mouse,      True)
    term.setctl(tickit.TermControl.keypad_app, True)

    term.clear()

    term.on_key = event
    term.on_mouse = event

    render_key(term, -1, '')
    render_mouse(term, -1, 0, 0, 0)

    while running:
        term.input_wait()

main()
