from flask import Flask #Llamamos a Flask , render_template

Flask(__name__) #arranca aplicación

app = Flask (__name__)

@app.route("/") #"objeto app"
#Ruta para mi página principal
def home() :
        return  ("Hola Mundo")
    
@app.route("/about")#mi otra ruta
def about():
    return"Sobre Nosotros"


if __name__ =="__main__":
    app.run()