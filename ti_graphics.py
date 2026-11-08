import pygame
import math
from pygame import gfxdraw

_screen = None
_color = (255, 255, 255)
_pen_width = 1
_font_size = 3
_font_metrics = {
    0: (6, 8),
    1: (10, 12),
    2: (12, 16),
    3: (10, 12),
    4: (6, 8)
}
_width, _height = 320, 240
m_font = None
s_font = None
class Font:
    SMALL = 0
    MEDIUM = 1
    LARGE = 2
    ICON = 3
    SMALLD = 4

class Color:
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    CYAN = (0, 255, 255)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

def _init():
    
    global m_font, s_font
    global _screen
    if _screen is None:
        pygame.init()
        _screen = pygame.display.set_mode((_width, _height))
        pygame.display.set_caption("Preview")
        cls()
    if m_font is None or s_font is None:
        m_font = pygame.font.Font("EvoFont.ttf", 24)
        s_font = pygame.font.Font("EvoFont.ttf", 16)

def _flip():
    pygame.event.pump()
    pygame.display.flip()
    pygame.time.wait(10)

def cls():
    _init()
    _screen.fill((255, 255, 255))
    pygame.draw.rect(_screen, (108, 108, 108), (0, 0, 320, 30))
    _flip()

def setColor(rgb):
    global _color
    try:
        _color = rgb[0], rgb[1], rgb[2]
    except:
        raise TypeError("expected (red, green, blue) tuple.")
def setPen(size, style):
    global _pen_width
    _pen_width = {"thin": 1, "medium": 2, "thick": 3}.get(size, 1)
    #will do style later lol

def setFont(size):
    global _font_size
    if 0<=size<=4:
        _font_size = size
    else:
        raise ValueError("font selection not available.")
def string_size(text, font=None):
    if font is None:
        font = _font_size
    if 0<=font<=4:
        return len(text) * _font_metrics[font][0], _font_metrics[font][1]
    else:
        raise ValueError("font selection not available.")


def draw_string(x, y, text):
    _init()
    text = str(text)
    fw, fh = string_size(text)
    if fh == 12:
        font = m_font
    else:
        font = s_font
    surface = font.render(text, False, _color)
    _screen.blit(surface, (int(x), int(y)-fh))
    _flip()

# drawing

def setPixel(x, y, color):
    _init()
    x, y, = int(x), int(y)
    if color and len(color) != 3:
        raise TypeError("expected (red, green, blue) tuple.")
    if 0 <= x < _width and 0 <= y < _height:
        _screen.set_at((x, y), color)
        _flip()

def getPixel(x, y):
    _init()
    x, y = int(x), int(y)
    if 0 <= x < _width and 0 <= y < _height:
        return _screen.get_at((x, y))
    else:
        raise ValueError("coordinates out of range. This can crash the calculator.")
def drawLine(x1, y1, x2, y2):
    _init()
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    pygame.draw.line(_screen, _color, (x1, y1), (x2, y2), _pen_width)
    _flip()
def drawRect(x, y, w, h):
    _init()
    x, y, w, h = int(x), int(y), int(w), int(h)
    pygame.draw.rect(_screen, _color, (x, y, w, h), _pen_width)
    _flip()
def fillRect(x, y, w, h):
    _init()
    x, y, w, h = int(x), int(y), int(w), int(h)
    pygame.draw.rect(_screen, _color, (x, y, w, h))
    _flip()
def fillCircle(x, y, r):
    ''' position, radius '''
    _init()
    x, y, r = int(x), int(y), int(r)
    pygame.draw.circle(_screen, _color, (int(x), int(y)), int(r))
    _flip()
def drawArc(x, y, w, h, start, sweep):
    _init()
    rect = pygame.Rect(int(x), int(y), int(w), int(h))
    start_rad = math.radians(-start/10)
    end_rad = math.radians(-(start+sweep)/10)
    pygame.draw.arc(_screen, _color, rect, start_rad, end_rad, _pen_width)
    _flip()

def fillArc(x, y, w, h, start, sweep):# so there is no way to do this except with polygon lol, thanks AI
    _init()
    cx = x + w / 2
    cy = y + h / 2
    points = [(cx, cy)]
    steps = max(16, int(abs(sweep)) // 20)
    for i in range(steps + 1):
        angle = math.radians(-(start + sweep * i / steps)/10)
        points.append((cx + w / 2 * math.cos(angle), cy + h / 2 * math.sin(angle)))
    pygame.draw.polygon(_screen, _color, points)
    _flip()
def hsv_to_rgb(h, s=1.0, v=1.0): #hue is 360 on calc
    import colorsys
    r, g, b = colorsys.hsv_to_rgb(h/360, s, v)
    return int(r * 255), int(g * 255), int(b * 255)

# useless stubs, again
def drawImage(*args, **kwargs):
    print("drawImage is not implemented.")
def checkImageExists(name):
    return False
def pushImage():
    pass
def popImage():
    pass
def drawPolyLine(points):
    pass
def fillPolygon(*args):
    pass