import curses
import logging


class File:
    def __init__(self, filepath):
        self.file = open(filepath, 'w')

    def info(self, s):
        self.file.write(s)
        if not s.endswith('\n'):
            self.file.write('\n')


log = File("color.md")

scr = curses.initscr()
scr.addstr("\n\n# 颜色")
curses.start_color()

"""
curses中与颜色有关的三个函数：
* start_color:颜色初始化，启用颜色
* color_pair(id):使用颜色id
* init_pair(n,foreground,background):注册id=>(前景色，背景色)的映射。
* can_change_color():是否允许注册终端颜色

 颜色对由前景色和背景色组成。 init_pair(n, f, b) 函数可改变颜色对 n 的定义 为前景色 f 和背景色 b。 颜色对 0 硬编码为黑底白字，不能改变。

颜色已经被编号，并且当其激活 color 模式时 start_color() 会初始化 8 种基本颜色。 它们是: 0:black, 1:red, 2:green, 3:yellow, 4:blue, 5:magenta, 6:cyan 和 7:white
"""

scr.addstr("Pretty text\n", curses.color_pair(1))
log.info(f"# COLORS={curses.COLORS}")
for i in range(curses.COLORS):
    log.info(f"* color_content={curses.color_content(i)}")
log.info(f"# COLOR_PAIRS={curses.COLOR_PAIRS}")
for i in range(curses.COLOR_PAIRS):
    log.info(f"* pair_content={curses.pair_content(i)}  color_pair={curses.color_pair(i)}")
scr.addstr(f"can change color={curses.can_change_color()}")
scr.getch()
