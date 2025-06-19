import pandas as pd
from pandas import DataFrame

def sort_pairs(df: DataFrame) -> DataFrame:
    """Excelの2列を比較して、共通の値と片方だけの値を整理してDataFrameで返す
    
    Args:
        df: A列とB列を含むDataFrame
        
    Returns:
        整理されたデータのDataFrame
    """
    df = df.fillna("")

    a_values = set(df["A"])
    b_values = set(df["B"])

    common = sorted(a_values & b_values)
    a_only = sorted(a_values - b_values)
    b_only = sorted(b_values - a_values)

    result_rows = []

    for val in common:
        result_rows.append([val, val])

    for val in a_only:
        if val == "":
            continue
        result_rows.append([val, ""])
    
    for val in b_only:
        if val == "":
            continue
        result_rows.append(["", val])

    result_df = pd.DataFrame(result_rows)
    return result_df

if __name__ == "__main__":
    filename = input("Excelファイル名を入力してください: ")
    df = pd.read_excel(filename)
    result_df = sort_pairs(df)
    print(result_df)