from ti_draw import *

a=["thin", "medium", "thick"]
for i in a:
 set_pen(i, "solid")
 draw_rect(a.index(i)*13, 10, 50, 50)