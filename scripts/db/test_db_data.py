import psycopg2
import pandas as pd

def test_db_data():
    """
    連線到 election_db 資料庫，查詢 area_data 表格的前 10 筆資料，
    並以 pandas DataFrame 形式印出。
    """
    try:
        # 根據您的實際連線參數修改
        conn = psycopg2.connect(
            dbname="election_db",
            user="postgres",
            password="rs781023",
            host="localhost",
            port="5432"
        )
    except Exception as e:
        print(f"❌ 連線資料庫失敗：{e}")
        return

    try:
        # 使用 pandas 的 read_sql 來查詢並載入成 DataFrame
        df = pd.read_sql("SELECT * FROM area_data LIMIT 10;", conn)
        conn.close()
        print("✅ 查詢成功，前 10 筆資料如下：\n")
        print(df)
    except Exception as e:
        print(f"❌ 查詢資料失敗：{e}")
    finally:
        conn.close()

if __name__ == "__main__":
    test_db_data()
