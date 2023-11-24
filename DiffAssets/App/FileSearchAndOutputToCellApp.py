from Common.FileSearchAndOutputToCellConstantsCmn import FileSearchAndOutputToCellConstantsCmn as ConstantsCmn

class FileSearchAndOutputToCellApp:
    """
    Excelシート内で特定の文字列を検索し、見つかった場合にその値を別のセルに移動するクラス。

    Attributes:
        worksheet (Worksheet): 操作対象のExcelワークシート。
    """

    def __init__(self, worksheet):
        """
        FileSearchAndOutputToCellAppのコンストラクタ。

        Args:
            worksheet (Worksheet): 操作するExcelワークシートのインスタンス。
        """
        self.worksheet = worksheet

    def main(self):
        """
        Excelシート内で特定の文字列を検索し、見つかった場合に別のセルに値を移動するメイン関数。
        """
        origin_cell = self.worksheet[ConstantsCmn.ORIGIN_RANGE]
        rows, cols = origin_cell.row, origin_cell.column
        for i in range(ConstantsCmn.CURRENT_SEARCH_RANGE_BEGIN_ROW_CNT, ConstantsCmn.CURRENT_SEARCH_RANGE_END_ROW_CNT):
            self.search_char_and_output(rows + i, cols)

    def search_char_and_output(self, rows, cols):
        """
        指定された行と列の範囲内でSEARCH_CHARが含まれているセルを検索し、
        見つかった場合にその値を別のセルに移動する。

        Args:
            rows (int): 検索する行の開始インデックス。
            cols (int): 検索する列の開始インデックス。
        """
        for i in range(ConstantsCmn.CURRENT_SEARCH_RANGE_BEGIN_COL_CNT, ConstantsCmn.CURRENT_SEARCH_RANGE_END_COL_CNT):
            cell_value = self.worksheet.cell(row=rows, column=cols + i).value
            if self.is_found(cell_value):
                self.cut_and_paste_of_variable(rows, cols + i, cols + ConstantsCmn.CURRENT_SEARCH_RANGE_OUTPUT_COL_CNT)
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

    @staticmethod
    def is_found(val):
        """
        与えられた文字列内にSEARCH_CHARが含まれているかどうかを判定する。

        Args:
            val (str): 検索する文字列。

        Returns:
            bool: SEARCH_CHARが含まれている場合はTrue、そうでない場合はFalse。
        """
        return ConstantsCmn.SEARCH_CHAR in val if val else False
