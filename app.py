
#my streamlit app
import streamlit as st

st.set_page_config(page_title="Mahathi Jammi", page_icon="✨")

st.title("Mahathi Jammi")
st.write("Welcome to your Streamlit app!")

st.header("About this app")
st.write(
    "This simple app uses Streamlit to show your name as the title and provide a basic interactive demo. "
    "Use the controls below to see Streamlit in action."
)

name = st.text_input("Enter your name", "Mahathi Jammi")
message = st.text_area("Write a message", "Hello from Streamlit!")

if st.button("Greet me"):
    st.success(f"Hi {name}! You said: {message}")

st.write("---")
st.subheader("Live summary")
st.write(f"**Name:** {name}")
st.write(f"**Message:** {message}")