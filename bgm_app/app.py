from pathlib import Path

import streamlit as st

st.title("Play BGM!")

for bgm_path in Path("bgm").glob("*.mp3"):
    st.write(bgm_path.name)
    bgm_file = bgm_path.open("rb")
    bgm_bytes = bgm_file.read()
    st.audio(bgm_bytes, format="audio/mp3")
