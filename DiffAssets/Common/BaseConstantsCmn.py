from enum import Enum

class BaseConstantsCmn:
    """
    ベースとなる定数
    """
    ORIGIN_BOOK = "C:\\Users\\kzpaqu\\OneDrive\\ドキュメント\\g_ゲーム制作「エンタロピーゲームズ」\\003_JapanGameAward＆神ゲー創造主エボリューション\\プロジェクトアセット比較_v0.1.0.xlsx"
    """
    ワークブックが存在するフルパス（バックスラッシュは二つ）
    """
    LEFT_OR_RIGHT = True
    """
    左／右どちらのシートを対象とするか
    """
    class OriginSheet(Enum):
        LEFT_TARGET_PROJECT = "LEFT_TARGET_PROJECT"
        RIGHT_TARGET_PROJECT = "RIGHT_TARGET_PROJECT"
    """
    左／右のシート名
    """
    ORIGIN_SHEET = OriginSheet.LEFT_TARGET_PROJECT.value if LEFT_OR_RIGHT else OriginSheet.RIGHT_TARGET_PROJECT.value
    """
    ワークブックで処理を実行する対象のシート名（変更禁止）
    """
    ORIGIN_RANGE = "B3"
    """
    上記シートにて基準とするセル座標（変更禁止）
    """
