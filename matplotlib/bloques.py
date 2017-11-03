import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as mticker

def Bloque(prof_ag, perf, prof_pag, ruta):
	
	#### Profundidad #### -> Obtenida por los avances
	profundidad=0
	for elem in perf['avances']:
		if elem['profundidad'] > profundidad: profundidad = elem['profundidad']
	#####################
	'''
	#### Profundidades por página #### -> Establece las profundidades a incluir en cada página
	prof_pag = list(prof_pag)
	if sum(prof_pag) > profundidad: print('La suma de profundidades no puede ser mayor que el avance máximo'); prof_pag = 0
	elif sum(prof_pag) < profundidad: prof_pag.append(profundidad-sum(prof_pag))
	prof_pag_aux = []
	import ipdb; ipdb.set_trace()    # TODO:  erase!!!!
	for elem in prof_pag:
		prof_pag_aux.append(list(range(int(elem))))
	prof_pag = prof_pag_aux
	#####################
    '''

	#### Creando Bloques ####
	
	# Bloque 1
	#### Tipo de Perforación ####
	tip_perf = perf['herr']
		
	#### Avances ####
	avances = perf['avances']
	
	#### Revestimiento ####
	reves = perf['reves']

	Bloque1(profundidad, prof_pag, tip_perf, avances, reves, prof_ag, ruta, 1, 1)	

	
	# Bloque 2
	#### Litología ####
	lito = perf['lito']
	
	Bloque2(profundidad, prof_pag, lito, ruta)


	# Bloque 3 y 4
	#### maniobras ####
	maniobras, recuperacion, rqd = [], [], []
	for elem in perf['maniobras']:
		maniobras.append(elem['profundidad'])
		recuperacion.append(elem['recuperacion'])
		rqd.append(elem['rqd'])
	
	Bloque3(profundidad, prof_pag, maniobras, ruta)
	Bloque4(profundidad, prof_pag, maniobras, recuperacion, rqd, ruta)

	
	# Bloque 5
	#### Meteorización ####
	meteorizacion = perf['meteor']
	
	Bloque5(profundidad, prof_pag, meteorizacion, ruta)
	

	# Bloque 6
	#### Numero de Juntas ####
	numero_de_juntas = perf['juntas']
	
	Bloque6(profundidad, prof_pag, numero_de_juntas, ruta)
	
	
	# Bloque 7
	#### RMR ####
	maniobras, rmrb, rmrs = [], [], []
	for elem in perf['rmr']:
		maniobras.append(elem['profundidad'])
		rmrb.append(elem['rmrb'])
		rmrs.append(elem['rmrs'])
	
	Bloque7(profundidad, prof_pag, maniobras, rmrb, rmrs, ruta)
	
	
	# Bloque 8
	#### Q de Barton ####
	Q_de_barton = perf['barton']
	
	Bloque8(profundidad, prof_pag, Q_de_barton, ruta)



def set_axis_appearance(subp,lwidth=1, l=True, r=True, b=True, t=True):   
	if l == False: subp.spines['left'].set_linewidth(0)
	else: subp.spines['left'].set_linewidth(lwidth)
	
	if r == False: subp.spines['right'].set_linewidth(0)
	else: subp.spines['right'].set_linewidth(lwidth)
	
	if b == False: subp.spines['bottom'].set_linewidth(0)
	else: subp.spines['bottom'].set_linewidth(lwidth)
	
	if t == False: subp.spines['top'].set_linewidth(0)
	else: subp.spines['top'].set_linewidth(lwidth)


def guardar(figure, ruta, nombre):
	figure.savefig(fname=ruta + nombre + '.svg',
		#dpi=300,
		facecolor='w',
		edgecolor='r',
		linewidth='10',
		frameon=True,
		orientation='landscape',
		papertype='A3',
		format='svg'
		)



