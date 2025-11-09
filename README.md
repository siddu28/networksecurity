### Network Security Project
🚀 MLOps Pipeline Workflow
This project is built as an end-to-end MLOps pipeline that automates data ingestion, validation, transformation, model training, and deployment. Each stage is a distinct component that creates artifacts used by the next step

### Project Flow

<img width="1363" height="427" alt="Image" src="https://github.com/user-attachments/assets/b1f43dbf-1c31-4435-bde0-7d2957ad935f" />

#### file Structure

```
├── Dockerfile
├── Network_Data
│   └── phisingData.csv
├── README.md
├── app.py
├── data_schema
│   └── schema.yaml
├── final_models
│   ├── model.pkl
│   └── preprocessing.pkl
├── main.py
├── networksecurity
│   ├── __init__.py
│   ├── cloud
│   │   └── __init__.py
│   ├── components
│   │   ├── Data_ingestion.py
│   │   ├── Data_transformation.py
│   │   ├── Data_validation.py
│   │   ├── __init__.py
│   │   └── model_trainer.py
│   ├── constants
│   │   ├── __init__.py
│   │   └── training_pipeline
│   │       └── __init__.py
│   ├── entity
│   │   ├── __init__.py
│   │   ├── artifact_entity.py
│   │   └── config_entity.py
│   ├── exception
│   │   ├── __init__.py
│   │   └── exception.py
│   ├── logging
│   │   ├── __init__.py
│   │   └── logger.py
│   ├── pipeline
│   │   ├── __init__.py
│   │   ├── batch_prediction.py
│   │   └── training_pipeline.py
│   └── utils
│       ├── __init__.py
│       ├── main_utils
│       │   ├── __init__.py
│       │   └── utils.py
│       └── ml_utils
│           ├── __init__.py
│           ├── metric
│           │   ├── __init__.py
│           │   └── classification_metric.py
│           └── model
│               ├── __init__.py
│               └── estimator.py
├── notebooks
├── prediction_output
│   └── output.csv
├── push_data.py
├── requirements.txt
├── setup.py
├── templates
│   └── table.html
├── test_mongodb.py
└── valid_data
    └── test.csv
```

## Steps followed during this project:

1. 📥 Data Ingestion
- The pipeline begins by extracting data from the source.
- Source: Data is pulled from a MongoDB database.
- Process:
The Data Ingestion Component exports the specified collection to a "feature store" as a raw CSV file.
Based on a provided schema, unnecessary columns are dropped.
The cleaned data is then split into train.csv and test.csv files.

- Output: A Data Ingestion Artifact  is created, which contains the paths to the raw train.csv and test.csv files.


<img width="1112" height="755" alt="Image" src="https://github.com/user-attachments/assets/255ea843-dbc0-45bf-8367-a25ce7e38716" />



2. ✅ Data Validation
- This step ensures the quality and integrity of the ingested data before any processing.
- Input: The Data Ingestion Artifact (the train.csv and test.csv files).
- Process:
Schema Validation: The Data Validation Component checks if the data matches the expected schema (e.g., correct number of columns , data types , and presence of all numerical columns ).
Data Drift Detection: It checks for significant changes in the data's distribution compared to a baseline. This is crucial for catching "model drift" before it happens.

- Output: A Data Validation Artifact is generated, which includes a status report and a drift report. If validation fails, the pipeline stops.


<img width="1331" height="835" alt="Image" src="https://github.com/user-attachments/assets/9786b402-522f-4913-9bd8-0e20f5bc250e" />


3. 🛠️ Data Transformation
- Once validated, the raw data is preprocessed and made ready for model training.
- Input: The validated train.csv and test.csv files from the Data Validation Artifact.
- Process:
A data transformation Pipeline is created , which includes steps for Handling Missing Values.
KNN Imputer is used to fill in missing (NAN) values.
Robust Scaler  is applied to scale the features.
This pipeline is fit-transformed on the training data and transformed on the test data.

- Output: A Data Transformation Artifact is produced, containing the transformed data as numpy arrays (train.npy, test.npy) and the saved preprocessing.pkl object.


<img width="1039" height="858" alt="Image" src="https://github.com/user-attachments/assets/481553e8-e18a-4f1f-969d-7c45035c6904" />


4. 🧠 Model Trainer
- This component uses the preprocessed data to train and select the best-performing model.
- Input: The Data Transformation Artifact (specifically the train.npy and test.npy arrays).
- Process:
The numpy arrays are loaded and split into X_train, y_train, X_test, and y_test.
A Model Factory is used to train multiple models and find the best one.
The best model's score is compared against a pre-defined expected accuracy threshold.
If the model meets the threshold, it is saved as model.pkl.

- Output: A Model Trainer Artifact is created, which contains the final model.pkl and a metric artifact  with its performance details.


<img width="886" height="869" alt="Image" src="https://github.com/user-attachments/assets/5b28cd7d-d3ba-49c7-bf4a-5cc2520cef75" />


5. 📈 Model Evaluation
- The newly trained model is now compared against the model that is currently in production (if one exists).
- Input: The Model Trainer Artifact.
- Process: The Model Evaluation Component  assesses the new model. If its performance is better than the production model (or meets the acceptance criteria), it is marked as Model Accepted.

- Output: If "Yes", the pipeline proceeds to the final step. If "No", the pipeline stops, and the old model remains in production.


6. ➡️ Model Pusher & Deployment
- Once a model is accepted, it is pushed to a central location for deployment.
- Process: The Model Pusher Component takes the accepted model artifacts and pushes them to a production location, such as a cloud bucket on AWS or Azure.
- CI/CD Deployment:
The entire "Network Security" application (including the API) is containerized into a Docker Image.
This image is pushed to AWS ECR (Elastic Container Registry).
- A GitHub Actions CI/CD pipeline automatically detects this new image, pulls it, and deploys it to a service like AWS EC2 or App Runner, making the new model available to users.
