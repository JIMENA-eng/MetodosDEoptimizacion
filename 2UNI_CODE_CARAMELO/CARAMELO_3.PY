import random
from collections import Counter

DULCES = {'limon', 'huevo', 'pera'}

def generar_jugadores(n):
    return {f'J{i+1}': [random.choice(list(DULCES)) for _ in range(2)] for i in range(n)}

def simular(jugadores):
    estado = {j: {'dulces': d[:], 'sobrevive': False, 'movs': []} for j, d in jugadores.items()}
    cambios, ronda, movs = True, 0, []

    while cambios and ronda < 20:
        cambios, ronda = False, ronda + 1
        inventario = Counter(d for j in estado.values() for d in j['dulces'])

        for j, info in estado.items():
            if info['sobrevive']: continue
            tiene, necesita = set(info['dulces']), list(DULCES - set(info['dulces']))
            if not necesita:
                info['sobrevive'] = True
                dulce = min(inventario, key=inventario.get)
                info['dulces'].append(dulce)
                movs.append(f"{j} ya tenía trío y recibe comodín '{dulce}'")
                cambios = True
                continue

            prestamistas = []
            for d in necesita:
                for pj, pi in estado.items():
                    if pj != j and d in pi['dulces'] and (pi['dulces'].count(d) > 1 or not pi['sobrevive']):
                        prestamistas.append((pj, d))
                        break

            if len(prestamistas) >= len(necesita):
                for pj, d in prestamistas[:len(necesita)]:
                    estado[pj]['dulces'].remove(d)
                    info['dulces'].append(d)
                    movs.append(f"{pj} presta '{d}' a {j}")
                info['sobrevive'] = True
                cambios = True

                # Devolver comodín
                for pj, _ in prestamistas[:len(necesita)]:
                    faltante = list(DULCES - set(estado[pj]['dulces']))
                    devolver = faltante[0] if faltante else min(inventario, key=inventario.get)
                    estado[pj]['dulces'].append(devolver)
                    movs.append(f"{j} devuelve comodín '{devolver}' a {pj}")
    return estado, movs

def main():
    n = random.randint(5, 7)
    jugadores = generar_jugadores(n)
    print("=== SIMULACIÓN DE DULCES ===\n")
    print(f"Jugadores: {n} | Mayoría necesaria: {(n+1)//2}\n--- INICIAL ---")
    for j, d in jugadores.items():
        falta = DULCES - set(d)
        print(f"{j}: {d} -> {'✓ YA SOBREVIVE' if not falta else f'✗ necesita {list(falta)}'}")
    estado, movs = simular(jugadores)
    print("\n--- MOVIMIENTOS ---")
    for i, m in enumerate(movs, 1): print(f"{i}. {m}")
    print("\n--- RESULTADO FINAL ---")
    vivos = 0
    for j, info in estado.items():
        falta = DULCES - set(info['dulces'])
        print(f"{j}: {info['dulces']} -> {'✓ SOBREVIVE' if info['sobrevive'] else f'✗ necesita {list(falta)}'}")
        vivos += info['sobrevive']
    print("\n--- RESUMEN ---")
    print(f"Supervivientes: {vivos}/{n}")
    m = (n+1)//2
    print(f"{'🎉 ÉXITO' if vivos >= m else '⚠️ FALTAN'} | Eficiencia: {vivos/n*100:.1f}%")

if __name__ == "__main__":
    main()