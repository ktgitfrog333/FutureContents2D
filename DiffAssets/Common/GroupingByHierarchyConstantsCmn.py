from Common.BaseConstantsCmn import BaseConstantsCmn as ConstantsCmn

class GroupingByHierarchyConstantsCmn(ConstantsCmn):
    """
    階層によるグループ化機能に特有の定数
    """
    CURRENT_SEARCH_RANGE_BEGIN_ROW_IDX = 1 if ConstantsCmn.LEFT_OR_RIGHT else 1
    """
    ORIGIN_RANGEを始点として何番目の行を始点とするか
    """
    CURRENT_SEARCH_RANGE_END_ROW_IDX = 6 if ConstantsCmn.LEFT_OR_RIGHT else 10
    """
    ORIGIN_RANGEを始点として何番目の行を終点とするか
    """
    CURRENT_SEARCH_RANGE_BEGIN_COL_IDX = 0 if ConstantsCmn.LEFT_OR_RIGHT else 0
    """
    ORIGIN_RANGEを始点として何番目の列を始点とするか
    """
    CURRENT_SEARCH_RANGE_END_COL_IDX = 433 if ConstantsCmn.LEFT_OR_RIGHT else 2697
    """
    ORIGIN_RANGEを始点として何番目の列を終点とするか
    """
