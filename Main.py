from rich.traceback import install
from einsteinpy.symbolic import ChristoffelSymbols, MetricTensor, EinsteinTensor, RicciTensor, RicciScalar, simplify_sympy_array
from sympy import symbols, Function, diff, simplify, Matrix, sin, lambdify, sqrt, exp, cos

install(show_locals=True)

def schwarzschild_metric(Massa, limite=500):

    t, r, θ, φ = symbols("t r θ φ")
    coords = [t, r, θ, φ]
    M, G, c = symbols("M G c")

    r_s = 2*G*M/c**2

    list = [[0 for i in range(4)] for j in range(4)]

    list[0][0] = -(1-r_s/r)*c**2
    list[1][1] = (1-r_s/r)**-1
    list[2][2] = r**2
    list[3][3] = r**2*sin(θ)**2

    metric=MetricTensor(list, syms=(t, r, θ, φ))
    Γ = ChristoffelSymbols.from_metric(metric)

    #print(EinsteinTensor.from_metric(metric=metric))

    #Ricci = RicciTensor.from_christoffels(Γ)
    #R = RicciScalar.from_christoffels(Γ)

    #for µ in range(4):
    #    for v in range(4):
    #        expr = Ricci[µ][v] - 1/2 * R.expr * metric[µ][v]

    #print(expr)


    Ricci = [[0 for i in range(4)] for j in range(4)]
    EFE = [[0 for i in range(4)] for j in range(4)]

    g_inv = metric.inv()

    for µ in range(4):
        for v in range(4):
            term_ricci = 0
            for p in range(4):
                term_ricci += diff(Γ[p,µ,v], coords[p]) - diff(Γ[p,µ,p], coords[v])
                for λ in range(4):
                    term_ricci += Γ[p,p,λ]*Γ[λ,µ,v] - Γ[p,v,λ]*Γ[λ,µ,p]
            
            Ricci[µ][v] = simplify(term_ricci)

    print("Ricci Tensor:", Ricci)

    print("Ricci Tensor of Einstenpy:",RicciTensor.from_christoffels(Γ).tensor)


    Ricci = Matrix(Ricci)
    for i in range(4):
        for j in range(4):
            if simplify(Ricci[i,j] - RicciTensor.from_christoffels(Γ).tensor()[i,j]).is_zero:
                #print("Ricci Tensor is correct")
                pass
            else:
                print("Ricci Tensor is NOT correct")

    print("---"*20)

    R = simplify(g_inv[0,0]*Ricci[0,0] + g_inv[1,1]*Ricci[1,1] + g_inv[2,2]*Ricci[2,2] + g_inv[3,3]*Ricci[3,3])
    print("\n\n\nRicci Scalar:", R)

    print("Ricci Scalar of Einstenpy:",RicciScalar.from_christoffels(Γ).expr)

    if simplify(R - RicciScalar.from_christoffels(Γ).expr).is_zero:
        #print("Ricci Scalar is correct")
        pass
    else:
        print("Ricci Scalar is NOT correct")

    print("---"*20)

    for µ in range(4):
        for v in range(4):
            EFE[µ][v] = simplify(Ricci[µ,v] - 1/2 * R * metric[µ,v])

    print("\n\n\nEFE:", EFE)

    print("Einstein Tensor of Einstenpy:",EinsteinTensor.from_metric(metric).tensor())

    EFE = Matrix(EFE)
    for i in range(4):
        for j in range(4):
            if simplify(EFE[i,j] - EinsteinTensor.from_metric(metric).tensor()[i,j]).is_zero:
                #print("Einstein Tensor is correct")
                pass
            else:
                print("Einstein Tensor is NOT correct")
    
    print("---"*20)

    import numpy as np
    import matplotlib
    matplotlib.use('tkagg')
    import matplotlib.pyplot as plt

    G = 1
    c = 1
    M = Massa
    r_s = 2*G*M/c**2

    theta_vals = np.linspace(-np.pi, np.pi, 1000, endpoint=True)
    r_vals = np.linspace(r_s+0.1, limite, 1000)

    R, Θ = np.meshgrid(r_vals, theta_vals)

    X = R * np.sin(Θ)
    Y = R * np.cos(Θ)

    if np.any(R <= r_s):
        Z = np.zeros_like(R)
        Z[R > r_s] = 2*np.sqrt(r_s*(R[R > r_s]-r_s))

    else:
        Z = 2*np.sqrt(r_s*(R-r_s))

    r_teste = 2 * r_s
    z_teorico = 2 * np.sqrt(r_s * (r_teste - r_s))
    print(f"Para r = {r_teste}, a profundidade Z no gráfico deve ser: {z_teorico:.4f}")


    fig = plt.figure(figsize=(16, 8), facecolor='black')

    ax = fig.add_subplot(111, projection='3d')
    surface = ax.plot_surface(X, Y, Z, cmap='magma', alpha=0.7, antialiased=True)
    
    ax.scatter(0, 0, np.max(Z), color='white', s=200, label='Buraco Negro / Massa')
    ax.set_title("Black Hole with mass of " + str(M) + " solar masses")
    MAX_R = limite

    ax.set_xlim(-MAX_R, MAX_R)
    ax.set_ylim(-MAX_R, MAX_R)
    ax.set_zlim(-MAX_R, 0)

    ax.axis('off')
    ax.set_facecolor('black')
    ax.grid(False)
    ax.view_init(elev=30, azim=-45)

    plt.tight_layout()
    plt.show()

