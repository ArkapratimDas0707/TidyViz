# TidyViz

TidyViz is an interactive web application that automatically cleans, analyzes, and visualizes datasets through a modern dark interface.

Upload a dataset (CSV, Excel, or Parquet), click Run Analysis, and TidyViz will:
- Ingest your data
- Clean it intelligently (imputation, outlier handling, duplicates, mixed-type fixes)
- Generate a full statistical report
- Create interactive visualizations
- Let you download a cleaned version of your dataset

---

## Quick Start

### Requirements
- Python 3.9 or higher
- Install dependencies:
```bash
pip install -r requirements.txt

# Run the app
streamlit run app.py
Open the local URL shown in your terminal (usually http://localhost:8501).

Upload and Analyze
Open the app in your browser.

Use the sidebar to upload your dataset (.csv, .xlsx, or .parquet).

Click Run Analysis.

Review the automatic cleaning log, statistical summary, and interactive charts.

Download the cleaned dataset as a CSV.

Features
Data Ingestion
Supports CSV, Excel, and Parquet.

Automatically detects file type and loads into a pandas DataFrame.

Generates an ingestion report showing column data types and missing-value percentages.

Cleaning Pipeline
When data is loaded, TidyViz runs these steps:

Mixed-type conversion: object columns containing numeric-looking values are converted to numeric.

Duplicate handling: detects and drops exact duplicate rows.

Smart missing-value imputation:

Numeric columns with less than 5% missing values are filled with the median.

Numeric columns with higher correlation to others use KNN imputation.

Otherwise, numeric columns are filled with the mean.

Categorical columns are filled with the most frequent category.

Outlier capping (IQR method): for each numeric column, values outside 1.5×IQR are clipped to the boundary.

All steps log what was done so you can review them.

Analysis and Visualization
After cleaning, TidyViz performs automated analysis:

Statistical Summary:

Row and column counts

Descriptive statistics (mean, standard deviation, quartiles)

Correlation matrix for numeric columns

Visualizations (using Plotly in dark theme):

Histograms for each numeric column

Bar charts: mean of numeric features grouped by categorical features

Correlation heatmap for numeric columns

Interface
The app uses Streamlit with a custom dark glassmorphism theme:

Dark backgrounds and blurred glass-like panels

Sidebar for uploading files and running analysis

Inline logs, summaries, and interactive charts

One-click CSV download for cleaned data

Tech Stack
pandas, numpy — data manipulation

scikit-learn — KNN imputation and preprocessing

Plotly — interactive visualizations

Streamlit — web app framework

Example Workflow
Upload a CSV with mixed types, missing values, and outliers.

TidyViz:

Fixes mixed types

Drops duplicates

Imputes missing values

Caps outliers

Displays:

Cleaning log

Statistical summary

Interactive histograms, bar charts, and heatmaps

Allows you to download the cleaned CSV.

License
MIT License — free to use, modify, and distribute

