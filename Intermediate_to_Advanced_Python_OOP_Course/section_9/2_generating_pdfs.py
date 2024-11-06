from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4') # this creates a PDF but without pages

pdf.add_page() # page is added, now we can add content

pdf.set_font(family='Times', size=24, style='B') # setting content format

# fpdf works based on cells (kind of cells in excel)

pdf.cell(w=0, h=80, txt='Flatmate Bill', border=1, align='C', ln=1) # default alignment is left
                                                                    # 0 width means this cell will take entri horizontal width
pdf.cell(w=100, h=40, txt='Period', border=1)

pdf.cell(w=125, h=40, txt='Nov 2024', border=1) # actual period

pdf.output('bill.pdf')