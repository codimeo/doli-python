# ContractsCloseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notrigger** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.contracts_close_model import ContractsCloseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ContractsCloseModel from a JSON string
contracts_close_model_instance = ContractsCloseModel.from_json(json)
# print the JSON string representation of the object
print(ContractsCloseModel.to_json())

# convert the object into a dict
contracts_close_model_dict = contracts_close_model_instance.to_dict()
# create an instance of ContractsCloseModel from a dict
contracts_close_model_from_dict = ContractsCloseModel.from_dict(contracts_close_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


