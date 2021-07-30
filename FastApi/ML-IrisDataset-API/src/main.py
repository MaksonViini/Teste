from fastapi import FastAPI, Depends, requests
import pickle
from basemodel import Iris


app = FastAPI()


def get_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model


model = get_model()


@app.post('/')
def get_prediction(details: Iris):
    features = details.dict()
    pred = model.predict([[
        features['sepal_length'], features['sepal_width'], features['petal_length'], features['petal_width'],
    ]]).tolist()[0]

    return {'Valor predito': str(pred)}
