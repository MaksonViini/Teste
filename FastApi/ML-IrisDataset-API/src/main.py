from fastapi import FastAPI, Depends
import pickle


app = FastAPI()

def get_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = get_model()

@app.get('/{pred}')
def get_prediction(pred: float):
    return model.predict([[pred]])
