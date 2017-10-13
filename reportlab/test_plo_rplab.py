from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, landscape
from plo_rplab import rect_data, draw_box, draw_text

sheet_from = (421.6, 298.1)
sheet_to = landscape(A3)
c = canvas.Canvas("h.pdf", pagesize=sheet_to)

# ############
# # OUTERBOX #
# ############

outerbox = rect_data(sheet_from, ratio=True, w_l=24, w_r=9.5, h_b=14.2, h_t=21.6)
draw_box(c, outerbox, sheet_to)


# ############
# # TOPBOXES #
# ############

#******************************************************
dim = (25.1, 11.4, 22.2, 21.4) # x_l, x_r, y_t, y_c (same units as sheet_from)
topb_lengths = (70.2, 90.2, 62, 65.9, 37.2, 59.6) #(same units as sheet_from)
horz_sp = 00 #(same units as sheet_from)
#******************************************************
topboxes = []
tot_length = sheet_from[0] - dim[0] - dim[1] - (len(topb_lengths)-1)*horz_sp
x_st = dim[0]
for length, a in zip(topb_lengths, range(len(topb_lengths))):
	l = length/sum(topb_lengths)*tot_length
	topboxes.append(rect_data(sheet_from, ratio=True, w_l=x_st, w_c=l, h_t=dim[2], h_c=dim[3]))
	draw_box(c, topboxes[a], sheet_to)
	x_st += l + horz_sp


# Topbox 1 Content #
#*******************

#******************************************************
box_ID = 0
spacings = (4,50) # dw, dh pixel points
#******************************************************
draw_text(c, topboxes[box_ID], sheet_to, 'CLIENTE:', 9, spac=spacings)






c.showPage()
c.save()
