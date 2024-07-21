# コード7-3 mathモジュールを利用する
import math # mathモジュールの取り込みを宣言

print(f"円周率は{math.pi}です") # mathモジュールの変数piを宣言
print(f"小数点以下を切り捨てれば{math.floor(math.pi)}です") # mathモジュールのfloor関数を呼び出す
print(f"小数点以下を切り上げれば{math.ceil(math.pi)}です") # mathモジュールのceil関数を呼び出す

# モジュールとは別のプログラムに取り込んで使うことを前提として、変数や関数、クラスなどある機能をひとまとまりにしたファイルを指す言葉

# モジュールが属する2種類のライブラリ
# 標準ライブラリ：Pythonが公式に用意したモジュールのまとまり
# 外部ライブラリ：別の組織や個人が用意したモジュールのまとまり




# コード7-4 mathモジュールに別名を付けて利用する
import math as m # mathモジュールをmとして取り込む

print(f"円周率は{m.pi}です") # m(mathモジュール)の変数piを参照
print(f"小数点以下を切り捨てれば{m.floor(m.pi)}です") # m(mathモジュール)のfloor関数を呼び出す
print(f"小数点以下を切り上げれば{m.ceil(m.pi)}です") # m(mathモジュール)のceil関数を呼び出す