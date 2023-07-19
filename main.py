from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

dataframe = pd.read_csv("topics.csv")

for index, row in dataframe.iterrows():
    pdf.add_page()

    # header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # lines
    for i in range(20, 280, 10):
        pdf.line(x1=10, y1=i, x2=200, y2=i)

    # footer
    pdf.ln(267)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # extra pages
    for i in range(row["Pages"]-1):
        pdf.add_page()

        for i in range(20, 280, 10):
            pdf.line(x1=10, y1=i, x2=200, y2=i)

        pdf.ln(278)

        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


pdf.output("output.pdf")
