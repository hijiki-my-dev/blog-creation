import streamlit as st

# ページ設定
st.set_page_config(
    page_title="小説感想生成アプリ（デモ）",
    page_icon="📚",
    layout="centered",
)

# アプリのタイトル
st.title("小説感想生成アプリ（デモ版）")
st.subheader("あなたの入力をそのまま返します")

# 入力フォーム
with st.form("input_form"):
    novel_title = st.text_input("小説のタイトル", placeholder="例：人間失格")
    summary = st.text_area("あらすじや感想メモ", height=200, placeholder="例：主人公の葉蔵は自分を「人間失格」だと考えている...")
    submit_button = st.form_submit_button("生成")

# 送信ボタンが押されたら結果を表示
if submit_button:
    st.markdown("## 入力内容")
    st.write(f"**タイトル:** {novel_title}")
    st.write("**あらすじや感想メモ:**")
    st.write(summary)

    st.markdown("---")

    st.markdown("## 生成された感想記事（デモ）")
    st.info(f"""
    【{novel_title}】についての感想

    {summary}

    ※このデモ版では入力内容をそのまま返しています。
    実際のアプリではここにLLMによって生成された内容が表示されます。
    """)

# フッター
st.markdown("---")
st.caption("Powered by Streamlit & Hugging Face")