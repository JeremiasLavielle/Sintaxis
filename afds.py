import string

letras = list(string.ascii_letters)
digitos = list(string.digits)
guion = ['_']
 
# q0: una letra o _ lleva a q1
delta_id_q0 = {c: 1 for c in letras + guion}
# q1: letra, digito o _ vuelve a q1 (auto-bucle)
delta_id_q1 = {c: 1 for c in letras + digitos + guion}
 
afd_id = {
    'estado_inicial': 0,
    'alfabeto': letras + digitos + guion,
    'estados': [0, 1],
    'delta': {
        0: delta_id_q0,
        1: delta_id_q1,
    },
    'estados_aceptados': [1],
}

afd_boolval = {
    'estado_inicial': 0,
    'alfabeto': ['t', 'r', 'u', 'e', 'f', 'a', 'l', 's'],
    'estados': [0, 1, 2, 3, 4, 5, 6, 7, 8],
    'delta': {
        0: {'t': 1, 'f': 5},
        1: {'r': 2},
        2: {'u': 3},
        3: {'e': 4},
        4: {},
        5: {'a': 6},
        6: {'l': 7},
        7: {'s': 8},
        8: {'e': 4},
    },
    'estados_aceptados': [4],
}

afd_assign = {
    'estado_inicial': 0,
    'alfabeto': ['='],
    'estados': [0, 1],
    'delta': {
        0: {'=': 1},
        1: {},
    },
    'estados_aceptados': [1],
}

afd_unlogop = {
    'estado_inicial': 0,
    'alfabeto': ['!'],
    'estados': [0, 1],
    'delta': {
        0: {'!': 1},
        1: {},
    },
    'estados_aceptados': [1],
}

afd_semicol = {
    'estado_inicial': 0,
    'alfabeto': [';'],
    'estados': [0, 1],
    'delta': {
        0: {';': 1},
        1: {},
    },
    'estados_aceptados': [1],
}