# コード7-5 特定の変数や関数だけを利用する
from math import floor # mathモジュールからfloor関数を取り込む
from math import pi # mathモジュールから変数piを取り込む

print(f"円周率は{pi}")
print(f"小数点以下を切り捨てれば{floor(pi)}です")

# モジュールから特定の変数や関数だけを取り込むことで、5.6行目のようにモジュール名を付けずに使用できる




# コード7-6 関数名が重複すると...
from math import log # mathモジュールからlog関数を取り込む

def log(msg): # 自作のログ関数を定義してしまっている
    print(f"{msg}を記録します")

log(10) # 対数を求めるつもりが、ログが出力されてしまった

# 後から実行した関数定義が優先されるため、mathのlog関数が呼び出せなくなってしまう




# コード7-7 特定の変数や関数だけを別名を付けて利用する
from math import pi as ensyuritsu
from math import floor as kirisute

print(f"円周率は{ensyuritsu}")
print(f"小数点以下を切り捨てれば{kirisute(ensyuritsu)}です")
