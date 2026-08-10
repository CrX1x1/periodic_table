from ti_draw import *

nonmetal_color=(200,255,200)
E=[
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


size=17
sx=6
sy=7

def boxpos(a):
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

set_color(200,200,200)

for i in range(119): # i forgor how many elements there are, thanks google
    temp = boxpos(i)
    set_color(85, 85, 85)
    draw_rect(temp[0], temp[1], size, size)
    if i in nm:
        set_color(0, 240, 0)
    elif i in hg:
        set_color(0, 222, 191)
    elif i in ng:
        set_color(143, 170, 255)
    elif i in am:
        set_color(255,171,0)
    elif i in aem:
        set_color(255,255,0)
    elif i in met:
        set_color(83, 207, 144)
    elif i in post:
        set_color(161, 188, 175)
    elif i in tm:
        set_color(224, 156, 160)
    elif i in lan:
        set_color(255, 171, 144)
    elif i in act:
        set_color(224, 171, 207)
    else:
        set_color(240, 240, 240)
    fill_rect(temp[0], temp[1], size, size)
show_draw()
selected = 1
while True:
    key = get_key()
    
