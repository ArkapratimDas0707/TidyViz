import pandas as pd
import plotly.express as px
import plotly.io as pio

# Use a professional dark theme
pio.templates.default = "plotly_dark"

def generate_summary(df: pd.DataFrame):
    n_rows, n_cols = df.shape
    stats = df.describe(include=[float, int]).to_string()
    corr = df.corr(numeric_only=True).round(2).to_string()
    return (
        f"Analysis Report\nRows: {n_rows}, Columns: {n_cols}\n\n"
        f"Descriptive Statistics:\n{stats}\n\n"
        f"Correlations:\n{corr}"
    )

def plotly_charts(df: pd.DataFrame, max_categories: int = 20):
    figs = []
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = [
        c for c in df.select_dtypes(include=['object','category']).columns
        if df[c].nunique() <= max_categories
    ]

    # Color palette for bars
    color_seq = ["#999999", "#777777", "#555555"]

    # Histograms for each numeric column
    for col in num_cols:
        if df[col].dropna().shape[0] == 0:
            continue
        fig = px.histogram(
            df, x=col, nbins=30, color_discrete_sequence=color_seq,
            title=f"Distribution of {col}"
        )
        fig.update_layout(
            paper_bgcolor="#000000",
            plot_bgcolor="#000000",
            font_color="#e0e0e0",
            margin=dict(l=40, r=40, t=40, b=40)
        )
        figs.append(fig)

    # Bar plots for categorical vs numeric
    for cat in cat_cols:
        for num in num_cols:
            if df[cat].nunique() > max_categories:
                continue
            agg = df.groupby(cat)[num].mean(numeric_only=True).reset_index()
            if agg.shape[0] == 0:
                continue
            fig = px.bar(
                agg, x=cat, y=num, color_discrete_sequence=color_seq,
                title=f"Average {num} by {cat}"
            )
            fig.update_layout(
                paper_bgcolor="#000000",
                plot_bgcolor="#000000",
                font_color="#e0e0e0",
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=True, zeroline=False),
                margin=dict(l=40, r=40, t=40, b=40)
            )
            figs.append(fig)

    # Correlation heatmap
    if len(num_cols) > 1:
        corr = df[num_cols].corr()
        corr_fig = px.imshow(
            corr, text_auto=True,
            color_continuous_scale="gray",
            title="Correlation Heatmap"
        )
        corr_fig.update_layout(
            paper_bgcolor="#000000",
            plot_bgcolor="#000000",
            font_color="#e0e0e0",
            margin=dict(l=40, r=40, t=40, b=40)
        )
        figs.append(corr_fig)

    return figs

def analyze_data(df: pd.DataFrame):
    summary = generate_summary(df)
    charts = plotly_charts(df)
    return summary, charts
