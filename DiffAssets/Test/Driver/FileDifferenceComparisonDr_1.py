import openpyxl
import sys
sys.path.append("C:\\FutureContents2D\\DiffAssets")
from Common.FileDifferenceComparisonCmn import FileDifferenceComparisonCmn as ConstantsCmn
from App.FileDifferenceComparisonApp import FileDifferenceComparisonApp
from App.Bean.FileDifferenceComparisonBean import FileDifferenceComparisonBean

# ワークブックを読み込む
wb = openpyxl.load_workbook(ConstantsCmn.ORIGIN_BOOK)
ws_l = wb[ConstantsCmn.ORIGIN_LEFT_SHEET]
ws_r = wb[ConstantsCmn.ORIGIN_RIGHT_SHEET]

# 新しいシートを作成
ws_d = wb.create_sheet(ConstantsCmn.DIFF_PROJECT)

# 列名を設定
app = FileDifferenceComparisonApp(ws_l, ws_r, ws_d)

# ディレクトリのパターン
#   ・第1引数
#       文字列の間に「/」が1以上つくかどうか
#       文字列の間に「.」が1つつくかどうか
#       文字列はランダムな組み合わせ
#   ・第2引数と第3引数
#       ConstantsCmn.QUESTION_MARKとConstantsCmn.QUESTION_MARKの組み合わせ
#       ConstantsCmn.HYPHENとConstantsCmn.CHECK_MARKの組み合わせ
#       ConstantsCmn.CHECK_MARKとConstantsCmn.HYPHENの組み合わせ
beans = [
    FileDifferenceComparisonBean("Test", ConstantsCmn.QUESTION_MARK, ConstantsCmn.QUESTION_MARK),
    FileDifferenceComparisonBean("Test/ASolution", ConstantsCmn.QUESTION_MARK, ConstantsCmn.QUESTION_MARK),
    FileDifferenceComparisonBean("Test/ASolution/ASubSolution", ConstantsCmn.QUESTION_MARK, ConstantsCmn.QUESTION_MARK),
    FileDifferenceComparisonBean("Test/ASolution/ASubSolution/AFeature.xxx", ConstantsCmn.QUESTION_MARK, ConstantsCmn.QUESTION_MARK),
    
    FileDifferenceComparisonBean("Test/CSolution", ConstantsCmn.CHECK_MARK, ConstantsCmn.HYPHEN),
    FileDifferenceComparisonBean("Test/CSolution/CSubSolution", ConstantsCmn.CHECK_MARK, ConstantsCmn.HYPHEN),
    FileDifferenceComparisonBean("Test/CSolution/CSubSolution/CFeature.xxx", ConstantsCmn.CHECK_MARK, ConstantsCmn.HYPHEN),

    FileDifferenceComparisonBean("Test/BSolution", ConstantsCmn.HYPHEN, ConstantsCmn.CHECK_MARK),
    FileDifferenceComparisonBean("Test/BSolution/BSubSolution", ConstantsCmn.HYPHEN, ConstantsCmn.CHECK_MARK),
    FileDifferenceComparisonBean("Test/BSolution/BSubSolution/BFeature.xxx", ConstantsCmn.HYPHEN, ConstantsCmn.CHECK_MARK),
]
app.sort_and_append_worksheet(beans, 3)

# 変更を保存
# wb.close()
wb.save(ConstantsCmn.ORIGIN_BOOK)
