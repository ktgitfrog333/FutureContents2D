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
beans_list = []  # 2次元配列を宣言
beans = []
bean = GroupingByHierarchyBean()
bean.begin_idx = 4
bean.end_idx = 277
beans.append(bean)
bean_a = GroupingByHierarchyBean()
bean_a.begin_idx = 279
bean_a.end_idx = 385
beans.append(bean_a)
beans_list.append(beans)
beans_2 = []
bean_2 = GroupingByHierarchyBean()
bean_2.begin_idx = 5
bean_2.end_idx = 22
beans_2.append(bean_2)
beans_list.append(beans_2)
# メイン関数を実行
app.control_excel(beans_list)

# 変更を保存
wb.save(ConstantsCmn.ORIGIN_BOOK)
