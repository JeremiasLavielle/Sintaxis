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
    'estados': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'delta': {
        0: {'t': 1, 'f': 5},
        1: {'r': 2},
        2: {'u': 3},
        3: {'e': 4},
        4: {},
        5: {'a': 6},
        6: {'l': 7},
        7: {'s': 8},
        8: {'e': 9},
        9: {},
    },
    'estados_aceptados': [4, 9],
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

afd_for = {
    'tipo_token': 'for',
    'estado_inicial': 0,
    'alfabeto': ['f', 'o', 'r'],
    'estados': [0, 1, 2, 3],
    'delta': { 
        0: {'f': 1},
        1: {'o': 2},
        2: {'r': 3},
        3: {} 
    },
    'estados_aceptados': [3]
}

afd_else = {
    'tipo_token': 'else',
    'estado_inicial': 0,
    'alfabeto': ['e', 'l', 's'], 
    'estados': [0, 1, 2, 3, 4],
    'delta': { 
        0: {'e': 1},
        1: {'l': 2},
        2: {'s': 3},
        3: {'e': 4},
        4: {} 
    },
    'estados_aceptados': [4]
}

afd_return = {
    'tipo_token': 'return',
    'estado_inicial': 0,
    'alfabeto': ['r', 'e', 't', 'u', 'n'],
    'estados': [0, 1, 2, 3, 4, 5, 6],
    'delta': { 
        0: {'r': 1},
        1: {'e': 2},
        2: {'t': 3},
        3: {'u': 4},
        4: {'r': 5},
        5: {'n': 6},
        6: {} 
    },
    'estados_aceptados': [6]
}

afd_print = {
    'tipo_token': 'print',
    'estado_inicial': 0,
    'alfabeto': ['p', 'r', 'i', 'n', 't'],
    'estados': [0, 1, 2, 3, 4, 5],
    'delta': { 
        0: {'p': 1},
        1: {'r': 2},
        2: {'i': 3},
        3: {'n': 4},
        4: {'t': 5},
        5: {} 
    },
    'estados_aceptados': [5]
}

afd_lbrace = {
    'tipo_token': 'lbrace',
    'estado_inicial': 0,
    'alfabeto': ['{'],
    'estados': [0, 1],
    'delta': { 
        0: {'{': 1},
        1: {} 
    },
    'estados_aceptados': [1]
}

afdstr = {
    "tipo_token": "str",
    "estado_inicial": 0,
    "alfabeto": "UTF-8",
    "estados": [0, 1, 2],
    "delta": {  
        0: {"'": 1},
        1: {"cualquiera": 1,"'":2},
        2: {},
    },
    "estados_aceptados": [2]
}

afdread = {
    "tipo_token": "read",
    "estado_inicial": 0,
    "alfabeto": ["r","e","a","d" ],
    "estados": [0, 1, 2, 3, 4],
    "delta": {  
        0: {"r": 1},
        1: {"e": 2},
        2: {"a": 3},
        3: {"d": 4},
        4: {},
    },
    "estados_aceptados": [4]
}

afdbinlogop = {
    "tipo_token": "binlogop",
    "estado_inicial": 0,
    "alfabeto": ["&","|" ],
    "estados": [0, 1, 2, 3],
    "delta": { 
        0: {"&": 1,"|":2},
        1: {"&": 3},
        2: {"|": 3},
    },
    "estados_aceptados": [3]
}

afdaddop = {
    "tipo_token": "addop",
    "estado_inicial": 0,
    "alfabeto": ["+","-" ],
    "estados": [0, 1],
    "delta": { 
        0: {"+": 1,"-":1},
    },
    "estados_aceptados": [1]
}