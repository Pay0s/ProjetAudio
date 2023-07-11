import pandas as pd
import os
from flask import Flask, request, jsonify, render_template
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
from pathlib import Path

app = Flask(__name__)
bootstrap_project(Path.cwd())

def save_from_post_request(request, filepath):
        data = request.json # Récupère les données JSON de la requête POST
        with open(filepath, "w") as file: json.dump(data, file) # Sauvegarde les données dans le fichier JSON

@app.route('/')
def home():
    
    return render_template('index.html')

# prédiction du modèle avec de nouvelle donnée
@app.route("/predict", methods=["POST"])
def predict():

    col_name = [
            "before_exam_125_Hz",
            "before_exam_250_Hz",
            "before_exam_500_Hz",
            "before_exam_1000_Hz",
            "before_exam_2000_Hz",
            "before_exam_4000_Hz",
            "before_exam_8000_Hz"
        ]
    data = request.get_json()

    # Vérifier si des données ont été reçues
    if data is None:
        return jsonify({'error': 'No data provided'}), 400

    try:
        # Convertir les données en DataFrame
        dfNewVal = pd.DataFrame(data)

        # Sauvegarde des données dans un fichier CSV
        dfNewVal.to_csv("data/05_model_input/value_user_input.csv", index=False)

        with KedroSession.create("projetaudio", project_path=".") as session:
            session.run(pipeline_name="apiV2")

        output = pd.read_csv('data/05_model_input/user_post_denormalize.csv')
        output.columns = col_name

        return output.to_json(orient='records')

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Pour entrainer le modèle
@app.route("/train", methods=["GET"])
def train():

    with KedroSession.create("projetaudio", project_path=".") as session:
        session.run(pipeline_name="entrainement")

        # Retournez un message de succès
        message = "L'entrainement du modele est termine avec succes"
        status = 200
        headers = {'Content-Type': 'text/plain'}

        return message, status, headers

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

