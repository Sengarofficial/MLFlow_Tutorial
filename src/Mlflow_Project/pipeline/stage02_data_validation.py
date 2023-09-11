from src.Mlflow_Project.entity.config_entity import DataIngestionConfig, DataValidationConfig
from src.Mlflow_Project.config.configuration import ConfigurationManager
from src.Mlflow_Project.components.data_ingestion import DataIngestion
from src.Mlflow_Project.components.data_validation import DataValidation
from src.Mlflow_Project import logger 


STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass 

    def main(self):

        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_columns()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e 
    