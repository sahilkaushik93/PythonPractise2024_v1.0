from fpdf import FPDF

loc = loc = "E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice\App6-PDF_Generator"

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

pdf.output(f'{loc}\output.pdf')


