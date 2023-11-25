class FileDifferenceComparisonBean:
    def __init__(self, full_path_source="", result_1="", result_2=""):
        self._full_path_source = full_path_source
        self._result_1 = result_1
        self._result_2 = result_2

    @property
    def full_path_source(self):
        """ファイルの完全パスを取得するゲッター"""
        return self._full_path_source

    @full_path_source.setter
    def full_path_source(self, value):
        """ファイルの完全パスを設定するセッター"""
        self._full_path_source = value

    @property
    def result_1(self):
        """比較結果1を取得するゲッター"""
        return self._result_1

    @result_1.setter
    def result_1(self, value):
        """比較結果1を設定するセッター"""
        self._result_1 = value

    @property
    def result_2(self):
        """比較結果2を取得するゲッター"""
        return self._result_2

    @result_2.setter
    def result_2(self, value):
        """比較結果2を設定するセッター"""
        self._result_2 = value
