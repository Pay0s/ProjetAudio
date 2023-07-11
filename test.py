import requests
import json
import pandas as pd

def send_data():
    url = 'http://127.0.0.1:5000/predict'

    col_name = [
        "before_exam_125_Hz",
        "before_exam_250_Hz",
        "before_exam_500_Hz",
        "before_exam_1000_Hz",
        "before_exam_2000_Hz",
        "before_exam_4000_Hz",
        "before_exam_8000_Hz"
    ]

    data = [45,75,90,84,86,33,119]  # Le tableau de données que vous souhaitez envoyer

    dfNewVal = pd.DataFrame([data], columns=col_name)

    # Converti le DataFrame en JSON
    json_data = dfNewVal.to_json(orient='records')

    # Défini les en-têtes de la requête
    headers = {'Content-Type': 'application/json'}

    # Envoye la requête POST avec le DataFrame
    response = requests.post(url, data=json_data, headers=headers)

    print(response.json())

if __name__ == '__main__':
    send_data()