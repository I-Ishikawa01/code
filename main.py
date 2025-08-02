import streamlit as st

# 1ターム目
# st.title("名前記憶アプリ")
# 2ターム目
st.title("ユーザー情報入力")

# 1ターム目
# if "name" not in st.session_state:
#     st.session_state.name = ""
# 2ターム目
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

name = st.text_input("あなたの名前を入力してください")
if st.button("名前を保存"):
    # st.session_state.name = name
    st.session_state.user_name = name
    st.success("名前を保存しました！")

# st.write(f"記憶している名前：{st.session_state.name}")
st.write(f"現在保存されている名前：{st.session_state.user_name}")