import streamlit as st
import tempfile

st.title("Movie Player")

# File uploader
uploaded_file = st.file_uploader("Choose a movie file", type=["mp4", "mov", "avi", "mkv"])

if uploaded_file is not None:
    # Create a temporary file to save the uploaded file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_file_path = tmp_file.name

    # Display the video
    st.video(temp_file_path)
