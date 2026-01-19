# CreateTasksModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_tasks_model import CreateTasksModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTasksModel from a JSON string
create_tasks_model_instance = CreateTasksModel.from_json(json)
# print the JSON string representation of the object
print(CreateTasksModel.to_json())

# convert the object into a dict
create_tasks_model_dict = create_tasks_model_instance.to_dict()
# create an instance of CreateTasksModel from a dict
create_tasks_model_from_dict = CreateTasksModel.from_dict(create_tasks_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


