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
beans_______ = app.load_left_sheet(min_row_idx_)
print(True if
      beans_______[0].full_path_source == "Main" and
      beans_______[0].result_1 == ConstantsCmn.QUESTION_MARK and
      beans_______[0].result_2 == ConstantsCmn.QUESTION_MARK and
      
      beans_______[1].full_path_source == "Main/Audios" and
      beans_______[1].result_1 == ConstantsCmn.QUESTION_MARK and
      beans_______[1].result_2 == ConstantsCmn.QUESTION_MARK and

      beans_______[9].full_path_source == "Main/Audios/Mixer/MainMixer.mixer" and
      beans_______[9].result_1 == ConstantsCmn.QUESTION_MARK and
      beans_______[9].result_2 == ConstantsCmn.QUESTION_MARK and

      beans_______[3].full_path_source == "Main/Audios/BGM/bgm_stage_vol1(1-10).mp3" and
      beans_______[3].result_1 == ConstantsCmn.CHECK_MARK and
      beans_______[3].result_2 == ConstantsCmn.HYPHEN else False)

# 変更を保存
wb.close()
# wb.save(ConstantsCmn.ORIGIN_BOOK)
