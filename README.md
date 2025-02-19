---
title: blog_creation
emoji: ✒️
colorFrom: green
colorTo: blue
sdk: streamlit
sdk_version: "1.42.1"
app_file: src/app.py
pinned: false
---

# LLM等を使用した自動ブログ記事生成

## 目的
LLMやBERTなどの自然言語処理技術を使ったプロジェクトの練習をする。対象は普段書いているラノベ感想記事の自動化（は無理だけどあらすじから自分の文章っぽい感想文を生成）。

機械学習を使用したプロジェクト作成〜クラウドへのデプロイまでを行う。

## ステップ
1. 既存のモデルを使用して、小説のあらすじを要約。
2. 簡単な感想も出力に含める。
3. 過去に書いたブログ記事を使ってファインチューニング。
    1. 自分の文章をNotionやWebページから取得
    2. 小説のあらすじをスクレイピングで取得
4. 推論時にあらすじより長い文章を入力できるようにする。
    1. 青空文庫など
5. gradioなどで公開する。
6. Google Cloudなどにデプロイ。

## 環境
- M1 MacBook Air(2020)
- Python 3.11.9
- llama-cpp-python
    - ELYZAの量子化モデルを使用する際には必要
    - コマンドラインツールだけでなく、XCodeのアプリ自体もインストール
    - brewでcmakeをインストール

## ディレクトリ構成

```
.
├── Dockerfile
├── README.md
├── practice
└── src
    ├── collect # データセットを作成する
    ├── data
    └── app.py
```