# ContractsValidateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notrigger** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.contracts_validate_model import ContractsValidateModel

# TODO update the JSON string below
json = "{}"
# create an instance of ContractsValidateModel from a JSON string
contracts_validate_model_instance = ContractsValidateModel.from_json(json)
# print the JSON string representation of the object
print(ContractsValidateModel.to_json())

# convert the object into a dict
contracts_validate_model_dict = contracts_validate_model_instance.to_dict()
# create an instance of ContractsValidateModel from a dict
contracts_validate_model_from_dict = ContractsValidateModel.from_dict(contracts_validate_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


