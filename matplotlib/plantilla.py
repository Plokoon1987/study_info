from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Frame

def rect_data(sheet, ratio=False, **kwargs):
	rect_w_data = {'w_l':0,'w_c':0,'w_r':0}
	rect_h_data = {'h_b':0,'h_c':0,'h_t':0}
	rect_data = {}
	 
	key_list = list(rect_w_data) + list(rect_h_data)
	
	# DATA VALIDATION #
	valid = False
	ans = ''
	if len(kwargs) != 4:
		ans = '4 params must be specified, 2 of width and 2 of height'
	elif not(set(kwargs) < set(key_list)):
		ans = 'One of the params introduced is not expected'
	elif len(set(kwargs) & set(rect_w_data)) != 2:
		ans = '2 width params and 2 height params are expected'	
	else: valid = True
	# END DATA VALIDATION #
		
	if valid == True:
		w_sum, h_sum = 0, 0 
		for ID_w, ID_h in zip((set(kwargs) & set(rect_w_data)), (set(kwargs) & set(rect_h_data))):
			rect_w_data[ID_w] = kwargs[ID_w]
			rect_h_data[ID_h] = kwargs[ID_h]
			w_sum, h_sum = w_sum +  kwargs[ID_w], h_sum + kwargs[ID_h]			
		ID_w = list(set(rect_w_data)-set(kwargs))
		ID_h = list(set(rect_h_data)-set(kwargs))
		rect_w_data[ID_w[0]] = sheet[0] - w_sum
		rect_h_data[ID_h[0]] = sheet[1] - h_sum
		
		if ratio == False:
			rect_data.update(rect_w_data)
			rect_data.update(rect_h_data)	
		else:
			for keys, value in rect_w_data.items():
				rect_w_data[keys] = value/sheet[0]
			for keys, value in rect_h_data.items():
				rect_h_data[keys] = value/sheet[1]
			rect_data.update(rect_w_data)
			rect_data.update(rect_h_data)
	
	return(rect_data)


def draw_box(c, rect, sheet):
	c.saveState()
	rect = dict(rect)
	for key, val in rect.items():
		if 'w' in key:
			rect[key] = rect[key]*sheet[0]
		elif 'h' in key:
			rect[key] = rect[key]*sheet[1]
	c.setFillColorRGB(1,1,1) # Color fill (white is default)
	c.setLineWidth(0.5)
	c.rect(rect['w_l'], rect['h_b'], rect['w_c'], rect['h_c'], fill=1)
	c.restoreState()


def draw_text(c, rect, sheet, text, size, **kwargs):
	c.saveState()
	rect = dict(rect)
	for key, val in rect.items():
		if 'w' in key:
			rect[key] = rect[key]*sheet[0]
		elif 'h' in key:
			rect[key] = rect[key]*sheet[1]
	c.setFillColorRGB(0,0,0) # Color fill
	c.setFont("Helvetica", size)
	
	# KWARGS DATA VALIDATION #
	kwarg_list = {'align':'', 'spac':''}
	valid = False
	ans = ''
	if len(kwargs) > 2:
		ans = 'Only 2 kwargs may be specified'
	elif not(set(kwargs) <= set(kwarg_list)):
		ans = 'One of the params introduced is not expected'
	else: valid = True
	# END DATA VALIDATION #
	
	if valid == True:
		for key, value in kwargs.items():
			kwarg_list[key] = kwargs[key]
		if kwarg_list['spac'] != '':
			rect['w_l'] = rect['w_l'] + kwarg_list['spac'][0]
			rect['h_b'] = rect['h_b'] + kwarg_list['spac'][1]
		if kwarg_list['align'] == 'centre':
			c.drawCentredString(rect['w_l'], rect['h_b'], text)
		elif kwarg_list['align'] == 'right':
			c.drawRightString(rect['w_l'], rect['h_b'], text)
		else:
			c.drawString(rect['w_l'], rect['h_b'], text)

	c.restoreState()


def draw_image(c, rect, sheet, img, **kwargs):
	c.saveState()
	rect = dict(rect)
	for key, val in rect.items():
		if 'w' in key:
			rect[key] = rect[key]*sheet[0]
		elif 'h' in key:
			rect[key] = rect[key]*sheet[1]
	
	# KWARGS DATA VALIDATION #
	kwarg_list = {'l_pad':0, 'r_pad':0,'b_pad':0, 't_pad':0}
	valid = False
	ans = ''
	if len(kwargs) > 4:
		ans = 'Only 4 kwargs may be specified'
	elif not(set(kwargs) <= set(kwarg_list)):
		ans = 'One of the params introduced is not expected'
	else: valid = True
	# END DATA VALIDATION #
	
	if valid == True:
		for key, value in kwargs.items():
			kwarg_list[key] = kwargs[key]
		rect['w_l'] += kwarg_list['l_pad']
		rect['h_b'] += kwarg_list['b_pad']
		rect['w_c'] -= (kwarg_list['r_pad'] + kwarg_list['l_pad'])
		rect['h_c'] -= (kwarg_list['t_pad'] + kwarg_list['b_pad'])
		c.drawImage(img, rect['w_l'],rect['h_b'], width=rect['w_c'], height=rect['h_c'])
	c.restoreState()


