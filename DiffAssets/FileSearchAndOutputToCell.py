import openpyxl

# 定数
ORIGIN_BOOK = "C:\\Users\\kzpaqu\\OneDrive\\ドキュメント\\g_ゲーム制作「エンタロピーゲームズ」\\003_JapanGameAward＆神ゲー創造主エボリューション\\プロジェクトアセット比較_v0.1.0.xlsx"
ORIGIN_SHEET = "RIGHT_TARGET_PROJECT"
ORIGIN_RANGE = "B3"
CURRENT_SEARCH_RANGE_BEGIN_ROW_IDX = 2
CURRENT_SEARCH_RANGE_END_ROW_IDX = 10
CURRENT_SEARCH_RANGE_BEGIN_COL_IDX = 0
CURRENT_SEARCH_RANGE_END_COL_IDX = 2697
CURRENT_OUTPUT_IDX = 10
SEARCH_CHAR = "."

# ワークブックを読み込む
wb = openpyxl.load_workbook(ORIGIN_BOOK)
ws = wb[ORIGIN_SHEET]

def main():
    """
    Excelシート内で特定の文字列を検索し、見つかった場合に別のセルに値を移動するメイン関数。
    """
    origin_cell = ws[ORIGIN_RANGE]
    rows, cols = origin_cell.row, origin_cell.column
    for i in range(CURRENT_SEARCH_RANGE_BEGIN_COL_IDX, CURRENT_SEARCH_RANGE_END_COL_IDX):
        search_char_and_output(rows + i, cols)

def search_char_and_output(rows, cols):
    """
    指定された行と列の範囲内でSEARCH_CHARが含まれているセルを検索し、
    見つかった場合にその値を別のセルに移動する。

    Args:
        rows (int): 検索する行の開始インデックス。
        cols (int): 検索する列の開始インデックス。
    """
    for i in range(CURRENT_SEARCH_RANGE_BEGIN_ROW_IDX, CURRENT_SEARCH_RANGE_END_ROW_IDX):
        cell_value = ws.cell(row=rows, column=cols + i).value
        if is_found(cell_value):
            cut_and_paste_of_variable(rows, cols + i, cols + CURRENT_OUTPUT_IDX)
            break

def cut_and_paste_of_variable(rows, cols, target_cols):
    """
    指定されたセルの値を別のセルに移動し、元のセルは空にする。

    Args:
        rows (int): 移動元のセルの行インデックス。
        cols (int): 移動元のセルの列インデックス。
        target_cols (int): 移動先のセルの列インデックス。
    """
    source_cell = ws.cell(row=rows, column=cols)
    target_cell = ws.cell(row=rows, column=target_cols)
    target_cell.value = source_cell.value
    source_cell.value = None

def is_found(val):
    """
    与えられた文字列内にSEARCH_CHARが含まれているかどうかを判定する。

    Args:
        val (str): 検索する文字列。

    Returns:
        bool: SEARCH_CHARが含まれている場合はTrue、そうでない場合はFalse。
    """
    return SEARCH_CHAR in val if val else False

# メイン関数を実行
main()

# 変更を保存
wb.save(ORIGIN_BOOK)
