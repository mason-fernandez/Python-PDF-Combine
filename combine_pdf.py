from pypdf import PdfWriter
import argparse, json
import sys

if __name__ == "__main__":
    files = ["C:\\Users\\Mason\\Documents\\cover_letter.pdf", "C:\\Users\\Mason\\Documents\\Durable_Power_of_Attorney.pdf", "C:\\Users\\Mason\\Documents\\Health_Care_Power_of_Attorney.pdf", "C:\\Users\\Mason\\Documents\\Living_Will_Advance_Health_Care_Directive.pdf", "C:\\Users\\Mason\\Documents\\HIPAA_Authorization_and_Instructions.pdf"]
    print(files)
    output_fn = "hello.pdf"

    merger = PdfWriter()

    for pdf in files:
        merger.append(pdf)

        merger.write(output_fn)
        merger.close()

    print("Creation success?")