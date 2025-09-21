### Network Security Project

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
