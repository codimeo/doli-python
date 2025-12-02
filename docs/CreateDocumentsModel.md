# CreateDocumentsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | Name of file to create (&#39;FA1705-0123.txt&#39;) | 
**modulepart** | **str** | Name of module or area concerned by file upload (&#39;product&#39;, &#39;service&#39;, &#39;invoice&#39;, &#39;proposal&#39;, &#39;project&#39;, &#39;project_task&#39;, &#39;supplier_invoice&#39;, &#39;expensereport&#39;, &#39;member&#39;, ...) | 
**ref** | **str** | Reference of object (This will define subdir automatically and store submitted file into it) | [optional] 
**subdir** | **str** | Subdirectory (Only if $ref is not provided) | [optional] 
**filecontent** | **str** | File content (string with file content. An empty file will be created if this parameter is not provided) | [optional] 
**fileencoding** | **str** | File encoding (&#39;&#39;&#x3D;no encoding, &#39;base64&#39;&#x3D;Base 64) | [optional] 
**overwriteifexists** | **int** | Overwrite file if exists (1 by default) | [optional] 
**createdirifnotexists** | **int** | Create subdirectories if the doesn&#39;t exists (1 by default) | [optional] 
**position** | **int** | Position | [optional] 
**cover** | **str** | Cover info | [optional] 
**array_options** | **List[str]** | Array for extrafields of ECM index table | [optional] 
**generate_thumbs** | **int** | 1&#x3D;Will generate the small and mini thumbs if applicable | [optional] 

## Example

```python
from dolibarr_api.models.create_documents_model import CreateDocumentsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDocumentsModel from a JSON string
create_documents_model_instance = CreateDocumentsModel.from_json(json)
# print the JSON string representation of the object
print(CreateDocumentsModel.to_json())

# convert the object into a dict
create_documents_model_dict = create_documents_model_instance.to_dict()
# create an instance of CreateDocumentsModel from a dict
create_documents_model_from_dict = CreateDocumentsModel.from_dict(create_documents_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


