import os
import logging
import azure.functions as func
from azure.storage.blob import BlobClient, BlobProperties, BlobType, ContentSettings


def main(destblob: func.InputStream):
    logging.info(f"SetDestinationContentType blob trigger function processed blob \n"
                 f"Name: {destblob.name}\n"
                 f"Blob Size: {destblob.length} bytes")

    blob_name = os.path.basename(destblob.name)
    default_default_blob_byte_type = "application/octet-stream"

    source_connection_string = os.environ["source_connection_string"]
    source_container_name = os.environ["source_container_name"]

    destination_connection_string = os.environ["destination_connection_string"]
    destination_container_name = os.environ["destination_container_name"]

    destination_client = BlobClient.from_connection_string(
        destination_connection_string,
        destination_container_name,
        blob_name)

    current_content_type = destination_client.get_blob_properties(
    ).content_settings.content_type

    if(current_content_type == default_blob_byte_type):
        logging.info(
            f"Blob has content-type '{default_blob_byte_type}'. Sourcing the content-type from {source_container_name}.")

        source_client = BlobClient.from_connection_string(
            source_connection_string,
            source_container_name,
            blob_name
        )

        source_properties = source_client.get_blob_properties()
        source_content_type = source_properties.content_settings.content_type

        logging.info(
            f"Setting content-type for {blob_name} in {destination_container_name} to {source_content_type}")

        destination_client.set_http_headers(
            content_settings=ContentSettings(content_type=source_content_type)
        )

        logging.info(f"Done setting content-type for {blob_name}")
    else:
        logging.info(
            f"Blob already has a content-type '{current_content_type}'. Exiting.")
