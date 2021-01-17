
# 文档
https://docs.python.org/zh-cn/3/howto/curses.html#curses-howto

https://docs.python.org/zh-cn/3/library/curses.html

# 颜色
以下颜色注册两个函数只有在can_change_color()为True的情况下才可以使用。

curses.init_color(color_number,R,G,B)
可以注册的颜色个数有限，0到curses.COLORS之间。
注册的颜色可以是RGB三种颜色,R，G，B的取值在0到1000之间。

curses.init_pair(pair_number,fg,bg)
可以注册前景背景色，fg和bg必须是0~COLORS-1之间的数值，表示一种颜色。pair_number必须是0~COLOR_PAIRS-1之间的数值。  

curses.pair_content获取color的pair

# 注意事项
调用`window.addchr()`，如果数组下标越界或者光标在右下角，则会抛出一个异常来。