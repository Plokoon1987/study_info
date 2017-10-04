import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from matplotlib.backends.backend_pdf import PdfPages

from matplotlib.ticker import FormatStrFormatter

# *********************
# 1) ***** Figure *****
# *********************
PageSizeInch = {
    'A4':(8.26771653543307,11.6929133858268), 'A4_L':(11.6929133858268,8.26771653543307),
    'A3':(11.6929133858268,16.5354330708661), 'A3_L':(16.5354330708661,11.6929133858268)
    }
    
fig = plt.figure(figsize=PageSizeInch['A3_L'])

# **** Rectangulo Exterior ****
left, bottom, width, height = 0.0571428571428571 , 0.0471380471380471 , 0.920238095238095 , 0.883838383838384
fig.add_axes([left, bottom, width, height], xticks=[], yticks=[])

# Removing xticks=[] or yticks=[] will draw 'ticks' and 'ticklabels'



# *********************
# 2) ***** OUTBOX *****
# *********************


gs = gridspec.GridSpec(6, 42, height_ratios=(21.5,7.4,9.5,11.6,198.5,10.5), hspace=0.03)
gs.update(left=0.0607142857142857, right=0.973333333333333, bottom=0.0505050505050505, top=0.928956228956229)



# *********************
# 2) ***** Subplots *****
# ********************

# 2a)**** Cabecera ****

cabecera = fig.add_subplot(gs[0,:42])
cabecera.set_xlim(xmin=0, xmax=38.5)
cabecera.tick_params(labelbottom='off', bottom='off', labelleft='off', left='off')



# *** Lineas de Separación ***
cabc_spacing = [7,16,22.2,28.8,32.5,38.5]
for spac in cabc_spacing:
    cabecera.axvline(x=spac, linewidth=0.5, color='k')


# **** Titulos ****
titulos = []

# ** Bloque 0 **
block_0 = 6
for x in range(block_0):
    titulos.append(fig.add_subplot(gs[1:4,x]))
    x+=1



'''
titulo1 = fig.add_subplot(gs[1:4,1])
titulo2 = fig.add_subplot(gs[1:4,2])
titulo3 = fig.add_subplot(gs[1:4,3])
titulo4 = fig.add_subplot(gs[1:4,4])
titulo5 = fig.add_subplot(gs[1:4,5])
titulo6 = fig.add_subplot(gs[1:4,6])
titulo7 = fig.add_subplot(gs[1:4,7])
titulo8 = fig.add_subplot(gs[1:4,8])
titulo9 = fig.add_subplot(gs[1:4,9])
titulo10 = fig.add_subplot(gs[1:4,10])
titulo11 = fig.add_subplot(gs[1:4,11])
titulo12 = fig.add_subplot(gs[1:4,12])
titulo13 = fig.add_subplot(gs[1:4,13])
titulo14 = fig.add_subplot(gs[1:4,14])
titulo15 = fig.add_subplot(gs[1:4,15])
titulo16 = fig.add_subplot(gs[1:4,16])
titulo17 = fig.add_subplot(gs[1:4,17])
titulo18 = fig.add_subplot(gs[1:4,18])
titulo19 = fig.add_subplot(gs[1:4,19])
titulo20 = fig.add_subplot(gs[1:4,20])
titulo21 = fig.add_subplot(gs[1:4,21])
titulo22 = fig.add_subplot(gs[1:4,22])
titulo23 = fig.add_subplot(gs[1:4,23])
titulo24 = fig.add_subplot(gs[1:4,24])
titulo25 = fig.add_subplot(gs[1:4,25])
titulo26 = fig.add_subplot(gs[1:4,26])
titulo27 = fig.add_subplot(gs[1:4,27])
titulo28 = fig.add_subplot(gs[1:4,28])
titulo29 = fig.add_subplot(gs[1:4,29])
titulo30 = fig.add_subplot(gs[1:4,30])
titulo31 = fig.add_subplot(gs[1:4,31])
titulo32 = fig.add_subplot(gs[1:4,32])
titulo33 = fig.add_subplot(gs[1:4,33])
titulo34 = fig.add_subplot(gs[1:4,34])
titulo35 = fig.add_subplot(gs[1:4,35])
titulo36 = fig.add_subplot(gs[1:4,36])
titulo37 = fig.add_subplot(gs[1:4,37])
titulo38 = fig.add_subplot(gs[1:4,38])
titulo39 = fig.add_subplot(gs[1:4,39])
titulo40 = fig.add_subplot(gs[1:4,40])
titulo41 = fig.add_subplot(gs[1:4,41])

'''

# **** Gráficas ****

grafica1 = fig.add_subplot(gs[4,0])

grafica2 = fig.add_subplot(gs[4,1])

grafica3 = fig.add_subplot(gs[4,2])

grafica4 = fig.add_subplot(gs[4,3])

grafica5 = fig.add_subplot(gs[4,4])

grafica6 = fig.add_subplot(gs[4,5])



# **** Pie ****

grafica1 = fig.add_subplot(gs[5,0])

grafica2 = fig.add_subplot(gs[5,1])





'''


# **** Tamaño ****

cabecera = plt.subplot(gs[0, :-1])
cabecera.set_xlim(xmin=0, xmax=38.5)

# Tamaños Standard:
#   -A3 = (xmin=0, xmax=38.5)

# **** Lineas de Separación ****
cabc_spacing = [7,16,22.2,28.8,32.5,38.5]
for spac in cabc_spacing:
    cabecera.axvline(x=spac, linewidth=0.5, color='k')




plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=0, hspace=0)

#plt.show() ### ADJUSTS PDF too
'''
print(fig.get_figwidth())
print(fig.get_figheight())


fig.savefig(filename='/home/froylan/windows/VBox/multipage1.pdf',
    facecolor='w',
    edgecolor='r',
    linewidth='10',
    frameon=True,
    orientation='landscape',
    papertype='A3',
    format='pdf',
    )
