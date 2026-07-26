import streamlit as st
from graphics.Visualization import (
    FLRW_metric_graphic,
    schwarzild_metric_graphic,
    kerr_metric_graphic,
    godel_metric_graphic
)

from data.texts.PT.GENERAL import GENERAL
from data.texts.PT.MESSAGES_SIMPLE import MESSAGES_SIMPLE
from data.texts.PT.METRIC_TEXT import METRIC_TEXT

from ui.style import load_style
from ui.components import (
    card, 
    metric_card,
    show_video
)

import random




load_style()

# ==========================================================
# CONFIG
# ==========================================================

st.set_page_config(
    page_title="Einstein Field Equations",
    layout="wide"
)

# ==========================================================
# SESSION STATE
# ==========================================================

if "page" not in st.session_state:
    st.session_state.page = "lobby"

if "language" not in st.session_state:
    st.session_state.language = "PT"

if "username" not in st.session_state:
    st.session_state.username = ""

if "metric" not in st.session_state:
    st.session_state.metric = "Schwarzschild"


# ==========================================================
# DICTIONARY
# ==========================================================

METRICS = {

    "Schwarzschild": {
        "graph": schwarzild_metric_graphic,
        "parameters": {
            "mass": {
                "type": "slider",
                "label": "Massa",
                "min": 1.0,
                "max": 100.0,
                "default": 10.0
            }
        }
    },


    "Kerr": {
        "graph": kerr_metric_graphic,
        "parameters": {
            "mass": {
                "type": "slider",
                "label": "Massa",
                "min": 1.0,
                "max": 100.0,
                "default": 10.0
            },

            "spin": {
                "type": "slider",
                "label": "Momento Angular",
                "min": 0.0,
                "max": 1.0,
                "default": 0.3
            }
        }
    },


    "FLRW": {
    "graph": FLRW_metric_graphic,

    "parameters": {

        "curvature": {
            "type": "selectbox",
            "label": "Curvatura espacial",
            "options": [
                1,
                0,
                -1
            ]
        },

        "fate": {
            "type": "selectbox",
            "label": "Destino do Universo",
            "options": [
                "no",
                "freeze",
                "big_rip",
                "big_crunch"
            ]
        }

    }
},
    "Godel": {
        "graph": godel_metric_graphic,
        "parameters": {
            "rotation": {
                "type": "slider",
                "label": "Rotação",
                "min": 0.1,
                "max": 1.0,
                "default": 0.5
            },

        }
    },

}

TEXTS = {

    "PT": {

        "title": "Equações de Campo de Einstein",

        "intro":
        "Explore algumas soluções clássicas da Relatividade Geral "
        "de maneira interativa.",

        "language": "Idioma",

        "name": "Seu nome",

        "welcome":
        "Bem-vindo {}, prepare-se para visualizar como massa e energia "
        "curvam o espaço-tempo.",

        "next": "Avançar",

        "back": "Voltar",

        "confirm": "Confirmar e Avançar",

        "simulation_title": "Simulação",

        "metric": "Escolha uma métrica",

        "mass": "Massa",

        "spin": "Momento Angular",

        "preset": "Condição",

        "placeholder": "Gráfico Interativo Aqui",

        "physics_title": "Visão Física",

        "math_title": "Detalhes Matemáticos",

        "to_math": "Avançar para Detalhes Matemáticos",

        "back_selection": "Voltar para Seleção",

        "back_simulation": "Voltar para Simulação",

        "preset_options": [
            "Buraco Negro Estelar",
            "Buraco Negro Supermassivo",
            "Valor Personalizado"
        ],

        "metrics": list(METRICS.keys())
        
    },

    "EN": {

        "title": "Einstein Field Equations",

        "intro":
        "Explore classical General Relativity solutions "
        "through an interactive interface.",

        "language": "Language",

        "name": "Your name",

        "welcome":
        "Welcome {}, explore how mass and energy curve spacetime.",

        "next": "Next",

        "back": "Back",

        "confirm": "Confirm and Continue",

        "simulation_title": "Simulation",

        "metric": "Choose a metric",

        "mass": "Mass",

        "spin": "Angular Momentum",

        "preset": "Preset",

        "placeholder": "Interactive Plot Here",

        "physics_title": "Physical Interpretation",

        "math_title": "Mathematical Details",

        "to_math": "Go to Mathematical Details",

        "back_selection": "Back to Selection",

        "back_simulation": "Back to Simulation",

        "preset_options": [
            "Stellar Black Hole",
            "Supermassive Black Hole",
            "Custom"
        ],

        "metrics": list(METRICS.keys())
        
    }
}




