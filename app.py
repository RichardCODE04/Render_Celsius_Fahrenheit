from flask import Flask, jsonify, render_template
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Cargar el modelo
modelo = tf.keras.models.load_model('C:\\Users\\Lenovo\\Desktop\\Proyecto1_Artificial\\modelo_c2f.h5')
print("Modelo cargado desde 'modelo_c2f.h5'")

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/IA/<float:celsius>', methods=['GET'])
def IA(celsius):
    # Ajustar la forma de la entrada para la predicción
    input_data = np.array([[celsius]], dtype=np.float32)
    # Realizar la predicción
    prediction = modelo.predict(input_data)
    fahrenheit_value = float(prediction[0][0])  
    # Convertir a float estándar de Python
    response = {
        'celsius': celsius,
        'fahrenheit': fahrenheit_value
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)