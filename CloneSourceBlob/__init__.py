import os
import logging
import azure.functions as func


def main(srcblob: func.InputStream,
         outputblob: func.Out[func.InputStream]):
    logging.info(f"CloneSourceBlob blob trigger function processed blob \n"
                 f"Name: {srcblob.name}\n"
                 f"Blob Size: {srcblob.length} bytes")

    logging.info("Set output blob")

    outputblob.set(srcblob)

    logging.info(f"done")
