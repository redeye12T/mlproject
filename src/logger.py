import logging
import os
from datetime import datetime


LOGE_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),'logs')
os.makedirs(log_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(log_path,LOGE_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    level=logging.INFO,


)
print("RUNNING:", __file__)
print("CWD:", os.getcwd())
print("LOG PATH:", LOG_FILE_PATH)


if __name__=="__main__":
    logging.info("Logging has start")



