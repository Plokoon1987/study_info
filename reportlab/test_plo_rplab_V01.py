#from reportlab.platypus import SimpleDocTemplate, PageTemplate, Frame, Paragraph, Spacer
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
from reportlab.lib.styles import ParagraphStyle

from reportlab.lib.pagesizes import A3, landscape
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
	)


Story = [Spacer(1,50.8)]	
bogustext = ("This is Paragraph number") *2000
p = Paragraph(bogustext, style1)
Story.append(p)


doc.build(Story, onFirstPage=Plantilla, onLaterPages=Plantilla)
