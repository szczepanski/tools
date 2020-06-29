#!/usr/bin/env python3
"""
simple pdf merger 
sample usage to merge 27 pdf files ['1.pdf', '2.pdf' ..., '27.pdf']:

pdfmerger.py 27

"""

__author__ = "Piotr Szczepanski"
__version__ = "0.1.0"
__license__ = "MIT"


from PyPDF2 import PdfFileMerger
import sys

number_of_files = int(sys.argv[1])

def merge_pdfs(number_of_files):
    pdfs = []
    for index in range(0, number_of_files):
        pdfs.append('{file_number}.pdf'.format(file_number = index + 1))


    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write('merged.pdf')
    merger.close()


def main(number_of_files):
    merge_pdfs(number_of_files)


if __name__ == "__main__":
    main(number_of_files)