def FLRW_metric(k=1, a=1, fate="no"):
    t, r, θ, φ = symbols("t r θ φ")
    coords = [t, r, θ, φ]
    M, G, c = symbols("M G c")

    list = [[0 for i in range(4)] for j in range(4)]

    list[0][0] = -1
    list[1][1] = a**2/(1-k*r**2)
    list[2][2] = a**2*r**2
    list[3][3] = a**2*r**2*sin(θ)**2

    metric=MetricTensor(list, syms=(t, r, θ, φ))
    Γ = ChristoffelSymbols.from_metric(metric)

    #print(EinsteinTensor.from_metric(metric=metric))

    #Ricci = RicciTensor.from_christoffels(Γ)
    #R = RicciScalar.from_christoffels(Γ)

    #for µ in range(4):
    #    for v in range(4):
    #        expr = Ricci[µ][v] - 1/2 * R.expr * metric[µ][v]

    #print(expr)


    Ricci = [[0 for i in range(4)] for j in range(4)]
    EFE = [[0 for i in range(4)] for j in range(4)]

    g_inv = metric.inv()

    for µ in range(4):
        for v in range(4):
            term_ricci = 0
            for p in range(4):
                term_ricci += diff(Γ[p,µ,v], coords[p]) - diff(Γ[p,µ,p], coords[v])
                for λ in range(4):
                    term_ricci += Γ[p,p,λ]*Γ[λ,µ,v] - Γ[p,v,λ]*Γ[λ,µ,p]
            
            Ricci[µ][v] = simplify(term_ricci)

    print("Ricci Tensor:", Ricci)

    print("Ricci Tensor of Einstenpy:",RicciTensor.from_christoffels(Γ).tensor)


    Ricci = Matrix(Ricci)
    for i in range(4):
        for j in range(4):
            if simplify(Ricci[i,j] - RicciTensor.from_christoffels(Γ).tensor()[i,j]).is_zero:
                #print("Ricci Tensor is correct")
                pass
            else:
                print("Ricci Tensor is NOT correct")

    print("---"*20)

    R = simplify(g_inv[0,0]*Ricci[0,0] + g_inv[1,1]*Ricci[1,1] + g_inv[2,2]*Ricci[2,2] + g_inv[3,3]*Ricci[3,3])
    print("\n\n\nRicci Scalar:", R)

    print("Ricci Scalar of Einstenpy:",RicciScalar.from_christoffels(Γ).expr)

    if simplify(R - RicciScalar.from_christoffels(Γ).expr).is_zero:
        #print("Ricci Scalar is correct")
        pass
    else:
        print("Ricci Scalar is NOT correct")

    print("---"*20)

    for µ in range(4):
        for v in range(4):
            EFE[µ][v] = simplify(Ricci[µ,v] - 1/2 * R * metric[µ,v])

    print("\n\n\nEFE:", EFE)

    print("Einstein Tensor of Einstenpy:",EinsteinTensor.from_metric(metric).tensor())

    EFE = Matrix(EFE)
    for i in range(4):
        for j in range(4):
            if simplify(EFE[i,j] - EinsteinTensor.from_metric(metric).tensor()[i,j]).is_zero:
                #print("Einstein Tensor is correct")
                pass
            else:
                print("Einstein Tensor is NOT correct")

    import numpy as np
    import matplotlib
    matplotlib.use('tkagg')
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    from matplotlib.widgets import Slider


    G, c = 1, 1

    fig = plt.figure(figsize=(100, 100), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    if k == -1:
        
        ax_slider = fig.add_axes([0.25, 0.05, 0.5, 0.03], facecolor='gray')

        slider_zoom = Slider(
            ax=ax_slider,
            label='Zoom da Câmera ',
            valmin=1,     
            valmax=100000,    
            valinit=25000,    
            valfmt='%1.0f',
            color='red'
        )
        slider_zoom.label.set_color('white')
        slider_zoom.valtext.set_color('white')

    if k == 0:

        ax_slider = fig.add_axes([0.25, 0.05, 0.5, 0.03], facecolor='gray')

        slider_zoom = Slider(
            ax=ax_slider,
            label='Zoom da Câmera ',
            valmin=1,     
            valmax=500,    
            valinit=50,    
            valfmt='%1.0f',
            color='red'
        )
        slider_zoom.label.set_color('white')
        slider_zoom.valtext.set_color('white')

    if k == 1:

        ax_slider = fig.add_axes([0.25, 0.05, 0.5, 0.03], facecolor='gray')

        slider_zoom = Slider(
            ax=ax_slider,
            label='Zoom da Câmera ',
            valmin=1,     
            valmax=1000,    
            valinit=100,    
            valfmt='%1.0f',
            color='red'
        )
        slider_zoom.label.set_color('white')
        slider_zoom.valtext.set_color('white')

    θ = np.linspace(0, np.pi, 1000, endpoint=True)
    φ = np.linspace(0, 2*np.pi, 1000, endpoint=True)
    t = np.linspace(0, 10, 1000, endpoint=True)

    def update(frame):
        ax.clear()
        ax.set_facecolor('black')

        if fate == "no" or fate == "freeze":
            a = np.exp(0.02 * frame)

        elif fate == "big_rip":
            tempo_fim = 105 
            if frame < tempo_fim:
                a = 1 / (1 - (frame / tempo_fim)) 
            else:
                a = np.nan

        elif fate == "big_crunch":
            a = np.sin(np.pi * frame/100)
            if a < 0:
                a = 0

        if k == 1:
            Θ, Φ = np.meshgrid(θ, φ)
            X = a * np.sin(Θ) * np.cos(Φ)
            Y = a * np.sin(Θ) * np.sin(Φ)
            Z = a * np.cos(Θ)
            ax.plot_surface(X, Y, Z, cmap='magma', alpha=0.7, antialiased=True)
        elif k == 0:
            r = np.linspace(0, 10, 250)
            r, Φ = np.meshgrid(r, φ)
            X = a * r * np.cos(Φ)
            Y = a * r * np.sin(Φ)
            Z = np.zeros_like(X)

            R_dist = np.sqrt(X**2 + Y**2)
            max_dist = np.max(R_dist) if np.max(R_dist) > 0 else 1
            cores = plt.cm.magma(R_dist / max_dist)
            
            ax.plot_surface(X, Y, Z, facecolors=cores, alpha=0.7, antialiased=True)
                
        elif k == -1:
            χ = np.linspace(0, 10, 250)
            χ, Φ = np.meshgrid(χ, φ)

            X = a * np.sinh(χ) * np.cos(Φ)
            Y = a * np.sinh(χ) * np.sin(Φ)
            Z = a * np.cosh(χ)
            Z_NEG = -a * np.cosh(χ)
            ax.plot_surface(X, Y, Z_NEG, cmap='magma', alpha=0.7, antialiased=True)
            ax.plot_surface(X, Y, Z, cmap='magma', alpha=0.7, antialiased=True)

        

        ax.set_title(f"FLRW Metric (k = {k}) | Fate: {fate.upper()}", color='white', fontsize=14)
        
        zoom_dinamico = slider_zoom.val
        ax.set_xlim(-zoom_dinamico, zoom_dinamico)
        ax.set_ylim(-zoom_dinamico, zoom_dinamico)
        ax.set_zlim(-zoom_dinamico, zoom_dinamico)


        plt.axis('off')
        ax.set_facecolor('black')
        ax.grid(False)
        plt.tight_layout()

    ani = FuncAnimation(fig, update, frames=1000, interval=100, blit=False)

    plt.show()

def Kerr_metric(a):
    t, r, θ, φ = symbols("t r θ φ")
    coords = [t, r, θ, φ]
    M, G, c = symbols("M G c")
    M = 1
    G = 1
    c = 1

    ρ = sqrt(r**2 + a * cos(θ)**2)
    Δ = r**2 - 2*G*M*r/c**2 + a**2

    list = [[0 for i in range(4)] for j in range(4)]

    list[0][0] = -(1 - 2*M*r/(ρ**2))
    list[0][3] = -2*M*a*r*sin(θ)**2/(ρ**2)
    list[1][1] = ρ**2/Δ
    list[2][2] = ρ**2
    list[3][0] = -2*M*a*r*sin(θ)**2/(ρ**2)
    list[3][3] = (r**2 + a**2 + 2*M*a**2*r*sin(θ)**2/(ρ**2))*sin(θ)**2

    metric=MetricTensor(list, syms=(t, r, θ, φ))
    Γ = ChristoffelSymbols.from_metric(metric)

    Ricci = [[0 for i in range(4)] for j in range(4)]
    EFE = [[0 for i in range(4)] for j in range(4)]

    g_inv = metric.inv()

    for µ in range(4):
        for v in range(4):
            term_ricci = 0
            for p in range(4):
                term_ricci += diff(Γ[p,µ,v], coords[p]) - diff(Γ[p,µ,p], coords[v])
                for λ in range(4):
                    term_ricci += Γ[p,p,λ]*Γ[λ,µ,v] - Γ[p,v,λ]*Γ[λ,µ,p]
            
            Ricci[µ][v] = simplify(term_ricci)

    for i in range(4):
        for j in range(4):
            if simplify(Ricci[i][j]).is_zero:
                #print("Ricci Tensor is correct")
                pass
    #print("Ricci Tensor:", (Ricci))

    print("Ricci Tensor of Einstenpy:",simplify_sympy_array(RicciTensor.from_christoffels(Γ).tensor))


    Ricci = Matrix(Ricci)
    for i in range(4):
        for j in range(4):
            if simplify(Ricci[i,j] - RicciTensor.from_christoffels(Γ).tensor()[i,j]).is_zero:
                #print("Ricci Tensor is correct")
                pass
            else:
                print("Ricci Tensor is NOT correct")

    print("---"*20)

    #R = simplify(g_inv[0,0]*Ricci[0,0] + g_inv[1,1]*Ricci[1,1] + g_inv[2,2]*Ricci[2,2] + g_inv[3,3]*Ricci[3,3])
    print("\n\n\nRicci Scalar:", R)
    print("Ricci Scalar of Einstenpy:",RicciScalar.from_christoffels(Γ).expr)

    if simplify(R - RicciScalar.from_christoffels(Γ).expr).is_zero:
        #print("Ricci Scalar is correct")
        pass
    else:
        print("Ricci Scalar is NOT correct")

    print("---"*20)

    for µ in range(4):
        for v in range(4):
            EFE[µ][v] = simplify(Ricci[µ,v] - 1/2 * R * metric[µ,v])

    #print("\n\n\nEFE:", EFE)

    print("Einstein Tensor of Einstenpy:",EinsteinTensor.from_metric(metric).tensor())

    EFE = Matrix(EFE)
    for i in range(4):
        for j in range(4):
            if simplify(EFE[i,j] - EinsteinTensor.from_metric(metric).tensor()[i,j]).is_zero:
                #print("Einstein Tensor is correct")
                pass
            else:
                print("Einstein Tensor is NOT correct")

schwarzschild_metric(100)


