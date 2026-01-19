# ExpensereportsDenyModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **str** | Comments for denial | 
**notrigger** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.expensereports_deny_model import ExpensereportsDenyModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExpensereportsDenyModel from a JSON string
expensereports_deny_model_instance = ExpensereportsDenyModel.from_json(json)
# print the JSON string representation of the object
print(ExpensereportsDenyModel.to_json())

# convert the object into a dict
expensereports_deny_model_dict = expensereports_deny_model_instance.to_dict()
# create an instance of ExpensereportsDenyModel from a dict
expensereports_deny_model_from_dict = ExpensereportsDenyModel.from_dict(expensereports_deny_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


