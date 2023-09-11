import sys
from src.logger import logging

def error_message_detail(exception_msg,sys_obj:sys):
    '''
    Function to get error details.
    It combines the error details tracked by sys library object and error message tracked by Exception class. 
    '''
    _,_,exc_tb=sys_obj.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message='Error occured in python script [{0}] line number [{1}] error message [{2}]'.format(file_name,exc_tb.tb_lineno,str(exception_msg))
    return error_message

class CustomException(Exception):
    def __init__(self,exception_msg,sys_obj:sys):
        super().__init__(exception_msg)
        self.error_message=error_message_detail(exception_msg,sys_obj)

    def __str__(self):
        return self.error_message
    
'''
if __name__=="__main__":

    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero.")
        raise CustomException(e,sys)
'''