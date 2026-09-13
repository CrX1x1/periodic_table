from ti_draw import *
from ti_system import *
from ti_graphics import *
from math import *
nonmetal_color=(200,255,200)
E=[
     (),
     ("Hydrogen",1,"H",1.00784,0,1,"1s",32,1312,2.2,0.000082,-259.16,252.879,"Gas",1,1766),
     
     ("Helium",2,"He",4.002602,2,2,"1s**2",37,2372,"N/A",0.000164,"N/A",-268.928,"Gas","N/A",1868)
]
#types of elements
nm = (1, 6, 7, 8, 15, 16, 34) # reactive nonmetals
ng = (2, 10, 18, 36, 54, 86, 118) # noble gases
am = (3, 11, 19, 37, 55, 87) # alkali metals
aem = (4, 12, 20, 38, 56, 88) # alkaline earth metals
met = (5, 14, 32, 33, 51, 52, 84) # metalloids
hg = (9, 17, 35, 53, 85, 117) # halogens
post = (13, 31, 49, 50, 81, 82, 83, 113, 114, 115, 116) # post-transition metals
tm = (
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
    72, 73, 74, 75, 76, 77, 78, 79, 80,
    104, 105, 106, 107, 108, 109, 110, 111, 112
) # transition metals
lan = tuple(range(57, 72)) # lanthanides (57-71)
act = tuple(range(89, 104)) # actinides (89-103)

class state:
    table = 0
    info = 1
    list = 2
    graph = 3
    splash = 4
class type:
    name = 0
    atomic_number = 1
    symbol = 2
    atomic_mass = 3
    electronegativity = 4
    ionization_energy = 5
    atomic_radius = 6
    melting_point = 7
    boiling_point = 8
    density = 9
    phase_at_room_temp = 10
    year_discovered = 11

size=17
sx=6
sy=7

def boxpos(a): # why did this take so long
    if a == 1:
        return (sx, sy)
    if a == 2:
        return (sx + 17 * size, sy)

    if 3 <= a <= 4:
        return (sx + (a - 3) * size, sy + size)
    if 5 <= a <= 10:
        return (sx + (a + 7) * size, sy + size)

    if 11 <= a <= 12:
        return (sx + (a - 11) * size, sy + 2 * size)
    if 13 <= a <= 18:
        return (sx + (a - 1) * size, sy + 2 * size)

    if 19 <= a <= 36:
        return (sx + (a - 19) * size, sy + 3 * size)

    if 37 <= a <= 54:
        return (sx + (a - 37) * size, sy + 4 * size)

    if 55 <= a <= 56:
        return (sx + (a - 55) * size, sy + 5 * size)
    if 72 <= a <= 86:
        return (sx + (a - 69) * size, sy + 5 * size)
        
    if 87 <= a <= 88:
        return (sx + (a - 87) * size, sy + 6 * size)
    if 104 <= a <= 118:
        return (sx + (a - 101) * size, sy + 6 * size)
        

    gap = size // 2
    if 57 <= a <= 71 :
        return (sx + (a - 54) * size, sy + 7 * size + gap)
    if 89 <= a <= 103:
        return (sx + (a - 86) * size, sy + 8 * size + gap)
        
    

    return (sx, sy)

def draw_box(a, selected=False): #finally putting abstraction to use lol
    pos = boxpos(a)
    x, y = pos[0], pos[1]

    get_color(a)
    fill_rect(x, y, size, size)

    if selected:
        set_color(0, 0, 0)
        draw_rect(x, y, size, size)
        draw_rect(x + 1, y + 1, size - 2, size - 2)
    else:
        set_color(85, 85, 85)
        draw_rect(x, y, size, size)

def get_color(a): #had to use some dumb screenshot from the calculator as ref
    if a in nm:
        set_color(0, 240, 0)
    elif a in hg:
        set_color(0, 222, 191)
    elif a in ng:
        set_color(143, 170, 255)
    elif a in am:
        set_color(255,171,0)
    elif a in aem:
        set_color(255,255,0)
    elif a in met:
        set_color(83, 207, 144)
    elif a in post:
        set_color(161, 188, 175)
    elif a in tm:
        set_color(224, 156, 160)
    elif a in lan:
        set_color(255, 171, 144)
    elif a in act:
        set_color(224, 171, 207)
    else:
        set_color(240, 240, 240)
    
def replace_selection(prev, new):
    draw_box(prev, selected=False)
    clear_rect(40, 0, 160, 50)
    draw_box(new, selected=True)
    try:
        draw_text(75, 25, str(E[new][0]))
        draw_text(160, 50, str(E[new][1]))
        draw_text(75, 50, str(E[new][2]))
    except IndexError:
        draw_text(75, 25, "N/A")
        draw_text(75, 50, "N/A")
        draw_text(160, 50, "N/A")
