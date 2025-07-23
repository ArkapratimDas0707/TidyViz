import pandas as pd

def ingest_data(file_path_or_obj):
    """
    Ingests a CSV file and returns:
    - The loaded DataFrame
    - readable ingestion report
    """
    # Step 1: Read CSV
    df = pd.read_csv(file_path_or_obj)

    # Step 2: Build ingestion report
    n_rows, n_cols = df.shape
    col_info = []
    for col in df.columns:
        missing_pct = df[col].isnull().mean() * 100
        col_info.append(f"{col} ({df[col].dtype}) - {missing_pct:.2f}% missing")
    col_info_text = "\n".join(col_info)

    report = (
        f"Data Ingestion Successful!\n"
        f"Rows: {n_rows}, Columns: {n_cols}\n\n"
        f"Column Info:\n{col_info_text}"
    )

    return df, report
