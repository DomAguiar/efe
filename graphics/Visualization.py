import numpy as np
import plotly.graph_objects as go

def apply_theme(fig):

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="#0b0b0b",

        font=dict(
            family="Inter",
            size=15,
            color="#f2f2f2"
        ),

        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        ),

        hovermode="closest",

        hoverlabel=dict(
            bgcolor="#111111",
            bordercolor="#ff8800",
            font=dict(
                family="Inter",
                color="white",
                size=14
            )
),

        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            borderwidth=0
        ),

        transition=dict(
            duration=400,
            easing="cubic-in-out"
),

        title=dict(
            x=0.5,
            font=dict(
                color="#ff9a1f",
                size=22
            )
),


    )

    fig.update_xaxes(

        showgrid=True,
        gridcolor="rgba(255,140,0,.15)",

        zeroline=False,

        linecolor="#ff8c00",

        tickfont=dict(color="#dddddd")
    )

    fig.update_yaxes(

        showgrid=True,
        gridcolor="rgba(255,140,0,.15)",

        zeroline=False,

        linecolor="#ff8c00",

        tickfont=dict(color="#dddddd")
    )

    return fig
def FLRW_metric_graphic(curvature, fate):

    theta = np.linspace(0, np.pi, 50)
    phi = np.linspace(0, 2*np.pi, 50)
    r_flat = np.linspace(0, 10, 30)
    chi = np.linspace(0, 3, 30) 

    a_values = []
    for frame in range(100):
        if fate in ["no", "freeze"]:
            a = np.exp(0.02 * frame)
        elif fate == "big_rip":
            tempo_fim = 100 + 5
            a = 1 / (1 - (frame / tempo_fim)) if frame < tempo_fim else 100
        elif fate == "big_crunch":
            a = np.sin(np.pi * frame / 100)
            if a < 0: a = 0
        a_values.append(a)

    def gerar_geometria(curvature, a):
        if curvature == 1: # Esfera
            THETA, PHI = np.meshgrid(theta, phi)
            X = a * np.sin(THETA) * np.cos(PHI)
            Y = a * np.sin(THETA) * np.sin(PHI)
            Z = a * np.cos(THETA)
            return [go.Surface(x=X, y=Y, z=Z, colorscale='magma', showscale=False)]
            
        elif curvature == 0: # Plano
            R, PHI = np.meshgrid(r_flat, phi)
            X = a * R * np.cos(PHI)
            Y = a * R * np.sin(PHI)
            Z = np.zeros_like(X)
            return [go.Surface(x=X, y=Y, z=Z, colorscale='magma', showscale=False)]
            
        elif curvature == -1: # Hiperboloide (Duas folhas)
            CHI, PHI = np.meshgrid(chi, phi)
            X = a * np.sinh(CHI) * np.cos(PHI)
            Y = a * np.sinh(CHI) * np.sin(PHI)
            Z_POS = a * np.cosh(CHI)
            Z_NEG = -a * np.cosh(CHI)
            
            return [
                go.Surface(x=X, y=Y, z=Z_POS, colorscale='magma', showscale=False),
                go.Surface(x=X, y=Y, z=Z_NEG, colorscale='magma', showscale=False, opacity=0.8)
            ]

    surfaces_iniciais = gerar_geometria(curvature, a_values[0])
    fig = go.Figure(data=surfaces_iniciais)

    frames_plotly = []
    for idx, a in enumerate(a_values):
        surfaces_frame = gerar_geometria(curvature, a)
        frames_plotly.append(go.Frame(
            data=surfaces_frame,
            name=str(idx)
        ))
    fig.frames = frames_plotly

    sliders_config = [{
        "active": 0,
        "yanchor": "top",
        "xanchor": "left",
        "currentvalue": {
            "font": {"size": 14, "color": "white"},
            "prefix": "Tempo (Frame): ",
            "visible": True,
            "xanchor": "right"
        },
        "transition": {"duration": 0},
        "pad": {"b": 10, "t": 50},
        "len": 0.9,
        "x": 0.1,
        "y": 0,
        "steps": [{
            "args": [[str(i)], {"frame": {"duration": 50, "redraw": True}, "mode": "immediate"}],
            "label": str(i),
            "method": "animate"
        } for i in range(100)]
    }]

    max_a = max(a_values)
    if curvature == 1: limit = max_a * 1.2
    elif curvature == 0: limit = max_a * 10 * 1.2
    elif curvature == -1: limit = max_a * np.sinh(max(chi)) * 1.2

    fig.update_layout(
        title=f"FLRW Metric (curvature = {curvature}) | Fate: {fate.upper()}",
        title_font=dict(size=18, color="white"),
        paper_bgcolor="black",
        plot_bgcolor="black",
        scene=dict(
            xaxis=dict(range=[-limit, limit], backgroundcolor="black", color="white", gridcolor="gray", showbackground=False),
            yaxis=dict(range=[-limit, limit], backgroundcolor="black", color="white", gridcolor="gray", showbackground=False),
            zaxis=dict(range=[-limit, limit], backgroundcolor="black", color="white", gridcolor="gray", showbackground=False),
            aspectmode="cube"
        ),
        updatemenus=[{
            "type": "buttons",
            "buttons": [
                {
                    "label": "▶ Play",
                    "method": "animate",
                    "args": [None, {"frame": {"duration": 50, "redraw": True}, "fromcurrent": True}]
                },
                {
                    "label": "⏸ Pause",
                    "method": "animate",
                    "args": [[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate"}]
                }
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top"
        }],
        sliders=sliders_config
    )

    return apply_theme(fig)
def schwarzild_metric_graphic(mass):
    G, c = 1, 1
    M = mass
    r_s = 2 * G * M / c**2

    theta_vals = np.linspace(-np.pi, np.pi, 200, endpoint=True)
    r_vals = np.linspace(r_s + 0.1, 500, 200)

    R, THETA = np.meshgrid(r_vals, theta_vals)

    X = R * np.sin(THETA)
    Y = R * np.cos(THETA)

    if np.any(R <= r_s):
        Z = np.zeros_like(R)
        Z[R > r_s] = 2 * np.sqrt(r_s * (R[R > r_s] - r_s))
    else:
        Z = 2 * np.sqrt(r_s * (R - r_s))

    Z_visual = Z

    surface = go.Surface(
        x=X,
        y=Y,
        z=Z_visual,
        colorscale="magma",
        showscale=False,
        lighting=dict(ambient=0.6, diffuse=0.8, roughness=0.5),
        name="Espaço-Tempo Curvo",
    )

    singularidade = go.Scatter3d(
        x=[0],
        y=[0],
        z=[np.max(Z_visual) + 1.5],  # Soma 1.5 para flutuar um pouco acima da malha
        mode="markers",
        marker=dict(size=12, color="white", symbol="circle"),
        name="Massa Central")


    MAX_R = 500
    MAX_Z = np.max(Z_visual)
    MIN_Z = np.min(Z_visual)

    fig = go.Figure(data=[surface, singularidade])

    fig.update_layout(
        title=f"Black Hole with mass of {M} solar masses (Flamm's Paraboloid)",
        title_font=dict(size=18, color="white"),
        paper_bgcolor="black",
        plot_bgcolor="black",
        showlegend=False,
        scene=dict(
            xaxis=dict(range=[-MAX_R, MAX_R], backgroundcolor="black", color="white", gridcolor="gray", showbackground=False),
            yaxis=dict(range=[-MAX_R, MAX_R], backgroundcolor="black", color="white", gridcolor="gray", showbackground=False),
            zaxis=dict(range=[MIN_Z - 1, MAX_Z * 1.1], backgroundcolor="black", color="white", gridcolor="gray", showbackground=False),

            aspectmode="cube",
            aspectratio=dict(x=1, y=1, z=0.6),
            camera=dict(
                eye=dict(x=1.3, y=-1.3, z=0.9), # Câmera padrão olhando levemente de cima
            )
        ),
        margin=dict(l=0, r=0, b=0, t=50)
    )

    return apply_theme(fig)
def kerr_metric_graphic(mass, spin):

    G, c = 1, 1
    M = mass
    r_plus = G * M / c**2 + np.sqrt((G * M / c**2) ** 2 - spin**2)

    theta_vals = np.linspace(-np.pi, np.pi, 200)
    r_vals = np.linspace(r_plus + 0.1, 500, 200)
    R, THETA = np.meshgrid(r_vals, theta_vals)

    X = R * np.sin(THETA)
    Y = R * np.cos(THETA)
    Z = 2 * np.sqrt((2 * G * M / c**2) * (R - (2 * G * M / c**2)) + spin**2 * np.cos(THETA) ** 2)
    Z_visual = Z

    surface = go.Surface(
        x=X,
        y=Y,
        z=Z_visual,
        colorscale="magma",
        showscale=False,
        lighting=dict(ambient=0.6, diffuse=0.8, roughness=0.5),
        name="Espaço-Tempo Curvo (Kerr)",
    )

    theta_ergo = np.linspace(0, np.pi, 50)
    phi_ergo = np.linspace(0, 2 * np.pi, 50)
    TE, PE = np.meshgrid(theta_ergo, phi_ergo)
    r_ergo = G * M / c**2 + np.sqrt(
        (G * M / c**2) ** 2 - spin**2 * np.cos(TE) ** 2
    )
    X_ergo = r_ergo * np.sin(TE) * np.cos(PE)
    Y_ergo = r_ergo * np.sin(TE) * np.sin(PE)
    Z_ergo = r_ergo * np.cos(TE) * 0.3 - Z.max()

    ergosfera = go.Surface(
        x=X_ergo,
        y=Y_ergo,
        z=Z_ergo,
        colorscale="blues",
        opacity=0.2,
        showscale=False,
        name="Black Hole",
    )

    theta_esfera = np.linspace(0, np.pi, 25)
    phi_esfera = np.linspace(0, 2 * np.pi, 25)
    TE, PE = np.meshgrid(theta_esfera, phi_esfera)
    
    X_bh = r_plus * np.sin(TE) * np.cos(PE)
    Y_bh = r_plus * np.sin(TE) * np.sin(PE)
    Z_bh = r_plus * np.cos(TE) * 0.3 + Z_visual.min() + 0.5

    black_hole_neon = go.Surface(
        x=X_bh,
        y=Y_bh,
        z=Z_bh,
        surfacecolor=np.zeros_like(X_bh),
        colorscale=[[0, "black"], [1, "black"]],
        showscale=False,
        opacity=0.95,
        contours=dict(
            x=dict(show=True, color="rgba(240, 240, 255, 0.9)", width=2),
            y=dict(show=True, color="rgba(240, 240, 255, 0.9)", width=2),
            z=dict(show=True, color="rgba(240, 240, 255, 0.9)", width=2)
        ),
        name="Horizonte de Eventos",
    )

    t_anel = np.linspace(0, 2 * np.pi, 200)
    singularidade_anel = go.Scatter3d(
        x=spin * np.cos(t_anel),
        y=spin * np.sin(t_anel),
        z=[Z_visual.max() + 1.5] * 200,
        line=dict(
            color="rgb(255, 255, 255)", 
            width=14, 
        ),
        name="Singularidade em Anel",
    )


    fig = go.Figure(data=[surface, black_hole_neon, singularidade_anel, ergosfera])

    angulos = np.linspace(0, 2 * np.pi, 100, endpoint=False)
    r_cam = 1.8

    frames_plotly = []
    for idx, ang in enumerate(angulos):
        frames_plotly.append(
            go.Frame(
                layout=dict(
                    scene=dict(
                        camera=dict(
                            eye=dict(
                                x=r_cam * np.cos(ang),
                                y=r_cam * np.sin(ang),
                                z=0.9,
                            )
                        )
                    )
                ),
                name=str(idx),
            )
        )
    fig.frames = frames_plotly

    MAX_R = 500
    MIN_Z = Z_visual.min()
    MAX_Z = Z_visual.max()

    fig.update_layout(
        title=f"Kerr Black Hole Animated (M={M}, a={spin})",
        title_font=dict(size=18, color="white"),
        paper_bgcolor="black",
        plot_bgcolor="black",
        showlegend=False,
        scene=dict(
            xaxis=dict(
                range=[-MAX_R, MAX_R],
                color="white",
                showgrid=False,
                showbackground=False,
                visible=True,
            ),
            yaxis=dict(
                range=[-MAX_R, MAX_R],
                color="white",
                showgrid=False,
                showbackground=False,
                visible=True,
            ),
            zaxis=dict(
                range=[MIN_Z - 1, MAX_Z * 1.1],
                color="white",
                showgrid=False,
                showbackground=False,
                visible=True,
            ),
            aspectmode="manual",
            aspectratio=dict(x=1, y=1, z=0.6),
            camera=dict(
                eye=dict(x=r_cam, y=0, z=0.9), up=dict(x=0, y=0, z=1)
            ),
        ),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "▶ Girar",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 30, "redraw": True},
                                "fromcurrent": True,
                                "transition": {"duration": 0},
                                "mode": "linear",
                            },
                        ],
                    },
                    {
                        "label": "⏸ Pausar",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 10},
                "showactive": False,
                "x": 0.1,
                "xanchor": "right",
                "y": 0,
                "yanchor": "top",
            }
        ],
    )

    return apply_theme(fig)
