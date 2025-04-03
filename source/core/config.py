import os

# Configuración de Selenium
SELENIUM_OPTIONS = [
    "--headless",
    "--disable-gpu",
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
]

# Configuraciones de scraping
LIMITE_CATEGORIAS = 1      # Limita la cantidad de categorías (None para todas)
LIMITE_PAGINAS = 1          # Número de páginas por categoría
LIMITE_PRODUCTOS = 1      # Número de productos por página
SHOW_FEEDBACK = True       # Mostrar mensajes de avance

# URLs y paths
BASE_URL = "https://es.openfoodfacts.org"
CATEGORIAS_URL = BASE_URL + "/facets/categorias"

# Output
BASE_DIR = os.path.join(os.path.dirname(__file__))
CSV_DIR =  os.path.abspath(os.path.join(BASE_DIR, '..', '..', 'dataset'))
LOG_DIR =  os.path.abspath(os.path.join(BASE_DIR, '..', 'output'))

# Asegurar que existen directorios dataset y output
os.makedirs(CSV_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# Paths
CSV_FILENAME = os.path.join(CSV_DIR, 'scraped_products.csv')
LOG_FILENAME = os.path.join(LOG_DIR, 'errores.log')
