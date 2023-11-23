from Common.GroupingByHierarchyConstantsCmn import GroupingByHierarchyConstantsCmn as ConstantsCmn
from App.Bean.GroupingByHierarchyBean import GroupingByHierarchyBean

class GroupingByHierarchyApp:
    # 定数
    SEARCH_CHAR = "."

    def __init__(self, worksheet):
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
        beans_list = []  # 2次元配列を宣言
        for i in range(ConstantsCmn.CURRENT_SEARCH_RANGE_BEGIN_ROW_IDX, ConstantsCmn.CURRENT_SEARCH_RANGE_END_ROW_IDX):
            beans = self.search_rows_and_get_indexes(rows, cols + i)
            if beans:
                beans_list.append(beans)
        return beans_list

    def control_excel(self, beans_list):
        level = 1  # グループ化レベルを設定
        for beans in beans_list:
            for item in beans:
                self.group_rows_in_excel(item.begin_idx, item.end_idx, level)
            level += 1  # 次のグループ化レベルに移行

    def search_rows_and_get_indexes(self, rows, cols):
        target_val= "", 
        begin_idx, end_idx = -1, -1
        beans = []
        for i in range(ConstantsCmn.CURRENT_SEARCH_RANGE_BEGIN_COL_IDX, ConstantsCmn.CURRENT_SEARCH_RANGE_END_COL_IDX):
            val = self.worksheet.cell(row=rows + i, column=cols).value
            if val and 0 < len(val):
                if val != target_val:
                    bean = self.set_index_and_responce(begin_idx, end_idx)
                    if bean:
                        beans.append(bean)
                    target_val = val
                    begin_idx = rows + i
                    end_idx = begin_idx
                else:
                    end_idx = rows + i
        val = self.worksheet.cell(end_idx, column=cols).value
        if val and 0 < len(val) and val == target_val:
            bean = self.set_index_and_responce(begin_idx, end_idx)
            if bean:
                beans.append(bean)
        return beans

    def set_index_and_responce(self, begin_idx, end_idx):
        if 0 < begin_idx and 0 < end_idx:
            bean = GroupingByHierarchyBean()
            # 先頭行はグループ化せずに残す
            bean.begin_idx = begin_idx + 1
            bean.end_idx = end_idx
            return bean
        else:
            None

    def group_rows_in_excel(self, start_row, end_row, level = 1):
        """
        特定の行をグループ化する。
        
        Args:
            start_row (int): グループ化を開始する行番号。
            end_row (int): グループ化を終了する行番号。
        """
        self.worksheet.row_dimensions.group(start_row, end_row, hidden=True, outline_level = level)

    def search_char_and_output(self, rows, cols):
        """
        指定された行と列の範囲内でSEARCH_CHARが含まれているセルを検索し、
        見つかった場合にその値を別のセルに移動する。

        Args:
            rows (int): 検索する行の開始インデックス。
            cols (int): 検索する列の開始インデックス。
        """
        for i in range(ConstantsCmn.CURRENT_SEARCH_RANGE_BEGIN_ROW_IDX, ConstantsCmn.CURRENT_SEARCH_RANGE_END_ROW_IDX):
            cell_value = self.worksheet.cell(row=rows, column=cols + i).value
            if self.is_found(cell_value):
                self.cut_and_paste_of_variable(self, rows, cols + i, cols + ConstantsCmn.CURRENT_OUTPUT_IDX)
                break

    def cut_and_paste_of_variable(self, rows, cols, target_cols):
        """
        指定されたセルの値を別のセルに移動し、元のセルは空にする。

        Args:
            rows (int): 移動元のセルの行インデックス。
            cols (int): 移動元のセルの列インデックス。
            target_cols (int): 移動先のセルの列インデックス。
        """
        source_cell = self.worksheet.cell(row=rows, column=cols)
        target_cell = self.worksheet.cell(row=rows, column=target_cols)
        target_cell.value = source_cell.value
        source_cell.value = None

    def is_found(val):
        """
        与えられた文字列内にSEARCH_CHARが含まれているかどうかを判定する。

        Args:
            val (str): 検索する文字列。

        Returns:
            bool: SEARCH_CHARが含まれている場合はTrue、そうでない場合はFalse。
        """
        return GroupingByHierarchyApp.SEARCH_CHAR in val if val else False
