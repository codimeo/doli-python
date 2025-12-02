# InvoicesSettodraftModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idwarehouse** | **int** | Warehouse ID | [optional] 

## Example

```python
from dolibarr_api.models.invoices_settodraft_model import InvoicesSettodraftModel

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicesSettodraftModel from a JSON string
invoices_settodraft_model_instance = InvoicesSettodraftModel.from_json(json)
# print the JSON string representation of the object
print(InvoicesSettodraftModel.to_json())

# convert the object into a dict
invoices_settodraft_model_dict = invoices_settodraft_model_instance.to_dict()
# create an instance of InvoicesSettodraftModel from a dict
invoices_settodraft_model_from_dict = InvoicesSettodraftModel.from_dict(invoices_settodraft_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


