# ベースイメージの指定
FROM python:3
USER root

# 作業ディレクトリの設定
WORKDIR /app

# images作成コマンド（ターミナル上で実行）
# docker build python_practice .

# --nameの後に任意のコンテナ名を指定できる(ターミナル上で実行)
# docker run -d -it --name back_python -v /Users/daiyunozaki/Desktop/Python_Practice:/app -p 8000:8000 python_practice /bin/bash

# コンテナの再起動
# docker start コンテナ名 or コンテナID

# コンテナ内に自分が入る（コンテナのpythonのバージョンは異なる、コマンド操作する前にdockerアプリを立ち上げてContainersにあるActionsのStartを押すこと）
# docker exec -it python /bin/bash

#ローカルに戻るコマンド
#exit

# コンテナの操作終了コマンド
# docker stop コンテナ名 or コンテナID

#コンテナ新規作成(任意のコンテナ名、バインドするディレクトリ、ポート番号の変更)
# docker run -d -it --name ###_python -v /Users/daiyunozaki/Desktop/Python_###:/app -p 80##:80## python_practice /bin/bash

