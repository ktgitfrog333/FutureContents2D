import openpyxl
from Common.FileSearchAndOutputToCellConstantsCmn import FileSearchAndOutputToCellConstantsCmn as ConstantsCmn
from App.FileSearchAndOutputToCellApp import FileSearchAndOutputToCellApp

# ワークブックを読み込む
wb = openpyxl.load_workbook(ConstantsCmn.ORIGIN_BOOK)
ws = wb[ConstantsCmn.ORIGIN_SHEET]

# メイン関数を実行
app = FileSearchAndOutputToCellApp(ws)
app.main()

# 変更を保存
wb.save(ConstantsCmn.ORIGIN_BOOK)
