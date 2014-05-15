#/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import re
from collections import defaultdict

from PyPDF2 import PdfFileReader


def parse_grade_doc(text):
    matches = re.findall('(\s[A-F](?:\*|\+|\s))\s*\|\s*([0-9.]+)', text)
    print len(matches), 'notes :'

    letter_grades = defaultdict(list)
    for letter, note in matches:
        letter_grades[letter].append(float(note))
    return letter_grades


def get_pdf_content(path):
    # Load PDF into pyPDF
    pdf = PdfFileReader(file(path, "rb"))
    # Iterate on pages and merge extracted text
    page_text = '\n'.join([pdf.getPage(i).extractText() for i in xrange(pdf.getNumPages())])
    return page_text


def display_thresholds(letter_grades):
    for letter, grades in sorted(letter_grades.items(), key=lambda x: max(x[1]), reverse=True):
        print '{:<2} ({:>2}) [ {:>5.2f} - {:>5.2f} ]'.format(letter, len(grades), min(grades), max(grades))


def validate_input_file(file_name):
    if file_name.split(".")[-1] != "txt" and file_name.split(".")[-1] != "pdf":
        raise argparse.ArgumentTypeError("L'extension du fichier de resultats finaux doit etre '.txt' ou '.pdf'")
    else:
        return file_name


def main():
    parser = argparse.ArgumentParser(description="Analyse des seuils de grades pour un cours")
    parser.add_argument('filename', help="Fichier de resultats finaux", type=validate_input_file)
    arg = parser.parse_args()

    extension = arg.filename.split(".")[-1].lower()
    if extension == "txt":
        with open(arg.filename, 'r') as content_file:
            file_content = content_file.read()
    elif extension == "pdf":
        file_content = get_pdf_content(arg.filename).encode("utf8", "ignore")

    letter_grades = parse_grade_doc(file_content)
    display_thresholds(letter_grades)


if __name__ == "__main__":
    main()