from src.Mlflow_Project import logger
from src.Mlflow_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()   # calling main method from DataIngestionTrainingPipeline class through data_ingestion object
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e 



