# ExpensereportsApproveModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notrigger** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.expensereports_approve_model import ExpensereportsApproveModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExpensereportsApproveModel from a JSON string
expensereports_approve_model_instance = ExpensereportsApproveModel.from_json(json)
# print the JSON string representation of the object
print(ExpensereportsApproveModel.to_json())

# convert the object into a dict
expensereports_approve_model_dict = expensereports_approve_model_instance.to_dict()
# create an instance of ExpensereportsApproveModel from a dict
expensereports_approve_model_from_dict = ExpensereportsApproveModel.from_dict(expensereports_approve_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


