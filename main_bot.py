import streamlit as st
from modules.sentiment_analysis import get_sentiment
from modules.technical_analysis import analyze_technical_indicators, make_trade_decision
from modules.market_data import get_market_data
from modules.trade_execution import execute_trade_auto
from modules.alerts import send_telegram_alert

# Interface Gráfica
st.title("Bot de Trading Integrado 🚀")

# Configurar Montante a Investir
st.sidebar.header("Configurações")
invest_amount = st.sidebar.number_input("Montante a Investir (USDT)", min_value=10.0, value=20.0, step=1.0)
symbol = st.sidebar.selectbox("Escolher Par", ["BTC/USDT", "ETH/USDT"])

# Secção: Análise de Sentimentos
st.header("📊 Análise de Sentimentos (Reddit)")
termos = ["Bitcoin", "Ethereum", "Cardano"]
sentimentos = {termo: get_sentiment(termo) for termo in termos}
st.write("Sentimentos Capturados:", sentimentos)

# Secção: Indicadores Técnicos
st.header("📈 Indicadores Técnicos (Binance + yfinance)")
indicators = analyze_technical_indicators(symbol)
decision = make_trade_decision(indicators)
st.write(f"Indicadores para {symbol}:", indicators)
st.write(f"Decisão baseada nos Indicadores: **{decision}**")

# Secção: Dados do CoinGecko
st.header("🌐 Dados do CoinGecko")
market_data = get_market_data(["bitcoin", "ethereum"])
st.dataframe(market_data)

# Secção: Execução de Trades Automáticos
st.header("💼 Execução de Trades Automáticos")
if st.button("Executar Trade Automático"):
    if decision == "BUY":
        execute_trade_auto(symbol, "buy", invest_amount)
        st.success(f"✅ Ordem de compra enviada para {symbol}.")
    elif decision == "SELL":
        execute_trade_auto(symbol, "sell", invest_amount)
        st.success(f"✅ Ordem de venda enviada para {symbol}.")
    else:
        st.warning("⚠️ Sem ação necessária no momento.")

# Secção: Alertas para Telegram
st.header("📨 Alertas (Telegram)")
if st.button("Enviar Alerta"):
    message = f"🚨 Sinal Detetado para {symbol}: {decision}"
    send_telegram_alert(message)
    st.success("Alerta enviado com sucesso!")
