import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.lines import Line2D



from matplotlib.ticker import FormatStrFormatter

def set_axis_appearance(subp):
    lwidth=0.6
            
    subp.spines['left'].set_linewidth(lwidth)
    subp.spines['right'].set_linewidth(lwidth)
    subp.spines['bottom'].set_linewidth(lwidth)
    subp.spines['top'].set_linewidth(lwidth)


# *********************
# 1) ***** Figure *****
# *********************
PageSizeInch = {
    'A4':(8.26771653543307,11.6929133858268), 'A4_L':(11.6929133858268,8.26771653543307),
    'A3':(11.6929133858268,16.5354330708661), 'A3_L':(420/25.4,11.6929133858268)
    }
    
fig = plt.figure(figsize=PageSizeInch['A3_L'])

# **** Rectangulo Exterior ****
left, bottom, width, height = 0.057 , 0.047, 0.920, 0.884
fig.add_axes([left, bottom, width, height], xticks=[], yticks=[])

# Removing xticks=[] or yticks=[] will draw 'ticks' and 'ticklabels'



# ***********************
# 2) ***** CABECERA *****
# ***********************
cabecera_grid = gridspec.GridSpec(1,1)
cabecera_grid.update(left=0.061, right=0.973, bottom=0.858, top = 0.929)
cabecera_plot = fig.add_subplot(cabecera_grid[0,0])
cabecera_plot.set_xlim(xmin=0, xmax=38.5)
cabecera_plot.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
set_axis_appearance(cabecera_plot)

# **** Lineas de Separación ****
cabc_spacing = [7,16,22.2,28.8,32.5,38.5]
for spac in cabc_spacing:
    cabecera_plot.axvline(x=spac, linewidth=0.5, color='k')





# ***********************
# 3) ***** CUERPO *****
# ***********************

num_fil=2
num_col=10

bl_sizew=(26.5,114,4.5,16.4,10.7,11.9,19.5,16.3,35.1,129.1)
#bl_sizeh=(7.5,9.5,11.8,198.5)
bl_sizeh=(28.8,198.5)

cuerpo_grid = gridspec.GridSpec(num_fil,num_col, width_ratios=bl_sizew, height_ratios=bl_sizeh, wspace=0.014, hspace=0)
cuerpo_grid.update(left=0.061, right=0.973, bottom=0.089, top=0.850)


###########
# BLOCK 1 #
###########

num_grid = 0
num_filas_titl = 1
num_cols = 6

w_ratios=[5.8,4.4,4.4,4.4,4.4,3.5]

# Titulos #
bl_titulos=['Profundidad (m)', 'Tipo de perforación', 'Fecha', 'Revestimiento', 'Prof. Agua (m)', 'Notas']

bl_grid_titl = gridspec.GridSpecFromSubplotSpec(num_filas_titl, num_cols, subplot_spec=cuerpo_grid[num_grid], wspace=0, width_ratios=w_ratios)

titl_block = []
for x in range(num_cols):
    titl_block.append(fig.add_subplot(bl_grid_titl[x]))
    titl_block[x].tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
    set_axis_appearance(titl_block[x])
    if x in [5]: col = '#0000FF'
    else: col = 'k'    
    titl_block[x].text(0.5, 0.03, bl_titulos[x], color=col, ha='center', va='bottom', size='x-small', rotation=90)

# Plots #
bl_grid_plots = gridspec.GridSpecFromSubplotSpec(1, num_cols, subplot_spec=cuerpo_grid[num_grid+num_col], wspace=0, width_ratios=w_ratios)

plots_block = []
for x in range(num_cols):
    plots_block.append(fig.add_subplot(bl_grid_plots[x]))
    plots_block[x].tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
    set_axis_appearance(plots_block[x])


###########
# BLOCK 2 #
###########

num_grid = 1
num_filas_titl = 1
num_cols = 4

w_ratios=[12,91,3.9,3.9]

# Titulos #
bl_titulos=['Columna litológica', 'Descripción litológica', 'Prof. inferior (m)', 'Espesor']

bl_grid_titl = gridspec.GridSpecFromSubplotSpec(num_filas_titl, num_cols, subplot_spec=cuerpo_grid[num_grid], wspace=0, width_ratios=w_ratios)

