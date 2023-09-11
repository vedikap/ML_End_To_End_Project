import logging
import os
from datetime import datetime


LOG_FILE=f"log_{datetime.now().strftime('%m_%d_%Y:%H:%M:%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

#override default logging 
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

'''
if __name__=="__main__":
    logging.info("Testing Logger Functionality")
'''