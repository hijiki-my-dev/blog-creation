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

# LLM等を使用した要約生成 in Hugging Face Spaces

## 実行環境
[Hugging Face Spaces](https://huggingface.co/spaces/Hijiki-HF/blog_creation)

## ディレクトリ構成

```
.
├── Dockerfile
├── README.md
└── src
    └── app.py
```

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
