from rectangle_data import rect_data

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, landscape
from reportlab.platypus import Image, Frame
from reportlab.lib.units import mm

def draw_box(c, x0, y0, w, h):
    x0, y0, w, h = x0*sheet_to[0], y0*sheet_to[1], w*sheet_to[0], h*sheet_to[1]
    c.setFillColorRGB(1,1,1) # Color fill
    c.setLineWidth(0.1)
    c.rect(x0, y0, w, h, fill=1) # (x0,y0,w,l)

#def draw_text(c, x_0, y_0, text, size, font, color, rotation):
def draw_text(c, x0, y0, text, size):
    x0, y0 = x0*sheet_to[0], y0*sheet_to[1]
    c.setFillColorRGB(0,0,0) # Color fill
    c.setFont("Helvetica", size)
    c.drawString(x0, y0, text)







  
sheet_from = (421.6, 298.1)
sheet_to = (A3[1], A3[0])
c = canvas.Canvas("hello.pdf", pagesize=landscape(A3))


# ############
# # OUTERBOX #
# ############

r_data = rect_data(sheet_from, ratio=True, w_l=24, w_r=9.5, h_b=14.2, h_t=21.6)
draw_box(c, r_data['w_l'], r_data['h_b'], r_data['w_c'], r_data['h_c'])
 
 

# ############
# # TOPBOXES #
# ############

# Boxes

x_l = 25.1  # Applies to first box, to set up starting point
y_t , y_c = 22.2, 21.4 # Common to all boxes
boxes_length = (70.2, 90.2, 62, 65.9, 37.2, 59.6)
w_spac = 0
tbox = []

for l in boxes_length: 
    r_data = rect_data(sheet_from, ratio=True, w_l=x_l, w_c=l, h_t=y_t, h_c=y_c)   
    draw_box(c, r_data['w_l'], r_data['h_b'], r_data['w_c'], r_data['h_c'])
    tbox.append(r_data)
    x_l += l + w_spac


# Texto Box 1
box_ID = 0
xt, yt = 0.003, 0.015 # Dist_from_Left, Dist_from_Top of box in ratio!!
draw_text(c, tbox[box_ID]['w_l'] + xt, 1 - tbox[box_ID]['h_t'] - yt, 'CLIENTE:', 8)


# Texto Box 2 (VALORES *******)
box_ID = 1
xt, yt = 0.003, 0.015 # Dist_from_Left, Dist_from_Top of box in ratio!!
draw_text(c, tbox[box_ID]['w_l'] + xt, 1 - tbox[box_ID]['h_t'] - yt, 'TRABAJO:', 8)

texto = 'PROYECTO DE CONSTRUCCIÓN LAV CANTÁBRICO'
xt, yt = 0.004, 0.05 # Dist_from_Left, Dist_from_Top of box in ratio!!
draw_text(c, tbox[box_ID]['w_l'] + xt, 1 - tbox[box_ID]['h_t'] - yt, texto, 9.5)


# Texto Box 3
box_ID = 2
xt, yt = 0.003, 0.015 # Dist_from_Left, Dist_from_Top of box in ratio!!
draw_text(c, tbox[box_ID]['w_l'] + xt, 1 - tbox[box_ID]['h_t'] - yt, 'EMPRESA CONSULTORA:', 8)


# Texto Box 4 (VALORES *******)

#**********************************
box_ID = 3
xt, yt = 0.003, 0.015 # Dist_from_Left, Dist_from_Top of first text in ratio!!
vert_spac = 0.016
Titulos = ['Supervisor:', 'Empresa:', 'Sondista:', 'Equipo:']
Valores = ['Antonio Muñoz Algobia (IDOM)', 'IDOM', 'Jose M.', 'TP-50 ORUGA']
Size = 8
xt_val = 0.04
# *********************************

for titl, val in zip(Titulos, Valores):
    draw_text(c, tbox[box_ID]['w_l'] + xt, 1 - tbox[box_ID]['h_t'] - yt, titl, Size)
    draw_text(c, tbox[box_ID]['w_l'] + xt_val, 1 - tbox[box_ID]['h_t'] - yt, val, Size)
    yt += vert_spac


