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
	# END DATA VALIDATION#
		
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
	rect = dict(rect)
	for key, val in rect.items():
		if 'w' in key:
			rect[key] = rect[key]*sheet[0]
		elif 'h' in key:
			rect[key] = rect[key]*sheet[1]
	c.setFillColorRGB(1,1,1) # Color fill (white is default)
	c.setLineWidth(0.1)
	c.rect(rect['w_l'], rect['h_b'], rect['w_c'], rect['h_c'], fill=1)


def draw_text(c, rect, sheet, text, size):
	rect = dict(rect)
	for key, val in rect.items():
		if 'w' in key:
			rect[key] = rect[key]*sheet[0]
		elif 'h' in key:
			rect[key] = rect[key]*sheet[1]
	c.setFillColorRGB(0,0,0) # Color fill
	c.setFont("Helvetica", size)
	c.drawString(rect['w_l'], rect['h_b'], text)


'''


    
    	c.translate(rect['w_l'], rect['h_b'])
	c.setFillColorRGB(1,1,1) # Color fill
	c.setLineWidth(0.1)
	c.rect(0, 0, rect['w_c'], rect['h_c'], fill=1) # (x0,y0,w,l)
	c.translate(-rect['w_l'], -rect['h_b'])
	c.setFillColorRGB(0,0,0) # Color fill
	c.drawCentredString(0, 0, 'text')
	c.restoreState()
'''
