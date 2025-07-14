import random
from collections import Counter

DULCES = ['limon', 'huevo', 'pera']

def generar_jugadores(n):
    """Genera n jugadores con 2 dulces aleatorios cada uno"""
    return {f'J{i+1}': [random.choice(DULCES) for _ in range(2)] for i in range(n)}

def calcular_supervivientes_matematico(inventario):
    """Calcula el número máximo de supervivientes usando el método matemático"""
    # Paso 1: Contar dulces por tipo
    contador = Counter(inventario)
    
    # Paso 2: Calcular grupos iniciales posibles
    min_dulces = min(contador[dulce] for dulce in DULCES)
    grupos_iniciales = min_dulces // 2
    
    # Paso 3: Calcular dulces usados y restantes
    dulces_usados = grupos_iniciales * 6  # 6 dulces por grupo (2 de cada tipo)
    dulces_restantes = sum(contador.values()) - dulces_usados
    
    # Paso 4: Calcular comodines generados
    comodines = grupos_iniciales * 2
    
    # Paso 5: Calcular supervivientes adicionales
    total_disponible = dulces_restantes + comodines
    supervivientes_adicionales = total_disponible // 6
    
    # Resultado final
    total_supervivientes = grupos_iniciales + supervivientes_adicionales
    
    return {
        'grupos_iniciales': grupos_iniciales,
        'dulces_usados': dulces_usados,
        'dulces_restantes': dulces_restantes,
        'comodines': comodines,
        'supervivientes_adicionales': supervivientes_adicionales,
        'total_supervivientes': total_supervivientes,
        'distribucion': dict(contador)
    }

def formar_grupos_optimizado(jugadores):
    """Forma grupos de supervivientes de manera optimizada"""
    # Recolectar todos los dulces
    todos_dulces = []
    for dulces in jugadores.values():
        todos_dulces.extend(dulces)
    
    # Calcular supervivientes matemáticamente
    resultado = calcular_supervivientes_matematico(todos_dulces)
    
    # Simular la formación de grupos
    contador = Counter(todos_dulces)
    movimientos = []
    supervivientes = []
    
    # Formar grupos iniciales
    for i in range(resultado['grupos_iniciales']):
        grupo = []
        for dulce in DULCES:
            for _ in range(2):  # 2 de cada tipo
                grupo.append(dulce)
                contador[dulce] -= 1
        
        superviviente = f"Grupo_{i+1}"
        supervivientes.append(superviviente)
        movimientos.append(f"Formado {superviviente}: {grupo}")
    
    # Generar comodines
    comodines_disponibles = []
    for i in range(resultado['comodines']):
        # Elegir comodín del dulce más escaso restante
        dulce_comodin = min(contador, key=contador.get)
        comodines_disponibles.append(dulce_comodin)
        contador[dulce_comodin] += 1
        movimientos.append(f"Generado comodín: '{dulce_comodin}'")
    
    # Formar grupos adicionales con dulces restantes + comodines
    dulces_restantes = []
    for dulce, cantidad in contador.items():
        dulces_restantes.extend([dulce] * cantidad)
    
    grupos_adicionales = len(dulces_restantes) // 6
    for i in range(grupos_adicionales):
        grupo = dulces_restantes[i*6:(i+1)*6]
        superviviente = f"Grupo_Extra_{i+1}"
        supervivientes.append(superviviente)
        movimientos.append(f"Formado {superviviente}: {grupo}")
    
    return supervivientes, movimientos, resultado

def asignar_supervivientes_a_jugadores(jugadores, total_supervivientes):
    """Asigna supervivientes a jugadores basado en sus dulces iniciales"""
    # Calcular puntaje de cada jugador (más variedad = mejor oportunidad)
    puntajes = {}
    for jugador, dulces in jugadores.items():
        variedad = len(set(dulces))
        contador = Counter(dulces)
        balance = min(contador.values())
        puntajes[jugador] = variedad * 10 + balance
    
    # Ordenar por puntaje descendente
    jugadores_ordenados = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
    
    # Asignar supervivientes
    supervivientes = []
    for i in range(min(total_supervivientes, len(jugadores_ordenados))):
        supervivientes.append(jugadores_ordenados[i][0])
    
    return supervivientes

def simular_matematico(jugadores):
    """Simulación usando el método matemático optimizado"""
    # Recolectar todos los dulces
    todos_dulces = []
    for dulces in jugadores.values():
        todos_dulces.extend(dulces)
    
    # Calcular resultado matemático
    resultado = calcular_supervivientes_matematico(todos_dulces)
    
    # Formar grupos y obtener movimientos
    grupos, movimientos, detalle = formar_grupos_optimizado(jugadores)
    
    # Asignar supervivientes a jugadores reales
    supervivientes_reales = asignar_supervivientes_a_jugadores(jugadores, resultado['total_supervivientes'])
    
    return supervivientes_reales, movimientos, resultado

