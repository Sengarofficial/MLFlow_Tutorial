from src.Mlflow_Project import logger
from src.Mlflow_Project.config.configuration import ConfigurationManager
from src.Mlflow_Project.components.data_transformation import DataTransformation
from src.Mlflow_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Mlflow_Project.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from src.Mlflow_Project.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.Mlflow_Project.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline


STAGE_NAME = "Data ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()   # calling main method from DataIngestionTrainingPipeline class through data_ingestion object
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    config = ConfigurationManager()
    data_transformation_config = config.get_data_transformation_config()
    data_transformation = DataTransformation(config = data_transformation_config)  
    data_transformation.train_test_split()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise e 




STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
