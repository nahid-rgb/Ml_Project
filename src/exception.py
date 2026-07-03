# Imports the sys module.
# Used to access sys.exc_info(), which returns details
# about the current exception (type, object, traceback).
import sys
import logging

def error_message_detail(error, error_detail: sys):
    # Generates a detailed error message.
    # error        -> Original exception object.
    # error_detail -> sys module.

    _, _, exc_tb = error_detail.exc_info()
    # exc_info() returns:
    # (Exception Type, Exception Object, Traceback)
    # We only need the traceback.

    file_name = exc_tb.tb_frame.f_code.co_filename
    # Gets the filename where the exception occurred.

    error_message = (
        "Error occurred in python script name [{0}] "
        "line number [{1}] "
        "error message [{2}]"
    ).format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )
    # Creates a formatted error message using:
    # • File name
    # • Line number
    # • Original exception message

    return error_message
    # Returns the formatted error message.


class CustomException(Exception):
    # Custom exception class.
    # Inherits from Exception to provide enhanced error details.

    def __init__(self, error_message, error_detail: sys):
        # Runs automatically when:
        # raise CustomException(error, sys)

        super().__init__(error_message)
        # Initializes the parent Exception class.

        self.error_message = error_message_detail(
            error_message,
            error_detail=error_detail
        )
        # Calls error_message_detail().
        # error_message -> error
        # error_detail  -> error_detail
        # Stores the returned formatted message in:
        # self.error_message

    def __str__(self):
        # Called automatically when the exception is printed
        # or converted to a string (print(e), str(e)).

        return self.error_message
        # Returns the custom formatted error message.



      