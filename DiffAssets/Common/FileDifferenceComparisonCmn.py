from enum import Enum
from Common.BaseConstantsCmn import BaseConstantsCmn as ConstantsCmn

class FileDifferenceComparisonCmn(ConstantsCmn):
    """
    階層によるグループ化機能に特有の定数
    """
    ORIGIN_LEFT_SHEET = ConstantsCmn.OriginSheet.LEFT_TARGET_PROJECT.value
    """
    ワークブックで処理を実行する対象の左のシート名（変更禁止）
    """
    ORIGIN_RIGHT_SHEET = ConstantsCmn.OriginSheet.RIGHT_TARGET_PROJECT.value
    """
    ワークブックで処理を実行する対象の右のシート名（変更禁止）
    """
    DIFF_PROJECT = "DIFF_PROJECT"
    """
    ワークブックで出力用の比較結果シート名（変更禁止）
    """
    class RowsKey(Enum):
        """
        列名
        """
        BLANK = ""
        """
        ""
        """
        NUMBER = "#"
        """
        "#"
        """
        FULL_PATH = "フルパス"
        """
        フルパス
        """
        COMPARISON_RESULT1 = "比較結果１"
        """
        比較結果１
        """
        COMPARISON_RESULT2 = "比較結果２"
        """
        比較結果２
        """
    BLANK = ""
    SLASH = '/'
    QUESTION_MARK = '？'
    CHECK_MARK = '✔'
    HYPHEN = '-'
    EX_METHOD_ROW = "=ROW()-3"
    SEARCH_CHAR = "."
    """
    検索する文字列
    """
