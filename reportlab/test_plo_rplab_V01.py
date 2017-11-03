#from reportlab.platypus import SimpleDocTemplate, PageTemplate, Frame, Paragraph, Spacer
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, Image
from reportlab.lib.styles import ParagraphStyle
from plantilla import Plantilla, sheet_to
from plo_rplab import rect_data

style1 = ParagraphStyle(
		name ='hola',
		fontName = 'Helvetica',
		fontSize=11,
		leading=13,
		alignment=1,
		spaceAfter=1)

doc = SimpleDocTemplate(
	filename='Plano Estatigrafico.pdf',
	pagesize=sheet_to,
	showBoundary=1
	)
libr = doc.__dict__

for key, vals in libr.items():
	print(key, ': ', vals)

Story = []	
bogustext = ("This is Paragraph number") *2000
p = Paragraph(bogustext, style1)
Story.append(p)
i = Image('images/image.jpg', width=sheet_to[0]*0.7, height=sheet_to[1]*0.8147)
Story.append(Spacer(1,50.8))
Story.append(i)

doc.build(Story, onFirstPage=Plantilla, onLaterPages=Plantilla)
