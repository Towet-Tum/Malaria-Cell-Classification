from MalariaClassifier import logger 
from MalariaClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from MalariaClassifier.pipeline.stage_02_training import TrainingPipeline
from MalariaClassifier.pipeline.stage_03_evalution import EvaluationPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"\n\n >>>>>>>>>> The {STAGE_NAME} has started >>>>>>>")
    ingest = DataIngestionPipeline()
    ingest.main()
    logger.info(f">>>>>>>>>>>> The {STAGE_NAME} has completed succefully >>>>>>>>> \n\n ================")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training Stage"
try:
    logger.info(f"\n\n >>>>>>>>>> The {STAGE_NAME} has started >>>>>>>")
    train = TrainingPipeline()
    train.main()
    logger.info(f">>>>>>>>>>>> The {STAGE_NAME} has completed succefully >>>>>>>>> \n\n ================")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f"\n\n >>>>>>>>>> The {STAGE_NAME} has started >>>>>>>>>>>>")
    eval_config = EvaluationPipeline()
    eval_config.main()
    logger.info(f" >>>>>>>>>> The {STAGE_NAME} has started >>>>>>>>>>>>\n\n ===========")
except Exception as e:
    logger.exception(e)
    raise e