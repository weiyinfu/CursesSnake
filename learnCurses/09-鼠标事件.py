import curses

scr = curses.initscr()

print(scr.getmaxyx())

while 1:
    x = scr.getch()
    if x == curses.KEY_MOUSE:
        res = curses.getmouse()
        print(res)
    else:
        print("keyboard", x)
