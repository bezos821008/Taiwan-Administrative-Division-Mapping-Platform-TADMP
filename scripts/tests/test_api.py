import requests

def test_api():
    base_url = "http://127.0.0.1:5000"  # 如果您在 app.py 中設定 host="0.0.0.0"，本機測試仍可用 127.0.0.1

    # 1) 測試不帶任何參數 (查詢全部資料)
    url_all = f"{base_url}/areas"
    resp_all = requests.get(url_all)
    print(f"[GET {url_all}] 狀態碼: {resp_all.status_code}")
    print(f"回應: {resp_all.json()}\n")

    # 2) 測試以縣市作為參數 (範例: '臺北市' 或 '台北市' 依資料而定)
    url_county = f"{base_url}/areas"
    params_county = {"county": "臺北市"}
    resp_county = requests.get(url_county, params=params_county)
    print(f"[GET {url_county} with params={params_county}] 狀態碼: {resp_county.status_code}")
    print(f"回應: {resp_county.json()}\n")

    # 3) 測試以鄉鎮市區作為參數 (範例: '松山區' 依實際資料而定)
    url_township = f"{base_url}/areas"
    params_township = {"township": "松山區"}
    resp_township = requests.get(url_township, params=params_township)
    print(f"[GET {url_township} with params={params_township}] 狀態碼: {resp_township.status_code}")
    print(f"回應: {resp_township.json()}\n")

if __name__ == "__main__":
    test_api()
