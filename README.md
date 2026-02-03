# Sales-Model-Deployment
Sales Forecasting API with FastAPI &amp; Machine Learning

Sales Forecasting API with FastAPI & Machine Learning

This repository contains an end-to-end machine learning deployment for predicting sales using a trained regression model exposed via a FastAPI service. The project moves beyond model training and focuses on serving predictions in a production-style API, simulating a real-world business use case.

The model predicts sales based on key commercial drivers such as marketing spend, store size, and seasonal timing (month number). The trained model and feature schema are serialized with joblib and loaded at runtime to ensure consistency between training and inference.

The API exposes:
	•	A health check endpoint to verify service availability
	•	A /predict endpoint that accepts structured input via Pydantic and returns real-time sales predictions

This project demonstrates practical skills in:
	•	Machine learning inference pipelines
	•	Model serialization and reuse
	•	API design for data products
	•	Feature alignment between training and deployment
	•	FastAPI-based model serving

Built to reflect how machine learning models are actually deployed and consumed in production environments, not just trained in notebooks.
