# pip install PyPDF2
# pip install fpdf2

import PyPDF2
from fpdf import FPDF

# Opening & extracting text from a PDF file
# rb = read binary

pdf_file = open('./PDF_files/cmd.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

print("The no. of pages of the pdf: " + str(len(pdf_reader.pages)))

activePage = pdf_reader.pages[3]
print(activePage.extract_text())

################################################################


# Create PDF - simple

pdf = FPDF()

# Add a page    

pdf.add_page()

# Set font and size

pdf.set_font('Arial', 'B', 16)

# Write some text

pdf.write(8, 'Hello, World!')

# Save the PDF

pdf.output('./PDF_files/simple_pdf.pdf')

print('PDF created successfully')
