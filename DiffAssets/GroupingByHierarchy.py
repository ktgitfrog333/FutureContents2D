import openpyxl
from Common.GroupingByHierarchyConstantsCmn import GroupingByHierarchyConstantsCmn as ConstantsCmn
from App.GroupingByHierarchyApp import GroupingByHierarchyApp

# ワークブックを読み込む
wb = openpyxl.load_workbook(ConstantsCmn.ORIGIN_BOOK)
ws = wb[ConstantsCmn.ORIGIN_SHEET]

# メイン関数を実行
app = GroupingByHierarchyApp(ws)
app.main()

# 変更を保存
wb.save(ConstantsCmn.ORIGIN_BOOK)
