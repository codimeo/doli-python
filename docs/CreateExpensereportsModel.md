# CreateExpensereportsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_expensereports_model import CreateExpensereportsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExpensereportsModel from a JSON string
create_expensereports_model_instance = CreateExpensereportsModel.from_json(json)
# print the JSON string representation of the object
print(CreateExpensereportsModel.to_json())

# convert the object into a dict
create_expensereports_model_dict = create_expensereports_model_instance.to_dict()
# create an instance of CreateExpensereportsModel from a dict
create_expensereports_model_from_dict = CreateExpensereportsModel.from_dict(create_expensereports_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


