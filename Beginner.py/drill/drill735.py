# コード7-8 ワイルドカードインポート（使用は推奨されていない）
from math import * # mathモジュールの全ての変数と関数を取り込む

print(f"円周率は{pi}です")
print(f"小数点以下を切り捨てれば{floor(pi)}です")
print(f"小数点以下を切り上げれば{ceil(pi)}です")

# コード7-5と同様に指定したモジュール内の全ての変数と関数をモジュール名を付けずにその名前だけで使用できる
# 取り込んだ変数や関数の把握が難しくなり、意図しない名前の衝突が起きやすくなる（例：コード7-6）
