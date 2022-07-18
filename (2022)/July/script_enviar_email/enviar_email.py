# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script para Enviar Correos Electrónicos en Python

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_correo(remitente, contraseña, destinatario, asunto, mensaje):
    try:
        # Configuración del servidor SMTP
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remitente, contraseña)
        
        # Composición del correo
        correo = MIMEMultipart()
        correo['From'] = remitente
        correo['To'] = destinatario
        correo['Subject'] = asunto
        correo.attach(MIMEText(mensaje, 'plain'))
        
        # Envío del correo
        servidor.send_message(correo)
        print(f"Correo enviado exitosamente a {destinatario}")
        servidor.quit()
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

if __name__ == "__main__":
    print("Script para enviar correos electrónicos")
    remitente = input("Ingrese su correo electrónico: ").strip()
    contraseña = input("Ingrese su contraseña: ").strip()
    destinatario = input("Ingrese el correo del destinatario: ").strip()
    asunto = input("Ingrese el asunto del correo: ").strip()
    mensaje = input("Ingrese el mensaje del correo: ").strip()
    
    enviar_correo(remitente, contraseña, destinatario, asunto, mensaje)
