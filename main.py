from textSummarizer.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_2_data_validation import DatavalidationTrainingPipeline
from textSummarizer.pipeline.stage_3_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"----- stage {STAGE_NAME} started ------")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"----- stage {STAGE_NAME} completed ------ \n \nx======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"----- stage {STAGE_NAME} started ------")
    data_validation = DatavalidationTrainingPipeline()
    data_validation.main()
    logger.info(f"----- stage {STAGE_NAME} completed ------ \n \nx======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"------ stage {STAGE_NAME} started-----")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"----- stage {STAGE_NAME} completed ------ \n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e



