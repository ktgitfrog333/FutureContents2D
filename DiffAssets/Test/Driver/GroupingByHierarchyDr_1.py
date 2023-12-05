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
case = app.set_index_and_response(4, 277)
print("case:", True if case.begin_idx == 5 and case.end_idx == 277 else False)
case_2 = app.set_index_and_response(1, 1)
print("case_2:", True if case_2.begin_idx == 2 and case_2.end_idx == 1 else False)
ng_case = app.set_index_and_response(0, 0)
print("ng_case:", True if not ng_case else False)
ng_case_2 = app.set_index_and_response(-1, -1)
print("ng_case_2:", True if not ng_case_2 else False)
ng_case_3 = app.set_index_and_response(1, 0)
print("ng_case_3:", True if not ng_case_3 else False)
ng_case_4 = app.set_index_and_response(1, -1)
print("ng_case_4:", True if not ng_case_4 else False)
ng_case_5 = app.set_index_and_response(0, 1)
print("ng_case_5:", True if not ng_case_5 else False)
ng_case_6 = app.set_index_and_response(-1, 1)
print("ng_case_6:", True if not ng_case_6 else False)

# 閉じる
wb.close()
