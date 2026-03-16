# -------------------------
# Ejercicio 1
# -------------------------
"""
T(n) = 2T(n/2) + n

# Identificar los valores
a = 2   
b = 2   
g(n) = Θ(n)  

# Sacar k
g(n) = Θ(n^k)
Como n = n^1
k = 1

# Calcular α
α = log_b(a)
α = log_2(2) = 1

# Comparar α con k
α = 1
# k = 1
Entonces α = k

# Se aplica el caso del Teorema Maestro
Si α = k, se usa el Caso 2

# Resultado final
# T(n) = Θ(n^k log n)
# T(n) = Θ(n log n)
"""

# -------------------------
# Ejercicio 2
# -------------------------
"""
T(n) = 4T(n/2) + n²

# Identificar los valores
a = 4
b = 2
g(n) = Θ(n²)

# Sacar k
g(n) = Θ(n^k)
Como n² = n^2
k = 2

# Calcular α
α = log_b(a)
α = log_2(4) = 2

# Comparar α con k
α = 2
k = 2
Entonces α = k

# Se aplica el caso del Teorema Maestro
Si α = k, se usa el Caso 2

# Resultado final
T(n) = Θ(n^k log n)
T(n) = Θ(n² log n)
"""
# -------------------------
# Ejercicio 3
# -------------------------
"""
T(n) = 3T(n/3) + n

# Identificar los valores
a = 3
b = 3
g(n) = Θ(n)

# Sacar k
g(n) = Θ(n^k)
Como n = n^1
k = 1

# Calcular α
α = log_b(a)
α = log_3(3) = 1

# Comparar α con k
α = 1
k = 1
Entonces α = k

# Se aplica el caso del Teorema Maestro
Si α = k, se usa el Caso 2

# Resultado final
T(n) = Θ(n^k log n)
T(n) = Θ(n log n)
"""
# -------------------------
# Ejercicio 4
# -------------------------
"""
T(n) = 5T(n/2) + n³

# Identificar los valores
a = 5
b = 2
g(n) = Θ(n³)

# Sacar k
g(n) = Θ(n^k)
Como n³ = n^3
k = 3

# Calcular α
α = log_b(a)
α = log_2(5) ≈ 2.32

# Comparar α con k
α ≈ 2.32
k = 3
Entonces α < k

# Se aplica el caso del Teorema Maestro
Si α < k, se usa el Caso 3

# Resultado final
T(n) = Θ(n^k)
T(n) = Θ(n³)
"""

# -------------------------
# Ejercicio 5
# -------------------------
"""
T(n) = 7T(n/4) + n²

# Identificar los valores
a = 7
b = 4
g(n) = Θ(n²)

# Sacar k
g(n) = Θ(n^k)
Como n² = n^2
k = 2

# Calcular α
α = log_b(a)
α = log_4(7) ≈ 1.40

# Comparar α con k
α ≈ 1.40
k = 2
Entonces α < k

# Se aplica el caso del Teorema Maestro
Si α < k, se usa el Caso 3

# Resultado final
T(n) = Θ(n^k)
T(n) = Θ(n²)
"""
# -------------------------
# PARTE 2
# -------------------------

