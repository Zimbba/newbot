import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(subject, message, recipient_email):
    # Configurações do Gmail
    sender_email = "SEU_EMAIL@gmail.com"  # Substituir pelo teu email
    sender_password = "SENHA_DE_APLICATIVO"  # Substituir pela senha de aplicativo gerada no Gmail

    # Criar a mensagem
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    try:
        # Conexão com o servidor SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Iniciar conexão segura
            server.login(sender_email, sender_password)  # Login no Gmail
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Enviar o email
        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
