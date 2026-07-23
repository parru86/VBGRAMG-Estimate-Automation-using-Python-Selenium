from parser.pdf_engine import PDFEngine

pdf = r"D:\1. Software\python\VBGRAMG_AUTO\pdf\model.pdf"

engine = PDFEngine(pdf)

pages = engine.open()

print()

print(engine.info())

print()

print("Pages :", engine.page_count)

print()

print("First Page Words :", len(pages[0]))

print()

for word in pages[0][:20]:

    print(word)