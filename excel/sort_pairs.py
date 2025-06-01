import pandas as pd

# Excelの2列を比較して、共通の値を横に並べるプログラム
def sort_pairs(df):
    # None → 空文字列に変換（扱いやすくする）
    df = df.fillna("")

    # A列・B列に出てくるすべての値を収集
    a_values = set(df["A"])
    b_values = set(df["B"])

    # 共通の値（両列に出てくる）をソート
    common = sorted(a_values & b_values)

    # 片方だけにある値
    a_only = sorted(a_values - b_values)
    b_only = sorted(b_values - a_values)

    # 出力用データを作成
    result_rows = []

    # 一致する値を横に並べる
    for val in common:
        result_rows.append([val, val])

    # 片側だけの値をそれぞれ追加
    for val in a_only:
        # 空文字の場合はスキップ
        if val == "":
            continue
        result_rows.append([val, ""])
    for val in b_only:
        if val == "":
            continue
        result_rows.append(["", val])

    # DataFrameに変換
    result_df = pd.DataFrame(result_rows)
    return result_df

if __name__ == "__main__":
    filename = input("Excelファイル名を入力してください: ")
    df = pd.read_excel(filename)
    result_df = sort_pairs(df)
    print(result_df)