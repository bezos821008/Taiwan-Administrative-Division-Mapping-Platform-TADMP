import os
import pandas as pd

def merge_all_sheets(election_file_path, merged_file_path):
    """
    1. 讀取 Election_Data.xlsx 中的所有工作表 (sheet)，以 skiprows=1 方式解析，
       新增「縣市」欄位 (sheet 名稱)。
    2. 只保留「縣市」「鄉鎮市區」「村里」三欄，並去除重複。
    3. 輸出為中繼檔 merged_file_path (例如: Election_Data_Merged.xlsx)。
    """
    try:
        xls = pd.ExcelFile(election_file_path, engine="openpyxl")
    except Exception as e:
        print(f"無法讀取 {election_file_path}，錯誤：{e}")
        return False

    sheet_names = xls.sheet_names
    print("所有工作表名稱：", sheet_names)

    df_list = []

    for sheet in sheet_names:
        try:
            # 跳過前 1 行（skiprows=1），將第 2 行當作欄位名稱
            df_temp = pd.read_excel(
                election_file_path,
                engine="openpyxl",
                sheet_name=sheet,
                header=0,
                skiprows=1
            )

            # 新增「縣市」欄位（值為該 sheet 的名稱）
            df_temp["縣市"] = sheet

            # 「行政區別」→「鄉鎮市區」，「村里別」→「村里」
            if "行政區別" in df_temp.columns:
                df_temp.rename(columns={"行政區別": "鄉鎮市區"}, inplace=True)
            else:
                print(f"工作表 {sheet} 中找不到『行政區別』欄位，將無法對應『鄉鎮市區』")
                continue

            if "村里別" in df_temp.columns:
                df_temp.rename(columns={"村里別": "村里"}, inplace=True)
            else:
                print(f"工作表 {sheet} 中找不到『村里別』欄位，將無法對應『村里』")
                continue

            # 只保留三個欄位
            df_temp = df_temp[["縣市", "鄉鎮市區", "村里"]]

            df_list.append(df_temp)

        except Exception as e:
            print(f"讀取 sheet={sheet} 時發生錯誤：{e}")

    if not df_list:
        print("無法合併任何工作表，請檢查檔案。")
        return False

    # 合併所有工作表的資料
    merged_df = pd.concat(df_list, ignore_index=True)

    # 去除重複資料
    merged_df.drop_duplicates(inplace=True)

    # 確保輸出目錄存在
    output_dir = os.path.dirname(merged_file_path)
    os.makedirs(output_dir, exist_ok=True)

    # 儲存結果
    try:
        merged_df.to_excel(merged_file_path, index=False)
        print(f"所有工作表合併完成，只保留「縣市」「鄉鎮市區」「村里」並去重，輸出至：{merged_file_path}")
        return True
    except Exception as e:
        print(f"儲存檔案時發生錯誤：{e}")
        return False


def create_township_urban_area(input_file_path, output_file_path):
    """
    1. 讀取合併後的 Election_Data_Merged.xlsx（含「縣市」「鄉鎮市區」「村里」）
    2. 產生 Township 與 Urban Area 欄位，最後輸出到 output_file_path
       (例如 County_City_Township_UrbanArea.xlsx)。
    """
    try:
        df = pd.read_excel(input_file_path, engine="openpyxl")
    except Exception as e:
        print(f"讀取檔案 {input_file_path} 時發生錯誤：{e}")
        return

    # 檢查必要欄位
    if '縣市' not in df.columns or '鄉鎮市區' not in df.columns:
        print("檔案中缺少必要的欄位（縣市、鄉鎮市區）")
        return

    # 將「鄉鎮市區」複製到 Township 欄位
    df['Township'] = df['鄉鎮市區']

    # 若字串中含有「市」，則在 Urban Area 欄位中填值，否則留空
    df['Urban Area'] = df['鄉鎮市區'].apply(lambda x: x if '市' in str(x) else '')

    # 視需求保留欄位
    keep_cols = ['縣市', 'Township', 'Urban Area', '村里'] if '村里' in df.columns else ['縣市', 'Township', 'Urban Area']
    df = df[keep_cols]

    # 確保輸出目錄存在
    output_dir = os.path.dirname(output_file_path)
    os.makedirs(output_dir, exist_ok=True)

    try:
        df.to_excel(output_file_path, index=False)
        print(f"已產生 Township/Urban Area 欄位，輸出至：{output_file_path}")
    except Exception as e:
        print(f"儲存檔案時發生錯誤：{e}")


if __name__ == "__main__":
    # 1) 定義原始檔案 (含多個工作表)
    election_file = os.path.join("..", "..", "data", "raw", "Election_Data.xlsx")

    # 2) 中繼檔：合併多工作表後，只留 縣市/鄉鎮市區/村里
    merged_file = os.path.join("..", "..", "data", "processed", "Election_Data_Merged.xlsx")

    # 3) 最終檔案：產生 Township/Urban Area 後的檔案
    final_file = os.path.join("..", "..", "data", "processed", "County_City_Township_UrbanArea.xlsx")

    # 第一步：合併多工作表，產生中繼檔
    success = merge_all_sheets(election_file, merged_file)
    if not success:
        print("合併多工作表失敗，請檢查前面訊息。")
    else:
        # 第二步：針對合併後的檔案，產生 Township / Urban Area 欄位
        create_township_urban_area(merged_file, final_file)
