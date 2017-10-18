from reportlab.lib.pagesizes import A3, landscape
sheet_from = (421.6, 298.1)
sheet_to = landscape(A3)

def Plantilla(c, d):
	from reportlab.lib.styles import ParagraphStyle
	from plo_rplab import rect_data, draw_box, draw_text, draw_image, draw_paragraph
	from reportlab.platypus import Frame
	from reportlab.lib.styles import getSampleStyleSheet
	style1 = ParagraphStyle(
		name ='hola',
		fontName = 'Helvetica',
		fontSize=11,
		leading=13,
		alignment=1,
		spaceAfter=1)

	style2 = ParagraphStyle(
		name ='hello',
		fontName = 'Helvetica',
		fontSize=8,
		leading=14.5,
		alignment=0,
		spaceAfter=1)

	style3 = ParagraphStyle(
		name ='hi',
		fontName = 'Helvetica',
		fontSize=8,
		leading=0,
		alignment=0,
		leftIndent=2)
	

										############
										# OUTERBOX #
										############

	outerbox = rect_data(sheet_from, ratio=True, w_l=24, w_r=9.5, h_b=14.2, h_t=21.6)
	draw_box(c, outerbox, sheet_to)


										############
										# TOPBOXES #
										############

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


	#*******************
	# Topbox 1 Content #
	#*******************
	box_ID = 0
	img = 'images/image.jpg'

	#Text
	#******
	spacings = (4,50) # dw, dh pixel points
	#******
	draw_text(c, topboxes[box_ID], sheet_to, 'CLIENTE:', 9, spac=spacings)

	#Image
	#******
	draw_image(c, topboxes[box_ID], sheet_to, img, l_pad=5, r_pad=5, b_pad=5, t_pad=15)


	#*******************
	# Topbox 2 Content #
	#*******************
	box_ID = 1

	#Text
	#******
	spacings = (4,50) # dw, dh pixel points
	#******
	draw_text(c, topboxes[box_ID], sheet_to, 'TRABAJO:', 9, spac=spacings)

	#Paragraph
	texto = '<b>PROYECTO DE CONSTRUCCIÓN LAV CANTÁBRICO-MEDITERRANEO. TRAMO: OLITE-TAFALLA</b>'
	#******
	draw_paragraph(c, topboxes[box_ID], sheet_to, texto, style1, l_pad=29, r_pad=29, b_pad=5, t_pad=15)


	#*******************
	# Topbox 3 Content #
	#*******************
	box_ID = 2
	img = 'images/Negro_10mm.jpg'

	#Text
	#******
	spacings = (4,50) # dw, dh pixel points
	#******
	draw_text(c, topboxes[box_ID], sheet_to, 'EMPRESA CONSULTORA:', 9, spac=spacings)

	#Image
	#******
	draw_image(c, topboxes[box_ID], sheet_to, img, l_pad=5, r_pad=10, b_pad=5, t_pad=15)


	#*******************
	# Topbox 4 Content #
	#*******************
	box_ID = 3

	#Paragraph
	texto = '<b>Supervisor:</b><br/><b>Empresa:</b><br/><b>Sondista:</b><br/><b>Equipo:</b>'
	#******
	draw_paragraph(c, topboxes[box_ID], sheet_to, texto, style2, l_pad=3, t_pad=2)

	#Paragraph
	texto = 'Antonio Muñoz Algobia (IDOM)<br/>IDOM<br/>Jose M.<br/>TP-50 ORUGA'
	#******
	draw_paragraph(c, topboxes[box_ID], sheet_to, texto, style2, l_pad=60, t_pad=2)


	#*******************
	# Topbox 5 Content #
	#*******************
	box_ID = 4

	#Paragraph
	texto = '<b>P.K.:</b><br/><b>X UTM:</b><br/><b>Y UTM:</b><br/><b>Z UTM:</b>'
	#******
	draw_paragraph(c, topboxes[box_ID], sheet_to, texto, style2, l_pad=3, t_pad=2)

	#Paragraph
	texto = '312+439<br/>607773,18<br/>4711123,55<br/>452,6'
	#******
	draw_paragraph(c, topboxes[box_ID], sheet_to, texto, style2, l_pad=35, t_pad=2)


	#*******************
	# Topbox 6 Content #
	#*******************
	box_ID = 5

	#Paragraph
	texto = '<b>SONDEO:</b><br/><b>Hoja:</b><br/><b>F. de inicio:</b><br/><b>F. finalización:</b>'
	#******
	draw_paragraph(c, topboxes[box_ID], sheet_to, texto, style2, l_pad=3, t_pad=2)

	#Paragraph
	texto = '<br/>1<br/>25/02/11<br/>30/02/11'
	#******
	draw_paragraph(c, topboxes[box_ID], sheet_to, texto, style2, l_pad=70, t_pad=2)

	#Paragraph
	texto = '<b> STU 312 +439 (I:25º)</b>'
	draw_paragraph(c, topboxes[box_ID], sheet_to, texto, style3, l_pad=68, r_pad=10,t_pad=2,b_pad=47, bbox=1)
