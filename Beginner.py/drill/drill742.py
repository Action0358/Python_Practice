# コード7-9 httpパッケージのclientモジュールを取り組む
import http.client

conn = http.client.HTTPConnection("www.python.org")


# コード7-10 httpパッケージのclientモジュールを取り組む(from利用)
from http import client

conn = client.HTTPConnection("www.python.org")


# コード7-11 httpパッケージのclientモジュールから関数だけを取り組む
from http.client import HTTPConnection

conn = HTTPConnection("www.python.org")
