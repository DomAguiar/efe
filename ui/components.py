import streamlit as st
import base64

def card(title, text):

    st.markdown(
        f"""

        <div class="card">

        <h2>{title}</h2>

        <p class="subtitle">

        {text}

        </p>

        </div>

        """,

        unsafe_allow_html=True
    )



def metric_card(name, description):

    st.markdown(
        f"""

        <div class="card metric-card">

        <h2>{name}</h2>

        <p>
        {description}
        </p>

        </div>

        """,

        unsafe_allow_html=True
    )

    return st.button(
        "Selecionar",
        key=f"card_{name}"
    )



def show_video(path):

    with open(path, "rb") as f:
        video_bytes = f.read()

    video_base64 = base64.b64encode(video_bytes).decode()

    st.markdown(
        f"""
        <video autoplay loop muted width="100%">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True
    )