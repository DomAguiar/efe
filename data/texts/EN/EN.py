from EFE.core.Calculation import(
    data,
    schwarzschild_metric,
    Kerr_metric,
    FLRW_metric,
    Godel_metric
)

a, b, c, d = schwarzschild_metric()
aa, bb, cc, dd = Kerr_metric()
aaa, bbb, ccc, ddd = FLRW_metric()
aaaa, bbbb, cccc, dddd = Godel_metric()

e, e1, e2, e3, f, g, h = data(a, b, c, d)
ee, ee1, ee2, ee3, ff, gg, hh = data(a, b, c, d)
eee, eee1, eee2, eee3, fff, ggg, hhh = data(a, b, c, d)
eeee, eeee1, eeee2, eeee3, ffff, gggg, hhhh = data(a, b, c, d)

MESSAGES_SIMPLE = {
    "EN": {

        "Schwarzschild": {
            "Curiosidades": [
                "It calculates the 'Schwarzschild Radius', the exact size an object must reach to become a black hole.",
                "If you compressed Earth until it was the size of a marble, it would become a black hole.",
                "The event horizon works like a border: after crossing it, even light cannot escape.",
                "The center of a black hole is predicted to contain a singularity, where our current physics breaks down.",
                "The Schwarzschild solution was discovered by Karl Schwarzschild while he was serving in World War I.",
                "A black hole is not a cosmic vacuum cleaner; if the Sun became one, Earth would keep orbiting normally."
                ],

            "Fórmulas": [
                "The formula is 'R = 2GM/c²', where 'R' is the Schwarzschild radius, 'M' is mass, 'G' is gravity and 'c' is the speed of light.",
                "If you double the mass of an object, its Schwarzschild radius also doubles.",
                "The speed of light appears squared in the equation, showing why enormous masses are needed to create large black holes.",
                "The Schwarzschild solution was the first exact solution of Einstein's Field Equations.",
                "The equation predicted black holes before we had evidence that they existed in the universe.",
                "The final result is a distance measured in meters, connecting cosmic physics with a simple length."
                ],

            "Easter Eggs": [
                "The speed of light is exactly 299,792,458 meters per second.",
                "The Cosmic Microwave Background is a frozen echo of the Big Bang at about 2.73 Kelvin.",
                "Gravity is the weakest known fundamental force, yet it controls the structure of galaxies.",
                "A black hole with the mass of the Sun would have a radius of only about 3 kilometers.",
                "Time itself slows down near extremely massive objects."
                ],

            "Equações": [
            {
                "name": "Christoffel Symbol⁰",
                "latex": fr"""
                    \Gamma^0_{{\mu\nu}} = {e}
                    """
            },

            {
                "name": "Christoffel Symbol¹",
                "latex": fr"""
                    \Gamma^1_{{\mu\nu}} = {e1}"""
            },
            {
                "name": "Christoffel Symbol²",
                "latex": fr"""
                    \Gamma^2_{{\mu\nu}} = {e2}"""
            },
            {
                "name": "Christoffel Symbol³",
                "latex": fr"""
                    \Gamma^3_{{\mu\nu}} = {e3}"""
            },
            {
                "name": "Ricci Tensor",
                "latex": fr"""
                    R_{{\mu\nu}} = {f}"""

            },
            {
                "name": "Ricci Scalar",
                "latex": f"R = {g}"
            },
            {
                "name": "Einstein Tensor",
                "latex": fr"""
            G_{{\mu\nu}} = {h}"""
            }
            ]

            },


"Kerr": {

"Curiosidades": [
"The Kerr metric describes rotating black holes, which are probably the most common type in nature.",
"A rotating black hole drags spacetime around it, an effect called frame dragging.",
"Near a Kerr black hole exists a region called the ergosphere, where nothing can remain completely still.",
"The spin of a black hole can store enormous amounts of rotational energy.",
"The Kerr solution was discovered by Roy Kerr in 1963.",
"A spinning black hole is not just a heavier Schwarzschild black hole; rotation changes spacetime itself."
],

"Fórmulas": [
"The Kerr metric depends on two main properties: mass and angular momentum.",
"The parameter 'a' represents the spin of the black hole and is related to its angular momentum.",
"When rotation disappears, the Kerr solution becomes the Schwarzschild solution.",
"The off-diagonal terms of the metric describe the mixing between time and rotation.",
"The ergosphere exists because spacetime itself is being dragged around the black hole.",
"The maximum possible spin of a black hole is limited by relativity."
],

"Easter Eggs": [
"A spinning black hole can lose energy through the Penrose process.",
"The Event Horizon Telescope photographed the shadow of a rotating black hole in M87.",
"Black holes can merge and create gravitational waves that travel across the universe.",
"The rotation of Earth also creates a tiny frame dragging effect.",
"A black hole has no memory of the object that formed it except mass, charge and spin."
],

"Equações": [
{
    "name": "Christoffel Symbol⁰",
    "latex": fr"""
\Gamma^0_{{\mu\nu}} = {ee}
"""
},

{
    "name": "Christoffel Symbol¹",
    "latex": fr"""
\Gamma^1_{{\mu\nu}} = {ee1}"""
},
{
    "name": "Christoffel Symbol²",
    "latex": fr"""
    \Gamma^2_{{\mu\nu}} = {ee2}"""
},
{
    "name": "Christoffel Symbol³",
    "latex": fr"""
    \Gamma^3_{{\mu\nu}} = {ee3}"""
},
{
    "name": "Ricci Tensor",
    "latex": fr"""
R_{{\mu\nu}} = {ff}"""
},
{
    "name": "Ricci Scalar",
    "latex": f"R = {gg}"
},
{
    "name": "Einstein Tensor",
    "latex": fr"""
G_{{\mu\nu}} = {hh}"""
}
]

},


"FLRW": {

"Curiosidades": [
"The FLRW metric is the mathematical foundation of modern cosmology.",
"It describes an expanding universe where galaxies move apart because space itself expands.",
"The universe can have positive, zero or negative spatial curvature.",
"The FLRW model assumes the universe is homogeneous and isotropic on large scales.",
"The Big Bang theory is based on solutions of Einstein's equations using this metric.",
"The expansion of the universe does not happen inside space; it is space itself that expands."
],

"Fórmulas": [
"The scale factor 'a(t)' describes how the size of the universe changes with time.",
"The curvature parameter 'k' determines whether the universe is closed, flat or open.",
"The Hubble parameter comes from the evolution of the scale factor.",
"The FLRW metric connects geometry with the large-scale evolution of the cosmos.",
"A changing scale factor means distances between galaxies change over time.",
"Einstein's equations transform the metric into predictions about the fate of the universe."
],

"Easter Eggs": [
"The universe is expanding faster today than it was billions of years ago.",
"Most of the universe is made of dark energy and dark matter, which we still do not fully understand.",
"Looking far away in space means looking back in time.",
"The observable universe is about 93 billion light-years wide.",
"The atoms in your body were created inside ancient stars."
],

"Equações": [
{
    "name": "Christoffel Symbol⁰",
    "latex": fr"""
\Gamma^0_{{\mu\nu}} = {eee}
"""
},

{
    "name": "Christoffel Symbol¹",
    "latex": fr"""
\Gamma^1_{{\mu\nu}} = {eee1}"""
},
{
    "name": "Christoffel Symbol²",
    "latex": fr"""
    \Gamma^2_{{\mu\nu}} = {eee2}"""
},
{
    "name": "Christoffel Symbol³",
    "latex": fr"""
    \Gamma^3_{{\mu\nu}} = {eee3}"""
},
{
    "name": "Ricci Tensor",
    "latex": fr"""
R_{{\mu\nu}} = {fff}"""
},
{
    "name": "Ricci Scalar",
    "latex": f"R = {ggg}"
},
{
    "name": "Einstein Tensor",
    "latex": fr"""
G_{{\mu\nu}} = {hhh}"""
}
]

},


"Godel": {

"Curiosidades": [
"The Gödel metric describes a universe that rotates as a whole.",
"It allows theoretical closed timelike curves, meaning paths that could return to the past.",
"Kurt Gödel discovered this solution in 1949 while studying Einstein's equations.",
"Einstein himself was interested in Gödel's ideas about time and the universe.",
"The solution shows that general relativity can create extremely strange universes.",
"A Gödel universe does not represent our actual universe, but it reveals possibilities of Einstein's theory."
],

"Fórmulas": [
"The Gödel metric contains terms that mix time and space, creating rotational effects.",
"The rotation of spacetime is represented by off-diagonal metric components.",
"Closed timelike curves appear because spacetime geometry allows unusual paths.",
"The solution requires a rotating universe filled with matter.",
"The metric shows that gravity can influence the structure of time itself.",
"Gödel's universe is one of the most unusual exact solutions of Einstein's equations."
],

"Easter Eggs": [
"Kurt Gödel was also one of the greatest logicians of the 20th century.",
"Gödel's incompleteness theorems changed the foundations of mathematics.",
"Einstein and Gödel often walked together at Princeton.",
"The possibility of time travel appears naturally in some solutions of relativity.",
"The universe described by Gödel is mathematically possible but probably not our own."
],

"Equações": [
{
    "name": "Christoffel Symbol⁰",
    "latex": fr"""
\Gamma^0_{{\mu\nu}} = {eeee}
"""
},

{
    "name": "Christoffel Symbol¹",
    "latex": fr"""
\Gamma^1_{{\mu\nu}} = {eeee1}"""
},
{
    "name": "Christoffel Symbol²",
    "latex": fr"""
    \Gamma^2_{{\mu\nu}} = {eeee2}"""
},
{
    "name": "Christoffel Symbol³",
    "latex": fr"""
    \Gamma^3_{{\mu\nu}} = {eeee3}"""
},
{
    "name": "Ricci Tensor",
    "latex": fr"""
R_{{\mu\nu}} = {ffff}"""
},
{
    "name": "Ricci Scalar",
    "latex": f"R = {gggg}"
},
{
    "name": "Einstein Tensor",
    "latex": fr"""
G_{{\mu\nu}} = {hhhh}"""
                }
            ]
        }
    }
}

METRIC_TEXT = {
"EN": {
        "Schwarzschild": {

            "what":
            "The Schwarzschild metric tells the universe how to behave in the presence of a massive object.",

            "how":
            "The universe responds by curving spacetime around the mass.",

            "latex": r"""
g_{\mu\nu}=
\begin{pmatrix}
-\left(1-\frac{2GM}{rc^2}\right) & 0 & 0 & 0\\
0 & \left(1-\frac{2GM}{rc^2}\right)^{-1} & 0 & 0\\
0 & 0 & r^2 & 0\\
0 & 0 & 0 & r^2\sin^2\theta
\end{pmatrix}
"""
        },


        "Kerr": {

            "what":
            "The Kerr metric describes how spacetime behaves around a rotating black hole.",

            "how":
            "Besides its mass curving spacetime, rotation causes frame dragging, an ergosphere and two event horizons.",

            "latex": r"""
g_{\mu\nu}=
\begin{pmatrix}
g_{00} & 0 & 0 & g_{03}\\
0 & g_{11} & 0 & 0\\
0 & 0 & g_{22} & 0\\
g_{30} & 0 & 0 & g_{33}
\end{pmatrix}
"""
        }

    }
}
