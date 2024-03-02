# Temperaturas diarias en varias ciudades: 3 ciudades, 7 dias a la semanana y 4 semanas
temperaturas = [
    # Semana 1
    [
             # Ciudad 1
        [[22, 23, 25, 22, 21, 24, 23],  # Temperaturas de Lunes a Domingo
         [21, 23, 22, 21, 20, 21, 23],
         [25, 24, 26, 23, 22, 25, 24],
         [23, 22, 25, 24, 26, 23, 22]],
        # Ciudad 2
        [[21, 23, 22, 21, 20, 21, 23],
         [19, 18, 20, 17, 18, 19, 21],
         [20, 22, 21, 20, 19, 20, 22],
         [22, 21, 20, 19, 20, 22, 21]],
        # Ciudad 3
        [[19, 18, 20, 17, 18, 19, 21],
         [20, 19, 18, 17, 18, 20, 19],
         [22, 23, 25, 22, 21, 24, 23],
         [20, 19, 18, 17, 18, 20, 19]]
    ],
    # Semana 2
    [
        # Ciudad 1
        [[24, 23, 23, 22, 25, 24, 25],
         [26, 23, 22, 25, 24, 26, 23],
         [24, 26, 23, 22, 25, 24, 26],
         [26, 23, 22, 25, 24, 26, 23]],
        # Ciudad 2
        [[22, 21, 20, 19, 20, 22, 21],
         [21, 20, 19, 20, 22, 21, 20],
         [22, 21, 20, 19, 20, 22, 21],
         [21, 20, 19, 20, 22, 21, 20]],
        # Ciudad 3
        [[20, 19, 18, 17, 18, 20, 19],
         [19, 18, 17, 19, 20, 19, 18],
         [20, 19, 18, 17, 18, 20, 19],
         [19, 17, 17, 18, 20, 17, 18]]
    ],
    # Semana 3
    [
        # Ciudad 1
        [[23, 22, 25, 24, 26, 23, 22],
         [19, 18, 20, 17, 18, 19, 21],
         [23, 22, 25, 24, 26, 23, 22],
         [22, 25, 24, 26, 23, 22, 25]],
        # Ciudad 2
        [[21, 23, 22, 21, 20, 21, 23],
         [20, 22, 21, 20, 19, 20, 22],
         [19, 20, 22, 21, 20, 19, 20],
         [20, 22, 21, 20, 19, 20, 22]],
        # Ciudad 3
        [[17, 18, 20, 19, 18, 17, 18],
         [18, 20, 19, 18, 17, 18, 20],
         [17, 18, 20, 19, 18, 17, 18],
         [18, 20, 19, 18, 17, 18, 20]]
    ],
    # Semana 4
    [
        # Ciudad 1
        [[24, 26, 23, 22, 25, 24, 26],
         [26, 23, 22, 25, 24, 26, 23],
         [24, 26, 23, 22, 25, 24, 26],
         [26, 23, 22, 25, 24, 26, 23]],
        # Ciudad 2
        [[22, 21, 20, 19, 20, 22, 21],
         [21, 20, 19, 20, 22, 21, 20],
         [22, 21, 20, 19, 20, 22, 21],
         [21, 20, 19, 20, 22, 21, 20]],
        # Ciudad 3
        [[20, 19, 18, 17, 18, 20, 19],
         [19, 18, 17, 18, 20, 19, 18],
         [20, 19, 18, 17, 18, 20, 19],
         [22, 23, 25, 22, 21, 24, 23]]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad por semana
for semana, semana_temperaturas in enumerate(temperaturas, start=1):
    print(f"Semana {semana}:")
    for ciudad, ciudad_temperaturas in enumerate(semana_temperaturas, start=1):
        suma_temperaturas = 0
        for dia_temperaturas in ciudad_temperaturas:
            suma_temperaturas += sum(dia_temperaturas)
        promedio_temperaturas = suma_temperaturas / (len(ciudad_temperaturas) * len(dia_temperaturas))
        print(f"  Ciudad {ciudad}: Promedio de temperaturas = {promedio_temperaturas:.2f}")
