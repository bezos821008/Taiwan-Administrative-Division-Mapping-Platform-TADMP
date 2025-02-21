import psycopg2

def create_database():
    """ 檢查並建立 election_db 資料庫 """
    conn = psycopg2.connect(
        dbname="postgres",  # 連線到 PostgreSQL 預設的 `postgres` 資料庫
        user="postgres",
        password="rs781023",
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    cur = conn.cursor()

    # 確保 `election_db` 存在
    cur.execute("SELECT 1 FROM pg_database WHERE datname = 'election_db';")
    exists = cur.fetchone()
    if not exists:
        cur.execute("CREATE DATABASE election_db;")
        print("✅ 資料庫 `election_db` 已建立！")
    else:
        print("✅ 資料庫 `election_db` 已存在，無需建立。")

    cur.close()
    conn.close()

def create_table():
    """ 連線到 `election_db`，並建立 `area_data` 表格 """
    conn = psycopg2.connect(
        dbname="election_db",
        user="postgres",
        password="rs781023",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # 建立 `area_data` 表格
    cur.execute("""
        CREATE TABLE IF NOT EXISTS area_data (
            id SERIAL PRIMARY KEY,
            county TEXT NOT NULL,
            township TEXT NOT NULL,
            urban_area TEXT,
            village TEXT
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("✅ `area_data` 表格建立完成！")

if __name__ == "__main__":
    create_database()  # 先確保資料庫存在
    create_table()  # 再建立表格
