# Implementación de algoritmo para la resolución de Sudoku
## Problemática
Sudoku es un juego matemático que consta de una matrix de 9x9, subdividida en 9 matrices más pequeñas de 3x3. Algunas celdas de dicha matriz contienen números del 1 al 9, mientras que otras se encuentran vacías. La finalidad del juego es ubicar 9 veces cada número del 1 al 9, respetando reglas específicas:
* Cada número no puede repetirse en la misma fila
* Cada número no puede repetirse en la misma columna
* Cada número no puede repetirse en la misma sub-matriz de 3x3

La cantidad de celdas vacías en la disposición inicial de la matriz determinará la dificultad del Sudoku.
## Solución
Se plantea la como solución la implementación de un algoritmo que reciba cualquier matriz que represente una jugada de Sudoku y devuelva dicha matriz completa respetando las reglas establecidas en el juego. Dada la dificultad del juego, se plantean dos posibles enfoques que deberá abarcar el algoritmo:
* Enfoque iterativo para sudokus simples – Se calcularán de manera iterativa los posibles valores para cada celda vacía de la matriz- Siempre y cuando exista dentro de las celdas vacías, alguna en donde sólo un número puede ser ubicado, estas serán completadas con dicho número. Luego de completar estas celdas, se procederá nuevamente a calcular los posibles valores para cada celda, ya que luego de completar una o más celdas vacías, existe la posibilidad de que luego de analizar, celdas en las que más de un número podía ser ubicado hayan descartado posibilidades.
*	Enfoque recursivo para sudokus complejos – Se establece como “sudoku complejo” a aquel en que, en algún punto de la ejecución del algoritmo y luego de analizar los posibles valores para cada celda, ninguna de ellas tiene un solo valor posible. Ante este caso, el algoritmo deberá “elegir” un valor posible de alguna de las celdas vacías y ubicarlo en la matriz. Luego de esto, se “intentará” resolver el sudoku resultante llamando de manera recursiva al mismo algoritmo. En caso de que la llamada recursiva no pueda resolver el sudoku (generalmente esto se identifica cuando existen celdas en las que no se puede ubicar ningún número), la llamada inicial descartará el valor con el que se “intentó”, y realizará lo mismo con otro de los valores posibles de la celda elegida.

## Descripción técnica - Funciones dentro del código
```Python
def valueexists(array, number)
```
  * Busca de manera lineal, un número dentro de un array. 
    * array: El array donde se desea realizar la búsqueda.
    * number: El número que se desea buscar dentro del array.
```Python
def validatesudoku(sudoku)
```
  * Valida que todas las celdas en un sudoku completo tengan valores correctos.
    * sudoku: El sudoku que se quiere validar.
```Python
def getpossiblevalues(sudoku, row, column)
```
  * Dado el sudoku, se indica una fila y columna para devolver todos los posibles valores que pueden ingresarse en la intersección.
    * sudoku: El sudoku que se quiere validar.
    * row: La fila donde se encuetnra la celda para la que se quieren conocer los valores posibles.
    * column: La columna donde se encuetnra la celda para la que se quieren conocer los valores posibles.
```Python
def getallemptycells(sudoku)
```
  * Dado el sudoku, se devuelve un array con todas las celdas vacías (aquellas que están marcadas con -1) y los valores posibles de dichas celdas.
    * sudoku: El sudoku para el que se quieren conocer las celdas vacías y sus valores posibles.
```Python
def merge(a, b)
```
  * Dados dos array ordenados de forma ascendente, devuelve un array con todos los valores ordenados.
    * a: El primer array a ordenar.
    * b: El segundo array a ordenar.
```Python
def sort(array)
```
  * Dado un array, devuelve el mismo con todos sus valores ordenados de forma ascendente. (MergeSort)
    * array: El array que se desea ordenar.
```Python
def solvesudoku(sudoku)
```
  * Dado un sudoku representado como un array de dos dimensiones, devuelve el mismo resuelto aplicacndo las reglas y limitaciones del juego. Las celdas vacías deben estar representadas con el número entero -1.
    * sudoku: El sudoku que se desea resolver.