def godel_metric_graphic(rotation):
    raio_critico = np.log(1 + np.sqrt(2)) / (np.sqrt(2) * rotation)
    raio_total = raio_critico * 1.5
    r_vals = np.linspace(0, raio_total, 50)
    theta_vals = np.linspace(0, 2 * np.pi, 100)
    R, THETA = np.meshgrid(r_vals, theta_vals)

    X = R * np.cos(THETA)
    Y = R * np.sin(THETA)

    data_plots = []
    for z_camada in np.linspace(-10 / 2, 10 / 2, 5):
        Z_layer = np.full_like(X, z_camada)
        v_arrasto = np.exp(np.sqrt(2) * rotation * X)
        universo_plano = go.Surface(
            x=X,
            y=Y,
            z=Z_layer,
            surfacecolor=v_arrasto,
            colorscale="twilight",
            showscale=False,
            opacity=0.4,
            name="Fluxo Matéria",
        )
        data_plots.append(universo_plano)

    z_cil = np.linspace(-10 / 2, 10 / 2, 50)
    t_cil = np.linspace(0, 2 * np.pi, 50)
    ZC, TC = np.meshgrid(z_cil, t_cil)
    X_critico = raio_critico * np.cos(TC)
    Y_critico = raio_critico * np.sin(TC)

    cilindro_critico = go.Surface(
        x=X_critico,
        y=Y_critico,
        z=ZC,
        colorscale="reds",
        opacity=0.25,
        showscale=False,
        name="Horizonte",
    )
    data_plots.append(cilindro_critico)

    for r_anel, cor in zip(
        [raio_critico * 0.5, raio_critico], ["cyan", "red"]
    ):
        t_linha = np.linspace(0, 2 * np.pi, 100)
        linha_tempo = go.Scatter3d(
            x=r_anel * np.cos(t_linha),
            y=r_anel * np.sin(t_linha),
            z=[0] * 100,
            mode="lines",
            line=dict(
                color=cor, width=4, dash="dash" if cor == "red" else "solid"
            ),
            name="Linha Tempo",
        )
        data_plots.append(linha_tempo)

    fig = go.Figure(data=data_plots)

    angulos = np.linspace(0, 2 * np.pi, 100, endpoint=False)
    r_cam = 2.0

    frames_plotly = []
    for idx, ang in enumerate(angulos):
        frames_plotly.append(
            go.Frame(
                layout=dict(
                    scene=dict(
                        camera=dict(
                            eye=dict(
                                x=r_cam * np.cos(ang),
                                y=r_cam * np.sin(ang),
                                z=1.0,
                            )
                        )
                    )
                ),
                name=str(idx),
            )
        )
    fig.frames = frames_plotly

    LIMIT = raio_total * 1.2
    fig.update_layout(
        title=f"Gödel Universe Animated (\u03c9 = {rotation})",
        title_font=dict(size=18, color="white"),
        paper_bgcolor="black",
        plot_bgcolor="black",
        showlegend=False,
        scene=dict(
            xaxis=dict(
                range=[-LIMIT, LIMIT],
                color="white",
                showgrid=False,
                showbackground=False,
                visible=True,
            ),
            yaxis=dict(
                range=[-LIMIT, LIMIT],
                color="white",
                showgrid=False,
                showbackground=False,
                visible=True,
            ),
            zaxis=dict(
                range=[-10, 10],
                color="white",
                showgrid=False,
                showbackground=False,
                visible=True,
            ),
            aspectmode="manual",
            aspectratio=dict(x=1, y=1, z=0.8),
            camera=dict(
                eye=dict(x=r_cam, y=0, z=1.0), up=dict(x=0, y=0, z=1)
            ),
        ),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "▶ Girar",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 30, "redraw": True},
                                "fromcurrent": True,
                                "transition": {"duration": 0},
                                "mode": "linear",
                            },
                        ],
                    },
                    {
                        "label": "⏸ Pausar",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 10},
                "showactive": False,
                "x": 0.1,
                "xanchor": "right",
                "y": 0,
                "yanchor": "top",
            }
        ],
    )

    return apply_theme(fig)