# ==========================================================
# AUXILIAR
# ==========================================================

def t(key):
    return TEXTS[st.session_state.language][key]


# ==========================================================
# LOBBY
# ==========================================================
def render_lobby():

    st.markdown(
"""
# Equações de Campo de Einstein

<div class="subtitle">

Explore soluções da Relatividade Geral:
Schwarzschild, Kerr, FLRW e Gödel.

</div>

""",
unsafe_allow_html=True
)


    card(
    "O Universo como geometria",
    "A massa e energia dizem ao espaço-tempo como se curvar.",
)
    show_video(
    "assets/blackhole.mp4"
)

    st.write(t("intro"))

    language = st.radio(
        t("language"),
        ["PT", "EN"],
        horizontal=True,
        index=0 if st.session_state.language == "PT" else 1
    )

    st.session_state.language = language

    st.session_state.username = st.text_input(
        t("name"),
        value=st.session_state.username
    )

    name = st.session_state.username or "..."

    st.success(
        t("welcome").format(name)
    )

    st.divider()

    if st.button(t("next"), use_container_width=True):
        st.session_state.page = "pss"
        st.rerun()


# ==========================================================
# PAGE SELECT SIMULATION
# ==========================================================

def render_pss():

    st.title(t("metric"))

    if metric_card(
    "Schwarzschild",
    "Buraco negro estático gerado apenas pela massa."
    ):
        st.session_state.metric = "Schwarzschild"
        st.session_state.page = "simulation"

    if metric_card(
        "Kerr",
        "Buraco negro rotacional com arrasto do espaço-tempo."):
        st.session_state.metric = "Kerr"
        st.session_state.page = "simulation"


    if metric_card(
        "FLRW",
        "Modelo cosmológico da expansão do universo."
    ):
        st.session_state.metric = "FLRW"
        st.session_state.page = "simulation"


    if metric_card(
        "Gödel",
        "Universo em rotação com curvas temporais fechadas."
    ):
        st.session_state.metric = "Gödel"
        st.session_state.page = "simulation"


    
    st.divider()

    if st.button(t("back"), use_container_width=True):
        st.session_state.page = "lobby"
        st.rerun()


# ==========================================================
# PARAMETERS
# ==========================================================

def render_metric_parameters(metric_name):

    parameters = METRICS[metric_name]["parameters"]

    values = {}

    cols = st.columns(len(parameters))

    for col, (name, config) in zip(cols, parameters.items()):

        with col:

            if config["type"] == "slider":

                values[name] = st.slider(
                    config["label"],
                    config["min"],
                    config["max"],
                    config["default"],
                    key=f"{metric_name}_{name}"
                )

            elif config["type"] == "selectbox":

                values[name] = st.selectbox(
                    config["label"],
                    config["options"],
                    key=f"{metric_name}_{name}"
                )

    return values

# ==========================================================
# SIMULATION
# ==========================================================

