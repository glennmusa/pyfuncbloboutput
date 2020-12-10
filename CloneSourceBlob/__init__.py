import os
import logging
import azure.functions as func


def main(srcblob: func.InputStream,
         destblob: func.Out[func.InputStream]):
    logging.info(f"CloneSourceBlob blob trigger function processed blob \n"
                 f"Name: {srcblob.name}\n"
                 f"Blob Size: {srcblob.length} bytes")

    blob_name = os.path.basename(srcblob.name)
    destination_container_name = os.environ["destination_container_name"]

    logging.info(
        f"Moving {blob_name} to {destination_container_name}...")

    destblob.set(srcblob)

    logging.info(
        f"Complete. {blob_name} copied to {destination_container_name}.")
