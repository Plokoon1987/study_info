from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, landscape
from reportlab.platypus import Image, Frame

def rect_params_pl(x, y, w, h, sheet, ref='LB', r_from='LB'):
    # (x, y) -> One reference point shall be specified ref = (x,y)  
    # (w, h) -> width and Height parameters shall be specified
    # (sheet) -> Tuple of the form (width,heigth) of the dimensions of the sheet
    # (ref=) -> String of the corner of reference, ie: 'LB' stands for LeftBottom corner  
    # (r_from=) -> String of the sides of reference for the measurements of x and y, 
    # ie: 'LB' stands for fromLeft and fromBottom
    
    if r_from == 'RB': x = sheet[0] - x
    elif r_from == 'LT': y = sheet[1] - y
    elif r_from == 'RT': x , y = sheet[0] - x, sheet[1] - y   
    
    if ref == 'RB': x0 = x - w
    elif ref == 'LT': y0 = y - h
    elif ref == 'RT': x0 = x - w; y0 = y - h
      
    return [x, y, x+w, y+h, w, h]

def rect_params_pp(xr, yr, xo, yo, sheet, r_from='LB', o_from='LB'):
    # (xr, yr, xo, yo) -> One reference point shall be specified (xr,yr) as well as the
    # opposite corner pint
    
    #One reference point shall be specified ref = (x,y)
    # Any two points shall be given ref = (xr,yr) and opposite = (xo,yo)  
    # Sheet is the size of the sheet (w,h) they are measured from, ie: Sheet = (200,10)
    # r_from amd o_from are the measurement references to point r and o, ie : 'LB' stands
    # for fromLeft and fromBottom   
    
    if r_from == 'RB': xr = sheet[0] - xr
    elif r_from == 'LT': yr = sheet[1] - yr
    elif r_from == 'RT': xr , yr = sheet[0] - xr, sheet[1] - yr
    
    if o_from == 'RB': xo = sheet[0] - xo
    elif o_from == 'LT': yo = sheet[1] - yo
    elif o_from == 'RT': xo , yo = sheet[0] - xo, sheet[1] - yo

    return [min(xr, xo), min(yr, yo), max(xr, xo), max(yr, yo), abs(xo-xr), abs(yo-yr)]

def draw_box(c, x_0, y_0, w, h):
    from reportlab.lib.units import mm
    c.setFillColorRGB(1,1,1) # Color fill
    c.setLineWidth(0.1)
    c.rect(x_0*mm, y_0*mm, w*mm, h*mm, fill=1) # (x0,y0,w,l)
'''    
def draw_box1(c, sheet, ref, x_0, y_0, w, h, *args):
    from reportlab.lib.units import mm
    
    
    if ref == 'BR': x_0 = x_0 - w
    else if ref == 'TL': y_0 = y_0 - h
    else if ref == 'TR': x_0 = x_0 - w; y_0 = y_0 - h
    
    c.rect(x_0*mm, y_0*mm, w*mm, h*mm, fill=1) # (x0,y0,w,l)
'''
#def draw_text(c, x_0, y_0, text, size, font, color, rotation):
def draw_text(c, x_0, y_0, text, size):
    from reportlab.lib.units import mm
    c.setFillColorRGB(0,0,0) # Color fill
    c.setFont("Helvetica", size)
    c.drawString(x_0*mm, y_0*mm, text)

#def draw_text_List(c, x_0, y_0, text, size):    
        


A3_mm = (421.6, 298.1)

c = canvas.Canvas("hello.pdf", pagesize=landscape(A3))


# ############
# # OUTERBOX #
# ############

x0, y0 = 24, 14.2 # LeftBottomPoint => Dist_from_Left, Dist_from_Bottom
x1, y1 = 9.5, 21.6 # RightTopPoint => Dist_from_Right, Dist_from_Top

draw_box(c, x0, y0, A3_mm[0] - x0 - x1, A3_mm[1] - y0 - y1)


# ############
# # TOPBOXES #
# ############

# Boxes

x0, y0 = 25.1, 43.6 # LeftTopPoint => Dist_from_Left, Dist_from_Top
boxes_length = (70.2, 90.2, 62, 65.9, 37.2, 59.6)
boxes_height = 21.4
box_spac = 0

x_0, y_0, x_1, y_1 = [], [], [], []

