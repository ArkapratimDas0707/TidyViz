import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
from fpdf import FPDF

# ==== THEME ====
plt.style.use("dark_background")
sns.set_theme(style="darkgrid", rc={
    "axes.facecolor": "#1e1e1e",
    "figure.facecolor": "#1e1e1e",
    "axes.edgecolor": "#cccccc",
    "axes.labelcolor": "#ffffff",
    "xtick.color": "#cccccc",
    "ytick.color": "#cccccc",
    "text.color": "#ffffff",
    "axes.titlecolor": "#ffffff"
})

# ==== PAGE CONFIG ====
st.set_page_config(page_title="📊 AutoAnalytics Dashboard", layout="wide")

# ==== CSS for sleek look ====
st.markdown("""
<style>
body {font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;}
.report-card {
    background: rgba(255,255,255,0.75);
    padding: 1.2rem;
    margin-bottom: 1rem;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
h1,h2,h3 {font-weight:600;}
</style>
""", unsafe_allow_html=True)

# ==== PDF GENERATOR ====
def create_pdf(summary_text, exec_summary, chart_buffers):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.multi_cell(0, 10, "📑 Executive Report", align='C')
    pdf.ln(8)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, "Executive Summary")
    pdf.ln(5)
    for line in exec_summary.split("\n"):
        pdf.multi_cell(0, 8, txt=line)
    pdf.ln(10)
    pdf.multi_cell(0, 8, "Statistical Summary")
    pdf.ln(5)
    for line in summary_text.split("\n"):
        pdf.multi_cell(0, 8, txt=line)
    for buf in chart_buffers:
        img = buf.getvalue()
        tmp_file = "temp_chart.png"
        with open(tmp_file, "wb") as f:
            f.write(img)
        pdf.add_page()
        pdf.image(tmp_file, x=10, y=20, w=180)
    return pdf.output(dest="S").encode("latin-1")

# ==== Dummy Analysis (no external files needed) ====
def analyze_data(df):
    summary = df.describe(include='all').transpose().to_string()
    charts = []
    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    for col in numeric_cols[:3]:  # limit to first 3 numeric columns
        fig, ax = plt.subplots(figsize=(6,4))
        sns.histplot(df[col], kde=True, ax=ax)
        ax.set_title(f"Distribution of {col}")
        b = io.BytesIO(); fig.tight_layout(); fig.savefig(b, format='png'); b.seek(0)
        charts.append(b)
        plt.close(fig)
    return summary, charts

def generate_exec_summary(df):
    n_rows, n_cols = df.shape
    missing = df.isna().sum().sum()
    return f"Rows: {n_rows}\nColumns: {n_cols}\nMissing values: {missing}"

# ==== SIDEBAR ====
st.sidebar.title("📂 Upload CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])
run_analysis = st.sidebar.button("🚀 Run Analysis")

# ==== MAIN DASHBOARD ====
st.title("✨ AutoAnalytics Dashboard")
st.write("Upload your dataset to automatically clean, analyze, and generate a report.")

# Show something immediately
st.markdown("> *Waiting for you to upload a file and click Run Analysis…*")

# ==== Only run after button click ====
if run_analysis and uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Just a placeholder cleaning log
    cleaning_log = "Dropped no rows (demo)."
    st.subheader("🧹 Cleaning Log")
    st.code(cleaning_log)

    # Perform simple analysis
    summary_text, charts = analyze_data(df)
    exec_summary = generate_exec_summary(df)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 📑 Executive Summary")
        st.markdown(f"<div class='report-card'>{exec_summary.replace(chr(10),'<br>')}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("### 📈 Statistical Summary")
        st.code(summary_text)

    # Downloads
    csv_data = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download Cleaned CSV", data=csv_data, file_name="cleaned_data.csv", mime="text/csv")

    pdf_bytes = create_pdf(summary_text, exec_summary, charts)
    st.download_button("⬇️ Download Executive PDF", data=pdf_bytes, file_name="executive_report.pdf", mime="application/pdf")

    st.markdown("---")
    st.markdown("## 📊 Visual Analysis")
    if charts:
        for buf in charts:
            st.image(buf.getvalue(), use_column_width=True)
    else:
        st.info("No charts generated.")
