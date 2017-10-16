from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, landscape

sheet_from = (421.6, 298.1)
sheet_to = (A3[1], A3[0])
c = canvas.Canvas("img_test.pdf", pagesize=landscape(A3))

c.drawImage('image.jpg', 100,100)

c.showPage()
c.save()
