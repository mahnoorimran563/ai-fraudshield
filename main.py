from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI()

# Load the trained model
model = joblib.load("fraud_model.pkl")

# Mount static folder (for CSS, JS, index.html, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve static index.html from /static/
@app.get("/")
def serve_index():
    return FileResponse("static/index.html")

# Define expected input schema
class Transaction(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

# API endpoint for fraud prediction
@app.post("/predict")
def predict(transaction: Transaction):
    # Order of input features
    features = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
    input_data = [transaction.dict()[key] for key in features]

    # Predict
    prediction = model.predict(np.array(input_data).reshape(1, -1))
    is_fraud = bool(prediction[0])

    return {
        "isFraud": is_fraud,
        "message": "⚠️ Fraudulent Transaction Detected" if is_fraud else "✅ Transaction is Safe"
    }

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
