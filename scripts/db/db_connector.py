import os
from sqlalchemy import create_engine

def get_engine():
    # 從環境變數取得資料庫設定，若未設定則使用預設值
    db_user = os.getenv("DB_USER", "postgresql")
    db_pass = os.getenv("DB_PASS", "rs781023")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "your_db")

    connection_string = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(connection_string)
    return engine

if __name__ == "__main__":
    engine = get_engine()
    print("Database engine created successfully.")
