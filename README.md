這個專案是藉由分析政府提供的全臺選舉名冊，去找出全臺的
縣市
鄉鎮市區
村里
的資料與對應關係


臺灣行政區域對應平台_Taiwan Administrative Division Mapping Platform (TADMP)/
├── 區域數據分析平台 (GeoInsight)/
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── .git/
│   ├── .idea/
│   ├── config/
│   ├── data/
│   │   ├── processed/
│   │   │   ├── County_City_Township_UrbanArea.xlsx
│   │   │   └── Election_Data_Merged.xlsx
│   │   └── raw/
│   │       └── Election_Data.xlsx
│   ├── scripts/
│   │   ├── analysis/
│   │   ├── db/
│   │   │   ├── test_db_data.py
│   │   │   ├── db_connector.py
│   │   │   ├── import_data.py
│   │   │   └── init_db.py
│   │   ├── etl/
│   │   │   ├── election_data_pipeline.py
│   │   │   └── scheduler/
│   │   ├── initialization/
│   │   │   ├── init_environment.py
│   │   │   ├── data/
│   │   │   │   ├── processed/
│   │   │   │   └── raw/
│   │   │   ├── docs/
│   │   │   └── scripts/
│   │   ├── scheduler/
│   │   └── tests/
│   │       ├── test_api.py
│   │       └── __pycache__/
│   ├── src/
│   │   ├── app.py
│   │   ├── core/
│   │   └── db/
│   └── __pycache__/


主要目錄說明：

config/：設定檔案目錄。
data/：存放資料，包括原始資料（raw）與處理後的資料（processed）。
scripts/：
analysis/：資料分析腳本
db/：與資料庫互動的模組，包括初始化、導入數據與連接功能。
etl/：ETL (Extract-Transform-Load) 流程，包括 election_data_pipeline.py 與排程器 (scheduler/)。
initialization/：環境初始化，如 init_environment.py。
scheduler/：排程管理模組。
tests/：測試腳本，如 test_api.py 和其他與資料庫相關的測試。
src/：
app.py：Flask 主應用程式入口。
core/ 與 db/：核心與資料庫模組程式碼。