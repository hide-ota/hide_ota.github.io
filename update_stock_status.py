import pandas as pd
import random

# 読み込み
df = pd.read_csv("data/products.csv")

# stock_status をランダムに設定（あり：50%、残りわずか：30%、なし：20%）
statuses = ["あり"] * 50 + ["残りわずか"] * 30 + ["なし"] * 20
df["stock_status"] = random.choices(statuses, k=len(df))

# 上書き保存
df.to_csv("data/products.csv", index=False)