
import afds

def adaptar(tipo, afd):
    delta_tuplas = {}
    for estado, transiciones in afd['delta'].items():
        for simbolo, destino in transiciones.items():
            delta_tuplas[(estado, simbolo)] = destino
    return (tipo, afd['estado_inicial'], delta_tuplas, set(afd['estados_aceptados']))

lista_afds=[
    # Palabras reservadas y tokens específicos
    adaptar("FOR", afds.afd_for),
    adaptar("ELSE", afds.afd_else),
    adaptar("RETURN", afds.afd_return),
    adaptar("PRINT", afds.afd_print),
    adaptar("READ", afds.afdread),
    adaptar("BOOLVAL", afds.afd_boolval),
    adaptar("ASSIGN", afds.afd_assign),
    #Resto de autómatas 
    adaptar("UNLOGOP", afds.afd_unlogop),
    adaptar("SEMICOL", afds.afd_semicol),
    adaptar("LBRACE", afds.afd_lbrace),
    adaptar("STR", afds.afdstr),
    adaptar("BINLOGOP", afds.afdbinlogop),
    adaptar("ADDOP", afds.afdaddop),
]

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
                    ultima_pos_aceptada = pos_lexema_actual

            if ultima_pos_aceptada > pos_actual:
                longitud_lexema_actual = ultima_pos_aceptada - pos_actual
                if longitud_lexema_actual > longitud_mejor_match: # principio maximal munch, lexema más largo gana
                                                                  # si son iguales, se mantiene el actual
                                                                  # por eso importa el orden en lista_afds
                    longitud_mejor_match = longitud_lexema_actual
                    tipo_mejor_match = tipo
                    lexema_mejor_match = codigo_fuente[pos_actual:ultima_pos_aceptada]

        if longitud_mejor_match == 0:
            raise ValueError(f"Carácter Inesperado en posición {pos_actual}")

        tokens.append((tipo_mejor_match, lexema_mejor_match))
        pos_actual += longitud_mejor_match

    tokens.append(("EOF", "EOF"))
    return tokens
