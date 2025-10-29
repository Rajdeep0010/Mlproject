import sys


def error_message_details(error, error_detail:sys):
    
    _,_,exc_tb=error_detail.exc.info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error occur in python script name [{0}] line number [{1}] error message [{2}]"
    file_name, exc_tb.tb_lineno, str(error)
    
    