# 📌 What is TidyViz?

**TidyViz** is an interactive data cleaning and visualization tool built with Python and Streamlit.  
It is designed to help data analysts, data scientists, and anyone working with raw datasets quickly:

- 🧹 **Clean messy data automatically**  
  - Handle mixed data types (e.g., numeric values stored as strings)
  - Impute missing values intelligently (median, mean, or KNN-based)
  - Detect and cap outliers using IQR
  - Remove or review duplicate rows
  - Produce a transparent, step‑by‑step cleaning log

- 📊 **Explore and visualize your data effortlessly**  
  - Generate descriptive statistics
  - Compute and visualize correlations
  - Create interactive charts (histograms, bar plots, heatmaps) in a dark theme

---

## 🎯 Intended Purpose

TidyViz is intended to:
- Accelerate **exploratory data analysis (EDA)** by automating repetitive preprocessing tasks.
- Provide a **user-friendly interface** for non‑technical users to upload and clean datasets.
- Offer **transparency** in data cleaning with detailed logs.
- Enable quick **visual insights** without writing a single line of code.

Simply upload your CSV file, click **Run Analysis**, and TidyViz will handle the rest — giving you a cleaned dataset and rich visual insights ready for further analysis or modeling.

## ✨ Key Features of TidyViz

TidyViz is designed to make data cleaning and exploration seamless and enjoyable, with features such as:

- 🧠 **Intelligent Imputation**  
  Automatically analyzes missingness patterns and chooses the best strategy:  
  - Median for <5% missing  
  - Mean for larger gaps  
  - KNN-based if there’s strong correlation  
  - Most-frequent for categorical columns  

- 🚦 **Outlier Handling**  
  Detects and caps outliers using the IQR method to prevent extreme values from skewing your analysis.

- 📈 **Generates Rich Summaries**  
  Outputs descriptive statistics and correlation matrices so you get a quick overview of your dataset.

- 📊 **Interactive Plotly Graphs**  
  Creates interactive histograms, bar charts, and correlation heatmaps for an engaging visual exploration.

- 🔄 **De‑duplicates Data**  
  Automatically identifies and optionally removes duplicate rows.

- 🖤 **Sleek Dark‑Themed UI**  
  A modern, glassmorphism‑inspired dark theme that looks professional and feels comfortable to use.

- 🖱️ **Easy and Intuitive Front End**  
  Powered by Streamlit, just upload your CSV and click **Run Analysis** — no code required.

---

TidyViz helps you save time, improve your workflow, and explore your data with clarity and style.

## 🚀 How to Use TidyViz

Using **TidyViz** is simple and intuitive. Follow these steps to get started:

1. **Open the App**  
   Visit the deployed TidyViz application here:  
   👉 [https://tidyviz.streamlit.app/](https://tidyviz.streamlit.app/)

2. **Upload Your Dataset**  
   - On the left sidebar, click on **📂 Upload CSV**.
   - Select a CSV file from your computer.
   - Once uploaded, click on **Run Analysis**.

3. **Automatic Cleaning & Processing**  
   - TidyViz will:
     - 🧹 Automatically clean your dataset (intelligent imputation, outlier handling, and de-duplication).
     - 📊 Generate descriptive summaries and correlations.
     - 🎨 Create interactive **Plotly** charts for deeper exploration.

4. **Review & Download**  
   - Inspect the **cleaning log** to see what transformations were applied.
   - View **interactive graphs** and **statistical summaries**.
   - Download the cleaned dataset by clicking **⬇️ Download Cleaned CSV**.

That’s it! 🎉  
Your data is now tidy, visualized, and ready for analysis.

