# ExpensereportsValidateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notrigger** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.expensereports_validate_model import ExpensereportsValidateModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExpensereportsValidateModel from a JSON string
expensereports_validate_model_instance = ExpensereportsValidateModel.from_json(json)
# print the JSON string representation of the object
print(ExpensereportsValidateModel.to_json())

# convert the object into a dict
expensereports_validate_model_dict = expensereports_validate_model_instance.to_dict()
# create an instance of ExpensereportsValidateModel from a dict
expensereports_validate_model_from_dict = ExpensereportsValidateModel.from_dict(expensereports_validate_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