for x in range(len(boxes_length)):
    x_0.append(x0)
    y_0.append(A3_mm[1] - y0)
    x_1.append(x0 + boxes_length[x])
    y_1.append(A3_mm[1] - y0 + boxes_height)
    
    draw_box(c, x_0[x], y_0[x], boxes_length[x], boxes_height)
    x0 += boxes_length[x] + box_spac


# Texto Box 1
box_ID = 0

xt, yt = 1, 4 # LeftTopPoint => Dist_from_Left, Dist_from_Top of box
draw_text(c, x_0[box_ID] + xt, y_1[box_ID] - yt, 'CLIENTE:', 9.5)

# Texto Box 2
box_ID = 1

xt, yt = 1, 4 # LeftTopPoint => Dist_from_Left, Dist_from_Top of box
draw_text(c, x_0[box_ID] + xt, y_1[box_ID] - yt, 'TRABAJO:', 9.5)
'''
texto = 'PROYECTO DE CONSTRUCCIÓN LAV CANTÁBRICO'
draw_text(c, x_0[1] + xt, y_1[1] - yt, texto, 9)
'''
# Texto Box 3
box_ID = 2

xt, yt = 1, 4 # LeftTopPoint => Dist_from_Left, Dist_from_Top of box
draw_text(c, x_0[box_ID] + xt, y_1[box_ID] - yt, 'EMPRESA CONSULTORA:', 9.5)

# Texto Box 4

#Titulos
#**********************************
box_ID = 3
xt, yt = 1, 4 # LeftTopPoint => Dist_from_Left, Dist_from_Top of box
vert_spac = 5
Titulos = ['Supervisor:', 'Empresa:', 'Sondista:', 'Equipo:']
Size = 8
# *********************************

for ID in range(len(Titulos)):
    if ID == 0: 
        draw_text(c, x_0[box_ID] + xt, y_1[box_ID] - yt, Titulos[ID] , Size)
        v_spac = 0
    else: 
        draw_text(c, x_0[box_ID] + xt, y_1[box_ID] - yt - v_spac, Titulos[ID] , Size)
    v_spac += vert_spac




# ############
# # BODYBOXES #
# ############

x0, y0 = 25, 26.7 # LeftBottomPoint => Dist_from_Left, Dist_from_Bottom
boxes_length = (26.5,114,4.5,16.4,10.7,11.9,19.5,16.3,35.1,129.1)
boxes_height = (198.5, 28.5)
spac = 0.25

for x in range(len(boxes_length)):
    draw_box(c, x0, y0, boxes_length[x], boxes_height[0])
    draw_box(c, x0, y0 + boxes_height[0], boxes_length[x], boxes_height[1])
    x0 += boxes_length[x] + spac


# ###############
# # BOTTOMBOXES #
# ###############

x0, y0 = 24.6, 15.8 # LeftBottomPoint => Dist_from_Left, Dist_from_Bottom
boxes_length = (166.8, 219.2)
boxes_height = 10.5
spac = 0.5

for x in range(len(boxes_length)):
    draw_box(c, x0, y0, boxes_length[x], boxes_height)
    x0 += boxes_length[x] + spac

c.showPage()
c.save()
'''
print(rect_params_pl(2, 3, 4, 5, (10,10), ref='LB', r_from='LB'))
print(rect_params_pl(8, 3, 4, 5, (10,10), ref='LB', r_from='RB'))
print(rect_params_pl(2, 7, 4, 5, (10,10), ref='LB', r_from='LT'))
print(rect_params_pl(8, 7, 4, 5, (10,10), ref='LB', r_from='RT'))
print('')
print(rect_params_pl(4, 3, 1, 3, (10,10), ref='LB', r_from='LB'))
print(rect_params_pl(5, 3, 1, 3, (10,10), ref='RB', r_from='LB'))
print(rect_params_pl(4, 6, 1, 3, (10,10), ref='LT', r_from='LB'))
print(rect_params_pl(5, 6, 1, 3, (10,10), ref='RT', r_from='LB'))
'''
print()
print('pp')
print(rect_params_pp(5, 5, 95, 95, (100,100), r_from='LB', o_from='LB'))
print(rect_params_pp(5, 5, 5, 95, (100,100), r_from='LB', o_from='RB'))
print(rect_params_pp(5, 5, 95, 5, (100,100), r_from='LB', o_from='LT'))
print(rect_params_pp(5, 5, 5, 5, (100,100), r_from='LB', o_from='RT'))