def Bloque1(prof, prof_pag, perf, avan, reves, prof_ag, ruta, adjx, adjy):

	bl_sizew=(5.8,4.4,4.4,4.4,4.4,3.5)
	bl_sizeh=(28.8,198.5)
	PageSizeInch = {'Sheet':(sum(bl_sizew)/25.4*adjx, sum(bl_sizeh)/25.4*adjy)}

	# *********************
	# 1) ***** Figure *****
	# *********************   
	fig = plt.figure(figsize=PageSizeInch['Sheet'])

	# ***********************
	# 2) ***** PLOT *****
	# ***********************
	num_fil=2
	num_col=6
	cuerpo_grid = gridspec.GridSpec(num_fil,num_col, width_ratios=bl_sizew, height_ratios=bl_sizeh, wspace=0, hspace=0)
	cuerpo_grid.update(left=0, right=1, bottom=0, top=1)
	
	# Creando Encabezados
	
	titulos=['Profundidad (m)', 'Tipo de perforación', 'Fecha', 'Revestimiento', 'Prof. Agua (m)', 'Notas']
	plot_titulos = []
	for x in range(num_col):
		plot_titulos.append(fig.add_subplot(cuerpo_grid[0,x]))
		plot_titulos[x].tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
		if x == 0:
			set_axis_appearance(plot_titulos[x], lwidth=0.2)
		elif x == num_col-1:
			set_axis_appearance(plot_titulos[x], lwidth=0.2)
		else:
			set_axis_appearance(plot_titulos[x], lwidth=0.2)
		if x in [5]: col = '#0000FF'
		else: col = 'k'
		plot_titulos[x].text(0.5, 0.03, titulos[x], color=col, ha='center', va='bottom', size='x-small', rotation=90)

	# Creando Gráficos -> Solo el contenedor

	plot_grafica = []
	for x in range(num_col): plot_grafica.append(fig.add_subplot(cuerpo_grid[1,x]))

	# Creando Gráfico 1
	for x in range(len(perf)):	
		if x == 0: cota = perf[x]['profundidad']/2
		else: cota = perf[x-1]['profundidad'] + (perf[x]['profundidad'] - perf[x-1]['profundidad'])/2
		plot_grafica[1].text(0.5, cota, perf[x]['herramienta'], color='k', ha='center', va='center', size='x-small', rotation=90)
		plot_grafica[1].axhline(perf[x]['profundidad'], linewidth=0.2, color='k')
			
	# Creando Gráfico 2
	for x in range(len(avan)):	
		if x == 0: cota = avan[x]['profundidad']/2
		else: cota = avan[x-1]['profundidad'] + (avan[x]['profundidad'] - avan[x-1]['profundidad'])/2
		plot_grafica[2].text(0.5, cota, avan[x]['fecha'], color='k', ha='center', va='center', size='x-small', rotation=90)
		plot_grafica[2].axhline(avan[x]['profundidad'], linewidth=0.2, color='k')
		
	# Creando Gráfico 3
	for x in range(len(reves)):	
		if x == 0: cota = reves[x]['profundidad']/2
		else: cota = reves[x-1]['profundidad'] + (reves[x]['profundidad'] - reves[x-1]['profundidad'])/2
		plot_grafica[3].text(0.5, cota, reves[x]['revestimiento'], color='k', ha='center', va='center', size='x-small', rotation=90)
		plot_grafica[3].axhline(reves[x]['profundidad'], linewidth=0.2, color='k')


	# Creando Gráfico 4
	plot_grafica[4].text(0.5, prof_ag, prof_ag, color='k', ha='center', va='center', size=4.5, rotation=0)
		
		
	# Creando Gráfico 0
	ID = 0
	plot_grafica[ID].set_ylim(ymin=prof, ymax=0)
	plot_grafica[ID].tick_params(width=0.1, labelbottom='off', bottom='off', labelleft='on', left='on', direction='in', pad=0)
	left_bar_labels = plot_grafica[ID].get_yticklabels()
	for label in left_bar_labels:
		if label == left_bar_labels[0]:
			label.set_verticalalignment('top')
			label.set_y(-10)
		elif label == left_bar_labels[-1]:
			label.set_verticalalignment('bottom')
		label.set_horizontalalignment('left')	
		label.set_x(0.4)	
		label.set_size('x-small')
	set_axis_appearance(plot_grafica[ID], lwidth=0.2)
		
	# Formato a Gráficos
	
	for x in range(1,num_col):
		plot_grafica[x].tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
		plot_grafica[x].set_ylim(ymin=prof, ymax=0)
		if x == num_col-1:
			set_axis_appearance(plot_grafica[x], lwidth=0.2)
		else:
			set_axis_appearance(plot_grafica[x], lwidth=0.2)
