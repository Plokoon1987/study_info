import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from matplotlib.backends.backend_pdf import PdfPages

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
# 4) ***** CUERPO *****
# ***********************

num_fil=4
num_col=10

g_sizew=(26.5,114,4.5,16.4,10.7,11.9,19.5,16.3,35.1,129.1)
g_sizeh=(7.5,9.5,11.8,198.5)

cuerpo_grid = gridspec.GridSpec(num_fil,num_col, width_ratios=g_sizew, height_ratios=g_sizeh, wspace=0.014, hspace=0)
cuerpo_grid.update(left=0.061, right=0.973, bottom=0.089, top=0.850)


# Creando y formateando contenedores de gráficas
titulos = []
plot = []

for x in range(num_col):
    titulos.append(fig.add_subplot(cuerpo_grid[0:3,x], frame_on=True, alpha=0.1))
    titulos[x].tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
    set_axis_appearance(titulos[x])
    
    plot.append(fig.add_subplot(cuerpo_grid[3,x], frame_on=True, alpha=0.9))
    plot[x].tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')
    set_axis_appearance(plot[x])





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




fig.savefig(filename='/home/froylan/windows/VBox/multipage1.pdf',
    facecolor='w',
    edgecolor='r',
    linewidth='10',
    frameon=True,
    orientation='landscape',
    papertype='A3',
    format='pdf',
    )
