from networksecurity.components.Data_ingestion import DataIngestion
from networksecurity.components.Data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
import sys
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.Data_transformation import DataTranformation

from networksecurity.entity.config_entity import ModelTrainerConfig
from networksecurity.components.model_trainer import ModelTrainer



if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)

        logging.info("Initiate the data ingestion")

        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation completed")
        print(dataingestionartifact)


        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)

        logging.info("Initiate Data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)

        DataTransformationConfig = DataTransformationConfig(trainingpipelineconfig)
        logging.info("data Transformation started")
        data_transformation = DataTranformation(data_validation_artifact,DataTransformationConfig)
        data_transformation_artifact = data_transformation.initiate_data_transformation()

        print(data_transformation_artifact)
        logging.info("data transformation completed")

        logging.info("Model Training started")
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer  = ModelTrainer(model_trainer_config,data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")
        
        

    except Exception as e:
           raise NetworkSecurityException(e,sys)