titl_block = []
for x in range(num_cols):
    titl_block.append(fig.add_subplot(bl_grid_titl[x]))
    titl_block[x].tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
    set_axis_appearance(titl_block[x])
    
    if x in [1]: bott, rot, verta, size_letra = 0.5, 0, 'center', 'small'
    else: bott, rot, verta, size_letra = 0.03, 90, 'bottom', 'x-small'
    
    titl_block[x].text(0.5, bott, bl_titulos[x], color='k', ha='center', va=verta, size=size_letra, rotation=rot)

# Plots #
bl_grid_plots = gridspec.GridSpecFromSubplotSpec(1, num_cols, subplot_spec=cuerpo_grid[num_grid+num_col], wspace=0, width_ratios=w_ratios)

plots_block = []
for x in range(num_cols):
    plots_block.append(fig.add_subplot(bl_grid_plots[x]))
    plots_block[x].tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
    set_axis_appearance(plots_block[x])


###########
# BLOCK 3 #
###########

num_grid = 2
titulo = 'Final maniobra (m)'

bl_titl = fig.add_subplot(cuerpo_grid[num_grid])
bl_titl.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
set_axis_appearance(bl_titl)
bl_titl.text(0.5, 0.03, titulo, color='k', ha='center', va='bottom', size='x-small', rotation=90)

bl_plot = fig.add_subplot(cuerpo_grid[num_grid + num_col])
bl_plot.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
set_axis_appearance(bl_plot)


###########
# BLOCK 4 #
###########

num_grid = 3
titulo1 = 'R.Q.D (%)'
titulo2 = 'Recuperación (%)'
min_x = 0
max_x = 100
num_ticks = 6
ticks = []
for x in range(num_ticks): ticks.append(int(min_x + x*((max_x - min_x) / (num_ticks - 1) )))

# Titulos

bl_titl = fig.add_subplot(cuerpo_grid[num_grid])
bl_titl.set_xticks(ticks)
bl_titl.tick_params(labelleft='off', left='off', direction='in', tickdir='in', length=2.5, width=0.4)

ticks[0], ticks[-1] = '', ''

bl_titl.set_xticklabels(ticks, size='4', va='bottom', position=(0,0.08))
set_axis_appearance(bl_titl)
bl_titl.text(38, 0.2, titulo1, color='#99CC00', ha='center', va='bottom', size='x-small', rotation=90)
bl_titl.text(62, 0.2, titulo2, color='#007F00', ha='center', va='bottom', size='x-small', rotation=90)

# Plot

bl_plot = fig.add_subplot(cuerpo_grid[num_grid + num_col])
bl_plot.set_xlim(xmin=min_x, xmax=max_x)
bl_plot.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
set_axis_appearance(bl_plot)


###########
# BLOCK 5 #
###########

num_grid = 4
titulo = 'Meteorización'
min_x = 6
max_x = 1
num_ticks = 6
ticks = []
for x in range(num_ticks): ticks.append(int(min_x + x*((max_x - min_x) / (num_ticks - 1) )))

# Titulos

bl_titl = fig.add_subplot(cuerpo_grid[num_grid])
bl_titl.set_xlim(xmin=min_x, xmax=max_x)
bl_titl.set_xticks(ticks)
bl_titl.tick_params(labelleft='off', left='off', direction='in', tickdir='in', length=2.5, width=0.4)

bl_titl.set_xticklabels(['', 'V', 'IV', 'III', 'II', ''], size='4', va='bottom', position=(0,0.08)) # Modificar manualmente los labels
set_axis_appearance(bl_titl)
bl_titl.text(3.5, 0.2, titulo, color='k', ha='center', va='bottom', size='x-small', rotation=90)

# Plot

bl_plot = fig.add_subplot(cuerpo_grid[num_grid + num_col])
bl_plot.set_xlim(xmin=min_x, xmax=max_x)
bl_plot.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
set_axis_appearance(bl_plot)


###########
# BLOCK 6 #
###########

num_grid = 5
titulo = r'$\mathregular{N^o de juntas/m}$'
min_x = 33
max_x = 0
ticks = [6,18,30]

# Titulos

