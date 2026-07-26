import streamlit as st


def load_style():

    st.markdown("""

<style>

/* ============================= */
/* FUNDO DO UNIVERSO */
/* ============================= */

.stApp {

    background:
    radial-gradient(
        circle at 50% 20%,
        #3b1a00 0%,
        #120800 25%,
        #050510 55%,
        #020208 100%
    );

    color: #f5f5f5;

}


/* ============================= */
/* TÍTULOS */
/* ============================= */

h1 {

    color: #ff9900 !important;

    text-shadow:
    0 0 10px #ff9900,
    0 0 30px #ff6600,
    0 0 60px #ff3300;

}


h2, h3 {

    color: #ffb347 !important;

    text-shadow:
    0 0 15px #ff8c00;

}


/* ============================= */
/* TEXTO */
/* ============================= */

p, label, span {

    color: #eeeeee;

}


/* ============================= */
/* BOTÕES */
/* ============================= */


.stButton > button {

    background: #d97706;

    color: white;

    border: 1px solid #f59e0b;

    border-radius: 10px;

    box-shadow: 0 0 8px rgba(245,158,11,.25);

    transition: .2s;
}

    color:white;

    border:none;

    border-radius:15px;


    box-shadow:

    0 0 15px #ff6600,
    0 0 35px #ff3300;


    font-weight:bold;

    transition:0.3s;

}



.stButton > button:hover {


    transform:scale(1.05);


    box-shadow:

    0 0 25px #ffaa00,
    0 0 70px #ff6600;

}



/* ============================= */
/* CAIXAS */
/* ============================= */


.stAlert {

    background:

    rgba(255,120,0,0.12);


    border-left:

    5px solid #ff9900;


    box-shadow:

    0 0 20px rgba(255,120,0,0.4);

}



/* ============================= */
/* SELECTBOX */
/* ============================= */


div[data-baseweb="select"] > div {

    background:

    rgba(20,10,5,0.8);


    border:

    1px solid #ff8800;


    box-shadow:

    0 0 15px rgba(255,120,0,0.5);

}



/* ============================= */
/* SLIDER */
/* ============================= */


.stSlider > div > div > div > div {

    background:

    linear-gradient(
        90deg,
        #ffcc00,
        #ff5500
    );


    box-shadow:

    0 0 15px #ff6600;

}



/* ============================= */
/* DIVISORES */
/* ============================= */


hr {

    border:

    1px solid #ff6600;


    box-shadow:

    0 0 10px #ff6600;

}



/* ============================= */
/* REMOVE ESPAÇOS PADRÃO */
/* ============================= */


.block-container {

    padding-top:2rem;

}



</style>

""", unsafe_allow_html=True)