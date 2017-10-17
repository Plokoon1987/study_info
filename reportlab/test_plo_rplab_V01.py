from reportlab.platypus import SimpleDocTemplate, PageTemplate, Frame, Paragraph, Spacer
from reportlab.lib.pagesizes import A3, landscape
from plantilla import Plantilla, sheet_from, sheet_to
from plo_rplab import rect_data


doc = SimpleDocTemplate(
	filename='Plano Estatigrafico.pdf',
	pagesize=sheet_to,
	)


Story = [Spacer(1,50.8)]	



doc.build(Story, onFirstPage=Plantilla)
