# SupplierinvoicesSettodraftModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idwarehouse** | **int** | Warehouse ID | [optional] 
**notrigger** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.supplierinvoices_settodraft_model import SupplierinvoicesSettodraftModel

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierinvoicesSettodraftModel from a JSON string
supplierinvoices_settodraft_model_instance = SupplierinvoicesSettodraftModel.from_json(json)
# print the JSON string representation of the object
print(SupplierinvoicesSettodraftModel.to_json())

# convert the object into a dict
supplierinvoices_settodraft_model_dict = supplierinvoices_settodraft_model_instance.to_dict()
# create an instance of SupplierinvoicesSettodraftModel from a dict
supplierinvoices_settodraft_model_from_dict = SupplierinvoicesSettodraftModel.from_dict(supplierinvoices_settodraft_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


