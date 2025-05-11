from huggingface_hub import hf_hub_download
from llama_cpp import Llama
import streamlit as st

MAX_OUTPUT_TOKENS = 512

def summarize_article(input_text):
    repo_id = "SakanaAI/TinySwallow-1.5B-Instruct-GGUF"
    filename = "tinyswallow-1.5b-instruct-q5_k_m.gguf"
    model_path = hf_hub_download(repo_id=repo_id, filename=filename)

    # モデルの読み込み
    llm = Llama(model_path=model_path, n_ctx=4096, n_gpu_layers=-1, verbose=False)
    prompt = f"以下のテキストを日本語で約400字程度に要約してください。特に固有名詞や専門用語は正確に含めてください。テキスト: {input_text} 要約: "
    response = llm(prompt, max_tokens=MAX_OUTPUT_TOKENS)
    return response["choices"][0]["text"]

# ページ設定
st.set_page_config(
    page_title="記事要約（デモ）",
    page_icon="📚",
    layout="centered",
)

# アプリのタイトル
st.title("記事要約（デモ）")
st.subheader("入力を元に要約を生成します")
st.markdown(
    """
    このアプリは、指定されたテキストを要約するためのデモです。以下の入力フォームに記事内容を入力してください。
    CPUで動作するため時間がかかり、精度も低いです。
    """
)

# 入力フォーム
with st.form("input_form"):
    input_text = st.text_area("記事内容", height=200, placeholder="例：主人公の葉蔵は自分を「人間失格」だと考えている...")
    submit_button = st.form_submit_button("生成")

# 送信ボタンが押されたら結果を表示
if submit_button:
    summary = summarize_article(input_text)

    st.markdown("## 生成された要約（デモ）")
    st.info(summary)

# フッター
st.markdown("---")
st.caption("Powered by Streamlit & Hugging Face")
