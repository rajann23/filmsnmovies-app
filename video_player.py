import streamlit as st
import moviepy.editor as mp
import tempfile
import os

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

    # Optional: Display some basic info about the file
    video_clip = mp.VideoFileClip(temp_file_path)
    st.write(f"Duration: {video_clip.duration} seconds")
    st.write(f"Resolution: {video_clip.size}")

    # Delete the temporary file after displaying
    os.remove(temp_file_path)
