import mlflow
import argparse
import os
import logging
from src.utils.common import read_yaml, create_directories


STAGE = "MAIN"  # <<< change stage name

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'),
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
)


def main():
    # using mlflow to run all the stages
    # '.' - current working directory where mlproject resides
    with mlflow.start_run() as run:
       # mlflow.run(current_working_dir, entry_point, i_dont_want_to_use_another_condaenv)
        mlflow.run(".", "get_data", use_conda=False)
        mlflow.run(".", "base_model_creation", use_conda=False)
        # we can pass the parameters through mlflow.run
        # mlflow.run(".", "base_model_creation", parameters={key: value pair}, use_conda=False)

if __name__ == '__main__':

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main()
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e
