import streamlit as st
import csv

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
file = open("data.csv")

csvreader = csv.reader(file, delimiter=';')
header = next(csvreader)
csvcount = 0
with col3:
    for row in csvreader:
        if csvcount < 10:
            st.title(row[0])
            content = row[1]
            st.write(content)
            st.image(row[3])
            st.link_button("Source code", row[2])
            csvcount = csvcount + 1
        else:
            break

csvcount = 0
with col4:
    for row in csvreader:

       # if csvcount >= 10:
       st.title(row[0])
       content = row[1]
       st.write(content)
       st.image(row[3])
       st.link_button("Source code", row[2])
               # csvcount = csvcount + 1
        # print (csvcount)