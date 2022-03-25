# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Generador de Reportes en PDF en Python

import sqlite3
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import inch

def generar_reporte(nombre_pdf):
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    
    # Consulta a la base de datos
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    
    # Crear el documento PDF
    pdf = SimpleDocTemplate(nombre_pdf, pagesize=A4)
    contenido = []
    
    # Título del reporte
    titulo = [["Reporte de Inventario"]]
    tabla_titulo = Table(titulo)
    tabla_titulo.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                      ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                                      ('FONTSIZE', (0, 0), (-1, -1), 18)]))
    contenido.append(tabla_titulo)
    contenido.append(Table([[""]]))  # Espacio

    # Encabezado de la tabla
    encabezado = [["ID", "Nombre", "Cantidad", "Precio"]]
    datos = encabezado + productos

    # Crear la tabla
    tabla = Table(datos, colWidths=[0.5*inch, 2*inch, 1*inch, 1*inch])
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    contenido.append(tabla)

    # Generar PDF
    pdf.build(contenido)
    print(f"Reporte generado: {nombre_pdf}")

if __name__ == "__main__":
    generar_reporte("reporte_inventario.pdf")
