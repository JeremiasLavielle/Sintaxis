# Ejemplo de Lexer Basado en un múltiples AFDs
# ============================================

# Notas:
# ------
# - Este código es una idea de implementación, no puede correrse pues como no sabemos
# el lenguaje para el cuál fue diseñado, no tenemos entrada disponible para el argumento
# de entrada 'codigo_fuente'
# - Ni tampoco disponemos de todos los tipos de tokens.

# Importante:
# -----------
# Para que este código funcione, debemos tener los AFDs que representan a cada uno de los tokens,
# o importarlos desde otro archivo
# En cada uno requerimos:
# - 'tipo': clase de token que reconoce dicho autómata
# - 'delta': dict[(estado, simbolo): estado_siguiente]
# - 'estados_aceptados': list[int]
# - 'estado_inicial': int


# Construimos una lista de tuplas (puede ser una lista de listas, diccionarios, etc)
# con todos los autómatas, con el siguiente formato para cada elemento de la lista:
# (tipo, estado_inicial, delta, estados_aceptados)
lista_afds = [
    ("PALABRA_RESERVADA_1", 0, {(0, 'i'): 1, ...}, {3, 7}),
    ("PALABRA_RESERVADA_2", 0, {(0, 'B'): 3, ...}, {4, 8}),
    # ...etc
    ("ID",      0, {(0, 'a'): 1, ...}, {5}),
    ("NUMERO",  0, {(0, '1'): 1, ...}, {9}),
    # ... etc
]
# MUY IMPORTANTE: EL ORDEN EN QUE SE COLOCAN LOS AFDS EN lista_afds DETERMINA QUE TIPO
# DE TOKEN SE SELECCIONA CUANDO UN LEXEMA VERIFICA MÁS DE UNO, ES DECIR, SE USA PARA ROMPER
# EMPATES.
# EN GENERAL LAS PALABRAS RESERVADAS TOMAN PRECEDENCIA, POR ESO EL ORDEN SUGERIDO.

def lexer_multiples_afds(codigo_fuente):
    tokens = []
    pos_actual = 0
    n = len(codigo_fuente)

    while pos_actual < n: # recorremos todos los caracteres del código fuente
        longitud_mejor_match = 0
        tipo_mejor_match = None
        lexema_mejor_match = ''

        for afd in lista_afds: # en este ciclo interno, alimentamos el lexema actual a todos los afds
            tipo, estado_inicial, delta, estados_aceptados = afd
            estado_actual = estado_inicial
            pos_lexema_actual = pos_actual # por cada afd, comenzamos desde la posición actual en el código fuente
                                           # después del último token aceptado
            ultima_pos_aceptada =-1

            while pos_lexema_actual < n:
                clave = (estado_actual, codigo_fuente[pos_lexema_actual])
                if clave not in delta:
                    break # salimos por el estado trampa
                estado_actual = delta[clave]
                pos_lexema_actual += 1 # avanzamos hasta llegar al estado trampa del afd actual
                if estado_actual in estados_aceptados:
                    ultima_pos_aceptada = # TO DO --> ajustar apropiadamente

            if ultima_pos_aceptada > pos_actual:
                longitud_lexema_actual = ultima_pos_aceptada - pos_actual
                if longitud_lexema_actual > longitud_mejor_match: # principio maximal munch, lexema más largo gana
                                                                  # si son iguales, se mantiene el actual
                                                                  # por eso importa el orden en lista_afds
                    longitud_mejor_match = # TO DO --> Asignar apropiadamente
                    tipo_mejor_match = # TO DO --> Asignar apropiadamente
                    lexema_mejor_match = # TO DO --> Seleccionar lexema a guardar

        if best_longitud_lexema_actual == 0:
            raise ValueError(f"Carácter Inesperado en posición {pos_actual}")

        tokens.append((tipo_mejor_match, lexema_mejor_match))
        pos_actual += # TO DO --> Ajustar nueva posición actual apropiadamente

    tokens.append(("EOF", "EOF"))
    return tokens
