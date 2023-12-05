import openpyxl
import sys
sys.path.append("C:\\FutureContents2D\\DiffAssets")
from Common.GroupingByHierarchyConstantsCmn import GroupingByHierarchyConstantsCmn as ConstantsCmn
from App.GroupingByHierarchyApp import GroupingByHierarchyApp
from App.Bean.GroupingByHierarchyBean import GroupingByHierarchyBean

# ワークブックを読み込む
wb = openpyxl.load_workbook(ConstantsCmn.ORIGIN_BOOK)
ws = wb[ConstantsCmn.ORIGIN_SHEET]

# input
app = GroupingByHierarchyApp(ws)
# メイン関数を実行
beans_list = app.instance_beans_list(3, 2)
level = 1  # グループ化レベルを設定
for beans in beans_list:
    for item in beans:
        print('begin_idx:' + str(item.begin_idx), 'end_idx:' + str(item.end_idx), 'level:' + str(level))
    level += 1  # 次のグループ化レベルに移行

# 変更を保存
wb.close()