#		set_axis_appearance(plot_grafica[x])


	# ***********************
	# X) ***** SAVING *****
	# ***********************

	guardar(fig, ruta, 'bloque1')


def Bloque2(prof, prof_pag, lito, ruta):

	bl_sizew=(12,91,3.9,3.9)
	bl_sizeh=(28.8,198.5)
	PageSizeInch = {'Sheet':(sum(bl_sizew)/25.4, sum(bl_sizeh)/25.4)}

	# *********************
	# 1) ***** Figure *****
	# *********************   
	fig = plt.figure(figsize=PageSizeInch['Sheet'])

	# ***********************
	# 2) ***** PLOT *****
	# ***********************
	num_fil=2
	num_col=4
	cuerpo_grid = gridspec.GridSpec(num_fil,num_col, width_ratios=bl_sizew, height_ratios=bl_sizeh, wspace=0, hspace=0)
	cuerpo_grid.update(left=0, right=1, bottom=0, top=1)
	
	# Creando Encabezados
	
	titulos=['Columna litológica', 'Descripción litológica', 'Prof. inferior (m)', 'Espesor']
	plot_titulos = []
	for x in range(num_col):
		plot_titulos.append(fig.add_subplot(cuerpo_grid[0,x]))
		plot_titulos[x].tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
		if x == 0:
			set_axis_appearance(plot_titulos[x], lwidth=0.2)
		elif x == num_col-1:
			set_axis_appearance(plot_titulos[x], lwidth=0.2)
		else:
			set_axis_appearance(plot_titulos[x], lwidth=0.2)
		if x in [1]: bott, rot, verta, size_letra = 0.5, 0, 'center', 'small'
		else: bott, rot, verta, size_letra = 0.03, 90, 'bottom', 'x-small'
		plot_titulos[x].text(0.5, bott, titulos[x], color='k', ha='center', va=verta, size=size_letra, rotation=rot)	

	# Creando Gráficos -> Solo el contenedor

	plot_grafica = []	
	for x in range(num_col): plot_grafica.append(fig.add_subplot(cuerpo_grid[1,x]))
	
	
	# Creando Gráfico 0
	ID = 0
	colors = {'Brecha tectónica':'blue', 'Marga':'red', 'Grava arenosa':'green', 'Arena':'pink', 'Carbon':'orange'}
	
	for x in range(len(lito)):	
		if x == 0:
			plot_grafica[ID].bar([1], lito[x]['profundidad'], color=colors[lito[x]['colum']])
		else:
			plot_grafica[ID].bar([1], lito[x]['profundidad']-lito[x-1]['profundidad'], color=colors[lito[x]['colum']], bottom=lito[x-1]['profundidad'])

	# Creando Gráfico 1
	ID = 1
	for x in range(len(lito)):
		if x == 0: cot_ini = 0;
		else: cot_ini = lito[x-1]['profundidad']
		plot_grafica[ID].text(0.01, cot_ini+0.2, lito[x]['descr'], color='k', va='top', size='x-small', rotation=0, wrap=True)
		plot_grafica[ID].axhline(lito[x]['profundidad'], linewidth=0.2, color='k')

	# Creando Gráfico 2
	ID = 2
	for x in range(len(lito)):	
		if x == 0: cota = lito[x]['profundidad']/2
		else: cota = lito[x-1]['profundidad'] + (lito[x]['profundidad'] - lito[x-1]['profundidad'])/2
		plot_grafica[ID].text(0.5, cota, lito[x]['profundidad'], color='k', ha='center', va='center', size='x-small', rotation=90)
		plot_grafica[ID].axhline(lito[x]['profundidad'], linewidth=0.2, color='k')

	# Creando Gráfico 3
	ID = 3
	for x in range(len(lito)):
		if x == 0: cota = lito[x]['profundidad']/2; delta_prof = lito[x]['profundidad']
		else:
			cota = lito[x-1]['profundidad'] + (lito[x]['profundidad'] - lito[x-1]['profundidad'])/2
			delta_prof = lito[x]['profundidad'] - lito[x-1]['profundidad']
		plot_grafica[ID].text(0.5, cota, delta_prof, color='k', ha='center', va='center', size='x-small', rotation=90)
		plot_grafica[ID].axhline(lito[x]['profundidad'], linewidth=0.2, color='k')
		

	# Formato a Gráficos
	
	for x in range(num_col):
		plot_grafica[x].tick_params(labelbottom='off', bottom='off', labelleft='off', left='off', direction='in')
		plot_grafica[x].set_ylim(ymin=prof, ymax=0)
		if x == num_col-1:
			set_axis_appearance(plot_grafica[x], lwidth=0.2)
		else:
			set_axis_appearance(plot_grafica[x], lwidth=0.2)
		

	

	# ***********************
	# X) ***** SAVING *****
	# ***********************

	guardar(fig, ruta, 'bloque2')


