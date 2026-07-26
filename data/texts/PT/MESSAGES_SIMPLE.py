from core.Calculation import (
    data,
    schwarzschild_metric,
    Kerr_metric,
    FLRW_metric,
    Godel_metric
)

z, s, c, h = schwarzschild_metric()

Γ, Γ1, Γ2, Γ3, Ricci, R, EFE = data(z, s, c, h)

k, e, r, r = Kerr_metric()

Γk, Γ1k, Γ2k, Γ3k, Riccik, Rk, EFEk = data(k, e, r, r)

f, l, r, w = FLRW_metric()

Γf, Γ1f, Γ2f, Γ3f, Riccif, Rf, EFEf = data(f,l,w,r)

g, o, d, e = Godel_metric()

Γg, Γ1g, Γ2g, Γ3g, Riccig, Rg, EFEg = data(g, o, d, e)

MESSAGES_SIMPLE = { 
    "PT": {
        "Schwarzschild": {
            "Curiosidades": [
    "Ela calcula o 'Raio de Schwarzschild', que é o tamanho exato que algo precisa ter para virar um buraco negro.",
    "Se você esmagasse a Terra inteira até ela ficar do tamanho de uma bolinha de gude, ela viraria um buraco negro.",
    "Esse raio funciona como uma fronteira: se você passar dele, nem a luz consegue escapar e você fica preso para sempre.",
    "A fórmula mostra que no centro de tudo existe a 'singularidade', um lugar bizarro onde o tempo para e a gravidade é infinita.",
    "A métrica foi criada por um soldado alemão no meio das trincheiras da Primeira Guerra Mundial, usando a teoria de Einstein.",
    "Ela prova que buracos negros não são aspiradores gigantes; se o Sol virasse um, a Terra continuaria orbitando ele normalmente."
],

            "Fórmulas": [
    "A fórmula é 'R = 2GM/c²', onde 'R' é o raio da borda, 'M' é a massa do objeto, 'G' é a gravidade e 'c' é a velocidade da luz.",
    "Ela é uma equação direta: se você dobrar a massa do objeto ('M'), o tamanho do buraco negro ('R') também dobra de tamanho exato.",
    "A letra 'c' (velocidade da luz) está ao quadrado e dividindo, o que significa que precisa de uma massa gigantesca para o raio ter um tamanho visível.",
    "Essa fórmula nasceu como a primeira resposta exata para as Equações de Campo de Einstein, que o próprio Einstein achava quase impossíveis de resolver.",
    "Apesar de definir o tamanho de um buraco negro, a fórmula foi criada antes mesmo de sabermos que os buracos negros existiam de verdade no universo.",
    "O resultado da conta é medido em metros, provando que a astrofísica mais complexa pode ser resumida em uma distância simples que você mede com fita métrica."
],

            "Easter Eggs": [
    "O metro existe por causa da velocidade da luz, que vale fixos 299.792.458 metros por segundo.",
    "A força que une a eletricidade e o magnetismo tem o número secreto de 1 dividido por 137.",
    "A internet do mundo inteiro funciona por elétrons que, juntos, pesam o mesmo que um morango.",
    "As contas de Albert Einstein permitem de verdade criar mapas para um universo com viagem no tempo.",
    "O espaço tem um eco congelado do Big Bang que mede exatamente 2,73 graus acima do zero absoluto."
],
            "Equações": [
    {
        "name": "Raio Schwarzschild",
        "latex": r"R_s=\frac{2GM}{c^2}"
    },

    {
        "name": "Métrica de Schwarzschild",
        "latex": r"""
        ds^2=
        -\left(1-\frac{2GM}{rc^2}\right)c^2dt^2
        +
        \left(1-\frac{2GM}{rc^2}\right)^{-1}dr^2
        +
        r^2d\Omega^2
        """
    },

    {
        "name": "Símbolos de Christoffel⁰",
        "latex": fr"""
\Gamma^0_{{\mu\nu}} =
{Γ}"""
    },
    {
        "name": "Símbolos de Christoffel¹",
        "latex": fr"""
\Gamma^1_{{\mu\nu}} =
{Γ1}"""
    },
    {
        "name": "Símbolos de Christoffel²",
        "latex": fr"""
\Gamma^2_{{\mu\nu}} =
{Γ2}"""
    },
    {    
        "name": "Símbolos de Christoffel³",
        "latex": fr"""
\Gamma^3_{{\mu\nu}} =
{Γ3}"""
    },

    {
        "name": "Tensor de Ricci",
        "latex": fr"""
R_{{\mu\nu}} =
{Ricci}"""
    },

    {
        "name": "Escalar de Ricci",
        "latex": fr"""
R =
{R}"""
    },
    {
        "name": "Tensor de Einstein",
        "latex": fr"""
G_{{\mu\nu}} = 
{EFE}"""
    }

]
        },
        "Kerr": {

    "Curiosidades": [
        "Todo buraco negro real provavelmente gira, tornando a métrica de Kerr muito mais comum que a de Schwarzschild.",
        "A rotação do buraco negro arrasta o próprio espaço-tempo, um fenômeno chamado arrasto de referenciais.",
        "Ao redor do buraco negro existe a ergosfera, uma região onde nada consegue permanecer parado.",
        "É teoricamente possível extrair energia de um buraco negro em rotação através do Processo de Penrose.",
        "A solução de Kerr prevê dois horizontes de eventos em vez de apenas um.",
        "Se a rotação fosse extrema, a estrutura interna do buraco negro seria muito mais complexa do que imaginamos."
    ],

    "Fórmulas": [
        "A métrica depende de dois parâmetros principais: a massa M e o parâmetro de rotação a.",
        "O parâmetro a é definido por a = J/(Mc), onde J representa o momento angular.",
        "Quando a = 0, a solução de Kerr se transforma exatamente na solução de Schwarzschild.",
        "A presença dos termos g₀₃ e g₃₀ mostra matematicamente que tempo e rotação estão acoplados.",
        "As quantidades Σ e Δ aparecem repetidamente para simplificar a escrita da métrica.",
        "A métrica de Kerr é uma solução exata das Equações de Campo de Einstein no vácuo."
    ],

    "Easter Eggs": [
        "O efeito de arrasto previsto por Kerr já foi medido experimentalmente por satélites ao redor da Terra.",
        "O filme Interestelar utilizou simulações baseadas na métrica de Kerr para representar Gargantua.",
        "A primeira imagem de um buraco negro provavelmente mostra um objeto descrito por Kerr.",
        "A ergosfera permite processos físicos impossíveis em qualquer outro lugar do Universo.",
        "A solução de Kerr inspirou inúmeras pesquisas sobre viagens no tempo e buracos de minhoca."
    ],

    "Equações": [
        {
            "name": "Símbolos de Christoffel⁰",
            "latex": fr"""
\Gamma^0_{{\mu\nu}} = {Γk}
"""
        },

        {
            "name": "Símbolos de Christoffel¹",
            "latex": fr"""
\Gamma^1_{{\mu\nu}} = {Γ1k}"""
        },
        {
            "name": "Símbolos de Christoffel²",
            "latex": fr"""
            \Gamma^2_{{\mu\nu}} = {Γ2k}"""
        },
        {
            "name": "Símbolos de Christoffel³",
            "latex": fr"""
            \Gamma^3_{{\mu\nu}} = {Γ3k}"""
        },
        {
            "name": "Tensor de Ricci",
            "latex": fr"""
R_{{\mu\nu}} = {Riccik}"""
        },
        {
            "name": "Escalar de Ricci",
            "latex": f"R = {Rk}"
        },
        {
            "name": "Tensor de Einstein",
            "latex": fr"""
G_{{\mu\nu}} = {EFEk}"""
        }
    ]
        },
        "FLRW": {

    "Curiosidades": [
        "A métrica FLRW descreve o Universo inteiro, e não apenas um objeto isolado.",
        "Ela assume que, em grande escala, o Universo é homogêneo e isotrópico.",
        "É a base matemática do modelo do Big Bang.",
        "Segundo essa métrica, o próprio espaço está se expandindo; não são apenas as galáxias que se movem.",
        "Dependendo da curvatura, o Universo pode ser fechado, plano ou aberto.",
        "Quase toda a cosmologia moderna utiliza alguma versão da métrica FLRW."
    ],

    "Fórmulas": [
        "O fator de escala a(t) determina o tamanho do Universo em cada instante.",
        "Quando a(t) aumenta, as distâncias entre galáxias também aumentam.",
        "O parâmetro k representa a curvatura espacial: +1, 0 ou -1.",
        "As Equações de Friedmann são obtidas aplicando as Equações de Einstein à métrica FLRW.",
        "O desvio para o vermelho cosmológico depende diretamente da evolução de a(t).",
        "A expansão acelerada pode ser representada adicionando a constante cosmológica Λ."
    ],

    "Easter Eggs": [
        "Toda a luz do Universo primitivo ainda existe como Radiação Cósmica de Fundo.",
        "Mesmo viajando para sempre, talvez nunca seja possível alcançar certas galáxias devido à expansão.",
        "O Universo observável possui aproximadamente 93 bilhões de anos-luz de diâmetro.",
        "O espaço pode crescer mais rápido que a luz sem violar a Relatividade.",
        "A idade estimada do Universo é de aproximadamente 13,8 bilhões de anos."
    ],
    "Equações": [
        {
            "name": "Símbolos de Christoffel⁰",
            "latex": fr"""
\Gamma^0_{{\mu\nu}} = {Γf}
"""
        },

        {
            "name": "Símbolos de Christoffel¹",
            "latex": fr"""
\Gamma^1_{{\mu\nu}} = {Γ1f}"""
        },
        {
            "name": "Símbolos de Christoffel²",
            "latex": fr"""
            \Gamma^2_{{\mu\nu}} = {Γ2f}"""
        },
        {
            "name": "Símbolos de Christoffel³",
            "latex": fr"""
            \Gamma^3_{{\mu\nu}} = {Γ3f}"""
        },
        {
            "name": "Tensor de Ricci",
            "latex": fr"""
R_{{\mu\nu}} = {Riccif}"""
        },
        {
            "name": "Escalar de Ricci",
            "latex": f"R = {Rf}"
        },
        {
            "name": "Tensor de Einstein",
            "latex": fr"""
G_{{\mu\nu}} = {EFEf}"""
        }
    ]
        },
        "Godel": {

    "Curiosidades": [
        "A solução de Gödel descreve um universo inteiro em rotação.",
        "Ela permite curvas temporais fechadas, trajetórias que retornam ao próprio passado.",
        "Foi proposta por Kurt Gödel, um dos maiores lógicos da história.",
        "Gödel criou essa solução como um desafio filosófico para a Relatividade Geral.",
        "Nesse universo, não existe um tempo absoluto compartilhado por todos os observadores.",
        "Apesar de matematicamente válida, acredita-se que ela não descreva o nosso Universo."
    ],

    "Fórmulas": [
        "A métrica contém termos mistos entre tempo e espaço, representando a rotação global.",
        "Os termos g₀₂ e g₂₀ mostram que tempo e direção Y estão acoplados.",
        "Ela é uma solução exata das Equações de Campo de Einstein.",
        "A solução exige uma distribuição específica de matéria e uma constante cosmológica.",
        "Sua geometria possui simetrias diferentes das métricas cosmológicas convencionais.",
        "Ela demonstra que a Relatividade Geral permite soluções extremamente exóticas."
    ],

    "Easter Eggs": [
        "Kurt Gödel era amigo pessoal de Albert Einstein em Princeton.",
        "Einstein considerava Gödel um dos maiores matemáticos de sua época.",
        "Gödel também demonstrou os famosos Teoremas da Incompletude.",
        "A existência de viagens ao passado em Gödel depende apenas da geometria do espaço-tempo.",
        "Até hoje físicos discutem se alguma lei fundamental impede soluções como essa de existirem na natureza."
    ],

    "Equações": [
        {
            "name": "Símbolos de Christoffel⁰",
            "latex": fr"""
\Gamma^0_{{\mu\nu}} = {Γ}
"""
        },

        {
            "name": "Símbolos de Christoffel¹",
            "latex": fr"""
\Gamma^1_{{\mu\nu}} = {Γ1g}"""
        },
        {
            "name": "Símbolos de Christoffel²",
            "latex": fr"""
            \Gamma^2_{{\mu\nu}} = {Γ2g}"""
        },
        {
            "name": "Símbolos de Christoffel³",
            "latex": fr"""
            \Gamma^3_{{\mu\nu}} = {Γ3g}"""
        },
        {
            "name": "Tensor de Ricci",
            "latex": fr"""
R_{{\mu\nu}} = {Riccig}"""
        },
        {
            "name": "Escalar de Ricci",
            "latex": f"R = {Rg}"
        },
        {
            "name": "Tensor de Einstein",
            "latex": fr"""
G_{{\mu\nu}} = {EFEg}"""

                }
            ]
        }
    }
}


