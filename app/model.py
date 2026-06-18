import mlflow.pyfunc

MODEL_PATH = "models/artifacts"
model = mlflow.pyfunc.load_model(MODEL_PATH)