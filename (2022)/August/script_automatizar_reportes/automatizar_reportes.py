# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script para Automatización de Reportes en Python

import csv
from fpdf import FPDF

def generar_reporte(input_csv, output_pdf):
    try:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Título del reporte
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(200, 10, txt="Reporte Automatizado", ln=True, align="C")
        pdf.ln(10)

        # Leer datos del archivo CSV
        with open(input_csv, mode='r') as file:
            reader = csv.reader(file)
            encabezados = next(reader)
            
            # Agregar encabezados al PDF
            pdf.set_font("Arial", style="B", size=12)
            for encabezado in encabezados:
                pdf.cell(50, 10, txt=encabezado, border=1, align="C")
            pdf.ln()

            # Agregar datos al PDF
            pdf.set_font("Arial", size=12)
            for fila in reader:
                for columna in fila:
                    pdf.cell(50, 10, txt=columna, border=1, align="C")
                pdf.ln()

        pdf.output(output_pdf)
        print(f"Reporte generado exitosamente: {output_pdf}")
    except Exception as e:
        print(f"Error al generar el reporte: {e}")

if __name__ == "__main__":
    print("Script para Automatización de Reportes")
    input_csv = "datos.csv"
    output_pdf = "reporte.pdf"
    generar_reporte(input_csv, output_pdf)