def draw_image_svg(c, rect, sheet, img, **kwargs):
	from svglib.svglib import svg2rlg
	from reportlab.graphics import renderPDF, renderPM
	from reportlab.platypus import Image
	
	c.saveState()
	rect = dict(rect)
	for key, val in rect.items():
		if 'w' in key:
			rect[key] = rect[key]*sheet[0]
		elif 'h' in key:
			rect[key] = rect[key]*sheet[1]
	
	# KWARGS DATA VALIDATION #
	kwarg_list = {'l_pad':0, 'r_pad':0,'b_pad':0, 't_pad':0, 'bbox':0}
	valid = False
	ans = ''
	if len(kwargs) > 5:
		ans = 'Only 5 kwargs may be specified'
	elif not(set(kwargs) <= set(kwarg_list)):
		ans = 'One of the params introduced is not expected'
	else: valid = True
	# END DATA VALIDATION #
	
	if valid == True:
		for key, value in kwargs.items():
			kwarg_list[key] = kwargs[key]
		rect['w_l'] += kwarg_list['l_pad']
		rect['h_b'] += kwarg_list['b_pad']
		rect['w_c'] -= (kwarg_list['r_pad'] + kwarg_list['l_pad'])
		rect['h_c'] -= (kwarg_list['t_pad'] + kwarg_list['b_pad'])
		
		drawing = svg2rlg(img)
		Img = Image(drawing, width=rect['w_c'], height=rect['h_c'])

		f = Frame(
			rect['w_l'], rect['h_b'], rect['w_c'], rect['h_c'],
			showBoundary=kwarg_list['bbox'], 
			leftPadding=0, rightPadding=0, bottomPadding=0, topPadding=0)
		story = [Img]
		f.addFromList(story,c)

	c.restoreState()

def draw_paragraph(c, rect, sheet, text, style, **kwargs):
	c.saveState()
	rect = dict(rect)
	for key, val in rect.items():
		if 'w' in key:
			rect[key] = rect[key]*sheet[0]
		elif 'h' in key:
			rect[key] = rect[key]*sheet[1]
	
	# KWARGS DATA VALIDATION #
	kwarg_list = {'l_pad':0, 'r_pad':0,'b_pad':0, 't_pad':0, 'bbox':0}
	valid = False
	ans = ''
	if len(kwargs) > 5:
		ans = 'Only 5 kwargs may be specified'
	elif not(set(kwargs) <= set(kwarg_list)):
		ans = 'One of the params introduced is not expected'
	else: valid = True
	# END DATA VALIDATION #
	
	if valid == True:
		for key, value in kwargs.items():
			kwarg_list[key] = kwargs[key]
		rect['w_l'] += kwarg_list['l_pad']
		rect['h_b'] += kwarg_list['b_pad']
		rect['w_c'] -= (kwarg_list['r_pad'] + kwarg_list['l_pad'])
		rect['h_c'] -= (kwarg_list['t_pad'] + kwarg_list['b_pad'])

		f = Frame(
			rect['w_l'], rect['h_b'], rect['w_c'], rect['h_c'],
			showBoundary=kwarg_list['bbox'], 
			leftPadding=0, rightPadding=0, bottomPadding=0, topPadding=0)
		story = [Paragraph(text, style)]
		f.addFromList(story,c)

	c.restoreState()


# ##################################   PLANTILLA   ##################################