def Bloque3(prof, prof_pag, maniob, ruta):

	bl_sizew=4.5
	bl_sizeh=(28.8,198.5)
	PageSizeInch = {'Sheet':(bl_sizew/25.4, sum(bl_sizeh)/25.4)}

	# *********************
	# 1) ***** Figure *****
	# *********************   
	fig = plt.figure(figsize=PageSizeInch['Sheet'])

	# ***********************
	# 2) ***** PLOT *****
	# ***********************
	num_fil=2
	num_col=1
	cuerpo_grid = gridspec.GridSpec(num_fil,num_col, height_ratios=bl_sizeh, wspace=0, hspace=0)
	cuerpo_grid.update(left=0, right=1, bottom=0, top=1)
	
	# Creando Encabezados	
	titulo='Final Maniobra (m)'
	plot_titulo = fig.add_subplot(cuerpo_grid[0,0])
	plot_titulo.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
	set_axis_appearance(plot_titulo, lwidth=0.2)	
	bott, rot, verta, size_letra = 0.03, 90, 'bottom', 'x-small'
	plot_titulo.text(0.5, bott, titulo, color='k', ha='center', va=verta, size=size_letra, rotation=rot)	

	# Creando Gráficos -> Solo el contenedor

	plot_grafica = fig.add_subplot(cuerpo_grid[1,0])

	# Formato a Gráficos	
	
	plot_grafica.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off', direction='in')
	plot_grafica.set_ylim(ymin=prof, ymax=0)
	set_axis_appearance(plot_grafica, lwidth=0.2)

	# Creando Gráfico
	for x in range(len(maniob)):
		plot_grafica.text(0.5, maniob[x]-0.03, maniob[x], color='k', ha='center', va='bottom', size='5.5', rotation=90)
		plot_grafica.axhline(maniob[x], linewidth=0.2, color='k')
	
		

	# ***********************
	# X) ***** SAVING *****
	# ***********************

	guardar(fig, ruta, 'bloque3')


