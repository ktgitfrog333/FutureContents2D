from Common.BaseConstantsCmn import BaseConstantsCmn as ConstantsCmn

class FileSearchAndOutputToCellConstantsCmn(ConstantsCmn):
    """
    検索機能に特有の定数
    """
    CURRENT_SEARCH_RANGE_BEGIN_COL_CNT = 2 if ConstantsCmn.LEFT_OR_RIGHT else 2
    """
    ORIGIN_RANGEを始点として何番目の列を始点とするか
    """
    CURRENT_SEARCH_RANGE_END_COL_CNT = 6 if ConstantsCmn.LEFT_OR_RIGHT else 10
    """
    ORIGIN_RANGEを始点として何番目の列を終点とするか
    """
    CURRENT_SEARCH_RANGE_BEGIN_ROW_CNT = 0 if ConstantsCmn.LEFT_OR_RIGHT else 0
    """
    ORIGIN_RANGEを始点として何番目の行を始点とするか
    """
    CURRENT_SEARCH_RANGE_END_ROW_CNT = 433 if ConstantsCmn.LEFT_OR_RIGHT else 2697
    """
    ORIGIN_RANGEを始点として何番目の行を終点とするか
    """
    CURRENT_SEARCH_RANGE_OUTPUT_COL_CNT = 6 if ConstantsCmn.LEFT_OR_RIGHT else 10
    """
    ORIGIN_RANGEを始点として何番目の列へ検索結果を出力するか
    """
    SEARCH_CHAR = "."
    """
    検索する文字列
    """
