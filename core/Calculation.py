from rich.traceback import install
from einsteinpy.symbolic import ChristoffelSymbols, MetricTensor, EinsteinTensor, RicciTensor, RicciScalar, simplify_sympy_array
from sympy import symbols, diff, simplify, Matrix, sin, exp, cos, latex, pprint

install(show_locals=True)

def calcular(metric, coords):

    Γ = ChristoffelSymbols.from_metric(metric)

    Ricci = [[0 for i in range(4)] for j in range(4)]
    EFE = [[0 for i in range(4)] for j in range(4)]

    g_inv = metric.inv()

    for µ in range(4):
        for v in range(4):
            term_ricci = 0

            for p in range(4):

                term_ricci += (
                    diff(Γ[p,µ,v], coords[p])
                    - diff(Γ[p,µ,p], coords[v])
                )

                for λ in range(4):

                    term_ricci += (
                        Γ[p,p,λ]*Γ[λ,µ,v]
                        - Γ[p,v,λ]*Γ[λ,µ,p]
                    )

            Ricci[µ][v] = simplify(term_ricci)

    Ricci = Matrix(Ricci)

    R = simplify(
        sum(
            g_inv[i,j]*Ricci[i,j]
            for i in range(4)
            for j in range(4)
        )
    )

    for µ in range(4):
        for v in range(4):

            EFE[µ][v] = simplify(
                Ricci[µ,v]
                - 1/2*R*metric[µ,v]
            )

    return Γ, Ricci, R, Matrix(EFE)

t, r, θ, φ = symbols("t r θ φ")
x, y, z = symbols("x y z")
coords = [t, r, θ, φ]
coords_xyz = [t, x, y, z]
M, G, c = symbols("M G c")

def schwarzschild_metric():

    list = [[0 for _ in range(4)] for _ in range(4)]
    r_s = 2*G*M/c**2

    list[0][0] = -(1-r_s/r)*c**2
    list[1][1] = (1-r_s/r)**-1
    list[2][2] = r**2
    list[3][3] = r**2*sin(θ)**2

    metric=MetricTensor(list, syms=(t, r, θ, φ))

    Γ, Ricci, R, EFE = calcular(metric, coords)
    return Γ, Ricci, R, EFE

def FLRW_metric():

    a, k = symbols("a k")

    list = [[0 for _ in range(4)] for _ in range(4)]

    list[0][0] = -1
    list[1][1] = a**2/(1-k*r**2)
    list[2][2] = a**2*r**2
    list[3][3] = a**2*r**2*sin(θ)**2

    metric=MetricTensor(list, syms=(t, r, θ, φ))

    Γ, Ricci, R, EFE = calcular(metric, coords)
    return Γ, Ricci, R, EFE

def Kerr_metric():
    a = symbols("a")

    list = [[0 for _ in range(4)] for _ in range(4)]

    rs = 2*G*M/c**2
    ρ = r**2 + a**2 * cos(θ)**2
    Δ = r**2 - rs*r + a**2

    list[0][0] = simplify(-(1 - (rs * r) / ρ) * c**2)
    list[0][3] = simplify(-(rs * r * a * sin(θ)**2) / ρ * c)
    list[1][1] = simplify(ρ / Δ)
    list[2][2] = simplify(ρ)
    list[3][0] = simplify(-(rs * r * a * sin(θ)**2) / ρ * c)
    list[3][3] = simplify((r**2 + a**2 + (rs * r * a**2 * sin(θ)**2) / ρ) * sin(θ)**2)

    metric=MetricTensor(list, syms=(t, r, θ, φ))

    Γ, Ricci, R, EFE = calcular(metric, coords)
    return Γ, Ricci, R, EFE

def Godel_metric():

    list = [[0 for _ in range(4)] for _ in range(4)]

    w = symbols("w")

    list[0][0] = -1
    list[0][2] = -exp((2**0.5) * w * x)
    list[1][1] = 1
    list[2][0] = -exp((2**0.5) * w * x)
    list[2][2] = 0.5 * exp(2 * (2**0.5) * w * x)
    list[3][3] = 1

    metric = MetricTensor(list, syms=(t, x, y, z))
    Γ, Ricci, R, EFE = calcular(metric, coords=coords_xyz)
    return Γ, Ricci, R, EFE

def data(Γ, Ricci, R, EFE):

    christoffel = []

    for l in range(4):

        M = Matrix([
            [Γ[i, j, l] for j in range(4)]
            for i in range(4)
        ])

        christoffel.append(latex(M))

    return (
        christoffel[0],
        christoffel[1],
        christoffel[2],
        christoffel[3],
        latex(Ricci),
        latex(R),
        latex(EFE)
    )

def relatório(Γ, Ricci, R, EFE):


    print(f"""
-------------------------------------------------------
Data from the Einstein Field Equation
-------------------------------------------------------
          
Christoffel Symbols:""")
    for l in range(4):
        a = Matrix([
        [Γ[i,j,l] for j in range(4)]
        for i in range(4)
    ])
        print(f"           Γ[i,j,{l}] =")
        pprint(a)
        

    print("-"*55, "\n\nTensor Ricci: ")
    pprint(Ricci)

    print("-"*55, "\n\nEscalar Ricci: ")
    pprint(R)

    print("-"*55, "\n\nEFE: ")
    pprint(EFE)

