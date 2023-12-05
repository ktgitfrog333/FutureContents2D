import openpyxl
import sys
sys.path.append("C:\\FutureContents2D\\DiffAssets")
from Common.FileDifferenceComparisonCmn import FileDifferenceComparisonCmn as ConstantsCmn
from App.FileDifferenceComparisonApp import FileDifferenceComparisonApp

# ワークブックを読み込む
wb = openpyxl.load_workbook(ConstantsCmn.ORIGIN_BOOK)
ws_l = wb[ConstantsCmn.ORIGIN_LEFT_SHEET]
ws_r = wb[ConstantsCmn.ORIGIN_RIGHT_SHEET]

# 新しいシートを作成
ws_d = wb.create_sheet(ConstantsCmn.DIFF_PROJECT)

# 列名を設定
app = FileDifferenceComparisonApp(ws_l, ws_r, ws_d)

full_path___ = "full_path"
min_row_idx_ = 3
bean________ = app.search_in_left_sheet(
full_path___,
min_row_idx_)
print(True if
    bean________  and 0 < len(
    bean________.full_path_source) and
    bean________.full_path_source ==
    full_path___ and
    bean________.result_1 == ConstantsCmn.HYPHEN and
    bean________.result_2 == ConstantsCmn.CHECK_MARK else False)

full_path___2 = "Main"
min_row_idx_2 = 3
bean________2 = app.search_in_left_sheet(
full_path___2,
min_row_idx_2)
print(True if not
    bean________2 else False)

full_path___3 = "Main/Audios"
min_row_idx_3 = 3
beans_______3 = app.search_in_left_sheet(
full_path___3,
min_row_idx_3)
print(True if not
    beans_______3 else False)

full_path___4 = "Main/Audios/BGM"
min_row_idx_4 = 3
beans_______4 = app.search_in_left_sheet(
full_path___4,
min_row_idx_4)
print(True if not
    beans_______4 else False)

full_path___5 = "Main/Audios/BGM/bgm_stage_vol1(1-10).mp3"
min_row_idx_5 = 3
beans_______5 = app.search_in_left_sheet(
full_path___5,
min_row_idx_5)
print(True if not
    beans_______5 else False)

# 変更を保存
wb.close()
# wb.save(ConstantsCmn.ORIGIN_BOOK)
