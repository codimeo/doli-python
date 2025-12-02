# UpdateTasksModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.update_tasks_model import UpdateTasksModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTasksModel from a JSON string
update_tasks_model_instance = UpdateTasksModel.from_json(json)
# print the JSON string representation of the object
print(UpdateTasksModel.to_json())

# convert the object into a dict
update_tasks_model_dict = update_tasks_model_instance.to_dict()
# create an instance of UpdateTasksModel from a dict
update_tasks_model_from_dict = UpdateTasksModel.from_dict(update_tasks_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


