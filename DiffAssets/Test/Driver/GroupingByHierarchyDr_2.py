import openpyxl
import sys
sys.path.append("C:\\FutureContents2D\\DiffAssets")
from Common.GroupingByHierarchyConstantsCmn import GroupingByHierarchyConstantsCmn as ConstantsCmn
from App.GroupingByHierarchyApp import GroupingByHierarchyApp

# ワークブックを読み込む
wb = openpyxl.load_workbook(ConstantsCmn.ORIGIN_BOOK)
ws = wb[ConstantsCmn.ORIGIN_SHEET]

# メイン関数を実行
app = GroupingByHierarchyApp(ws)
case = app.search_rows_and_get_indexes(3, 3)
print("case:", True if len(case) == 18 else False)
case_2 = app.search_rows_and_get_indexes(3, 4)
print("case_2:", True if len(case_2) == 91 else False)
case_3 = app.search_rows_and_get_indexes(3, 11)
print("case_3:", True if len(case_3) == 6 else False)

# 閉じる
wb.close()
