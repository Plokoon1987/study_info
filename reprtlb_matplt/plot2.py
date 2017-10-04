import matplotlib.pyplot as plt
#import matplotlib.ticker as mticker

f, ax = plt.subplots(2, 6, sharey='row')


title = [
    'Profundidad (m)',
    'Tipo de Perforación',
    'Fecha',
    'Revestimiento',
    'Prof.Agua (m)',
    'Notas']

ax[1,0].minorticks_on()




for subp, titl in zip(ax[0], title):
    subp.tick_params(labelbottom='off',labelleft='off', left='off')
    subp.text(0.5, 0.05, titl, color='k', ha='center', va='bottom', size='x-small', rotation=90)
    

for subp, titl in zip(ax[1], title):
    subp.tick_params(labelbottom='off',labelleft='off', direction='in')
    #subp.tick_params(labelbottom='off', direction='in', pad=-15)
    subp.text(0.5, 0.8, titl, color='k', ha='center', rotation=90)

#ax[1,1].minorticks_on()
    


# ***** Y axis Tick Labels Alignment *****
# Nota: Aplican los metodos de tipo Texto, ya que la funcion devuelve objetos Text

#maj_ylabels = ax[1,0].get_yticklabels()
#maj_ylabels[0].set_verticalalignment('top')
#maj_ylabels[-1].set_verticalalignment('bottom')


#for label in maj_ylabels:
#    label.set_horizontalalignment('left')
#    label.set_x(0.2)
#    label.set_size('x-small')


plt.ylim(ymin=10.0, ymax=0.0)


ax[1,1].axhline(y=1)
ax[1,1].axhline(y=3)
ax[1,1].axhline(y=5)


ax[1,3].axhline(y=6)
ax[1,3].axhline(y=7)
ax[1,3].axhline(y=8)

plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=0, hspace=0)

plt.show()

    #subp.set_title(titl)
    #subp.title.set_rotation(90)
    #subp.set_label_position('top')
    #YAxis.set_major_formatter(mticker.MaxNLocator(10))