# -------------------------
# Ejercicio 6
# -------------------------
"""
T(n) = T(n-1) + n

# Identificar los valores
a = 1
c = 1
g(n) = Θ(n)

# Sacar k
g(n) = Θ(n^k)
Como n = n^1
k = 1

# Aplicar el teorema de recurrencias sustractivas
Si a = 1 → T(n) = Θ(n^(k+1))

# Sustituir k
T(n) = Θ(n^(1+1))

# Resultado final
T(n) = Θ(n²)
"""
# -------------------------
# Ejercicio 7
# -------------------------
"""
T(n) = T(n-2) + n²

# Identificar los valores
a = 1
c = 2
g(n) = Θ(n²)

# Sacar k
g(n) = Θ(n^k)
Como n² = n^2
k = 2

# Aplicar el teorema de recurrencias sustractivas
Si a = 1 → T(n) = Θ(n^(k+1))

# Sustituir k
T(n) = Θ(n^(2+1))

# Resultado final
T(n) = Θ(n³)
"""
# -------------------------
# Ejercicio 8
# -------------------------
"""
T(n) = T(n-1) + log n

# Identificar los valores
a = 1
c = 1
g(n) = Θ(log n)

# Observación
Este teorema se aplica cuando g(n) = Θ(n^k), k ≥ 0
Pero log n no tiene la forma n^k

# Desarrollo por expansión
T(n) = T(n-1) + log n
T(n-1) = T(n-2) + log(n-1)
T(n-2) = T(n-3) + log(n-2)
...
T(1) = c

# Sumando todo
T(n) = c + log 2 + log 3 + ... + log n

# Propiedad de logaritmos
log 2 + log 3 + ... + log n = log(n!)

# Usando la aproximación de Stirling
log(n!) = Θ(n log n)

# Resultado final
T(n) = Θ(n log n)
"""
# -------------------------
# Ejercicio 9
# -------------------------
"""
T(n) = T(n-3) + n³

# Identificar los valores
a = 1
c = 3
g(n) = Θ(n³)

# Sacar k
g(n) = Θ(n^k)
Como n³ = n^3
k = 3

# Aplicar el teorema de recurrencias sustractivas
Si a = 1 → T(n) = Θ(n^(k+1))

# Sustituir k
T(n) = Θ(n^(3+1))

# Resultado final
T(n) = Θ(n⁴)
"""
# -------------------------
# Ejercicio 10
# -------------------------
"""
T(n) = T(n-2) + n log n

# Identificar los valores
a = 1
c = 2
g(n) = Θ(n log n)

# Observación
Este teorema se aplica cuando g(n) = Θ(n^k), k ≥ 0
Pero n log n no es exactamente de la forma n^k

# Desarrollo por expansión
T(n) = T(n-2) + n log n
T(n-2) = T(n-4) + (n-2) log(n-2)
T(n-4) = T(n-6) + (n-4) log(n-4)
...

# Sumando todo
T(n) = c + n log n + (n-2) log(n-2) + (n-4) log(n-4) + ...

# Análisis del crecimiento
Hay aproximadamente n/2 términos
y el tamaño dominante de los términos es del orden de n log n

# Entonces
T(n) = Θ(n² log n)

# Resultado final
T(n) = Θ(n² log n)
"""
# =========================================================
# PARTE 3: ALGORITMOS DE DIVIDE Y VENCERÁS
# =========================================================


# -------------------------
# Ejercicio 1
# -------------------------
"""
Problema:
Calcular la suma de los elementos de un arreglo usando Divide y Vencerás.

Idea:
- Si el arreglo tiene un solo elemento, esa es la suma.
- Si tiene varios, se divide en dos mitades.
- Se suma recursivamente la mitad izquierda y la mitad derecha.
- Luego se combinan ambas sumas.

Recurrencia:
T(n) = 2T(n/2) + Θ(1)

Explicación:
- Se hacen 2 llamadas recursivas sobre mitades del arreglo.
- Combinar consiste solo en sumar dos resultados, eso cuesta Θ(1).

Aplicando Teorema Maestro:
a = 2
b = 2
g(n) = Θ(1)
k = 0

α = log_b(a)
α = log_2(2) = 1

Comparación:
α > k
1 > 0

Caso 1:
T(n) = Θ(n^α)

Resultado final:
T(n) = Θ(n)
"""

