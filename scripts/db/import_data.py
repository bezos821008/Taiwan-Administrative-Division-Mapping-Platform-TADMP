import os
import pandas as pd
import psycopg2

def import_data(excel_path):
    """ 將 Excel 數據寫入 PostgreSQL """
    try:
        df = pd.read_excel(excel_path, engine="openpyxl")
    except Exception as e:
        print(f"讀取 Excel 檔案時發生錯誤：{e}")
        return

    if '縣市' not in df.columns or 'Township' not in df.columns:
        print("❌ 缺少必要欄位（縣市、Township），請確認 Excel 格式")
        return

    conn = psycopg2.connect(
        dbname="election_db",
        user="postgres",
        password="rs781023",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO area_data (county, township, urban_area, village)
            VALUES (%s, %s, %s, %s)
        """, (row['縣市'], row['Township'], row.get('Urban Area', None), row.get('村里', None)))

    conn.commit()
    cur.close()
    conn.close()
    print("✅ 資料匯入成功！")

if __name__ == "__main__":
    excel_file = os.path.join("..", "..", "data", "processed", "County_City_Township_UrbanArea.xlsx")
    import_data(excel_file)
