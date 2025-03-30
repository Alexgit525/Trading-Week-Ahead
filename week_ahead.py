
import streamlit as st
import pandas as pd
from datetime import date

# Sample economic calendar data
events = [
    {"Date": "2025-04-01", "Region": "China", "Event": "Caixin Manufacturing PMI", "Forecast": 50.1},
    {"Date": "2025-04-02", "Region": "US", "Event": "JOLTS Job Openings", "Forecast": 8800},
    {"Date": "2025-04-03", "Region": "Hong Kong", "Event": "Retail Sales YoY", "Forecast": -1.5},
    {"Date": "2025-04-04", "Region": "US", "Event": "Nonfarm Payrolls", "Forecast": 215000}
]
df = pd.DataFrame(events)

# Page config
st.set_page_config(page_title="📅 Week Ahead Dashboard", layout="wide")

st.title("📅 Week Ahead: Economic Preview")
st.caption("Auto-updating dashboard with key events, reminders, and watchlist")

# Tabs
tab1, tab2, tab3 = st.tabs(["Economic Calendar", "Weekly Notes", "Watchlist"])

with tab1:
    st.subheader("Key Economic Events (Auto-updated soon)")
    st.dataframe(df)

with tab2:
    st.subheader("📝 Weekly Summary Notes")
    notes = st.text_area("Write your strategy, expectations or to-dos for the week...")
    if st.button("Save Notes (Mock)"):
        st.success("Your notes have been saved.")

with tab3:
    st.subheader("📌 Watchlist")
    watchlist = st.text_input("Stocks, sectors, or macro themes to watch...")
    if st.button("Update Watchlist (Mock)"):
        st.success("Watchlist updated.")
