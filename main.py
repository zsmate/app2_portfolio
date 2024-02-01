import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("photo.png")

with col2:
    st.title("Mate Zsofia")
    content ="""
    Hello from my computer! I am a C++ developer, who is learning Python. 
    I found this language fun and interesting.
    I enjoy learning new things.
    """
    st.write(content)

col3, col4 = st.columns(2)

with col3:
    st.title("Todo app")
    content = """
    An app for managing todos for yourself.
    """
    st.write(content)
    st.image("1.png")
    st.link_button("Source code","https://github.com/zsmate/my-todo-app/blob/master/web.py")

with col4:
    st.title("Portfolio website")
    content = """
        A website for presenting several apps.
        """
    st.write(content)
    st.image("2.png")
    st.link_button("Source code", "https://github.com/zsmate/app2_portfolio")
