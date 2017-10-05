from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, landscape
from reportlab.platypus import Image, Frame

def draw_box(c, x_0, y_0, w, h):
    from reportlab.lib.units import mm
    c.setFillColorRGB(1,1,1) # Color fill
    c.setLineWidth(0.1)
    c.rect(x_0*mm, y_0*mm, w*mm, h*mm, fill=1) # (x0,y0,w,l)

#def draw_text(c, x_0, y_0, text, size, font, color, rotation):
def draw_text(c, x_0, y_0, text, size):
    from reportlab.lib.units import mm
    c.setFillColorRGB(0,0,0) # Color fill
    c.setFont("Helvetica", size)
    c.drawString(x_0*mm, y_0*mm, text)


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
