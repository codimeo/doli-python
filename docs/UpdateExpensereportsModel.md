# UpdateExpensereportsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Expense report data | [optional] 

## Example

```python
from dolibarr_api.models.update_expensereports_model import UpdateExpensereportsModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExpensereportsModel from a JSON string
update_expensereports_model_instance = UpdateExpensereportsModel.from_json(json)
# print the JSON string representation of the object
print(UpdateExpensereportsModel.to_json())

# convert the object into a dict
update_expensereports_model_dict = update_expensereports_model_instance.to_dict()
# create an instance of UpdateExpensereportsModel from a dict
update_expensereports_model_from_dict = UpdateExpensereportsModel.from_dict(update_expensereports_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


