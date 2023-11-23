class GroupingByHierarchyBean:
    def __init__(self, begin_idx=0, end_idx=0):
        self._begin_idx = begin_idx
        self._end_idx = end_idx

    @property
    def begin_idx(self):
        """begin_idxのゲッター"""
        return self._begin_idx

    @begin_idx.setter
    def begin_idx(self, value):
        """begin_idxのセッター。値の検証を行うことができる"""
        if value < 0:
            raise ValueError("begin_idxは0以上でなければなりません。")
        self._begin_idx = value

    @property
    def end_idx(self):
        """end_idxのゲッター"""
        return self._end_idx

    @end_idx.setter
    def end_idx(self, value):
        """end_idxのセッター。値の検証を行うことができる"""
        if value < 0:
            raise ValueError("end_idxは0以上でなければなりません。")
        self._end_idx = value
