from parser.pdf_engine import PDFEngine
from parser.row_detector import RowDetector
from parser.column_detector import ColumnDetector

pdf = r"D:\1. Software\python\VBGRAMG_AUTO\pdf\model.pdf"

engine = PDFEngine(pdf)

pages = engine.open()

rows = RowDetector().detect(

    pages[0]

)

detector = ColumnDetector()

for row in rows:

    if row.text.startswith("Sl No Description"):

        columns = detector.detect(row)

        detector.print(columns)

        break