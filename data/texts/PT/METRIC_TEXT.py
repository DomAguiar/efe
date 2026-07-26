METRIC_TEXT = {
    "PT": {
        "Schwarzschild": {
            "metric": {


                "what":
                    "A métrica de Schwarzschild instrui ao universo como se comportar perante a uma grande Massa.",

                "how":
                    "O universo obedece curvando-se a massa.",

                "latex": r"""
        g_{\mu\nu}=
        \begin{pmatrix}
        -\left(1-\frac{2GM}{rc^2}\right) & 0 & 0 & 0\\
        0 & \left(1-\frac{2GM}{rc^2}\right)^{-1} & 0 & 0\\
        0 & 0 & r^2 & 0\\
        0 & 0 & 0 & r^2\sin^2\theta
        \end{pmatrix}
        """,

            },

        },


        "Kerr": {

        "what":
            "A métrica de Kerr instrui ao universo como se comporta perante a um Buraco-Negro que está girando.",

        "how":
            "Além de sua Massa distorcer por si só o tecido do espaço-tempo, ele cria mais três propriedades. Ao girar ele arrasta o espaço-tempo consigo. Uma região com velocidade maior que a velocidade da luz. E dois horizontes de evento.",

        "guide": {
            "g03_g30":
                "Possui termos fora da diagonal (g03 e g30) que misturam o Tempo com o ângulo de rotação."
        },

        "latex": r"""
    g_{\mu\nu}=
    \begin{pmatrix}
    -\left(1-\frac{2GMr}{\Sigma c^2}\right)
    &0&0&
    -\frac{2GMar\sin^2\theta}{\Sigma c}
    \\
    0&
    \frac{\Sigma}{\Delta}
    &0&0
    \\
    0&0&
    \Sigma
    &0
    \\
    -\frac{2GMar\sin^2\theta}{\Sigma c}
    &0&0&
    \left(r^2+a^2+
    \frac{2GMa^2r\sin^2\theta}{\Sigma c^2}
    \right)\sin^2\theta
    \end{pmatrix}
    """
    },


        "FLRW": {

            "what":
                "A métrica de FLWR instrui ao universo o formato que deve assumir durante sua expansão.",

            "how":
                "O universo pode formatar-se em três formatos: plano, esférico, cone de dois lados.",

            "latex": r"""
    g_{\mu\nu}=
    \begin{pmatrix}
    -c^2 & 0 & 0 & 0\\
    0 & \dfrac{a(t)^2}{1-kr^2} & 0 & 0\\
    0 & 0 & a(t)^2r^2 & 0\\
    0 & 0 & 0 & a(t)^2r^2\sin^2\theta
    \end{pmatrix}
    """
        },


        "Godel": {

            "what":
                "A métrida de Godel instrui ao universo a girar.",

            "how":
                "O universo possui um movimento de rotação. Toda matéria e energia está girando em torno de um eixo.",

            "guide": {
                "g02_g20":
                    "Possui termos fora da diagonal, entre o Tempo e o Y (g02 e g20), que rotacionam o universo."},

            "latex": r"""
    g_{\mu\nu}=
    \begin{pmatrix}
    -1 & 0 & -e^x & 0\\
    0 & 1 & 0 & 0\\
    -e^x & 0 & \dfrac{1}{2}e^{2x} & 0\\
    0 & 0 & 0 & 1
    \end{pmatrix}
    """

        }
    },
}
