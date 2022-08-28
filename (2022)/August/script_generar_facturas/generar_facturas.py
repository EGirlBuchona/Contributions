# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script para Generar Facturas en Python

from fpdf import FPDF

def generar_factura(nombre_cliente, detalles_productos, total, archivo_salida):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        # Título de la factura
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(200, 10, txt="Factura", ln=True, align="C")
        pdf.ln(10)

        # Información del cliente
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Cliente: {nombre_cliente}", ln=True, align="L")
        pdf.ln(10)

        # Detalles de los productos
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(100, 10, txt="Producto", border=1, align="C")
        pdf.cell(50, 10, txt="Cantidad", border=1, align="C")
        pdf.cell(50, 10, txt="Precio", border=1, align="C")
        pdf.ln()

        pdf.set_font("Arial", size=12)
        for producto, cantidad, precio in detalles_productos:
            pdf.cell(100, 10, txt=producto, border=1, align="C")
            pdf.cell(50, 10, txt=str(cantidad), border=1, align="C")
            pdf.cell(50, 10, txt=f"${precio:.2f}", border=1, align="C")
            pdf.ln()

        # Total
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(150, 10, txt="Total", border=1, align="C")
        pdf.cell(50, 10, txt=f"${total:.2f}", border=1, align="C")

        pdf.output(archivo_salida)
        print(f"Factura generada exitosamente: {archivo_salida}")

    except Exception as e:
        print(f"Error al generar la factura: {e}")

if __name__ == "__main__":
    print("Generador de Facturas")
    nombre = input("Ingrese el nombre del cliente: ")
    productos = [
        ("Camisa", 2, 25.00),
        ("Pantalón", 1, 50.00),
        ("Zapatos", 1, 80.00)
    ]
    total_factura = sum(cantidad * precio for _, cantidad, precio in productos)
    generar_factura(nombre, productos, total_factura, "factura.pdf")
