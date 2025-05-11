from optimum.onnxruntime import ORTModelForSeq2SeqLM
import streamlit as st
import torch
from transformers import AutoTokenizer, pipeline

torch.classes.__path__ = []

def summarize_article(input_text):
    MODEL_PATH = "model/mt5_onnx"

    # ONNXモデルの読み込み
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, local_files_only=True)
    model = ORTModelForSeq2SeqLM.from_pretrained(MODEL_PATH, local_files_only=True)

    summarizer = pipeline(
        "summarization",
        model=model,
        tokenizer=tokenizer
    )
    return summarizer(
        input_text,
        max_length=600,
        min_length=200,
        do_sample=True,
        temperature=0.5,
        num_beams=4,
        early_stopping=True
    )


# ページ設定
st.set_page_config(
    page_title="記事要約（デモ）",
    page_icon="📚",
    layout="centered",
)

# アプリのタイトル
st.title("記事要約（デモ）")
st.subheader("入力を元に要約を生成します")

# 入力フォーム
with st.form("input_form"):
    # novel_title = st.text_input("小説のタイトル", placeholder="例：人間失格")
    input_text = st.text_area("記事内容", height=200, placeholder="例：主人公の葉蔵は自分を「人間失格」だと考えている...")
    submit_button = st.form_submit_button("生成")

# 送信ボタンが押されたら結果を表示
if submit_button:
    # st.markdown("## 入力内容")
    # # st.write(f"**タイトル:** {novel_title}")
    # st.write("**あらすじや感想メモ:**")
    # st.write(summary)

    # st.markdown("---")

    summary = summarize_article(input_text)

    st.markdown("## 生成された感想記事（デモ）")
    st.info(f"""
    {summary["summary_text"][0]}
    """)

# フッター
st.markdown("---")
st.caption("Powered by Streamlit & Hugging Face")
