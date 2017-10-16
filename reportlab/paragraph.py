from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, landscape

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']


sheet_from = (421.6, 298.1)
sheet_to = (A3[1], A3[0])
c = canvas.Canvas("paragraph_test.pdf", pagesize=landscape(A3))
f = Frame(100, 100, 100, 300, showBoundary=0)

story = []
story.append(Paragraph("This is a Heading",styleH))
story.append(Paragraph("This is a paragraph in <i>Normal</i> style.", styleN))

f.addFromList(story,c)
c.save()
