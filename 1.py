import streamlit as st

st.title("mikutyのアプリ 🚀")
name = st.text_input("名前を教えて！")
if name:
    st.write(f"{name}さん、Webアプリ開発へようこそ！")
    st.balloons()  # ←これ、消さないで入れてみて！