def Bloque4(prof, prof_pag, maniob, recup, rqd_vals, ruta):

	bl_sizew=16.4
	bl_sizeh=(28.8,198.5)
	PageSizeInch = {'Sheet':(bl_sizew/25.4, sum(bl_sizeh)/25.4)}

	# *********************
	# 1) ***** Figure *****
	# *********************   
	fig = plt.figure(figsize=PageSizeInch['Sheet'])

	# ***********************
	# 2) ***** PLOT *****
	# ***********************
	num_fil=2
	num_col=1
	cuerpo_grid = gridspec.GridSpec(num_fil,num_col, height_ratios=bl_sizeh, wspace=0, hspace=0)
	cuerpo_grid.update(left=0, right=1, bottom=0, top=1)
	
	# Creando Encabezados
	titulo1 = 'R.Q.D (%)'
	titulo2 = 'Recuperación (%)'
	min_x = 0
	max_x = 100
	ticks = [20,40,60,80]
	plot_titulo = fig.add_subplot(cuerpo_grid[0,0])
	plot_titulo.set_xlim(xmin=min_x, xmax=max_x)
	plot_titulo.set_xticks(ticks)
	plot_titulo.tick_params(labelleft='off', left='off', direction='in', tickdir='in', length=2.5, width=0.4)
	
	plot_titulo.set_xticklabels(ticks, size='4', va='bottom', position=(0,0.08))
	set_axis_appearance(plot_titulo, lwidth=0.2)
	plot_titulo.text(38, 0.2, titulo1, color='#99CC00', ha='center', va='bottom', size='x-small', rotation=90)
	plot_titulo.text(62, 0.2, titulo2, color='#007F00', ha='center', va='bottom', size='x-small', rotation=90)
	
	
	# Creando Gráficos -> Solo el contenedor

	plot_grafica = fig.add_subplot(cuerpo_grid[1,0])

	# Formato a Gráficos	
	
	plot_grafica.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off', direction='in')
	plot_grafica.set_ylim(ymin=prof, ymax=0)
	plot_grafica.set_xlim(xmin=min_x, xmax=max_x)
	set_axis_appearance(plot_grafica, lwidth=0.2)
	
	grid_main = [10,20,30,40,50,60,70,80,90]
	for grid in grid_main:
		if (grid/10) % 2 == 0: plot_grafica.axvline(grid, linewidth=0.5, color='k')
		else: plot_grafica.axvline(grid, linewidth=0.2, color='k')
	
	recuperacion, rqd , maniobra = [], [], [0]
	for x in range(len(maniob)):
		maniobra += [maniob[x]]*2
		recuperacion += [recup[x]]*2
		rqd += [rqd_vals[x]]*2
	recuperacion += [0]
	rqd += [0]
	
	plot_grafica.fill_between(x=recuperacion, y1=maniobra, y2=0, color='#007F00', linewidth=0)
	plot_grafica.fill_between(x=rqd, y1=maniobra, y2=0, color='#99CC00', linewidth=0)


	# ***********************
	# X) ***** SAVING *****
	# ***********************

	guardar(fig, ruta, 'bloque4')


