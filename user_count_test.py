import streamlit as st
import uuid

user_id = st.query_params.get("user_id", None)

if user_id is None:

    user_id = str(uuid.uuid4())
    st.query_params["user_id"] = user_id

if 'unique_users' not in st.session_state:
    st.session_state.unique_users = set()

if user_id not in st.session_state.unique_users:
    st.session_state.unique_users.add(user_id)

st.write(f"고유 방문자 수: {len(st.session_state.unique_users)}")

st.write(f"현재 사용자 ID: {user_id}")
