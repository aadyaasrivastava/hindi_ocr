import docx
from docx.shared import Pt
from fpdf import FPDF, fpdf

def converter(txt):
    DOWNLOAD_FOLDER = 'static/Download/document/'
    doc = docx.Document()
    para = doc.add_paragraph().add_run(txt)
    para.font.size = Pt(12)
    # filename = str(uuid.uuid4())
    doc.save(DOWNLOAD_FOLDER+"hindi_doc.docx")

def converter_1(txt):
    DOWNLOAD_FOLDER = 'static/Download/pdf/'
    
    # document=FPDF()
    # document.add_page()
    # document.cell(400, 50, txt, ln=1, align="L")
    # document.output("pdf_file_name.pdf")
    # document=FPDF(orientation='P', unit='mm', format='A3''A2''A1')
    # fpdf.save(DOWNLOAD_FOLDER+ "filename"+".pdf")

    pdf = FPDF()
    pdf.add_font('gargi', '', 'gargi.ttf', uni=True)
    pdf.set_font('gargi', '', 14)
    pdf.add_page()
    # pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=txt, border = 0, align="C")
    pdf.output(DOWNLOAD_FOLDER + "hindi_pdf.pdf")