def main():
    print("=== SIMULACIÓN MATEMÁTICA DE SUPERVIVENCIA ===\n")
    
    # Generar jugadores
    jugadores = generar_jugadores(12)
    
    # Análisis inicial
    todos_dulces = [dulce for dulces in jugadores.values() for dulce in dulces]
    contador_inicial = Counter(todos_dulces)
    
    print("--- ESTADO INICIAL ---")
    print(f"Jugadores: {len(jugadores)}")
    print(f"Distribución: {dict(contador_inicial)}")
    print(f"Total dulces: {sum(contador_inicial.values())}")
    
    print("\n--- JUGADORES INDIVIDUALES ---")
    for jugador, dulces in jugadores.items():
        contador = Counter(dulces)
        print(f"{jugador}: {dulces} -> {dict(contador)}")
    
    # Calcular supervivientes matemáticamente
    resultado = calcular_supervivientes_matematico(todos_dulces)
    
    print("\n--- CÁLCULO MATEMÁTICO ---")
    print(f"Dulce más escaso: {min(resultado['distribucion'], key=resultado['distribucion'].get)} ({min(resultado['distribucion'].values())} unidades)")
    print(f"Grupos iniciales posibles: {resultado['grupos_iniciales']}")
    print(f"Dulces usados: {resultado['dulces_usados']}")
    print(f"Dulces restantes: {resultado['dulces_restantes']}")
    print(f"Comodines generados: {resultado['comodines']}")
    print(f"Total disponible: {resultado['dulces_restantes'] + resultado['comodines']}")
    print(f"Supervivientes adicionales: {resultado['supervivientes_adicionales']}")
    print(f"TOTAL SUPERVIVIENTES: {resultado['total_supervivientes']}")
    
    # Simular formación de grupos
    supervivientes, movimientos, _ = simular_matematico(jugadores)
    
    print(f"\n--- PROCESO DE FORMACIÓN ({len(movimientos)} pasos) ---")
    for i, mov in enumerate(movimientos, 1):
        print(f"{i}. {mov}")
    
    print(f"\n--- RESULTADO FINAL ---")
    print(f"Supervivientes seleccionados: {supervivientes}")
    
    for jugador in jugadores:
        if jugador in supervivientes:
            print(f"{jugador}: {jugadores[jugador]} -> ✓ SOBREVIVE")
        else:
            print(f"{jugador}: {jugadores[jugador]} -> ✗ No sobrevive")
    
    print(f"\n--- RESUMEN ---")
    print(f"Supervivientes: {len(supervivientes)}/{len(jugadores)} ({len(supervivientes)/len(jugadores)*100:.1f}%)")
    print(f"Eficiencia: {len(supervivientes) * 6}/{sum(contador_inicial.values())} dulces = {len(supervivientes) * 6 / sum(contador_inicial.values()) * 100:.1f}%")
    
    # Mostrar fórmula
    print(f"\n--- FÓRMULA APLICADA ---")
    print(f"Supervivientes = min(dulces) ÷ 2 + (restantes + comodines) ÷ 6")
    print(f"Supervivientes = {min(resultado['distribucion'].values())} ÷ 2 + ({resultado['dulces_restantes']} + {resultado['comodines']}) ÷ 6")
    print(f"Supervivientes = {resultado['grupos_iniciales']} + {resultado['supervivientes_adicionales']} = {resultado['total_supervivientes']}")

def test_multiples_distribuciones():
    """Prueba diferentes distribuciones para verificar el algoritmo"""
    print("\n=== PRUEBA DE DIFERENTES DISTRIBUCIONES ===")
    
    distribuciones_test = [
        [8, 8, 8],
        [10, 7, 7],
        [12, 6, 6],
        [14, 5, 5],
        [16, 4, 4],
        [6, 9, 9]
    ]
    
    for i, dist in enumerate(distribuciones_test, 1):
        todos_dulces = []
        for j, cantidad in enumerate(dist):
            todos_dulces.extend([DULCES[j]] * cantidad)
        
        resultado = calcular_supervivientes_matematico(todos_dulces)
        print(f"Distribución {i}: {dict(zip(DULCES, dist))} -> {resultado['total_supervivientes']} supervivientes")

if __name__ == "__main__":
    main()
    test_multiples_distribuciones()