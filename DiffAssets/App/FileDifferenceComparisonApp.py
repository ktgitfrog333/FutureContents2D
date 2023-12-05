from Common.FileDifferenceComparisonCmn import FileDifferenceComparisonCmn as ConstantsCmn
from App.Bean.FileDifferenceComparisonBean import FileDifferenceComparisonBean

class FileDifferenceComparisonApp:
    def __init__(self, worksheet_left, worksheet_right, worksheet_diff):
        """
        FileDifferenceComparisonAppクラスのコンストラクタ。左右両方のワークシートと結果を格納するワークシートを初期化する。

        Args:
            worksheet_left (Worksheet): 比較のための左側のワークシート。
            worksheet_right (Worksheet): 比較のための右側のワークシート。
            worksheet_diff (Worksheet): 比較結果を格納するワークシート。
        """
        self.worksheet_left = worksheet_left
        self.worksheet_right = worksheet_right
        self.worksheet_diff = worksheet_diff

    def main(self):
        """
        メイン処理を実行するメソッド。左右のワークシートからデータを読み込み、差分を比較し、結果を別のワークシートに追記する。
        """
        rows = self.worksheet_left[ConstantsCmn.ORIGIN_RANGE].row
        # 左側のシートを読み込む
        left_beans = self.load_left_sheet(rows)
        # 右側のシートを読み込む
        right_beans = self.load_right_sheet(self.worksheet_right[ConstantsCmn.ORIGIN_RANGE].row)
        merge_beans = []
        merge_beans = left_beans + right_beans  # リストの加算で結合
        self.header_append_worksheet(rows - 1)
        self.sort_and_append_worksheet(merge_beans, rows)

    def load_right_sheet(self, rows: int) -> 'list[FileDifferenceComparisonBean]':
        """
        右側のワークシートからデータを読み込み、FileDifferenceComparisonBeanオブジェクトのリストを生成する。

        Args:
            rows (int): 読み込み開始行。

        Returns:
            list[FileDifferenceComparisonBean]: 生成されたBeanのリスト。
        """
        return self.load_any_sheet(self.worksheet_right, rows, self.search_in_left_sheet)

    def load_left_sheet(self, rows: int) -> 'list[FileDifferenceComparisonBean]':
        """
        左側のワークシートからデータを読み込み、FileDifferenceComparisonBeanオブジェクトのリストを生成する。

        Args:
            rows (int): 読み込み開始行。

        Returns:
            list[FileDifferenceComparisonBean]: 生成されたBeanのリスト。
        """
        return self.load_any_sheet(self.worksheet_left, rows, self.search_in_right_sheet)
    
    def load_any_sheet(self, worksheet_source, rows, search_in_anu_sheet) -> 'list[FileDifferenceComparisonBean]':
        """
        任意のワークシートからデータを読み込み、条件に基づいてFileDifferenceComparisonBeanオブジェクトを生成する。

        Args:
            worksheet_source (Worksheet): データの読み込み元ワークシート。
            rows (int): 読み込み開始行。
            search_in_anu_sheet (Callable): 特定の条件に基づくBeanを生成する関数。

        Returns:
            list[FileDifferenceComparisonBean]: 生成されたBeanのリスト。
        """
        beans: list[FileDifferenceComparisonBean] = []
        for vals in worksheet_source.iter_rows(min_row=rows, values_only=True):
            bean = search_in_anu_sheet(self.get_full_path(vals), rows)
            if bean:
                beans.append(bean)
        return beans

    def search_in_right_sheet(self, full_path_source: str, rows: int) -> FileDifferenceComparisonBean:
        """
        右側のワークシートからデータを読み込み、FileDifferenceComparisonBeanオブジェクトを生成する。
        比較した結果により返却内容が下記の様に異なる
            ・一致：    フルパス、検索結果①「？」、検索結果②「？」
            ・不一致：  フルパス、検索結果①「✔」、検索結果②「-」

        Args:
            full_path_source（str）: フルパス
            rows (int): 読み込み開始行。

        Returns:
            FileDifferenceComparisonBean 生成されたBean。
        """
        for vals in self.worksheet_right.iter_rows(min_row=rows, values_only=True):
            if full_path_source == self.get_full_path(vals):
                return FileDifferenceComparisonBean(full_path_source, ConstantsCmn.QUESTION_MARK, ConstantsCmn.QUESTION_MARK)
        else:
            return FileDifferenceComparisonBean(full_path_source, ConstantsCmn.CHECK_MARK, ConstantsCmn.HYPHEN)

    def search_in_left_sheet(self, full_path_source: str, rows: int) -> FileDifferenceComparisonBean or None:
        """
        左側のワークシートからデータを読み込み、FileDifferenceComparisonBeanオブジェクトを生成する。
        比較した結果により返却内容が下記の様に異なる
            ・一致：    None
            ・不一致：  フルパス、検索結果①「-」、検索結果②「✔」

        Args:
            full_path_source（str）: フルパス
            rows (int): 読み込み開始行。

        Returns:
            FileDifferenceComparisonBean 生成されたBean。
        """
        for vals in self.worksheet_left.iter_rows(min_row=rows, values_only=True):
            if full_path_source == self.get_full_path(vals):
                return None
        else:
            return FileDifferenceComparisonBean(full_path_source, ConstantsCmn.HYPHEN, ConstantsCmn.CHECK_MARK)

    @staticmethod
    def get_full_path(vals) -> str:
        """
        与えられた行データから完全なファイルパスを生成する。

        Args:
            vals (tuple): 行データ。

        Returns:
            str: 生成された完全なファイルパス。
        """
        contents = [content for idx, content in enumerate(vals) if idx > 1 and content is not None]
        directory_path = ConstantsCmn.SLASH.join([content[1] for content in enumerate(contents) if ConstantsCmn.SEARCH_CHAR not in content])
        asset_name = [content for content in enumerate(contents) if ConstantsCmn.SEARCH_CHAR in content]
        return directory_path + ConstantsCmn.SLASH + asset_name if asset_name and 0 < len(asset_name) else directory_path

    def header_append_worksheet(self, rows: int):
        """
        指定された行にヘッダーを追加する。

        Args:
            rows (int): 追加する行番号。
        """
        row_values = [ConstantsCmn.RowsKey.BLANK.value,
                      ConstantsCmn.RowsKey.NUMBER.value,
                      ConstantsCmn.RowsKey.FULL_PATH.value,
                      ConstantsCmn.RowsKey.COMPARISON_RESULT1.value,
                      ConstantsCmn.RowsKey.COMPARISON_RESULT2.value]
        for col, value in enumerate(row_values, start=1):
            self.worksheet_diff.cell(row=rows, column=col).value = value

    def sort_and_append_worksheet(self, beans: 'list[FileDifferenceComparisonBean]', rows: int):
        """
        与えられたBeanのリストをソートし、結果をワークシートに追記する。

        Args:
            beans (list[FileDifferenceComparisonBean]): ソートおよび追記するBeanのリスト。
            rows (int): データの追記を開始する行番号。
        """
        beans.sort(key=lambda x: x.full_path_source)
        for idx, bean in enumerate(beans, start=rows):
            row_values = [ConstantsCmn.BLANK, ConstantsCmn.EX_METHOD_ROW, bean.full_path_source, bean.result_1, bean.result_2]
            for col, value in enumerate(row_values, start=1):
                self.worksheet_diff.cell(row=idx, column=col).value = value