def Bloque5(prof, prof_pag, meteor, ruta):

	bl_sizew=10.7
	bl_sizeh=(28.8,198.5)
	PageSizeInch = {'Sheet':(bl_sizew/25.4, sum(bl_sizeh)/25.4)}

	# *********************
	# 1) ***** Figure *****
	# *********************   
	fig = plt.figure(figsize=PageSizeInch['Sheet'])

	# ***********************
	# 2) ***** PLOT *****
	# ***********************
	num_fil=2
	num_col=1
	cuerpo_grid = gridspec.GridSpec(num_fil,num_col, height_ratios=bl_sizeh, wspace=0, hspace=0)
	cuerpo_grid.update(left=0, right=1, bottom=0, top=1)
	
	# Creando Encabezados
	titulo1 = 'Meteorización'
	min_x = 0
	max_x = 5
	ticks = [1,2,3,4]
	
	plot_titulo = fig.add_subplot(cuerpo_grid[0,0])
	plot_titulo.set_xlim(xmin=min_x, xmax=max_x)
	plot_titulo.set_xticks(ticks)
	plot_titulo.tick_params(labelleft='off', left='off', direction='in', tickdir='in', length=2.5, width=0.4)

	ticks[0], ticks[-1] = '', ''
	
	plot_titulo.set_xticklabels(['V', 'IV', 'III', 'II'], size='4', va='bottom', position=(0,0.08))
	set_axis_appearance(plot_titulo, lwidth=0.2)
	plot_titulo.text((min_x+max_x)/2, 0.2, titulo1, color='k', ha='center', va='bottom', size='x-small', rotation=90)
	
	
	# Creando Gráficos -> Solo el contenedor

	plot_grafica = fig.add_subplot(cuerpo_grid[1,0])

	# Formato a Gráficos	
	
	plot_grafica.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off', direction='in')
	plot_grafica.set_ylim(ymin=prof, ymax=0)
	plot_grafica.set_xlim(xmin=min_x, xmax=max_x)
	set_axis_appearance(plot_grafica, lwidth=0.2)
	
	grid_main = [1,2,3,4]
	for grid in grid_main:
		plot_grafica.axvline(grid, linewidth=0.5, color='k')

	meteoriz, maniob = [], []
	for x in range(len(meteor)):
		if x == 0: val = meteor[x]['profundidad']/2
		else: val = (meteor[x]['profundidad'] + meteor[x-1]['profundidad'])/2	
		meteoriz += [val]*(6 - int(meteor[x]['meteorizacion']))
		maniob += [meteor[x]['profundidad']]

	plot_grafica.hist(meteoriz, [0]+maniob, histtype='bar', rwidth=1, orientation='horizontal',color='#F3BD3D')


	# ***********************
	# X) ***** SAVING *****
	# ***********************

	guardar(fig, ruta, 'bloque5')


def Bloque6(prof, prof_pag, num_juntas, ruta):

	bl_sizew=11.9
	bl_sizeh=(28.8,198.5)
	PageSizeInch = {'Sheet':(bl_sizew/25.4, sum(bl_sizeh)/25.4)}

	# *********************
	# 1) ***** Figure *****
	# *********************   
	fig = plt.figure(figsize=PageSizeInch['Sheet'])

	# ***********************
	# 2) ***** PLOT *****
	# ***********************
	num_fil=2
	num_col=1
	cuerpo_grid = gridspec.GridSpec(num_fil,num_col, height_ratios=bl_sizeh, wspace=0, hspace=0)
	cuerpo_grid.update(left=0, right=1, bottom=0, top=1)
	
	# Creando Encabezados
	titulo1 = r'$\mathregular{N^o de juntas/m}$'
	min_x = 0
	max_x = 33
	ticks = [3,15,27]
	
	plot_titulo = fig.add_subplot(cuerpo_grid[0,0])
	plot_titulo.set_xlim(xmin=min_x, xmax=max_x)
	plot_titulo.set_xticks(ticks)
	plot_titulo.tick_params(labelleft='off', left='off', direction='in', tickdir='in', length=2.5, width=0.4)
	
	plot_titulo.set_xticklabels(['',18,6], size='3', va='bottom', position=(0,0.08))
	plot_titulo.text(21, 0.08, '12', color='k', ha='center', va='bottom', size=3.5)
	plot_titulo.text(9, 0.08, '24', color='k', ha='center', va='bottom', size=3.5)
	plot_titulo.text(4, 0.039, '>30', color='k', ha='center', va='bottom', size=3)
	plot_titulo.axvline(x=21, ymin=0, ymax=0.05, linewidth=0.4, color='k')
	plot_titulo.axvline(x=9, ymin=0, ymax=0.05, linewidth=0.4, color='k')
	
	set_axis_appearance(plot_titulo, lwidth=0.2)
	plot_titulo.text((min_x+max_x)/2, 0.2, titulo1, color='k', ha='center', va='bottom', size='x-small', rotation=90)
	
	
	# Creando Gráficos -> Solo el contenedor

	plot_grafica = fig.add_subplot(cuerpo_grid[1,0])

	# Formato a Gráficos	
	
	plot_grafica.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off', direction='in')
	plot_grafica.set_ylim(ymin=prof, ymax=0)
	plot_grafica.set_xlim(xmin=min_x, xmax=max_x)
	set_axis_appearance(plot_grafica, lwidth=0.2)
	
	grid_main = [3,6,9,12,15,18,21,24,27,30]
	for grid in grid_main:
		if grid % 6 != 0: plot_grafica.axvline(grid, linewidth=0.5, color='k')
		else: plot_grafica.axvline(grid, linewidth=0.2, color='k')

	n_juntas, maniob = [], []
	for x in range(len(num_juntas)):
		if x == 0: val = num_juntas[x]['profundidad']/2
		else: val = (num_juntas[x]['profundidad'] + num_juntas[x-1]['profundidad'])/2	
		n_juntas += [val]*(33 - int(num_juntas[x]['juntas']))
		maniob += [num_juntas[x]['profundidad']]

	plot_grafica.hist(n_juntas, [0]+maniob, histtype='bar', rwidth=1, orientation='horizontal',color='#E82E29')


	# ***********************
	# X) ***** SAVING *****
	# ***********************

	guardar(fig, ruta, 'bloque6')


