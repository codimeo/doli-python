# InvoicesValidateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_number** | **str** | force ref invoice | [optional] 
**idwarehouse** | **int** | Warehouse ID | [optional] 
**notrigger** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.invoices_validate_model import InvoicesValidateModel

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicesValidateModel from a JSON string
invoices_validate_model_instance = InvoicesValidateModel.from_json(json)
# print the JSON string representation of the object
print(InvoicesValidateModel.to_json())

# convert the object into a dict
invoices_validate_model_dict = invoices_validate_model_instance.to_dict()
# create an instance of InvoicesValidateModel from a dict
invoices_validate_model_from_dict = InvoicesValidateModel.from_dict(invoices_validate_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