bl_titl = fig.add_subplot(cuerpo_grid[num_grid])
bl_titl.set_xlim(xmin=min_x, xmax=max_x)
bl_titl.set_ylim(ymin=0, ymax=1)
bl_titl.set_xticks(ticks)
bl_titl.tick_params(labelleft='off', left='off', direction='in', tickdir='in', length=2.5, width=0.4)

bl_titl.set_xticklabels([6,18,'>30'], size='3', va='bottom', position=(0,0.08)) # Modificar manualmente los labels
bl_titl.text(24, 0.08, '24', color='k', ha='center', va='bottom', size=3.5)
bl_titl.text(12, 0.08, '12', color='k', ha='center', va='bottom', size=3.5)
bl_titl.axvline(x=12, ymin=0, ymax=0.05, linewidth=0.4, color='k')
bl_titl.axvline(x=24, ymin=0, ymax=0.05, linewidth=0.4, color='k')
label = bl_titl.xaxis.get_ticklabels()
label[-1].set_rotation(0)
label[-1].set_x(10)
set_axis_appearance(bl_titl)


bl_titl.text(16.5, 0.2, titulo, color='k', ha='center', va='bottom', size='x-small', rotation=90)


# Plot

bl_plot = fig.add_subplot(cuerpo_grid[num_grid + num_col])
bl_plot.set_xlim(xmin=min_x, xmax=max_x)
bl_plot.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
set_axis_appearance(bl_plot)


###########
# BLOCK 7 #
###########

num_grid = 6
titulo1 = 'RMR (Básico)'
titulo2 = 'RMR (Seco)'

bl_titl = fig.add_subplot(cuerpo_grid[num_grid])
bl_titl.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
set_axis_appearance(bl_titl)
bl_titl.text(0.38, 0.2, titulo1, color='#CC99FF', ha='center', va='bottom', size='x-small', rotation=90)
bl_titl.text(0.62, 0.2, titulo2, color='#7F007F', ha='center', va='bottom', size='x-small', rotation=90)

bl_plot = fig.add_subplot(cuerpo_grid[num_grid + num_col])
bl_plot.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
set_axis_appearance(bl_plot)


###########
# BLOCK 8 #
###########

num_grid = 7
titulo = 'Q de Barton'

bl_titl = fig.add_subplot(cuerpo_grid[num_grid])
bl_titl.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
set_axis_appearance(bl_titl)
bl_titl.text(0.5, 0.2, titulo, color='k', ha='center', va='bottom', size='x-small', rotation=90)

bl_plot = fig.add_subplot(cuerpo_grid[num_grid + num_col])
bl_plot.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
set_axis_appearance(bl_plot)


###########
# BLOCK 9 #
###########

num_grid = 8
num_filas_titl = 2
num_cols = 4

w_ratios=[5.1,8.8,16.5,4.9]
h_ratios=[7.4,21.1]


# Titulos #
titl = 'Muestras/Ensayos'
sub_titl =['Tipo', 'Intervalo (m)', 'Resultados', 'Golpes/30cm']

bl_grid_titl = gridspec.GridSpecFromSubplotSpec(num_filas_titl, num_cols, subplot_spec=cuerpo_grid[num_grid], wspace=0, width_ratios=w_ratios, hspace=0, height_ratios=h_ratios)


titl_block = fig.add_subplot(bl_grid_titl[0,0:])
titl_block.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
set_axis_appearance(titl_block)
titl_block.text(0.5, 0.5, titl, color='k', ha='center', va='center', size='x-small')

sub_titl_block = []
for x in range(num_cols):
    sub_titl_block.append(fig.add_subplot(bl_grid_titl[x+num_cols]))
    sub_titl_block[x].tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
    set_axis_appearance(sub_titl_block[x])
    sub_titl_block[x].text(0.5, 0.03, sub_titl[x], color='k', ha='center', va='bottom', size='x-small', rotation=90)

# Plots #
bl_grid_plots = gridspec.GridSpecFromSubplotSpec(1, num_cols, subplot_spec=cuerpo_grid[num_grid+num_col], wspace=0, width_ratios=w_ratios)

plots_block = []
for x in range(num_cols):
    plots_block.append(fig.add_subplot(bl_grid_plots[x]))
    plots_block[x].tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
    set_axis_appearance(plots_block[x])


############
# BLOCK 10 #
############

num_grid = 9
num_filas_titl = 3
num_cols = 22
num_cols_per_sub_titl = [5, 2, 2, 2, 3, 3, 3]

