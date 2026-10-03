from ti_draw import *
from ti_system import *
from ti_graphics import *
from math import *
selected_color=(2,107,249)#so i don't forget what color the Evo uses for selected stuff in text
E=[
     (),
     ("Hydrogen",1,"H",1.00784,0,1,"1s",32,1312,2.2,0.000082,-259.16,-252.879,"Gas",1,1766),#dum float inaccuracy smh, how tf did it turn into 8.20000... oh, right, E/sci notation
     
     ("Helium",2,"He",4.002602,2,2,"1s**2",37,2372,"N/A",0.000164,"N/A",-268.928,"Gas","N/A",1868),
     
     ("Lithium",3,"Li",6.938,4,3,"1s**2 2s",130,520,"0.98",0.534,180.5,1342,"Solid",1,1817),
     
     ("Beryllium",4,"Be",9.12182,5,4,"1s**2 2s**2",99,899,1.57,1.85,1287,2468,"Solid",2,1828),
     
     ("Boron",5,"B",10.806,6,5,"1s2 2s2 2p",84,801,2.04,2.34,2077,4000,"Solid",3,1808),
     
     ("Carbon",6,"C",12.0096,6,6,"1s2 2s2 2p2",75,1086,2.55,2.2,"N/A",3825,"Solid","+-4(2)","ANCIENT"),
     
     ("Nitrogen",7,"N",14.00643,7,7,"1s2 2s2 2p3",71,1402,3.04,0.001145,-210.0,-195.795,"Gas","+-3(5,4,2)",1772)
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
    global selectable #screw you, python
    draw_box(prev, selected=False)
    clear_rect(40, 0, 160, 50)
    draw_box(new, selected=True)
    try:
        draw_text(75, 25, str(E[new][0]))
        draw_text(160, 50, str(E[new][1]))
        draw_text(75, 50, str(E[new][2]))
        selectable = True
    except IndexError:
        draw_text(75, 25, "N/A")
        draw_text(75, 50, "N/A")
        draw_text(160, 50, "N/A")
        selectable = False
def drawSoftkey(size, pos, text):
    width = size * 62 + (size - 1)
    x = (pos - 1) * 62 + 5 #crunch them numbers
    set_pen("medium","solid")
    draw_rect(x, 210-20, width, 40)
    draw_text(x+5, 212, str(text))
    set_pen("thin","solid")
def draw_table():
    for i in range(1, 119): # i forgor how many elements there are, thanks google
        draw_box(i, selected=(i == selected))
    #fork looking thing from the CE
    draw_rect(48,100, 1, 60)
    draw_rect(48, 160, 8, 1)
    draw_rect(48, 143, 8, 1)
def draw_splash():
    set_color(0, 0, 0)
    draw_text(100, 100, "Periodic Table")
    setFont(4)
    draw_text(160, 120, "V7.0.0.3996")
    draw_text(110, 200, "PRESS ANY KEY")
    draw_text(114, 213, "©2026 CrX1x1")
    setFont(2)
def draw_text_row(y, align, text, is_selected, height=18): 
    
    if align=="middle":
        text_x=160-(6*len(text))
    else:
        text_x=160-(str(text).index(align)+1)*12
    if is_selected:
        set_color(0,0,0)
    else:
        set_color(255,255,255)
    fill_rect(text_x-2,y-(height+1),len(text)*12+3,height+1)
    if is_selected:
        set_color(255,255,255)
    else:
        set_color(0,0,0)
    draw_text(text_x,y,text)
    set_color(0,0,0)
def replace_text_selection(prev, new):
    draw_text_row(60, ":", info_rows[prev], False)
    draw_text_row(60, ":", info_rows[new], True)

prev_selected = 0
selected = 1
current_state = state.splash
setFont(2)
stuff_drawn = False
prev_list_pos = 0
list_pos = 0
selectable = True
while True:
    key = getKey(0)
    if current_state == state.splash:
        if not stuff_drawn:
            #draw static text, of course
            draw_splash()
            stuff_drawn = True
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
                stuff_drawn = False
                break
        clear()
        key = 0
        current_state = state.table
    if current_state == state.table:
        if not stuff_drawn:
            draw_table()
            replace_selection(prev_selected, selected)
            drawSoftkey(2, 1, "OPTIONS")
            drawSoftkey(1, 3, "LIST")
            drawSoftkey(1, 4, "INFO")
            drawSoftkey(1, 5, "QUIT")
            stuff_drawn = True
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
            stuff_drawn = False
        if key == 15: # graph
            #quit
            break
        if key == 105:
            #enter
            if selectable:
                clear()
                current_state = state.info
                stuff_drawn = False
            else:
                #todo, make a "not selectable" message
                pass
    if current_state == state.info:
        charsize = 12 #measurement of how many pixels a character takes up horizontally, will do later, placeholder
        if not stuff_drawn:
            drawSoftkey(1, 1, "SET")
            drawSoftkey(1, 2, "HELP")
            drawSoftkey(1, 3, "LIST")
            drawSoftkey(1, 4, "TBL")
            drawSoftkey(1, 5, "QUIT")
            set_pen("thin","solid")
            
            get_color(selected)
            fill_rect(6, 4, 308, 30)
            set_color(0, 0, 0)
            draw_rect(6, 38, 308, 145)
            draw_rect(6, 4, 308, 30)
            draw_text(160 - (len(str(E[selected][0])) * charsize // 2), 26, str(E[selected][0]))
            stuff_drawn = True
            text_drawn = False
        if not text_drawn:
            if list_pos in range(0, 6):
                draw_text_row(60, ":", "ATOMIC #: "+str(E[selected][1]), list_pos == 0)
                draw_text_row(80, ":", "SYMBOL: "+str(E[selected][2]), list_pos == 1)
                draw_text_row(100, ":", "WEIGHT: "+str(E[selected][3]), list_pos == 2)
                draw_text_row(120, ":", "NEUTRONS: "+str(E[selected][4]), list_pos == 3)
                draw_text_row(140, ":", "PROTONS: "+str(E[selected][5]), list_pos == 4)
                draw_text_row(170, "middle", str(E[selected][6]), list_pos == 5, 20)
            if list_pos in range(6,12):
                draw_text_row(60, ":", "RADIUS: "+str(E[selected][7]), list_pos == 6)
                draw_text_row(80, ":", "1ST IONIZE: "+str(E[selected][8]), list_pos == 7)
                draw_text_row(100, ":", "ELECTRONEG: "+str(E[selected][9]), list_pos == 8)
                draw_text_row(120, ":", "DENSITY: "+str(E[selected][10]), list_pos == 9)
                draw_text_row(140, ":", "MELTING PT: "+str(E[selected][11]), list_pos == 10)
                draw_text_row(160, ":", "BOILING PT: "+str(E[selected][12]), list_pos == 11)
            if list_pos in range(12,15):
                draw_text_row(60, ":", "STATE: "+str(E[selected][13]), list_pos == 12)
                draw_text_row(80, ":", "OX STATES: "+str(E[selected][14]), list_pos == 13)
                draw_text_row(100, ":", "DISCOVERED: "+str(E[selected][15]), list_pos == 14)
            text_drawn = True
        if key == 25:# up
            if list_pos == 0:
                continue
            if list_pos in (6,12):
                 clear_rect(6, 38, 308, 145)
            prev_list_pos = list_pos
            list_pos -= 1
            text_drawn = False
        if key == 34:# down
            if list_pos == 14:
                continue
            if list_pos in (5,11):
                clear_rect(6, 38, 308, 145)
            
            prev_list_pos = list_pos
            list_pos += 1
            text_drawn = False
        if key == 24: #left
            if selected == 1:
                continue
            prev_selected = selected
            selected -= 1
            stuff_drawn = False
            text_drawn = False
            clear_rect(6, 38, 308, 145)
        if key == 26:
            if selected == (len(E)-1):
                continue
            prev_selected = selected
            selected += 1
            stuff_drawn = False
            text_drawn = False
            clear_rect(6, 38, 308, 145)
        if key == 15:
             break
        if key == 14:
            text_drawn = False
            stuff_drawn = False
            clear()
            current_state = state.table