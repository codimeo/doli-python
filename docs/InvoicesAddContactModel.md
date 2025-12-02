# InvoicesAddContactModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_socpeople** | **int** | Id of thirdparty contact (if source &#x3D; &#39;external&#39;) or id of user (if source &#x3D; &#39;internal&#39;) to link | 
**type_contact** | **str** | Type of contact (code). Must a code found into table llx_c_type_contact. For example: BILLING | 
**source** | **str** | external&#x3D;Contact extern (llx_socpeople), internal&#x3D;Contact intern (llx_user) | 
**notrigger** | **int** | Disable all triggers | [optional] 

## Example

```python
from dolibarr_api.models.invoices_add_contact_model import InvoicesAddContactModel

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicesAddContactModel from a JSON string
invoices_add_contact_model_instance = InvoicesAddContactModel.from_json(json)
# print the JSON string representation of the object
print(InvoicesAddContactModel.to_json())

# convert the object into a dict
invoices_add_contact_model_dict = invoices_add_contact_model_instance.to_dict()
# create an instance of InvoicesAddContactModel from a dict
invoices_add_contact_model_from_dict = InvoicesAddContactModel.from_dict(invoices_add_contact_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


