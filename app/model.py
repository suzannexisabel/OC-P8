import mlflow.pyfunc

MODEL_PATH = "models/artifacts"
model = mlflow.sklearn.load_model(MODEL_PATH)