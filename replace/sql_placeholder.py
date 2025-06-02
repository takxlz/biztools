
def replace_sql_placeholder(sql: str, params: list) -> str:
    """
    SQLのプレースホルダーをパラメータで置き換える関数

    :param sql: SQL文（プレースホルダーを含む）
    :param params: プレースホルダーに対応する値のリスト
    :return: プレースホルダーが置き換えられたSQL文
    """
    for i, value in enumerate(params):
        sql = sql.replace("?", value, 1)
    return sql


if __name__ == "__main__":
    sql_input = input("SQL文を入力してください: ")
    params_input = input("パラメータをカンマ区切りで入力してください: ")
    params = [p.strip().strip("'") for p in params_input.split(",")]
    result = replace_sql_placeholder(sql_input, params)
    print(result)