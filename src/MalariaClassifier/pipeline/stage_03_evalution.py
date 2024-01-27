from MalariaClassifier import logger
from MalariaClassifier.config.configuration import ConfigurationManager
from MalariaClassifier.components.model_evalutation import Evaluation 

STAGE_NAME = "Model Evalution Stage"
class EvaluationPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f"\n\n >>>>>>>>>> The {STAGE_NAME} has started >>>>>>>>>>>>")
        eval_config = EvaluationPipeline()
        eval_config.main()
        logger.info(f" >>>>>>>>>> The {STAGE_NAME} has completed succefully >>>>>>>>>>>>\n\n ===========")
    except Exception as e:
        logger.exception(e)
        raise e
