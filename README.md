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

## 実行方法

- ローカル


## メモ
### モデルについて
- （2025/5/10）LLMをCPUで使用するのはかなり厳しい。gguf形式のものを適切に使用すれば可能かもしれないが、まずはt5などを使用する？
- LLMについて比較を行った結果
    - SakanaAI/TinySwallow-1.5B-Instruct（1.5Bということを考慮に入れるとgemma3以上？）
    -   gguf形式ならCPUでも推論可能なはず。だけどcolabで6分かかる、、、
    - google/gemma-3-4b-it（圧倒的。1bは英語のみ対応）
    - Rakuten/RakutenAI-2.0-mini-instruct（かなり良い）
    - rinna/gemma-2-baku-2b-it（そこそこ。実行方法が悪い？）
    - google/gemma-2-2b-jpn-it（同）
    - meta-llama/Llama-3.2-3B-Instruct（日本語対応してない）
    - microsoft/Phi-4-mini-instruct
    - lightblue/DeepSeek-R1-Distill-Qwen-1.5B-Multilingual
