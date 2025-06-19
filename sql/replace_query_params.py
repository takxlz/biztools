
def replace_sql_placeholder(sql: str, params: list) -> str:
    """SQLのプレースホルダー（?）をパラメータで順次置き換える
    
    Args:
        sql: プレースホルダーを含むSQL文
        params: 置き換える値のリスト
        
    Returns:
        パラメータが適用されたSQL文
    """
    for value in params:
        sql = sql.replace("?", value, 1)
    return sql


if __name__ == "__main__":
    sql_input = input("SQL文を入力してください: ")
    params_input = input("パラメータをカンマ区切りで入力してください: ")
    params = [p.strip().strip("'") for p in params_input.split(",")]
    result = replace_sql_placeholder(sql_input, params)
    print(result)