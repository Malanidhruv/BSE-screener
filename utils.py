import pandas as pd
import streamlit as st
import json

def generate_tradingview_link(stock_name):
    """Generate a TradingView link for a given stock."""
    return f'<a href="https://in.tradingview.com/chart?symbol=BSE%3A{stock_name}" target="_blank">{stock_name}</a>'



def display_buy_candidates(signals):
    """Displays the top 10 buy candidates in a Streamlit app with clickable links."""
    st.subheader("🚀 Top 10 Buy Candidates (Sorted by Strength)")
    
    if not signals:
        st.warning("No buy candidates found.")
        return

    # Debug: Print data before sorting
    st.text("Raw Buy Candidates Data:")
    st.text(json.dumps(signals[:10], indent=2))  # Pretty-print first 10 entries

    # Convert Strength & Distance_pct to float safely
    for signal in signals:
        signal['Strength'] = float(signal.get('Strength', 0))  # Default to 0 if missing
        signal['Distance_pct'] = float(signal.get('Distance_pct', 0))  # Default to 0 if missing

    # Corrected sorting order: Strength (highest first), then Distance% (lowest first)
    sorted_signals = sorted(signals, key=lambda x: (-x['Strength'], x['Distance_pct']))

    # Debug: Print sorted data
    st.text("Sorted Data:")
    st.text(json.dumps(sorted_signals[:10], indent=2))

    top_candidates = sorted_signals[:10]
    
    df = pd.DataFrame(top_candidates)
    
    # Convert stock names into TradingView links
    df['Name'] = df['Name'].apply(generate_tradingview_link)
    
    # Select relevant columns
    df = df[['Name', 'Close', 'Support', 'Strength', 'Distance_pct', 'RSI', 'Trend']]
    
    # Display DataFrame with HTML rendering
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

def display_sell_candidates(signals):
    """Displays the top 10 sell candidates in a Streamlit app with clickable links."""
    st.subheader("🔻 Top 10 Sell Candidates (Sorted by Strength)")
    
    if not signals:
        st.warning("No sell candidates found.")
        return

    # Debug: Print data before sorting
    st.text("Raw Sell Candidates Data:")
    st.text(json.dumps(signals[:10], indent=2))  # Pretty-print first 10 entries

    # Convert Strength & Distance_pct to float safely
    for signal in signals:
        signal['Strength'] = float(signal.get('Strength', 0))  # Default to 0 if missing
        signal['Distance_pct'] = float(signal.get('Distance_pct', 0))  # Default to 0 if missing

    # Corrected sorting order: Strength (highest first), then Distance% (lowest first)
    sorted_signals = sorted(signals, key=lambda x: (-x['Strength'], x['Distance_pct']))

    # Debug: Print sorted data
    st.text("Sorted Data:")
    st.text(json.dumps(sorted_signals[:10], indent=2))

    top_candidates = sorted_signals[:10]
    
    df = pd.DataFrame(top_candidates)
    
    # Convert stock names into TradingView links
    df['Name'] = df['Name'].apply(generate_tradingview_link)
    
    # Select relevant columns
    df = df[['Name', 'Close', 'Resistance', 'Strength', 'Distance_pct', 'RSI', 'Trend']]
    
    # Display DataFrame with HTML rendering
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)
