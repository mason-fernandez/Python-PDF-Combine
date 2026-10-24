from pypdf import PdfWriter
import argparse, json, tkinter, tkinter.filedialog

if __name__ == "__main__":
    root = tkinter.Tk()
    root.withdraw()

    files = tkinter.filedialog.askopenfilenames()
    output = tkinter.filedialog.asksaveasfilename(filetypes=[('PDF files', '*.pdf')], defaultextension=('PDF files', '*.pdf'))

    merger = PdfWriter()

    for pdf in files:
        merger.append(pdf)

        merger.write(output)
        merger.close()