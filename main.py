# import streamlit as st

# # 1ターム目
# # st.title("名前記憶アプリ")
# # 2ターム目
# st.title("ユーザー情報入力")

# # 1ターム目
# # if "name" not in st.session_state:
# #     st.session_state.name = ""
# # 2ターム目
# if "user_name" not in st.session_state:
#     st.session_state.user_name = ""

# name = st.text_input("あなたの名前を入力してください")
# if st.button("名前を保存"):
#     # st.session_state.name = name
#     st.session_state.user_name = name
#     st.success("名前を保存しました！")

# # st.write(f"記憶している名前：{st.session_state.name}")
# st.write(f"現在保存されている名前：{st.session_state.user_name}")

# 3ターム目
import streamlit as st

st.title("📝 ユーザー情報入力")

# session_stateの初期化
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'grade' not in st.session_state:
    st.session_state.grade = ""
if 'hobbies' not in st.session_state:
    st.session_state.hobbies = []

# 入力フィールド
name = st.text_input("名前")
grade = st.selectbox("学年", 
    ["", "小学5年", "小学6年", "中学1年", "中学2年", "中学3年"])
hobbies = st.multiselect("趣味", 
    ["読書", "スポーツ", "ゲーム", "音楽", "絵画", "その他"])

if st.button("💾 情報を保存"):
    st.session_state.user_name = name
    st.session_state.grade = grade
    st.session_state.hobbies = hobbies
    st.success("✅ 情報を保存しました!")