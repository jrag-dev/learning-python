"""
    Programa que muestra como convertir en mayúsculas y minúsculas
"""

s = "Erre con erre guitarra"
print("Original: ", s)

s_lower = s.lower()
print("Lowercase: ", s_lower)

s_upper = s.upper()
print("Uppercase: ", s_upper)

# verificar si una palabra se encuentra en una cadena

is_content = "erre" in s
print(is_content)

is_content = "a" in s
print(is_content)

# verificar palabra en una cadena usando not in

s = "Juan compró un auto"

is_content = "juan" not in s.lower()
print(is_content)

# contar las ocurrencias de una letra o palabra en una cadena de caracteres

t = "un tigre, dos tigres, se están comiendo a otro tigre. el otro tigre es como un gatito."

palabra = "tigre"
count_content = t.count(palabra)
print("La parabra %s aparece %s veces." % (palabra, count_content))