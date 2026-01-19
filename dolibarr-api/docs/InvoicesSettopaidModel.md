# InvoicesSettopaidModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close_code** | **str** | Code filled if we classify to &#39;Paid completely&#39; when payment is not complete (for escompte for example) | [optional] 
**close_note** | **str** | Comment defined if we classify to &#39;Paid&#39; when payment is not complete (for escompte for example) | [optional] 

## Example

```python
from dolibarr_api.models.invoices_settopaid_model import InvoicesSettopaidModel

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicesSettopaidModel from a JSON string
invoices_settopaid_model_instance = InvoicesSettopaidModel.from_json(json)
# print the JSON string representation of the object
print(InvoicesSettopaidModel.to_json())

# convert the object into a dict
invoices_settopaid_model_dict = invoices_settopaid_model_instance.to_dict()
# create an instance of InvoicesSettopaidModel from a dict
invoices_settopaid_model_from_dict = InvoicesSettopaidModel.from_dict(invoices_settopaid_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