def Bloque7(prof, prof_pag, maniob, rmrb_vals, rmrs_vals, ruta):

	bl_sizew=19.5
	bl_sizeh=(28.8,198.5)
	PageSizeInch = {'Sheet':(bl_sizew/25.4, sum(bl_sizeh)/25.4)}

	# *********************
	# 1) ***** Figure *****
	# *********************   
	fig = plt.figure(figsize=PageSizeInch['Sheet'])

	# ***********************
	# 2) ***** PLOT *****
	# ***********************
	num_fil=2
	num_col=1
	cuerpo_grid = gridspec.GridSpec(num_fil,num_col, height_ratios=bl_sizeh, wspace=0, hspace=0)
	cuerpo_grid.update(left=0, right=1, bottom=0, top=1)
	
	# Creando Encabezados
	titulo1 = 'RMR (Básico)'
	titulo2 = 'RMR (Seco)'
	min_x = 0
	max_x = 100
	ticks = [10,20,30,40,50,60,70,80,90]
	
	plot_titulo = fig.add_subplot(cuerpo_grid[0,0])
	plot_titulo.set_xlim(xmin=min_x, xmax=max_x)
	plot_titulo.set_xticks(ticks)
	plot_titulo.tick_params(labelleft='off', left='off', direction='in', tickdir='in', length=2.5, width=0.4)
	
	plot_titulo.set_xticklabels(ticks, size='3.5', va='bottom', position=(0,0.08))
	set_axis_appearance(plot_titulo, lwidth=0.2)
	plot_titulo.text(38, 0.2, titulo1, color='#9C7FBA', ha='center', va='bottom', size='x-small', rotation=90)
	plot_titulo.text(62, 0.2, titulo2, color='#962150', ha='center', va='bottom', size='x-small', rotation=90)
	
	
	# Creando Gráficos -> Solo el contenedor

	plot_grafica = fig.add_subplot(cuerpo_grid[1,0])

	# Formato a Gráficos	
	
	plot_grafica.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off', direction='in')
	plot_grafica.set_ylim(ymin=prof, ymax=0)
	plot_grafica.set_xlim(xmin=min_x, xmax=max_x)
	set_axis_appearance(plot_grafica, lwidth=0.2)
	
	grid_main = [10,20,30,40,50,60,70,80,90]
	for grid in grid_main:
		if (grid/10) % 2 == 0: plot_grafica.axvline(grid, linewidth=0.5, color='k')
		else: plot_grafica.axvline(grid, linewidth=0.2, color='k')
	
	rmrb, rmrs = [], []
	for x in range(len(maniob)):
		if x == 0: val = maniob[x]/2
		else: val = (maniob[x] + maniob[x-1])/2	
		rmrb += [val]*int(round(rmrb_vals[x],0))
		rmrs += [val]*int(round(rmrb_vals[x],0)) + [val]*int(round(rmrs_vals[x],0))
	
	plot_grafica.hist(rmrs, [0]+maniob, histtype='bar', rwidth=1, orientation='horizontal',color='#962150')
	plot_grafica.hist(rmrb, [0]+maniob, histtype='bar', rwidth=1, orientation='horizontal',color='#9C7FBA')	
	

	# ***********************
	# X) ***** SAVING *****
	# ***********************

	guardar(fig, ruta, 'bloque7')


