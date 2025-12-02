# DocumentsBuilddocModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modulepart** | **str** | Name of module or area concerned by file download (&#39;thirdparty&#39;, &#39;member&#39;, &#39;proposal&#39;, &#39;supplier_proposal&#39;, &#39;order&#39;, &#39;supplier_order&#39;, &#39;invoice&#39;, &#39;supplier_invoice&#39;, &#39;shipment&#39;, &#39;project&#39;, ...) | 
**original_file** | **str** | Relative path with filename, relative to modulepart (for example: IN201701-999/IN201701-999.pdf). | [optional] 
**doctemplate** | **str** | Set here the doc template to use for document generation (If not set, use the default template). | [optional] 
**langcode** | **str** | Language code like &#39;en_US&#39;, &#39;fr_FR&#39;, &#39;es_ES&#39;, ... (If not set, use the default language). | [optional] 

## Example

```python
from dolibarr_api.models.documents_builddoc_model import DocumentsBuilddocModel

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsBuilddocModel from a JSON string
documents_builddoc_model_instance = DocumentsBuilddocModel.from_json(json)
# print the JSON string representation of the object
print(DocumentsBuilddocModel.to_json())

# convert the object into a dict
documents_builddoc_model_dict = documents_builddoc_model_instance.to_dict()
# create an instance of DocumentsBuilddocModel from a dict
documents_builddoc_model_from_dict = DocumentsBuilddocModel.from_dict(documents_builddoc_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


