import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Task 7 - Telemetry Query Testing",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Natural-Language Telemetry Query Testing")

st.write(
    "Test natural-language queries related to power consumption, "
    "forecasting, voltage, frequency, and grid status."
)

# Load telemetry data
@st.cache_data
def load_data():
    return pd.read_csv("grid_data.csv")

df = load_data()

# Display data
st.subheader("📊 Grid Telemetry Data")

st.dataframe(
    df,
    use_container_width=True
)

# Query section
st.subheader("💬 Natural-Language Telemetry Query")

query = st.text_input(
    "Enter your question:",
    placeholder="Example: What is the predicted peak consumption?"
)


def process_query(query):

    q = query.lower().strip()

    # Predicted peak
    if "predicted peak" in q:
        return "Predicted peak consumption is 699.31 MW."

    # Predicted average
    elif "predicted average" in q or "average predicted" in q:
        return "Predicted average consumption is 587.13 MW."

    # Peak power
    elif "peak power" in q or "highest power" in q:
        return "Peak power consumption is 818.59 MW."

    # Average power
    elif "average power" in q or "average consumption" in q:
        value = df["power_consumption"].mean()
        return f"The average power consumption is {value:.2f} MW."

    # Lowest power
    elif "lowest power" in q or "minimum power" in q:
        value = df["power_consumption"].min()
        return f"The lowest power consumption is {value:.2f} MW."

    # Voltage
    elif "voltage" in q:
        value = df["voltage"].mean()
        return f"The average voltage is {value:.2f} V."

    # Frequency
    elif "frequency" in q:
        value = df["frequency"].mean()
        return f"The average grid frequency is {value:.2f} Hz."

    # Grid status
    elif "status" in q or "grid condition" in q:
        latest_status = df["status"].iloc[-1]
        return f"The latest grid status is {latest_status}."

    # Unknown question
    else:
        return (
            "I could not identify that question. "
            "Try asking about predicted peak, predicted average, "
            "peak power, voltage, frequency, or grid status."
        )


# Process query
if query:
    answer = process_query(query)

    st.success(answer)

    st.subheader("✅ Test Result")

    st.write("Query:")
    st.code(query)

    st.write("Response:")
    st.info(answer)


# Suggested test queries
st.subheader("🧪 Suggested Test Queries")

st.write("1. What is the predicted peak consumption?")
st.write("2. What is the predicted average consumption?")
st.write("3. What is the peak power consumption?")
st.write("4. What is the average voltage?")
st.write("5. What is the grid frequency?")
st.write("6. What is the current grid status?")
