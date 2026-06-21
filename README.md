
# Analizador Léxico de Mini C

# Cambios al codigo base utilizado

Para construir el analizador, fue utilizado el codigo ejemplo brindado por la catedra para elaborar un lexer a traves de multiples AFDS. Sobre él se realizaron modificaciones para adaptarlo al caso de los tokens que planteamos.

A continuación, detallamos los cambios realizados:

## 1. Función de Adaptación de AFDs (`adaptar`)

El bucle principal (`lexer_multiples_afds`) esperaba que la función de transición de cada autómata (`delta`) estuviera formateada como un diccionario con tuplas como claves: `{(estado, simbolo): estado_siguiente}`. Sin embargo, por practicidad en la lectura del codigo (considerando en un futuro el desarrollo del parser), los autómatas se definieron como diccionarios anidados: `{estado: {simbolo: estado_siguiente}}`, en un archivo por separado.

Para solucionar esto se implementó la función `adaptar(tipo, afd)` que convierte el formato de nuestros AFDS al que espera el codigo.

En su funcionamiento, recorre el diccionario anidado del AFD original, Aplana las transiciones y genera el diccionario requerido, y devuelve la tupla que el bucle necesita: `(tipo, estado_inicial, delta_tuplas, set(estados_aceptados))`.

## 2. Orden de AFDS(`lista_afds`)

Se importaron los autómatas  desde afds.py.

Las palabras reservadas (`FOR`, `WHILE`, `IF`, etc.) se colocaron estrictamente antes que los tokens generales (como `ID`).

Si se lee la cadena `"while"`, tanto el autómata de la palabra reservada como el de identificadores devolverán un match de largo 5. Al estar `WHILE` primero en la lista y usarse un `>` en la condición `longitud_lexema_actual > longitud_mejor_match`, el lexer rompe el empate a favor de la palabra reservada.

## 3. Manejo de Caracteres en Blanco

El código base no contemplaba qué hacer con los espacios, saltos de línea o tabulaciones.

Para esto se definió un conjunto: `ESPACIOS = {' ', '\t', '\n', '\r'}`.

Al inicio del bucle principal, se agregó un condicional que evalua si el carácter actual es un espacio. De ser así, se incrementa el puntero `pos_actual` en 1 y se fuerza a la siguiente iteración con `continue`, ignorando el blanco pero avanzando la lectura.

## 4. Resolución de la lógica principal (Maximal Munch y Punteros)

Se reemplazaron todos los comentarios `# TO DO` con la implementación de la lógica de los autómatas, terminando el algoritmo de Maximal Munch:

1. **Registro de la última posición válida:**
    Cuando un estado es de aceptación, registramos hasta dónde leímos

   ```python
   if estado_actual in estados_aceptados:
       ultima_pos_aceptada = pos_lexema_actual
   ```

2. **Actualización del Token Ganador:**
    Si el lexema actual es el más largo encontrado hasta ahora, lo guardamos como el ganador
   ```python
   
   if longitud_lexema_actual > longitud_mejor_match: 
       longitud_mejor_match = longitud_lexema_actual
       tipo_mejor_match = tipo
       lexema_mejor_match = codigo_fuente[pos_actual:ultima_pos_aceptada]
   ```

3. **Avance del Puntero Principal:**
    Avanzamos el puntero global la cantidad exacta de caracteres que consumió el token ganador

   ```python
   
   pos_actual += longitud_mejor_match
   
   ```

# Pruebas

Se adjuntaron 11 archivos de prueba, los cuales están divididos en 7 **Casos de exito** (para comprobar que el lexer reconoce los tokens) y  4 **Casos de error** (para detectar fallos léxicos).

Tambien se añadio el archivo test_ejemplos.py, que utiliza la libreria pytest para realizar testing del codigo. En el caso de querer utilizarlo, es necesario instalar la libreria y ejecutar en terminal el comando "python -m pytest -v -s" o "python3 -m pytest -v -s", en la ruta de la carpeta de codigo. 

El codigo pasa el test en los casos de exito e imprime los pares token/lexema, y devuelve error en los casos de error.

A continuacion, detallamos cada caso de prueba:

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