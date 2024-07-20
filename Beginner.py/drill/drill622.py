# コード6-5 勇者を表すクラスの定義と利用
class Hero:
    name = "松田"
    hp = 100
    
    def sleep(self, hours):
        print(f"{self.name}は{hours}時間だ！")
        
        self.hp += hours
        
        print(f"{self.name}の体力は{self.hp}だ！")
        

# ゲーム開発
print("スッキリファンタジーXII 〜金色の理想郷〜")

h = Hero()
h.sleep(3)


# self はクラスのインスタンス（変数）を指し、そのインスタンスの属性（デフォルトの名前や体力など）にアクセスするために使われる（name, hp）
# h.sleep(3) は、def sleep(self, hours): の hours 引数に値 3 を渡している
