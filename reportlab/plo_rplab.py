from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
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
	c.setLineWidth(0.1)
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


def draw_paragraph(c, rect, sheet, text, **kwargs):
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
		
		style = ParagraphStyle(
			name ='hola',
			fontName = 'Helvetica',
			fontSize=11,
			leading=13,
			alignment=1,
			spaceAfter=1)

		f = Frame(
			rect['w_l'], rect['h_b'], rect['w_c'], rect['h_c'],
			showBoundary=0, 
			leftPadding=0, rightPadding=0, bottomPadding=0, topPadding=0)
		story = [Paragraph(text, style)]
		f.addFromList(story,c)

	c.restoreState()
