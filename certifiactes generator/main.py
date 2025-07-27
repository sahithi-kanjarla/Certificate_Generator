import os
import csv
import io
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def generate_certificates():
    os.makedirs("certificates", exist_ok=True)

    with open("names4.csv", mode="r", encoding="utf-8") as file:
        names = [row[0].strip() for row in csv.reader(file) if row]

    template_path = "canva_template4.pdf"
    page_width, page_height = landscape(A4)

    base_font = "Montserrat-Bold"
    max_font_size = 30
    min_font_size = 12
    try:
        pdfmetrics.registerFont(TTFont("Arial", "arial.ttf"))
        base_font = "Arial"
    except:
        pass

    for name in names:
        if not name:
            continue

        name = name.strip()
        packet = io.BytesIO()
        c = canvas.Canvas(packet, pagesize=landscape(A4))

        # Auto scale name to fit max width
        max_text_width = 500  # Adjust as needed
        font_size = max_font_size
        while font_size >= min_font_size:
            text_width = pdfmetrics.stringWidth(name, base_font, font_size)
            if text_width <= max_text_width:
                break
            font_size -= 1

        c.setFont(base_font, font_size)

        # Center name on landscape A4
        name_x = (page_width - text_width) / 2
        name_y = 310 # Adjust this based on where you want the name vertically

        c.drawString(name_x, name_y, name)
        c.showPage()
        c.save()
        packet.seek(0)

        template = PdfReader(template_path)
        overlay = PdfReader(packet)
        output = PdfWriter()
        page = template.pages[0]
        page.merge_page(overlay.pages[0])
        output.add_page(page)

        safe_name = "".join(c for c in name if c.isalnum() or c in (' ', '.')).strip()
        output_path = f"certificates/{safe_name}.pdf"
        with open(output_path, "wb") as f:
            output.write(f)
        print(f"✓ Generated: {output_path}")

if __name__ == "__main__":
    generate_certificates()
