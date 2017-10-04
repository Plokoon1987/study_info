import Image as image
from matplotlib.pyplot import figure
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

can = canvas.Canvas()
self.f = figure()
self.a = self.f.add_subplot(2,1,1)
self.a.plot(x,y)
self.a2 =self.a.twinx()
self.a2.plot(x,y2,'r')
self.a2.set_ylabel(ylbl2,color='r')
self.a.set_xlabel(xlbl)
self.a.set_ylabel(ylbl,color='b')


self.f.savefig('plot.png',format='png')
image.open('plot.png').save('plot.png','PNG')   
can.drawImage('plot.png',100,250, width=400,height=350)
