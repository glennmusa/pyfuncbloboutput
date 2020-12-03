import logging

import azure.functions as func


def main(myblob: func.InputStream,
         outputblob: func.Out[func.InputStream]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    outputblob.set(myblob)
