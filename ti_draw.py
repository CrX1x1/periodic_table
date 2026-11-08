import ti_graphics as g

STATUS = 30
DIM_W = 320
DIM_H = 210

#window state (pixel mode by default)
_use_window = False
_xmin, _xmax, _ymin, _ymax = 0, DIM_W-1, 0, DIM_H-1
def clear():
    g.cls()
def set_color(r, green, b):
    if r < 0 or r > 255 or green < 0 or green > 255 or b < 0 or b > 255:
        raise TypeError("expected (red,green,blue) tuple.")
    g.setColor((r, green, b))
def set_pen(size, style):
    g.setPen(size, style)
def get_screen_dim():
    return [DIM_W-1, DIM_H-1]
def set_window(xmin, xmax, ymin, ymax):
    global _xmin, _xmax, _ymin, _ymax, _use_window
    if xmin is None or xmax is None or ymin is None or ymax is None:
        _use_window = False
        return
    if xmin >= xmax:
        raise ValueError("Invalid x range.")
    if ymin >= ymax:
        raise ValueError("Invalid y range.")
    _xmin = xmin
    _xmax = xmax
    _ymin = ymin
    _ymax = ymax
    _use_window = True
def _map(x, y):
    global _use_window, _xmin, _xmax, _ymin, _ymax
    if not _use_window:
        return x, y + STATUS
    px = (x - _xmin) * (DIM_W - 1) / (_xmax - _xmin)
    # y is inverted because the screen origin is at the top-left
    py = (1 - (y - _ymin) / (_ymax - _ymin)) * (DIM_H - 1) + STATUS
    return px, py
def draw_line(x1, y1, x2, y2):
    p1 = _map(x1, y1)
    p2 = _map(x2, y2)
    g.drawLine(p1[0], p1[1], p2[0], p2[1])
def draw_rect(x, y, w, h):
    p1 = _map(x, y)
    p2 = _map(x + w, y + h)
    g.drawRect(p1[0], p1[1], p2[0] - p1[0], p2[1] - p1[1])
def fill_rect(x, y, w, h):
    p1 = _map(x, y)
    p2 = _map(x + w, y + h)
    g.fillRect(p1[0], p1[1], p2[0] - p1[0], p2[1] - p1[1])
def draw_circle(x, y, r):
    cx, cy = _map(x, y)
    g.drawArc(cx - r, cy - r, 2 * r, 2 * r, 0, 3600) # good enough
def fill_circle(x, y, r):
    cx, cy = _map(x, y)
    g.fillCircle(cx, cy, r)
def draw_text(x, y, text):
    px, py = _map(x, y)
    g.draw_string(px, py, text)
def clear_rect(x, y, w, h):
    old = g._color
    g.setColor((255, 255, 255))
    fill_rect(x, y, w, h)
    g.setColor(old)
def plot_xy(x, y, sh=1):
    fill_circle(x, y, 2)#whatever
def fill_poly(xlist, ylist):
    if len(xlist) != len(ylist):
        raise ValueError("Lists must be the same length.")
    points = [_map(x, y) for x, y in zip(xlist, ylist)]
    if len(points) >= 3:
        g.fillPolygon([p[0] for p in points], [p[1] for p in points])
def show_draw():
    import ti_system
    ti_system.wait_key() #blocks till keypress
    