def Bloque8(prof, prof_pag, q_barton, ruta):

	bl_sizew=16.3
	bl_sizeh=(28.8,198.5)
	PageSizeInch = {'Sheet':(bl_sizew/25.4, sum(bl_sizeh)/25.4)}

	# *********************
	# 1) ***** Figure *****
	# *********************   
	fig = plt.figure(figsize=PageSizeInch['Sheet'])

	# ***********************
	# 2) ***** PLOT *****
	# ***********************
	num_fil=2
	num_col=1
	cuerpo_grid = gridspec.GridSpec(num_fil,num_col, height_ratios=bl_sizeh, wspace=0, hspace=0)
	cuerpo_grid.update(left=0, right=1, bottom=0, top=1)
	
	# Creando Encabezados
	titulo1 = 'Q de Barton'
	min_x = 0.001
	max_x = 1000
	ticks = [0.01,0.1,1,10,100]
	
	plot_titulo = fig.add_subplot(cuerpo_grid[0,0])
	plot_titulo.set_xscale('log')
	plot_titulo.set_xlim(xmin=min_x, xmax=max_x)
	plot_titulo.set_xticks(ticks)
	plot_titulo.tick_params(labelleft='off', left='off', direction='in', tickdir='in', length=2.5, width=0.4)
	plot_titulo.set_xticklabels(ticks, size='3', va='bottom', position=(0,0.08))

	plot_titulo.text(4, 0.08, '4', color='k', ha='center', va='bottom', size=3.5)
	plot_titulo.text(40, 0.08, '40', color='k', ha='center', va='bottom', size=3.5)
	plot_titulo.axvline(x=4, ymin=0, ymax=0.05, linewidth=0.2, color='k')
	plot_titulo.axvline(x=40, ymin=0, ymax=0.05, linewidth=0.2, color='k')
	set_axis_appearance(plot_titulo, lwidth=0.2)
	plot_titulo.text(1, 0.2, titulo1, color='k', ha='center', va='bottom', size='x-small', rotation=90)
	
	
	# Creando Gráficos -> Solo el contenedor

	plot_grafica = fig.add_subplot(cuerpo_grid[1,0])
	plot_grafica.set_xscale('log')

	# Formato a Gráficos	
	
	plot_grafica.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off', direction='in')
	plot_grafica.set_ylim(ymin=prof, ymax=0)
	plot_grafica.set_xlim(xmin=min_x, xmax=max_x)
	set_axis_appearance(plot_grafica, lwidth=0.2)
	
	grid_main = [0.01,0.1,1,10,100]
	plot_grafica.axvline(0.004, linewidth=0.2, color='k')
	for grid in grid_main:
		plot_grafica.axvline(grid, linewidth=0.5, color='k')
		plot_grafica.axvline(grid*4, linewidth=0.2, color='k')
	
	q_bart, maniob = [], [0.001]
	for elem in q_barton:
		q_bart += [elem['barton']]*2
		maniob += [elem['profundidad']]*2
	q_bart += [0.001]

	plot_grafica.fill_between(x=q_bart, y1=maniob, y2=0.001, color='#14527F',linewidth=0)


	# ***********************
	# X) ***** SAVING *****
	# ***********************

	guardar(fig, ruta, 'bloque8')
