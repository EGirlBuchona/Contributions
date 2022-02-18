# Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
# Proyecto: Script de Automatización de Emails en Python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(destinatario, asunto, mensaje):
    remitente = "tu_correo@example.com"
    contraseña = "tu_contraseña"

    # Configurar el servidor SMTP
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(remitente, contraseña)

    # Crear el mensaje
    email = MIMEMultipart()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = asunto
    email.attach(MIMEText(mensaje, "plain"))

    # Enviar el correo
    servidor.sendmail(remitente, destinatario, email.as_string())
    servidor.quit()
    print(f"Correo enviado a {destinatario}")

if __name__ == "__main__":
    destinatario = input("Ingrese el correo del destinatario: ")
    asunto = input("Ingrese el asunto del correo: ")
    mensaje = input("Ingrese el mensaje del correo: ")
    enviar_email(destinatario, asunto, mensaje)
