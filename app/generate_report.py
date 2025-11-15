from fpdf import FPDF
import os
from datetime import datetime
import textwrap

class PDFReport(FPDF):
    def header(self):
        logo_path = os.path.join('static', 'logo.png')
        if os.path.exists(logo_path):
            try:
                self.image(logo_path, 10, 8, 33)
            except Exception as e:
                print(f"Warning: cannot load logo: {e}")
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(0, 51, 102)  # Dark Blue
        self.cell(0, 10, 'MineChain Report', new_x="LMARGIN", new_y="NEXT", align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 10)
        self.set_text_color(128)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def add_section_table(pdf, title, content):
    # Section header
    pdf.set_font("Helvetica", 'B', 14)
    pdf.set_text_color(0, 102, 204)
    pdf.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    pdf.set_font("Helvetica", '', 12)
    pdf.set_text_color(0, 0, 0)

    # Determine table structure
    if isinstance(content, list):
        # Single column table
        col_widths = [180]
        headers = ["Details"]
        data_rows = [[str(item)] for item in content]
    elif isinstance(content, dict):
        col_widths = [80, 100]  # two columns
        headers = ["Key", "Value"]
        data_rows = [[str(k), str(v)] for k, v in content.items()]
    else:
        col_widths = [180]
        headers = ["Details"]
        data_rows = [[str(content)]]

    # Draw header
    pdf.set_fill_color(200, 200, 255)
    pdf.set_font("Helvetica", 'B', 12)
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 8, header, border=1, align='C', fill=True)
    pdf.ln()

    # Draw rows with alternating colors
    fill = False
    pdf.set_font("Helvetica", '', 12)
    for row in data_rows:
        if fill:
            pdf.set_fill_color(230, 230, 250)
        else:
            pdf.set_fill_color(255, 255, 255)

        # Wrap each cell text if too long
        max_lines = max([len(textwrap.wrap(str(cell), width=25)) for cell in row])
        for line_idx in range(max_lines):
            for i, cell in enumerate(row):
                lines = textwrap.wrap(str(cell), width=25)
                text = lines[line_idx] if line_idx < len(lines) else ""
                pdf.cell(col_widths[i], 8, text, border=1, align='L', fill=True)
            pdf.ln()
        fill = not fill

    pdf.ln(5)

def generate_pdf_report(data, filename="MineChain_Report.pdf"):
    pdf = PDFReport()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)

    # Timestamp
    pdf.set_font("Helvetica", '', 12)
    pdf.set_text_color(80)
    pdf.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
             new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    # Add all sections as tables
    for section, content in data.items():
        add_section_table(pdf, section, content)

    # Save PDF
    os.makedirs("reports", exist_ok=True)
    output_path = os.path.join("reports", filename)
    pdf.output(output_path)
    return output_path

# Example usage
if __name__ == "__main__":
    sample_data = {
        "Dashboard Summary": ["Total Mines: 12", "Active Suppliers: 8", "Total Batches: 56"],
        "Supply Chain Status": ["Supplier A: OK", "Supplier B: Delay", "Supplier C: OK"],
        "LCA Calculator Results": {"CO2 Emission": "1200 kg", "Energy Used": "5000 kWh"}
    }

    pdf_path = generate_pdf_report(sample_data)
    print(f"PDF Report generated: {pdf_path}")
