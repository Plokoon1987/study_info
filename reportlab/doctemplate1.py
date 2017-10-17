from reportlab.pdfgen import canvas
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer
from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib.styles import ParagraphStyle

style3 = ParagraphStyle(
	name ='hi',
	fontName = 'Helvetica',
	fontSize=8,
	leading=0,
	alignment=0,
	leftIndent=2)
	
def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "First Page / %s" % pageinfo)
    canvas.restoreState()
    
def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()

sheet_to = landscape(A3)
f = Frame(10, 10, 20, 50, showBoundary=1, leftPadding=0, rightPadding=0, bottomPadding=0, topPadding=0)

doc = BaseDocTemplate(
	filename='hola.pdf',
	pageTemplates=PageTemplate(id='FirstPage', frames = [f]),
	pagesize=sheet_to,
	showBoundary=1)

bogustext = ''
for i in range(100):
	bogustext += ("This is Paragraph number %s.  " % i) *20

p = Paragraph(bogustext, style3)
Story = []
templates = []
Story.append(p)
doc.build(Story)
