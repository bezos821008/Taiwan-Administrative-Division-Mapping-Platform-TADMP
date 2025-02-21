from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

def get_db_connection():
    """
    建立並回傳資料庫連線物件 (例如 PostgreSQL)
    - 若使用 docker-compose，請確認 host、port、user、password、dbname
    """
    print("== DEBUG: 建立資料庫連線 ==")  # Debug
    conn = psycopg2.connect(
        dbname="election_db",
        user="postgres",
        password="rs781023",
        host="localhost",
        port="5432"
    )
    return conn

@app.route("/areas", methods=["GET"])
def get_areas():
    """
    查詢區域資料
    GET /areas?county=臺北市&township=松山區
    """
    print("== DEBUG: get_areas route called ==")  # Debug

    # 從查詢參數中取值
    county = request.args.get("county")
    township = request.args.get("township")
    print(f"== DEBUG: 參數 county={county}, township={township} ==")  # Debug

    # 準備 SQL
    query = "SELECT county, township, urban_area, village FROM area_data WHERE 1=1"
    params = []

    if county:
        query += " AND county = %s"
        params.append(county)
    if township:
        query += " AND township = %s"
        params.append(township)

    print(f"== DEBUG: 即將執行 SQL: {query}, params={params} ==")  # Debug

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query, tuple(params))
        results = cur.fetchall()
        cur.close()
        conn.close()
        print("== DEBUG: 資料庫查詢成功，筆數：", len(results))  # Debug

        data = []
        for row in results:
            data.append({
                "縣市": row[0],  # county
                "鄉鎮市區": row[1],  # township
                "村里": row[3]
            })

        return jsonify(data)

    except Exception as e:
        # 若出現錯誤，印出錯誤訊息，並回傳 JSON 格式的錯誤
        print("== ERROR: 發生例外 ==", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
