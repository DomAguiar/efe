GENERAL = {
    "PT": {
        "metric": {

            "definition":
                "Uma métrica é o manual de instrução de como o universo deve se comportar.",

            "matrix": {

                "matrix": """
    [g00, g01, g02, g03]
    [g10, g11, g12, g13]
    [g20, g21, g22, g23]
    [g30, g31, g32, g33]
    """,

                "guide": {

                    "rows_columns":
                        "O número indica a dimensão: 0 é Tempo, 1 é o eixo X, 2 é o eixo Y e 3 é o eixo Z.",

                    "identical_terms":
                        "A diagonal pura dita o ritmo próprio de cada dimensão (g00 dita o tempo, g11 dita o X, g22 dita o Y, g33 dita o Z).",

                    "mixed_terms":
                        "Os cruzamentos ditam como duas dimensões se misturam (ex: g01 mistura Tempo e X; g12 entorta o ângulo entre X e Y)."
                }
            }
        },
    
        "christoffel": {
            "definition": "Mede a curvatura do espaço",
            "formula": {
                "expression": 
                r"""
    \Gamma^\lambda_{\mu\nu} = \frac{1}{2} g^{\lambda\sigma} \left( \partial_\nu g_{\sigma\mu} + \partial_\mu g_{\sigma\nu} - \partial_\sigma g_{\mu\nu} \right)
    """,
            "guide": {

                "indice": 
                    r"\lambda, \mu, \nu : Se referem-se a qual dimensão está sendo distorcida.",

                "metric": 
                    r"g^{\lambda\sigma}, g_{\mu\nu} : são as configurações do universo.",

                "diff":
                    r"\frac{\partial g}{\partial x} : são as mudanças que ocorrem em cada direção."
                }

            }
        },

        "ricci": {

            "definition":
                "O Tensor de Ricci mede como o espaço-tempo se curva quando observamos a concentração de matéria e energia. Ele resume a curvatura causada pela geometria do universo.",

            "formula": {

                "expression":
                r"""
R_{\mu\nu} =
\partial_\lambda \Gamma^\lambda_{\mu\nu}
-
\partial_\nu \Gamma^\lambda_{\mu\lambda}
+
\Gamma^\lambda_{\lambda\sigma}\Gamma^\sigma_{\mu\nu}
-
\Gamma^\lambda_{\nu\sigma}\Gamma^\sigma_{\mu\lambda}
""",

                "guide": {

                    "indice":
                        r"\mu,\nu : Indicam quais dimensões do espaço-tempo estão sendo analisadas.",

                    "christoffel":
                        r"\Gamma^\lambda_{\mu\nu} : São os símbolos de Christoffel, que descrevem como as coordenadas mudam dentro do espaço curvo.",

                    "derivative":
                        r"\partial : Representa a variação dos símbolos de Christoffel em cada direção.",

                    "meaning":
                        "O Tensor de Ricci transforma a informação da curvatura local em uma medida de como volumes e trajetórias são comprimidos ou expandidos pelo espaço-tempo."
                }
            }
        },


        "ricci_scalar": {

            "definition":
                "O Escalar de Ricci é uma medida única da curvatura total do espaço-tempo em um ponto. Ele transforma o Tensor de Ricci, que possui várias componentes, em apenas um número.",

            "formula": {

                "expression":
                r"""
R = g^{\mu\nu}R_{\mu\nu}
""",

                "guide": {

                    "metric_inverse":
                        r"g^{\mu\nu} : É a métrica inversa, usada para transformar o Tensor de Ricci em um escalar.",

                    "ricci":
                        r"R_{\mu\nu} : É o Tensor de Ricci, que contém as informações da curvatura do espaço-tempo.",

                    "meaning":
                        "O resultado final é um único valor que indica o quanto o espaço-tempo está curvado naquele ponto."
                }
            }
        },


        "einstein_tensor": {

            "definition":
                "O Tensor de Einstein representa a curvatura do espaço-tempo que aparece diretamente nas Equações de Campo de Einstein. Ele conecta a geometria do universo com a matéria e energia existentes.",

            "formula": {

                "expression":
                r"""
G_{\mu\nu}=R_{\mu\nu}-\frac{1}{2}Rg_{\mu\nu}
""",

                "guide": {

                    "ricci":
                        r"R_{\mu\nu} : Representa uma parte da curvatura causada pela geometria do espaço-tempo.",

                    "scalar":
                        r"R : É o Escalar de Ricci, que remove a parte da curvatura total.",

                    "metric":
                        r"g_{\mu\nu} : É a própria métrica, que define a estrutura do espaço-tempo.",

                    "meaning":
                        "O Tensor de Einstein é a parte geométrica das Equações de Campo de Einstein. Ele descreve como a curvatura do universo deve responder à presença de energia e matéria."
                }
            }
        }
    }
}
