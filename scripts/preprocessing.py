import numpy as np
from sklearn.impute import SimpleImputer, KNNImputer
from ingestion import ingest_data
import pandas as pd

def analyze_missingness(df):
    """Analyze missingness patterns and return a report dict."""
    report = {}
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            rate = df[col].isnull().mean()
            # quick correlation check for numeric columns
            if pd.api.types.is_numeric_dtype(df[col]):
                mask = df[col].isnull().astype(int)
                max_corr = df.drop(columns=[col]).select_dtypes(include=[np.number]).corrwith(mask).abs().max()
                report[col] = {"rate": rate, "max_corr": max_corr, "type": "numeric"}
            else:
                report[col] = {"rate": rate, "max_corr": None, "type": "categorical"}
    return report

def smart_impute(df):
    """Impute missing values intelligently and produce explanation."""
    miss_report = analyze_missingness(df)
    explanations = []
    df_clean = df.copy()
    
    # numeric columns
    for col, info in miss_report.items():
        if info["type"] == "numeric":
            if info["rate"] < 0.05:
                imputer = SimpleImputer(strategy='median')
                df_clean[[col]] = imputer.fit_transform(df_clean[[col]])
                explanations.append(f"{col}: <5% missing → imputed with median.")
            elif info["max_corr"] and info["max_corr"] > 0.3:
                imputer = KNNImputer(n_neighbors=5)
                df_clean[[col]] = imputer.fit_transform(df_clean[[col]])
                explanations.append(f"{col}: correlated with others → imputed with KNN.")
            else:
                imputer = SimpleImputer(strategy='mean')
                df_clean[[col]] = imputer.fit_transform(df_clean[[col]])
                explanations.append(f"{col}: fallback → imputed with mean.")
        else:
            imputer = SimpleImputer(strategy='most_frequent')
            df_clean[[col]] = imputer.fit_transform(df_clean[[col]])
            explanations.append(f"{col}: categorical → imputed with most frequent value.")
    
    return df_clean, explanations

def handle_outliers(df):
    """Cap outliers using IQR and explain."""
    df_clean = df.copy()
    outlier_explanations = []
    for col in df_clean.select_dtypes(include=[np.number]).columns:
        q1 = df_clean[col].quantile(0.25)
        q3 = df_clean[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5*iqr
        upper = q3 + 1.5*iqr
        original_outliers = ((df_clean[col] < lower) | (df_clean[col] > upper)).sum()
        if original_outliers > 0:
            df_clean[col] = np.clip(df_clean[col], lower, upper)
            outlier_explanations.append(f"{col}: capped {original_outliers} outliers using IQR method.")
    return df_clean, outlier_explanations


def clean_data_pipeline(df):
    df_imputed, impute_expl = smart_impute(df)
    df_final, outlier_expl = handle_outliers(df_imputed)
    explanation_text = "🔧 Cleaning Decisions:\n" + "\n".join(impute_expl)
    explanation_text += "\n\n📌 Outlier Handling:\n"
    explanation_text += "\n".join(outlier_expl) if outlier_expl else "No significant outliers."
    return df_final, explanation_text