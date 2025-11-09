### Network Security Project
🚀 MLOps Pipeline Workflow
This project is built as an end-to-end MLOps pipeline that automates data ingestion, validation, transformation, model training, and deployment. Each stage is a distinct component that creates artifacts used by the next step

#### Project Structure

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
