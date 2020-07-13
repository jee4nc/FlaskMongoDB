# Se importa flask desde la libreria
from flask import Flask

# Creamos una instancia del Framework Flask llamado "app"
app = Flask(__name__)

# Se crea la condicional la cual permite poder runear el programa
if __name__ == "__main__":
    app.run(debug=True)
