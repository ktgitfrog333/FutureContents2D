from Common.GroupingByHierarchyConstantsCmn import GroupingByHierarchyConstantsCmn as ConstantsCmn
from App.Bean.GroupingByHierarchyBean import GroupingByHierarchyBean

class GroupingByHierarchyApp:
    def __init__(self, worksheet):
        """
        GroupingByHierarchyAppクラスのコンストラクタ。

        Args:
            worksheet (Worksheet): 操作するExcelのワークシート。
        """
        self.worksheet = worksheet

    def main(self):
        """
        Excelシート内で特定の文字列を検索し、見つかった場合に別のセルに値を移動するメイン関数。
        """
        origin_cell = self.worksheet[ConstantsCmn.ORIGIN_RANGE]
        rows, cols = origin_cell.row, origin_cell.column
        beans_list = self.instance_beans_list(rows, cols)
        self.control_excel(beans_list)  # beans_listを使用してcontrol_excelを呼び出す
    
    def instance_beans_list(self, rows, cols):
        """
        指定された行と列に基づいて、GroupingByHierarchyBeanオブジェクトのリストを生成する。

        Args:
            rows (int): 開始行インデックス。
            cols (int): 開始列インデックス。

        Returns:
            list: 生成されたGroupingByHierarchyBeanオブジェクトのリスト。
        """
        beans_list = []
        for i in range(ConstantsCmn.CURRENT_SEARCH_RANGE_BEGIN_ROW_IDX, ConstantsCmn.CURRENT_SEARCH_RANGE_END_ROW_IDX):
            beans = self.search_rows_and_get_indexes(rows, cols + i)
            if beans:
                beans_list.append(beans)
        return beans_list

    def control_excel(self, beans_list):
        """
        与えられたBeanリストに基づいてExcelシートの行をグループ化する。

        Args:
            beans_list (list): グループ化する行のBeanリスト。
        """
        level = 1
        for beans in beans_list:
            for item in beans:
                self.group_rows_in_excel(item.begin_idx, item.end_idx, level)
            level += 1

    def search_rows_and_get_indexes(self, rows, cols):
        """
        指定された行と列から、検索条件に合致する行のインデックスを取得する。

        Args:
            rows (int): 検索を開始する行インデックス。
            cols (int): 検索を開始する列インデックス。

        Returns:
            list: 検索に合致したGroupingByHierarchyBeanオブジェクトのリスト。
        """
        target_val = ""  # タプルではなく単一の文字列で初期化
        begin_idx, end_idx = -1, -1
        beans = []
        for i in range(ConstantsCmn.CURRENT_SEARCH_RANGE_BEGIN_COL_IDX, ConstantsCmn.CURRENT_SEARCH_RANGE_END_COL_IDX):
            val = self.worksheet.cell(row=rows + i, column=cols).value
            if val and 0 < len(val):
                if val != target_val:
                    bean = self.set_index_and_response(begin_idx, end_idx)
                    if bean:
                        beans.append(bean)
                    target_val = val
                    begin_idx = rows + i
                    end_idx = begin_idx
                else:
                    end_idx = rows + i
        val = self.worksheet.cell(end_idx, column=cols).value
        if val and 0 < len(val) and val == target_val:
            bean = self.set_index_and_response(begin_idx, end_idx)
            if bean:
                beans.append(bean)
        return beans

    def set_index_and_response(self, begin_idx, end_idx):
        """
        指定された開始行と終了行に基づいてGroupingByHierarchyBeanオブジェクトを生成する。

        Args:
            begin_idx (int): 開始行インデックス。
            end_idx (int): 終了行インデックス。

        Returns:
            GroupingByHierarchyBean: 生成されたオブジェクト。条件に合致しない場合はNone。
        """
        if begin_idx > 0 and end_idx > 0:
            bean = GroupingByHierarchyBean()
            bean.begin_idx = begin_idx + 1
            bean.end_idx = end_idx
            return bean
        return None

    def group_rows_in_excel(self, start_row, end_row, level=1):
        """
        特定の行をグループ化する。

        Args:
            start_row (int): グループ化を開始する行番号。
            end_row (int): グループ化を終了する行番号。
            level (int): グループ化のレベル。デフォルトは1。
        """
        self.worksheet.row_dimensions.group(start_row, end_row, hidden=True, outline_level=level)
