

def sad(trajectory1, trajectory2, grid_size):
  """
  Calcula la distancia SAD entre dos trayectorias.

  Args:
      trajectory1: Una lista de coordenadas (x, y) que representan la primera trayectoria.
      trajectory2: Una lista de coordenadas (x, y) que representan la segunda trayectoria.
      grid_size: El tamaño de las celdas de la cuadrícula.

  Returns:
      La distancia SAD entre las dos trayectorias.
  """

  # Discretizar las trayectorias en una cuadrícula
  grid1 = discretize(trajectory1, grid_size)
  grid2 = discretize(trajectory2, grid_size)

  # Convertir las cuadrículas a secuencias de palabras espaciales
  words1 = grid_to_words(grid1)
  words2 = grid_to_words(grid2)

  # Calcular la distancia de Levenshtein entre las secuencias de palabras
  distance = levenshtein_distance(words1, words2)

  return distance

def discretize(trajectory, grid_size):
  """
  Discretiza una trayectoria en una cuadrícula.

  Args:
      trajectory: Una lista de coordenadas (x, y) que representan la trayectoria.
      grid_size: El tamaño de las celdas de la cuadrícula.

  Returns:
      Una lista de listas, donde cada sublista representa una celda de la cuadrícula
      visitada por la trayectoria.
  """

  grid = []
  for x, y in trajectory:
    i = int(y // grid_size)
    j = int(x // grid_size)
    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
      grid[i][j] = True
    else:
      # Manejar puntos fuera de la cuadrícula (opcional)
      pass
  return grid

def grid_to_words(grid):
  """
  Convierte una cuadrícula en una secuencia de palabras espaciales.

  Args:
      grid: Una lista de listas, donde cada sublista representa una celda de la cuadrícula.

  Returns:
      Una lista de palabras espaciales.
  """

  words = []
  for row in grid:
    for cell in row:
      if cell:
        words.append((row, col))
  return words

def levenshtein_distance(s1, s2):
  """
  Calcula la distancia de Levenshtein entre dos cadenas.

  Args:
      s1: La primera cadena.
      s2: La segunda cadena.

  Returns:
      La distancia de Levenshtein entre las dos cadenas.
  """

  m = len(s1)
  n = len(s2)

  # Matriz de distancias
  d = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

  # Inicializar la matriz
  for i in range(m + 1):
    d[i][0] = i
  for j in range(n + 1):
    d[0][j] = j

  # Calcular las distancias
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if s1[i - 1] == s2[j - 1]:
        cost = 0
      else:
        cost = 1
      d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost)

  return d[m][n]