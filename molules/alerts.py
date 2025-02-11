# Secção: Alertas por Email
st.header("📨 Alertas (E-mail)")
if st.button("Enviar Alerta por E-mail"):
    message = f"Sinal Detetado para {symbol}: {decision}"
    send_email_alert("Alerta do Bot de Trading", message, "sandromiau@gmail.com")
    st.success("Alerta enviado por e-mail com sucesso!")
