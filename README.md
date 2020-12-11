# pyfuncbloboutput
This repo https://github.com/glennmusa/pyfuncblobclone, but use the Blob Output Binding instead of uploading the blob yourself.

Uses the [Azure Functions Storage Blob Trigger](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python#example) and the [Azure Functions Storage Blob Output Binding](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-output?tabs=python) to clone a blob from the configured `input_container_name` in local.settings.json and makes use of the Azure Storage Blob SDK [BlobClient](https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blobclient?view=azure-python) to set its content type in the configured `output_container_name` in local.settings.json.

## To get started:
1. Clone [./local.settings.json.sample](./local.settings.json.sample) and rename it to `local.settings.json`
1. Subtitute the settings values with your resources
1. The blob is cloned in [./CloneSourceBlob/\_\_init\_\_.py](./CloneSourceBlob/__init__.py)
1. Content-type is set in [./SetDestinationContentType/\_\_init\_\_.py](./SetDestinationContentType/__init__.py)