# -------------------------
# Ejercicio 2
# -------------------------
"""
Problema:
Encontrar el máximo y el mínimo de un arreglo usando Divide y Vencerás.

Idea:
- Si hay un solo elemento, ese elemento es máximo y mínimo.
- Si hay dos, se comparan directamente.
- Si hay más, se divide el arreglo en dos mitades.
- Se obtiene (min, max) de cada mitad.
- Luego se combinan comparando los mínimos y los máximos.

Recurrencia:
T(n) = 2T(n/2) + Θ(1)

Explicación:
- Se resuelve recursivamente cada mitad.
- Combinar cuesta Θ(1), porque solo se hacen pocas comparaciones.

Aplicando Teorema Maestro:
a = 2
b = 2
g(n) = Θ(1)
k = 0

α = log_b(a)
α = log_2(2) = 1

Comparación:
α > k
1 > 0

Caso 1:
T(n) = Θ(n^α)

Resultado final:
T(n) = Θ(n)

Comparación con el método iterativo:
- El enfoque iterativo también es Θ(n)
- Divide y Vencerás no mejora el orden asintótico
- Pero sí ofrece una solución recursiva elegante
"""
# -------------------------
# Ejercicio 3
# -------------------------
"""
Problema:
Multiplicar dos números grandes usando Divide y Vencerás
(por ejemplo, con el algoritmo de Karatsuba).

Idea:
- Se dividen los números en dos mitades.
- En vez de hacer 4 multiplicaciones como el método clásico,
  Karatsuba hace 3 multiplicaciones recursivas.
- Luego combina los resultados.

Recurrencia:
T(n) = 3T(n/2) + Θ(n)

Explicación:
- Hay 3 multiplicaciones recursivas sobre números de tamaño n/2.
- El trabajo extra para sumar, restar y combinar cuesta Θ(n).

Aplicando Teorema Maestro:
a = 3
b = 2
g(n) = Θ(n)
k = 1

α = log_b(a)
α = log_2(3) ≈ 1.585

Comparación:
α > k
1.585 > 1

Caso 1:
T(n) = Θ(n^α)

Resultado final:
T(n) = Θ(n^log_2(3))
T(n) ≈ Θ(n^1.585)
"""
# -------------------------
# Ejercicio 4: Potenciación rápida
# -------------------------
"""
Problema:
Calcular a^b usando Divide y Vencerás.

Idea:
- Si b = 0, el resultado es 1.
- Si b es par:
      a^b = (a^(b/2))^2
- Si b es impar:
      a^b = a * (a^((b-1)/2))^2

Recurrencia:
T(n) = T(n/2) + Θ(1)

Explicación:
- Solo hay 1 llamada recursiva.
- El trabajo extra es constante.

Aplicando Teorema Maestro:
a = 1
b = 2
g(n) = Θ(1)
k = 0

α = log_b(a)
α = log_2(1) = 0

Comparación:
α = k
0 = 0

Caso 2:
T(n) = Θ(n^k log n)

Resultado final:
T(n) = Θ(log n)

Comparación con el método ingenuo:
- Método ingenuo: Θ(n)
- Potenciación rápida: Θ(log n)

Mejora:
- Reduce muchísimo la cantidad de multiplicaciones
"""
# -------------------------
# Ejercicio 5: Ordenación con Merge Sort
# -------------------------
"""
Problema:
Ordenar un arreglo usando Merge Sort.

Idea:
- Dividir el arreglo en dos mitades.
- Ordenar recursivamente cada mitad.
- Mezclar las dos mitades ordenadas.

Recurrencia:
T(n) = 2T(n/2) + Θ(n)

Explicación:
- Hay 2 llamadas recursivas.
- Mezclar las dos mitades cuesta Θ(n).

Aplicando Teorema Maestro:
a = 2
b = 2
g(n) = Θ(n)
k = 1

α = log_b(a)
α = log_2(2) = 1

Comparación:
α = k
1 = 1

Caso 2:
T(n) = Θ(n^k log n)

Resultado final:
T(n) = Θ(n log n)
"""
# -------------------------
# Ejercicio 6: Multiplicación de matrices con Strassen
# -------------------------
"""
Problema:
Multiplicar matrices usando el algoritmo de Strassen.

Idea:
- Una matriz se divide en 4 submatrices.
- Strassen reduce el número de multiplicaciones recursivas de 8 a 7.
- Luego combina los resultados con sumas y restas de matrices.

Recurrencia:
T(n) = 7T(n/2) + Θ(n²)

Explicación:
- Hay 7 multiplicaciones recursivas.
- El trabajo extra para sumar y combinar matrices cuesta Θ(n²).

Aplicando Teorema Maestro:
a = 7
b = 2
g(n) = Θ(n²)
k = 2

α = log_b(a)
α = log_2(7) ≈ 2.807

Comparación:
α > k
2.807 > 2

Caso 1:
T(n) = Θ(n^α)

Resultado final:
T(n) = Θ(n^log_2(7))
T(n) ≈ Θ(n^2.807)
"""
# -------------------------
# Ejercicio 7: Búsqueda en una matriz ordenada
# -------------------------
"""
Problema:
Buscar un número en una matriz n x n donde filas y columnas
están ordenadas ascendentemente.

Idea:
Hay varias soluciones posibles. Una opción clásica eficiente es:
- Empezar en la esquina superior derecha
- Si el número actual es mayor que el buscado, mover a la izquierda
- Si es menor, mover hacia abajo
- Repetir hasta encontrarlo o salir de la matriz

Complejidad:
Tarda como máximo n + n pasos

Resultado final:
T(n) = Θ(n)

Observación:
- Esto ya es subcuadrático porque mejora a Θ(n²)
- Aunque el enunciado pide Divide y Vencerás, en muchos cursos
  aceptan esta solución por ser más simple y eficiente

Si se exige una formulación recursiva de Divide y Vencerás:
- Se puede dividir la matriz y descartar regiones
- Pero el análisis es más complejo
- La solución práctica más conocida sigue siendo Θ(n)
"""
"""
Ejercicio 1: Suma de un arreglo
T(n) = 2T(n/2) + Θ(1)
Resultado: Θ(n)

Ejercicio 2: Máximo y mínimo
T(n) = 2T(n/2) + Θ(1)
Resultado: Θ(n)

Ejercicio 3: Karatsuba
T(n) = 3T(n/2) + Θ(n)
Resultado: Θ(n^log_2(3)) ≈ Θ(n^1.585)

Ejercicio 4: Potenciación rápida
T(n) = T(n/2) + Θ(1)
Resultado: Θ(log n)

Ejercicio 5: Merge Sort
T(n) = 2T(n/2) + Θ(n)
Resultado: Θ(n log n)

Ejercicio 6: Strassen
T(n) = 7T(n/2) + Θ(n²)
Resultado: Θ(n^log_2(7)) ≈ Θ(n^2.807)

Ejercicio 7: Búsqueda en matriz ordenada
Resultado: Θ(n)
"""