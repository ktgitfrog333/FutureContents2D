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

min_row_idx_ = 3
beans = app.load_right_sheet(min_row_idx_)
print(True if
      beans[0].full_path_source == "Area" and
      beans[0].result_1 == ConstantsCmn.HYPHEN and
      beans[0].result_2 == ConstantsCmn.CHECK_MARK and

      not [beans for bean in beans if bean.full_path_source == "Main" and
            bean.result_1 == ConstantsCmn.QUESTION_MARK and
            bean.result_2 == ConstantsCmn.QUESTION_MARK in bean] and

      not [beans for bean in beans if bean.full_path_source == "Main/Audios" and
            bean.result_1 == ConstantsCmn.QUESTION_MARK and
            bean.result_2 == ConstantsCmn.QUESTION_MARK in bean] and

      not [beans for bean in beans if bean.full_path_source == "Main/Audios/Mixer/MainMixer.mixer" and
            bean.result_1 == ConstantsCmn.QUESTION_MARK and
            bean.result_2 == ConstantsCmn.QUESTION_MARK in bean] and

      beans[1].full_path_source == "Area/Animations" and
      beans[1].result_1 == ConstantsCmn.HYPHEN and
      beans[1].result_2 == ConstantsCmn.CHECK_MARK and

      beans[22].full_path_source == "Area/Audios/BGM/bgm_ending.wav" and
      beans[22].result_1 == ConstantsCmn.HYPHEN and
      beans[22].result_2 == ConstantsCmn.CHECK_MARK else False)

# 変更を保存
wb.close()
# wb.save(ConstantsCmn.ORIGIN_BOOK)
