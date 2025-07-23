import streamlit as st
import pandas as pd
from preprocessing import clean_data_pipeline
from analysis import analyze_data

# =========================
# Streamlit Page Config
# =========================
st.set_page_config(page_title="TidyViz", layout="wide")

# =========================
# Dark Glassmorphism Theme
# =========================
st.markdown("""
<style>
/* Overall background */
.stApp {
    background-color: #0e0e0e;
    color: #e0e0e0;
    font-family: 'Inter', sans-serif;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(25, 25, 25, 0.85);
    backdrop-filter: blur(8px);
    border-right: 1px solid rgba(255,255,255,0.1);
}

/* Headers */
h1, h2, h3, h4 {
    color: #ffffff;
    font-weight: 600;
    letter-spacing: -0.5px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #3a3a3a, #5a5a5a);
    color: #ffffff;
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 12px;
    font-weight: 600;
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    transition: all 0.3s ease;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #5a5a5a, #7a7a7a);
    transform: translateY(-1px);
}

/* Code blocks */
.stCodeBlock {
    background-color: #1a1a1a;
    border-radius: 10px;
    padding: 10px;
    font-size: 0.9rem;
}

/* Glass effect for main content blocks */
.main > div {
    background: rgba(30,30,30,0.65);
    padding: 1rem;
    border-radius: 16px;
    backdrop-filter: blur(6px);
}

/* Download button */
.stDownloadButton > button {
    background: linear-gradient(135deg, #0052cc, #3388ff);
    color: #ffffff;
    font-weight: 600;
    border-radius: 12px;
    padding: 0.6rem 1.2rem;
    border: none;
}
.stDownloadButton > button:hover {
    background: linear-gradient(135deg, #3388ff, #66aaff);
}

/* Info boxes */
.stAlert {
    background-color: rgba(50,50,50,0.8);
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.1);
}
</style>
""", unsafe_allow_html=True)

# =========================
# Sidebar
# =========================
st.sidebar.title("📂 Upload CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])
run_analysis = st.sidebar.button("Run Analysis")

# =========================
# Main Content
# =========================
st.title("TidyViz")
st.write("Upload your dataset to automatically clean and analyze it in a modern dark interface.")

if run_analysis and uploaded_file is not None:
    # Load & clean
    df = pd.read_csv(uploaded_file)
    df_cleaned, cleaning_log = clean_data_pipeline(df)

    st.subheader("🧹 Cleaning Log")
    st.code(cleaning_log, language="markdown")

    # Analyze
    summary_text, charts = analyze_data(df_cleaned)

    st.subheader("📈 Statistical Summary")
    st.code(summary_text, language="markdown")

    # Download cleaned CSV
    csv_data = df_cleaned.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download Cleaned CSV",
        data=csv_data,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )

    st.markdown("---")
    st.subheader("📊 Visual Analysis")
    if charts and len(charts) > 0:
        for fig in charts:
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No charts generated.")
else:
    st.info("Upload a CSV file in the sidebar and click **Run Analysis** to get started.")
