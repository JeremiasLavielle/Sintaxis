import pytest
from main import lexer_multiples_afds

archivos = [
    "Codigos_ejemplo/ejemplo1.txt",
    "Codigos_ejemplo/ejemplo2.txt",
    "Codigos_ejemplo/ejemplo3.txt",
    "Codigos_ejemplo/ejemplo4.txt",
    "Codigos_ejemplo/ejemplo5.txt",
    "Codigos_ejemplo/ejemplo6.txt",
    "Codigos_ejemplo/ejemplo7.txt",
    "Codigos_ejemplo/error1.txt",
    "Codigos_ejemplo/error2.txt",
    "Codigos_ejemplo/error3.txt",
    "Codigos_ejemplo/error4.txt"
]

@pytest.mark.parametrize("archivo", archivos)

def test_ejemplo(archivo):
    fuente = open(archivo, encoding="utf-8").read()
    tokens = lexer_multiples_afds(fuente)   # si el código no es válido, lanza error y falla
    print(f"\n--- {archivo} ---")
    for t in tokens:
        print("   ", t)
    assert tokens[-1] == ("EOF", "EOF")     # lo aceptó hasta el final