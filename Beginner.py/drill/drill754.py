# コード7-13 requestsでPythonの公式サイトを取得する
# import requests

# requests = requests.get("http://www.python.org/downloads/")
# text = response.text
# print(text)

# 今回はrequestsをインストールしていないため、コメントアウトとする




# コード7-14 標準ライブラリを利用したWebページの取得
import http.client

conn = http.client.HTTPConnection("www.python.org")
conn.request("GET", "/downloads/")

response = conn.getresponse()
text = response.read().decode("UTF-8")

print(text)
conn.close()