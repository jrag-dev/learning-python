"""
    Separación de cadenas de caracteres
"""

s = "un tigre, dos tigres, tres tigres"

s_list = s.split(",")
print(s_list)

s_list2 = s.split(" ")
print(s_list2)

# Cuando se tienen varias líneas de texto
p = "Una lineal\nOtra línea de texto\ny una más"
p_list = p.splitlines()
print(p_list)

# usando rsplit para remover caracteres y crear una nueva lista
m = "un tigre, dos tigres, tres tigres"

m_list = m.rsplit("t")
print(m_list)