# Texto Box 5 (VALORES *******)

#**********************************
box_ID = 4
xt, yt = 0.003, 0.015 # Dist_from_Left, Dist_from_Top of first text in ratio!!
vert_spac = 0.016
Titulos = ['P.K:', 'X UTM:', 'Y UTM:', 'Z UTM:']
Valores = ['312+439', '607773,18', '4711123,55', '452,6']
Size = 8
xt_val = 0.03
# *********************************

for titl, val in zip(Titulos, Valores):
    draw_text(c, tbox[box_ID]['w_l'] + xt, 1 - tbox[box_ID]['h_t'] - yt, titl, Size)
    draw_text(c, tbox[box_ID]['w_l'] + xt_val, 1 - tbox[box_ID]['h_t'] - yt, val, Size)
    yt += vert_spac


# Texto Box 6 (VALORES *******)

#**********************************
box_ID = 5
xt, yt = 0.003, 0.015 # Dist_from_Left, Dist_from_Top of first text in ratio!!
vert_spac = 0.016
Titulos = ['SONDEO:', 'Hoja:', 'F. de inicio:', 'F. finalización:']
Valores = ['STU 312+439 (I:25º)', '1', '25/02/11', '30/02/11']
Size = 8
xt_val = 0.07
# *********************************

for titl, val in zip(Titulos, Valores):
    draw_text(c, tbox[box_ID]['w_l'] + xt, 1 - tbox[box_ID]['h_t'] - yt, titl, Size)
    draw_text(c, tbox[box_ID]['w_l'] + xt_val, 1 - tbox[box_ID]['h_t'] - yt, val, Size)
    yt += vert_spac



# ############
# # BODYBOXES #
# ############

# Títulos
x_l, y_t = 25.1, 44.5   # Applies to first box, to set up starting point
y_c = (28.8,198.5)
main_boxes_w = (26.9,114,4.5,16.4,10.7,11.9,19.5,16.3,35.1,129.1)
w_spac = 0.2  # in mm

size_cols = [       # in mm
    (5.8,4.4,4.4,4.4,4.4,3.5),
    (12,91,3.9,3.9),
    (),
    (),
    (),
    (),
    (),
    (),
    (5.1,8.8,16.5,4.9),
    (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
    ]

titulos_per_box = [
    ('Profundidad (m)'),
    (''),
    (''),
    (''),
    (''),
    (''),
    (''),
    (''),
    (''),
    ('')
    ]

bbox_titl = []
    
for l, a in zip(main_boxes_w, size_cols):
    r_data = rect_data(sheet_from, ratio=True, w_l=x_l, w_c=l, h_t=y_t, h_c=y_c[0])
    draw_box(c, r_data['w_l'], r_data['h_b'], r_data['w_c'], r_data['h_c'])
    bbox_titl.append(r_data)
    
    start_p = r_data['w_l']
    for x in a:        
        draw_box(c, start_p, r_data['h_b'], r_data['w_c']*x/sum(a), r_data['h_c'])
        draw_box(c, start_p, r_data['h_b'], r_data['w_c']*x/sum(a), r_data['h_c'])
        start_p += r_data['w_c']*x/sum(a)
    x_l += l + w_spac



    


'''

for box in col_per_box:
    for x in range(box):
        
'''

'''
# Boxes

x_l, y_b = 25.1, 21.4  # Applies to first box, to set up starting point
boxes_length = (26.5,114,4.5,16.4,10.7,11.9,19.5,16.3,35.1,129.1)
boxes_height = (198.5, 28.5)
w_spac = 0
tbox = []

for l in boxes_length: 
    r_data = rect_data(sheet_from, ratio=True, w_l=x_l, w_c=l, h_b=y_b, h_c=boxes_height[0])
    draw_box(c, r_data['w_l'], r_data['h_b'], r_data['w_c'], r_data['h_c'])
    
    draw_box(c, r_data['w_l'], r_data['h_b'], r_data['w_c'], r_data['h_c'])
    
    
    
    tbox.append(r_data)
    x_l += l + w_spac
'''
'''

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
'''
c.showPage()
c.save()
