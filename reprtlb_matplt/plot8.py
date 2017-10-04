from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, landscape

def draw_box(c,x_0,y0,w,h):
    from reportlab.lib.units import mm
    c.setFillColorRGB(1,1,1) # Color fill
    c.rect(x_0*mm, y0*mm, w*mm, h*mm, fill=1) # (x0,y0,w,l)

A3_mm = [241.6, 298.1]

c = canvas.Canvas("hello.pdf", pagesize=landscape(A3))


# ############
# # OUTERBOX #
# ############

draw_box(c,24,14.2,388.1,262.3)


# ############
# # TOPBOXES #
# ############

x_start = 25.1
y_start = 254.5
boxes_length = [70.2, 90.2, 62, 65.9, 37.2, 59.6]
boxes_height = 21.4

for x in range(len(boxes_length)):
    draw_box(c, x_start, y_start, boxes_length[x], boxes_height)
    x_start += boxes_length[x]
    print(x_start)

'''
# BOX 1
draw_box(c,24,14.2,388.1,262.3)

# BOX 2
draw_box(c,24,14.2,388.1,262.3)

# BOX 3
draw_box(c,24,14.2,388.1,262.3)

# BOX 4
draw_box(c,24,14.2,388.1,262.3)

# BOX 5
draw_box(c,24,14.2,388.1,262.3)

# BOX 6
draw_box(c,24,14.2,388.1,262.3)
'''

# ###############
# # BOTTOMBOXES #
# ###############

# BOX 1

draw_box(c,24.6,15.8,166.8,10.5)


# BOX 2

draw_box(c,191.9,15.8,219,10.5)



c.showPage()
c.save()


'''
def draw_outerbox(c,x_0,y0,w,h):
    from reportlab.lib.units import mm
#    c.translate(0, 0) # To choose Origin point
    c.setFont("Helvetica",28)
    c.setStrokeColorRGB(0.2,0.5,0.3)
    c.setFillColorRGB(1,0,1)
#    c.line(0,0,0,1.7*inch) # (x0,y0,x1,x2)
#    c.line(0,0,1.7*inch,0) # (x0,y0,x1,x2)
    c.rect(24*mm, 14.2*mm, 386.5*mm, 261.2*mm, fill=1) # (x0,y0,w,l)
    c.rotate(90)
    c.setFillColorRGB(0,0,0.77)
#    c.drawString(0.3*inch, -inch, "HOLAS")

'''
