import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Dummy data for trends
dates = pd.date_range(end=datetime.today(), periods=30)
trend_data = pd.DataFrame({
    "date": dates,
    "mentions": np.random.poisson(lam=20, size=30).cumsum(),
    "price_index": np.random.normal(loc=100, scale=5, size=30).cumsum(),
})

# Dummy competitors data
competitors = [
    {
        "name": "Brand A",
        "price_range": "11000 - 14500 PKR",
        "sentiment": 0.12,
        "market_position": "Mid-range",
        "last_launch": "2025-03-12",
    },
    {
        "name": "Brand B",
        "price_range": "9000 - 12000 PKR",
        "sentiment": -0.05,
        "market_position": "Budget",
        "last_launch": "2025-01-25",
    },
]

# Simple chat history stored in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def render_chat():
    st.header("💬 Market Research Assistant Chat")
    query = st.text_input("Ask me about your market research...", key="chat_input")

    if query:
        # Append user message
        st.session_state.chat_history.append({"from": "user", "text": query})

        # Fake assistant response — replace with your AI backend call
        answer = f"Analyzing your query: '{query}'. Here's a quick insight:\n\n- Market mentions increased by 15% in last month.\n- Brand A shows positive sentiment."
        st.session_state.chat_history.append({"from": "assistant", "text": answer})

        # Clear input after sending
        st.session_state.chat_input = ""

    # Display chat history
    for msg in st.session_state.chat_history:
        if msg["from"] == "user":
            st.markdown(f"**You:** {msg['text']}")
        else:
            st.markdown(f"**AMRA:** {msg['text']}")

def render_dashboard():
    st.header("📊 Market Research Dashboard")

    # Summary cards
    col1, col2, col3 = st.columns(3)
    col1.metric("Market Growth (%)", "24%")
    col2.metric("Sentiment Score", "+0.12")
    col3.metric("Competitors Tracked", "5")

    # Line chart for trend
    st.subheader("Market Mentions Over Last 30 Days")
    chart_data = trend_data.set_index("date")[["mentions"]]
    st.line_chart(chart_data)

def render_competitor_details():
    st.header("🏆 Competitor Details")

    comp_names = [c["name"] for c in competitors]
    selected = st.selectbox("Select Competitor", comp_names)

    comp = next(c for c in competitors if c["name"] == selected)
    st.write(f"**Name:** {comp['name']}")
    st.write(f"**Price Range:** {comp['price_range']}")
    st.write(f"**Sentiment Score:** {comp['sentiment']}")
    st.write(f"**Market Position:** {comp['market_position']}")
    st.write(f"**Last Product Launch:** {comp['last_launch']}")

    # Dummy price trend
    price_trend = pd.DataFrame({
        "date": dates,
        "price": np.linspace(11000, 14500, len(dates)) + np.random.normal(0, 200, len(dates))
    }).set_index("date")

    st.subheader("Price Trend (PKR)")
    st.line_chart(price_trend)

def main():
    st.set_page_config(page_title="Autonomous Market Research Assistant (AMRA)", layout="wide")

    st.title("🤖 Autonomous Market Research Assistant (AMRA)")

    tab = st.sidebar.radio("Navigate", ["Chat", "Dashboard", "Competitor Details"])

    if tab == "Chat":
        render_chat()
    elif tab == "Dashboard":
        render_dashboard()
    elif tab == "Competitor Details":
        render_competitor_details()

if __name__ == "__main__":
    main()
