from bson import ObjectId
import flask
from mongoApi import Mongo
from flask import render_template, render_template_string, request, jsonify



app = flask.Flask(__name__)

mongo = Mongo("Coop_Taxi")

@app.route('/', methods=['GET'])
def home():
    try:
        socios = mongo.find_all("Socio", {})
        socios = list(socios)
        unidades = mongo.find_all("Unidad", {})
        unidades = list(unidades)

        return render_template('index.html', socios=socios, unidades=unidades)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return render_template('index.html', socios=socios, unidades=unidades)



@app.route('/delete_socio/<string:socio_id>', methods=['DELETE'])
def delete_socio(socio_id):
    try:
        try:
            obj_id = ObjectId(socio_id)
        except Exception as ex:
            raise ValueError(f"Invalid ObjectId format: {socio_id}") from ex

        mongo.delete("Socio", {"_id": obj_id})
        
        return render_template_string("<h3>Socio eliminado correctamente</h3>")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return render_template_string("<h3>Ha ocurrido un error</h3>")
    


@app.route('/add_socio', methods=['POST'])
def add_socio():
    try:
        socio = request.form.to_dict()
        socio['Direccion'] = {
            "Sector": socio["Sector"],
            "CallePrincipal": socio["CallePrincipal"],
            "CalleSecundaria": socio["CalleSecundaria"],
            "Numero": socio["Numero"],
        }

        del socio["Sector"]
        del socio["CallePrincipal"]
        del socio["CalleSecundaria"]
        del socio["Numero"]

      
        mongo.insert("Socio", socio)
        return render_template_string("<h3>Socio agregado correctamente</h3>")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return render_template_string("<h3>Ha ocurrido un error</h3>")
    


@app.route('/update_socio', methods=['POST'])
def update_socio():
    try:
        socio = request.form.to_dict()
        socio['Direccion'] = {
            "Sector": socio["Sector"],
            "CallePrincipal": socio["CallePrincipal"],
            "CalleSecundaria": socio["CalleSecundaria"],
            "Numero": socio["Numero"],
        }
        obj_id = ObjectId(socio["_id"])
        del socio["Sector"]
        del socio["CallePrincipal"]
        del socio["CalleSecundaria"]
        del socio["Numero"]
        del socio["_id"]

        res = mongo.update("Socio", {"_id": obj_id}, {"$set": socio})
        return render_template_string(f" {res} <h3>Socio actualizado correctamente: id-> {obj_id}</h3>")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return render_template_string("<h3>Ha ocurrido un error</h3>")
 



if __name__ == '__main__':
    app.run(debug=True)