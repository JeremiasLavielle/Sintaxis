
# Analizador Léxico de Mini C

Este documento describe el propósito de cada archivo de prueba incluido para evaluar el analizador léxico. Los casos de prueba están divididos en **ejemplos válidos** (para comprobar que el lexer reconoce los tokens) y **ejemplos con errores** (para detectar fallos léxicos).

## Casos de Éxito

*   **ejemplo1.txt**,**ejemplo2.txt**, **ejemplo3.txt**, **ejemplo4.txt**: Se encargan de poner a prueba el funcionamiento de todos los tokens con diferentes ejemplos de codigos usuales.
*   **ejemplo5.txt**: Pone a prueba el token string, y asegura que palabras reservadas dentro de comillas no sean reconocidas como tokens individuales.
*   **ejemplo6.txt**: Verifica que los identificadores que contienen palabras reservadas como parte de su nombre sean reconocidos correctamente y no se dividan.
*   **ejemplo7.txt**: Pone a prueba el lexer en el caso de que varios tokens esten agrupados sin espacios en blanco de por medio.

## Casos de Error

*   **error1.txt**: Evalúa la detección de caracteres especiales no válidos dentro de un identificador.
*   **error2.txt**: Prueba el manejo de errores ante un string no cerrado.
*   **error3.txt**: Verifica el comportamiento ante operadores incompletos o mal escitos.
*   **error4.txt**: Pone a prueba la detección de numeros decimales mal escritos.