
import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Set page config
st.set_page_config(page_title="📅 Week Ahead Dashboard", layout="wide")

st.title("📅 Week Ahead: Economic Preview")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Economic Calendar", "Weekly Notes", "Watchlist", "Weekly Index Performance"])

# --- Economic Calendar Placeholder ---
with tab1:
    st.subheader("Key Economic Events (Example Data)")
    data = [
        {"Date": "2025-04-01", "Region": "China", "Event": "Caixin Manufacturing PMI", "Forecast": 50.1},
        {"Date": "2025-04-02", "Region": "US", "Event": "JOLTS Job Openings", "Forecast": 8800},
        {"Date": "2025-04-03", "Region": "Hong Kong", "Event": "Retail Sales YoY", "Forecast": -1.5},
        {"Date": "2025-04-04", "Region": "US", "Event": "Nonfarm Payrolls", "Forecast": 215000}
    ]
    df = pd.DataFrame(data)
    st.dataframe(df)

# --- Weekly Notes ---
with tab2:
    st.subheader("📝 Weekly Summary Notes")
    notes = st.text_area("Write your strategy, expectations or to-dos for the week...")
    if st.button("Save Notes (Mock)"):
        st.success("Your notes have been saved.")

# --- Watchlist ---
with tab3:
    st.subheader("📌 Watchlist")
    watchlist = st.text_input("Stocks, sectors, or macro themes to watch...")
    if st.button("Update Watchlist (Mock)"):
        st.success("Watchlist updated.")

# --- Weekly Index Performance ---
with tab4:
    st.subheader("📈 U.S. Indices: Weekly Performance (Fri vs Fri)")
    tickers = {
        "S&P 500": "^GSPC",
        "Nasdaq 100": "^NDX",
        "Dow Jones": "^DJI"
    }

    end_date = datetime.today()
    start_date = end_date - timedelta(days=14)

    index_data = {}
    for name, ticker in tickers.items():
        hist = yf.download(ticker, start=start_date.strftime("%Y-%m-%d"), end=end_date.strftime("%Y-%m-%d"))
        fridays = hist[hist.index.weekday == 4]
        if len(fridays) >= 2:
            latest_friday = fridays.index[-1]
            previous_friday = fridays.index[-2]
            latest_close = fridays["Close"].iloc[-1]
            previous_close = fridays["Close"].iloc[-2]
            change_pct = (latest_close - previous_close) / previous_close * 100
            index_data[name] = {
                "This Friday (Date)": latest_friday.strftime("%Y-%m-%d (%A)"),
                "Last Friday (Date)": previous_friday.strftime("%Y-%m-%d (%A)"),
                "Weekly % Change": f"{change_pct:+.2f}%" if pd.notnull(change_pct) else "N/A"
            }

    if index_data:
        df_perf = pd.DataFrame.from_dict(index_data, orient="index")
        st.table(df_perf)
    else:
        st.warning("Not enough Friday data available for this week.")
