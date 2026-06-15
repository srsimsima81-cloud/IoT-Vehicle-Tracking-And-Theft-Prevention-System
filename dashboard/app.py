import streamlit as st
import pandas as pd
import os

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="SafeTrack Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# ==========================
# FUTURISTIC UI STYLE
# ==========================

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700&family=Exo+2:wght@300;400;500;600&display=swap" rel="stylesheet">

<style>

html, body, [class*="css"] {
    font-family: 'Exo 2', sans-serif;
}

/* Background */
.stApp {
    background:
    radial-gradient(circle at top left, rgba(0,229,255,0.12), transparent 40%),
    radial-gradient(circle at bottom right, rgba(0,157,255,0.10), transparent 40%),
    #050B18;
}

/* Hide Streamlit UI */
header, footer {
    visibility: hidden;
}

/* TITLE */
.main-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 24px;
    font-weight: 800;
    text-align: center;
    white-space: nowrap;
    color: white;
    margin-bottom: 20px;

    text-shadow:
    0 0 8px #00E5FF,
    0 0 16px #00E5FF,
    0 0 30px #009DFF;
}

/* SECTION TITLE */
.section-title {
    font-family: 'Orbitron', sans-serif;
    color: #00E5FF;
    font-size: 18px;
    margin-bottom: 10px;
}

/* CARD */
.card {
    background: rgba(17,34,64,0.75);
    border: 1px solid rgba(0,229,255,0.25);
    border-radius: 16px;
    padding: 18px;
    backdrop-filter: blur(14px);
    box-shadow: 0 0 15px rgba(0,229,255,0.10);
}

/* KPI */
.kpi-value {
    font-family: 'Orbitron', sans-serif;
    font-size: 28px;
    color: #00E5FF;
    text-align: center;
}

.kpi-label {
    text-align: center;
    color: #B8D4FF;
    font-size: 13px;
}

/* STATUS */
.safe {
    color: #00FF9D;
    font-weight: bold;
    text-shadow: 0 0 10px #00FF9D;
}

.alert {
    color: #FF3B5C;
    font-weight: bold;
    text-shadow: 0 0 10px #FF3B5C;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# TITLE
# ==========================

st.markdown("""
<div class='main-title'>
🛣️ SafeTrack - IoT Vehicle Tracking & Theft Prevention System 🛡️
</div>
""", unsafe_allow_html=True)

# ==========================
# LOAD DATA
# ==========================

if os.path.exists("data/log.csv"):

    df = pd.read_csv(
        "data/log.csv",
        header=None,
        names=["Timestamp", "Latitude", "Longitude", "Status", "Alert"]
    )

    latest = df.iloc[-1]

    total = len(df)
    safe = len(df[df["Status"] == "SAFE"])
    alert = len(df[df["Status"] == "THEFT ALERT"])

    # ==========================
    # KPI CARDS
    # ==========================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class='card'>
            <div class='kpi-value'>{total}</div>
            <div class='kpi-label'>Total Records</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='card'>
            <div class='kpi-value'>{safe}</div>
            <div class='kpi-label'>Safe Events</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class='card'>
            <div class='kpi-value'>{alert}</div>
            <div class='kpi-label'>Theft Alerts</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class='card'>
            <div class='kpi-value'>LIVE</div>
            <div class='kpi-label'>System Status</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # ==========================
    # VEHICLE STATUS + MAP
    # ==========================

    left, right = st.columns([1, 2])

    with left:

        st.markdown("<div class='section-title'>VEHICLE STATUS</div>", unsafe_allow_html=True)

        st.metric("Latitude", f"{latest['Latitude']:.6f}")
        st.metric("Longitude", f"{latest['Longitude']:.6f}")

        if latest["Status"] == "SAFE":
            st.success(f"Status: {latest['Status']}")
        else:
            st.error(f"Status: {latest['Status']}")

        st.info(f"Alert: {latest['Alert']}")

    with right:

        st.markdown("<div class='section-title'>LIVE GPS LOCATION</div>", unsafe_allow_html=True)

        map_data = pd.DataFrame({
            "lat": [latest["Latitude"]],
            "lon": [latest["Longitude"]]
        })

        st.map(map_data)

    st.write("")

    # ==========================
    # ANALYTICS
    # ==========================

    st.markdown("<div class='section-title'>ALERT ANALYTICS</div>", unsafe_allow_html=True)

    st.line_chart(df["Latitude"])

    # ==========================
    # HISTORY TABLE
    # ==========================

    st.markdown("<div class='section-title'>TRACKING HISTORY</div>", unsafe_allow_html=True)

    st.dataframe(df, use_container_width=True, height=350)

    # ==========================
    # DOWNLOAD REPORT
    # ==========================

    csv = df.to_csv(index=False)

    st.download_button(
        "📥 Download Report",
        csv,
        file_name="SafeTrack_Report.csv",
        mime="text/csv"
    )

else:
    st.error("No data found. Run main.py first.")