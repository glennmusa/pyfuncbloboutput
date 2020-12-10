import os
import logging
import azure.functions as func
from azure.storage.blob import BlobClient, BlobProperties, BlobType, ContentSettings


def main(destblob: func.InputStream):
    logging.info(f"SetDestinationContentType blob trigger function processed blob \n"
                 f"Name: {destblob.name}\n"
                 f"Blob Size: {destblob.length} bytes")

    source_connection_string = os.environ["source_connection_string"]
    source_container_name = os.environ["source_container_name"]
    source_blob_name = os.path.basename(destblob.name)

    destination_connection_string = os.environ["destination_connection_string"]
    destination_container_name = os.environ["destination_container_name"]

    logging.info(
        f"Instantiate client for {source_blob_name} in {source_container_name}")

    source_client = BlobClient.from_connection_string(
        source_connection_string,
        source_container_name,
        source_blob_name
    )

    properties = source_client.get_blob_properties()
    name = properties.name
    content_type = properties.content_settings.content_type

    logging.info(
        f"Instantiate client for {name} in {destination_container_name}")

    destination_client = BlobClient.from_connection_string(
        destination_connection_string,
        destination_container_name,
        name)

    logging.info(f"Set headers for {name} in {destination_container_name}")

    destination_client.set_http_headers(
        content_settings=ContentSettings(content_type=content_type)
    )

    logging.info(f"done")