def Plantilla(img_1, trab, img_2, bl4_dat, bl5_dat, bl6_dat):
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
	
	style4bot = ParagraphStyle(
		name ='hello',
		fontName = 'Helvetica',
		fontSize=7,
		leading=9.5,
		alignment=0,
		spaceAfter=1)
	

	sheet_from = (421.6, 298.1)
	sheet_to = landscape(A3)
	c = canvas.Canvas("h.pdf", pagesize=sheet_to)


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
	img = img_1

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
	texto = trab
	#******
	draw_paragraph(c, topboxes[box_ID], sheet_to, texto, style1, l_pad=29, r_pad=29, b_pad=5, t_pad=15)


	#*******************
	# Topbox 3 Content #
	#*******************
	box_ID = 2
	img = img_2

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
	texto = '' 
	for x in range(len(bl4_dat)):
		texto += bl4_dat[x]
		if x < (len(bl4_dat)-1): texto += '<br/>'
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
	texto = '' 
	for x in range(len(bl5_dat)):
		texto += bl5_dat[x]
		if x < (len(bl5_dat)-1): texto += '<br/>'
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
	texto = '' 
	for x in range(1,len(bl5_dat)):
		texto += '<br/>'
		texto += bl6_dat[x]
	#******
	draw_paragraph(c, topboxes[box_ID], sheet_to, texto, style2, l_pad=70, t_pad=2)

	#Paragraph
	texto = '<b>' + bl6_dat[0] + '</b>'
	draw_paragraph(c, topboxes[box_ID], sheet_to, texto, style3, l_pad=68, r_pad=10,t_pad=2,b_pad=47, bbox=1)


										#############
										# BODYBOXES #
										#############
	#******************************************************
	dim = (25.1, 11.1, 27, 44.5) # x_l, x_r, y_b, y_t (same units as sheet_from)
	bodyb_lengths = (26.5,114,4.5,16.4,10.7,11.9,19.5,16.3,35.1,129.1) #(same units as sheet_from)
	horz_sp = 0.5 #(same units as sheet_from)
	#******************************************************
	bodyboxes = []
	tot_length = sheet_from[0] - dim[0] - dim[1] - (len(bodyb_lengths)-1)*horz_sp
	x_st = dim[0]
	for length, a in zip(bodyb_lengths, range(len(bodyb_lengths))):
		l = length/sum(bodyb_lengths)*tot_length
		bodyboxes.append(rect_data(sheet_from, ratio=True, w_l=x_st, w_c=l, h_b=dim[2], h_t=dim[3]))
#		draw_box(c, bodyboxes[a], sheet_to)
		x_st += l + horz_sp
	
	for x in range(len(bodyboxes)):
		img = 'bloque' + str(x+1) + '.svg'
		if x < len(bodyboxes)-2:
			draw_image_svg(c, bodyboxes[x], sheet_to, img, l_pad=0.1, r_pad=0, b_pad=0, t_pad=0)

										###############
										# BOTTOMBOXES #
										###############
	#******************************************************
	dim = (24.6, 10.8, 15.8, 10.5) # x_l, x_r, y_b, y_c (same units as sheet_from)
	botb_lengths = (166.8, 219.2) #(same units as sheet_from)
	horz_sp = 0.5 #(same units as sheet_from)
	#******************************************************
	bottomboxes = []
	tot_length = sheet_from[0] - dim[0] - dim[1] - (len(botb_lengths)-1)*horz_sp
	x_st = dim[0]
	for length, a in zip(botb_lengths, range(len(botb_lengths))):
		l = length/sum(botb_lengths)*tot_length
		bottomboxes.append(rect_data(sheet_from, ratio=True, w_l=x_st, w_c=l, h_b=dim[2], h_c=dim[3]))
		draw_box(c, bottomboxes[a], sheet_to)
		x_st += l + horz_sp


	#**********************
	# Bottombox 2 Content #
	#**********************
	box_ID = 1
	
	#Paragraph
	texto = 'MI: MUESTRA INALTERADA<br/>LF: ENSAYO LEFRANC<br/>Ox: ÓXIDO'
	#******
	draw_paragraph(c, bottomboxes[box_ID], sheet_to, texto, style4bot, l_pad=3, r_pad=0, b_pad=0, t_pad=1)
	
	#Paragraph
	texto = 'MA: MUESTRA ALTERADA<br/>LG: ENSAYO LUGEON<br/>Q: CUARZO'
	#******
	draw_paragraph(c, bottomboxes[box_ID], sheet_to, texto, style4bot, l_pad=125, r_pad=0, b_pad=0, t_pad=1)
	
	#Paragraph
	texto = 'SPT: PENETRÓMETRO<br/>MB: MUESTRA EN BOTE<br/>Ar: ARCILLA'
	#******
	draw_paragraph(c, bottomboxes[box_ID], sheet_to, texto, style4bot, l_pad=250, r_pad=0, b_pad=0, t_pad=1)

	#Paragraph
	texto = 'TP: TESTIGO PARAFINADO<br/><br/>PR: ENSAYO PRESIOMÉTRICO'
	#******
	draw_paragraph(c, bottomboxes[box_ID], sheet_to, texto, style4bot, l_pad=375, r_pad=0, b_pad=0, t_pad=1)

	#Paragraph
	texto = 'MW: MUESTRA DE AGUA<br/><br/>DL: ENSAYO DILATOMÉTRICO'
	#******
	draw_paragraph(c, bottomboxes[box_ID], sheet_to, texto, style4bot, l_pad=500, r_pad=0, b_pad=0, t_pad=1)


	c.showPage()
	c.save()
