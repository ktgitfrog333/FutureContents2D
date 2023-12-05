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
bean________ = app.search_in_right_sheet(full_path___, min_row_idx_)
print(True if bean________.full_path_source == full_path___ and
      bean________.result_1 == ConstantsCmn.CHECK_MARK and
      bean________.result_2 == ConstantsCmn.HYPHEN else False)

full_path___2 = "Area"
min_row_idx_2 = 3
bean________2 = app.search_in_right_sheet(
full_path___2,
min_row_idx_2)
print(True if
    bean________2.full_path_source ==
    full_path___2 and
    bean________2.result_1 == ConstantsCmn.QUESTION_MARK and
    bean________2.result_2 == ConstantsCmn.QUESTION_MARK else False)

full_path___3 = "Area/Animations"
min_row_idx_3 = 3
bean________3 = app.search_in_right_sheet(
full_path___3,
min_row_idx_3)
print(True if
    bean________3.full_path_source ==
    full_path___3 and
    bean________3.result_1 == ConstantsCmn.QUESTION_MARK and
    bean________3.result_2 == ConstantsCmn.QUESTION_MARK else False)

full_path___4 = "Area/Audios/BGM/bgm_ending.wav"
min_row_idx_4 = 3
bean________4 = app.search_in_right_sheet(
full_path___4,
min_row_idx_4)
print(True if
    bean________4.full_path_source ==
    full_path___4 and
    bean________4.result_1 == ConstantsCmn.QUESTION_MARK and
    bean________4.result_2 == ConstantsCmn.QUESTION_MARK else False)

full_path___5 = "Area/Audios/BGM/bgm_ending_testtest.wav"
min_row_idx_5 = 3
bean________5 = app.search_in_right_sheet(
full_path___5,
min_row_idx_5)
print(True if
      bean________5.full_path_source ==
      full_path___5 and
      bean________5.result_1 == ConstantsCmn.CHECK_MARK and
      bean________5.result_2 == ConstantsCmn.HYPHEN else False)

# 変更を保存
wb.close()
# wb.save(ConstantsCmn.ORIGIN_BOOK)
