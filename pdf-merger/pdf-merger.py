from PyPDF2 import PdfFileMerger

pdfs = ['1.pdf', '2.pdf', '3.pdf', '4.pdf', '5.pdf', '6.pdf', '7.pdf', '8.pdf', '9.pdf', '10.pdf', '11.pdf', '.pdf', '.pdf', '.pdf', '.pdf', '.pdf', '.pdf', '.pdf', '.pdf', '.pdf', '.pdf', '.pdf', '.pdf', '.pdf', '.pdf', '.pdf', '.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