@st.fragment(run_every="3s")
def render_simulation():
    def random_message():

        language = st.session_state.language

        category = random.choice(
            list(MESSAGES_SIMPLE[language][metric_name].keys())
        )

        message = random.choice(
            MESSAGES_SIMPLE[language][metric_name][category]
        )

        st.caption(category)

        if category == "Equações":

            st.info(message["name"])
            st.latex(message["latex"])

        else:

            st.info(message)

    st.title(t("simulation_title"))

    metric_name = st.session_state.metric
    metric = METRICS[metric_name]

    st.subheader(metric_name)

    params = render_metric_parameters(metric_name)

    st.divider()

    st.write("Chamando função...")

    # Calcula a figura primeiro
    fig = metric["graph"](**params)

    st.write("Função terminou.")

    col1, col2 = st.columns([5, 1])

    with col1:
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        random_message()


    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            t("back_selection"),
            use_container_width=True
        ):
            st.session_state.page = "pss"
            st.rerun()

    with c2:

        if st.button(
            t("to_math"),
            use_container_width=True
        ):
            st.session_state.page = "explication"
            st.rerun()


# ==========================================================
# EXPLICATION
# ==========================================================

def render_explication():

    st.title(t("math_title"))

    metric = METRIC_TEXT[st.session_state.language][st.session_state.metric]

    general = GENERAL[st.session_state.language]

    st.subheader("Métrica")

    st.subheader("O que é?")

    st.write(metric["metric"]["what"])

    st.subheader("Como funciona?")

    st.write(metric["metric"]["how"])

    st.subheader("Tensor Métrico")

    st.latex(metric["metric"]["latex"])


    # CHRISTOFFEL

    st.subheader("Símbolos de Christoffel")

    st.subheader("O que é?")

    st.write(general["christoffel"]["definition"])

    st.subheader("Como funciona?")

    st.latex(
        general["christoffel"]["formula"]["expression"]
    )

    st.write(
        general["christoffel"]["formula"]["guide"]["indice"]
    )

    st.write(
        general["christoffel"]["formula"]["guide"]["metric"]
    )

    st.write(
        general["christoffel"]["formula"]["guide"]["diff"]
    )


    # RICCI

    st.subheader("Tensor de Ricci")

    st.subheader("O que é?")

    st.write(
        general["ricci"]["definition"]
    )

    st.subheader("Como funciona?")

    st.latex(
        general["ricci"]["formula"]["expression"]
    )

    st.write(
        general["ricci"]["formula"]["guide"]["indice"]
    )

    st.write(
        general["ricci"]["formula"]["guide"]["christoffel"]
    )

    st.write(
        general["ricci"]["formula"]["guide"]["derivative"]
    )

    st.write(
        general["ricci"]["formula"]["guide"]["meaning"]
    )


    # RICCI SCALAR

    st.subheader("Escalar de Ricci")

    st.subheader("O que é?")

    st.write(
        general["ricci_scalar"]["definition"]
    )

    st.subheader("Como funciona?")

    st.latex(
        general["ricci_scalar"]["formula"]["expression"]
    )

    st.write(
        general["ricci_scalar"]["formula"]["guide"]["metric_inverse"]
    )

    st.write(
        general["ricci_scalar"]["formula"]["guide"]["ricci"]
    )

    st.write(
        general["ricci_scalar"]["formula"]["guide"]["meaning"]
    )


    # EINSTEIN

    st.subheader("Tensor de Einstein")

    st.subheader("O que é?")

    st.write(
        general["einstein_tensor"]["definition"]
    )

    st.subheader("Como funciona?")

    st.latex(
        general["einstein_tensor"]["formula"]["expression"]
    )

    st.write(
        general["einstein_tensor"]["formula"]["guide"]["ricci"]
    )

    st.write(
        general["einstein_tensor"]["formula"]["guide"]["scalar"]
    )

    st.write(
        general["einstein_tensor"]["formula"]["guide"]["metric"]
    )

    st.write(
        general["einstein_tensor"]["formula"]["guide"]["meaning"]
    )   

    if st.button(
            t("back_simulation"),
            use_container_width=True):

        st.session_state.page = "simulation"
        st.rerun()


# ==========================================================
# ROUTER
# ==========================================================

if st.session_state.page == "lobby":
    render_lobby()

elif st.session_state.page == "pss":
    render_pss()

elif st.session_state.page == "simulation":
    render_simulation()

elif st.session_state.page == "explication":
    render_explication()

