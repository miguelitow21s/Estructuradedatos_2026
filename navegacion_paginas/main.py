from pagina import Pagina
from navegador import Navegador

nav = Navegador()

# Visitar paginas
nav.visitar(Pagina("google.com"))
nav.visitar(Pagina("youtube.com"))
nav.visitar(Pagina("github.com"))

# Retroceder
nav.atras()   # github -> youtube
nav.atras()   # youtube -> google
nav.adelante() # google -> youtube
nav.adelante() # youtube -> github
nav.adelante() # no hay siguiente
