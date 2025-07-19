"""
このファイルは、固定の文字列や数値などのデータを変数として一括管理するファイルです。
"""

############################################################
# 共通変数の定義
############################################################

# ==========================================
# 画面表示系
# ==========================================
APP_NAME = "対話型商品レコメンド生成AIアプリ"
USER_ICON_FILE_PATH = "./images/user_icon.jpg"
AI_ICON_FILE_PATH = "./images/ai_icon.jpg"
ERROR_ICON = ":material/error:"
WARNING_ICON_URL = "https://hide-ota.github.io/hide_ota.github.io/images/icons/warning_icon.png"
CHAT_INPUT_HELPER_TEXT = "こちらからお探しの商品の特徴や名前を入力してください。"
SPINNER_TEXT = "レコメンドする商品の検討中..."


# ==========================================
# ログ出力系
# ==========================================
LOG_DIR_PATH = "./logs"
LOGGER_NAME = "ApplicationLog"
LOG_FILE = "application.log"
APP_BOOT_MESSAGE = "アプリが起動されました。"

# ==========================================
# Retriever設定系
# ==========================================
TOP_K = 5
RETRIEVER_WEIGHTS = [0.5, 0.5]


# ==========================================
# RAG参照用のデータソース系
# ==========================================
RAG_SOURCE_PATH = "./data/products.csv"


# ==========================================
# エラー・警告メッセージ
# ==========================================
COMMON_ERROR_MESSAGE = "このエラーが繰り返し発生する場合は、管理者にお問い合わせください。"
INITIALIZE_ERROR_MESSAGE = "初期化処理に失敗しました。"
CONVERSATION_LOG_ERROR_MESSAGE = "過去の会話履歴の表示に失敗しました。"
RECOMMEND_ERROR_MESSAGE = "商品レコメンドに失敗しました。"
LLM_RESPONSE_DISP_ERROR_MESSAGE = "商品情報の表示に失敗しました。"

STOCK_FEW_WARNING_MESSAGE = "⚠ご好評につき、在庫数が残りわずかです。購入をご希望の場合、お早めのご注文をおすすめいたします。"

STOCK_NONE_WARNING_MESSAGE_HTML = f"""
<div style="
    display: flex;
    align-items: center;
    background-color: #f8d7da;
    padding: 10px;
    border-radius: 5px;">
    <img src="{WARNING_ICON_URL}" width="24" style="margin-right: 10px;">
    <span style="color: #721c24;">
        申し訳ございませんが、本商品は在庫切れとなっております。入荷までもうしばらくお待ちください。
    </span>
</div>
"""
# ==========================================
# 在庫ステータス関連定数
# ==========================================
STOCK_STATUS_FEW = "残りわずか"
STOCK_STATUS_NONE = "なし"

