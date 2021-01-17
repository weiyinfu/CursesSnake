"""
A_BLINK 闪烁文本
A_BOLD 超亮或粗体文本
A_DIM 半明亮文本
A_REVERSE 反相显示文本
A_STANDOUT 可用的最佳突出显示模式
A_UNDERLINE 带下划线的文本
"""
import curses

scr = curses.initscr()
scr.addstr('# 文本属性\n')
scr.addstr("* blink\n", curses.A_BLINK)
scr.addstr("* bold\n", curses.A_BOLD)
scr.addstr("* dim\n", curses.A_DIM)
scr.addstr("* reverse\n", curses.A_REVERSE)
scr.addstr("* standout\n", curses.A_STANDOUT)
scr.addstr("* underline\n", curses.A_UNDERLINE)
scr.getch()