def drawSoftkey(size, pos, text):
    width = size * 62 + (size - 1)
    x = (pos - 1) * 62 + 5 #crunch them numbers
    set_pen("medium","solid")
    draw_rect(x, 210-20, width, 40)
    draw_text(x+5, 212, str(text))
    set_pen("thin","solid")
def draw_table():
    for i in range(1, 119): # i forgor how many elements there are, thanks google
        draw_box(i, selected=(i == 1))
def draw_splash():
    set_color(0, 0, 0)
    draw_text(100, 100, "Periodic Table")
    setFont(4)
    draw_text(160, 120, "V7.0.0.3996")
    draw_text(120, 200, "PRESS ANY KEY")
    draw_text(120, 213, "©2026 CrX1x1")
    setFont(2)


prev_selected = 0
selected = 1
current_state = state.splash
setFont(2)
softkeys_drawn = False
table_drawn = False
splash_drawn = False
while True:
    key = getKey(0)
    if current_state == state.splash:
        if not splash_drawn:
            #draw static text, of course
            draw_splash()
            splash_drawn = True
        # animation that i made on-calculator when i got bored
        cx = 40
        cy = 90
        orbit_rad = 30
        electron_rad = 3

        set_color(255, 0, 0)
        fill_circle(cx, cy, 5)  # draw the singular proton in the center

        # plus sign
        set_color(255, 255, 255)
        draw_line(cx-2, cy, cx+2, cy)
        draw_line(cx, cy-2, cx, cy+2)

        # draw the electron orbit
        set_color(100, 100, 100)
        draw_circle(cx, cy, orbit_rad)

        #previous pos
        prev_ex = cx + orbit_rad
        prev_ey = cy

        while True:
            for deg in range(0, 360, 5):
                key = getKey(0)
                if key != 0:
                    break
                angle = radians(deg)
                ex = cx + orbit_rad * cos(angle)
                ey = cy + orbit_rad * sin(angle)
                clear_rect(prev_ex - electron_rad, prev_ey - electron_rad - 1, (electron_rad * 2) + 2, (electron_rad * 2) + 2)
                set_color(100, 100, 100)
                draw_circle(cx, cy, orbit_rad)
                set_color(0, 0, 255)
                fill_circle(ex, ey, electron_rad)
                prev_ex, prev_ey = ex, ey
            if key != 0:
                break
        clear()
        current_state = state.table
    if current_state == state.table:
        if not table_drawn:
            draw_table()
            replace_selection(prev_selected, selected)
            table_drawn = True
        if not softkeys_drawn:
            drawSoftkey(2, 1, "OPTIONS")
            drawSoftkey(1, 3, "LIST")
            drawSoftkey(1, 4, "INFO")
            drawSoftkey(1, 5, "QUIT")
            softkeys_drawn = True
        if key == 0:
            continue
        if key == 24: #left
            if selected == 1:
                continue
            prev_selected = selected
            selected -= 1
            replace_selection(prev_selected, selected)
        if key == 26: #right
            if selected == 118:
                continue
            prev_selected = selected
            selected += 1
            replace_selection(prev_selected, selected)
        if key == 25: #up, save my sanity
            if selected in (1, 2, 4, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 5, 6, 7, 8, 9):
                continue
            prev_selected = selected
            if selected == 3:
                selected = 1
            elif selected == 10:
                selected = 2
            elif 11 <= selected <= 20:
                selected -= 8
            elif 31 <= selected <= 56:
                selected -= 18
            elif 57 <= selected <= 71:
                selected += 47
            elif 72 <= selected <= 118:
                selected -= 32    
            replace_selection(prev_selected, selected)
            continue
        if key == 34: #down
            if 87 <= selected <= 103 or selected == 39:
                continue
            prev_selected = selected
            if selected == 1:
                selected = 3
            elif selected == 2:
                selected = 10
            elif 3 <= selected <= 12:
                selected += 8
            elif 13 <= selected <= 38:
                selected += 18
            elif 40 <= selected <= 86:
                selected += 32
            elif 104 <= selected <= 118:  
                selected -= 47
            replace_selection(prev_selected, selected)
            continue
        if key in (11, 12): # y= and window
            #todo
            pass
        if key == 13: # zoom
            #todo
            pass
        if key == 14: # trace
            #splash screen
            clear()
            current_state = state.splash
        if key == 15: # graph
            #quit
            break