h_ratios=[7.4,9.4,11.7]


# Titulos #
titl = 'Ensayos de laboratorio'
sub_titl = ['Granulometría\n% Paso', 'Limites\nAtterberg', 'Estado\nnatural', 'Edómetro', 'Ensayo\nde corte', 'Triaxial', 'Contenidos']

sub_sub_titl = ['max.', '2 mm', '0,4 mm', '0,08 mm', r'$\mathregular{2 \mu m}$', 'WL', 'WP', 'Humedad', 'Dens.\nSeca', 'P. especifico', r'$\mathregular{R.C.S. (kp/cm^2)}$', 'ec', 'cc', 'Tipo', 'c\n' + r'$\mathregular{(kp/cm^2)}$', r'$\mathregular{\phi}$' + ' ' + r'$\mathregular{(^o)}$', 'Tipo', 'c\n' + r'$\mathregular{(kp/cm^2)}$', r'$\mathregular{\phi}$' + ' ' + r'$\mathregular{(^o)}$', 'M.O.', 'SO3', 'CO3Ca']

bl_grid_titl = gridspec.GridSpecFromSubplotSpec(num_filas_titl, num_cols, subplot_spec=cuerpo_grid[num_grid], wspace=0, hspace=0, height_ratios=h_ratios)

# (Titulo)
titl_block = fig.add_subplot(bl_grid_titl[0,0:])
titl_block.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
set_axis_appearance(titl_block)
titl_block.text(0.5, 0.5, titl, color='k', ha='center', va='center', size='small')

# (Sub Titulo)
sub_titl_block = []
start_col = 0
i = 0
for x in num_cols_per_sub_titl:    
    sub_titl_block.append(fig.add_subplot(bl_grid_titl[1,start_col:start_col+x]))
    sub_titl_block[i].tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
    set_axis_appearance(sub_titl_block[i])
    sub_titl_block[i].text(0.5, 0.5, sub_titl[i], color='k', ha='center', va='center', size=6)
    
    if i == 2:
        start_col += x + 2
    else:
        start_col += x
    i += 1



# (Sub Sub Titulo)
sub_sub_titl_block = []
for x in range(num_cols):
    if x == 9 or x == 10:  
        sub_sub_titl_block.append(fig.add_subplot(bl_grid_titl[1:,x]))
        sub_sub_titl_block[x].tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')   
    else:
        sub_sub_titl_block.append(fig.add_subplot(bl_grid_titl[2,x]))
        sub_sub_titl_block[x].tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
    set_axis_appearance(sub_sub_titl_block[x])
    
    if x == 14 or x == 17:
        sub_sub_titl_block[x].text(0.1, 0.03, sub_sub_titl[x], color='k', ha='left', va='bottom', size=6, rotation=90)
    else:
        sub_sub_titl_block[x].text(0.5, 0.03, sub_sub_titl[x], color='k', ha='center', va='bottom', size=6, rotation=90)
        

# Plots #
bl_grid_plots = gridspec.GridSpecFromSubplotSpec(1, num_cols, subplot_spec=cuerpo_grid[num_grid+num_col], wspace=0)

plots_block = []
for x in range(num_cols):
    plots_block.append(fig.add_subplot(bl_grid_plots[x]))
    plots_block[x].tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
    set_axis_appearance(plots_block[x])





# ***********************
# 4) ***** PIE *****
# ***********************
pie_grid = gridspec.GridSpec(1,2, width_ratios=(167,219), wspace=0.002)
pie_grid.update(left=0.061, right=0.973, bottom=0.052, top = 0.082)

pie_plot1 = fig.add_subplot(pie_grid[0,0])
pie_plot1.set_xlim(xmin=0, xmax=16.7)
pie_plot1.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
set_axis_appearance(pie_plot1)

pie_plot2 = fig.add_subplot(pie_grid[0,1])
pie_plot2.set_xlim(xmin=0, xmax=21.9)
pie_plot2.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
set_axis_appearance(pie_plot2)




fig.savefig(fname='multipage1.pdf',
    facecolor='w',
    edgecolor='r',
    linewidth='10',
    frameon=True,
    orientation='landscape',
    papertype='A3',
    format='pdf'
    )
