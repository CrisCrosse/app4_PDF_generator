from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

dataframe = pd.read_csv("topics.csv")

for index, row in dataframe.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)


    pages = row["Pages"]
    print(pages)
    topic = row["Topic"]
    print(topic)

    while pages > 1:
        pdf.add_page()
        pages -= 1

# pdf.add_page()
#
# pdf.set_font(family="Times", style="B", size=12)
# pdf.cell(w=0, h=12, txt="Hello There!", align="L", ln=1, border=1)
#
# pdf.set_font(family="Times", style="B", size=8)
# pdf.cell(w=0, h=8, txt="Kenobi!", align="L", ln=1, border=1)


pdf.output("output.pdf")
