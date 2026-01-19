# TasksAddTimeSpentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Date (YYYY-MM-DD HH:MI:SS in GMT) | 
**duration** | **int** | Duration in seconds (3600 &#x3D; 1h) | 
**user_id** | **int** | User (Use 0 for connected user) | [optional] 
**note** | **str** | Note | [optional] 

## Example

```python
from dolibarr_api.models.tasks_add_time_spent_model import TasksAddTimeSpentModel

# TODO update the JSON string below
json = "{}"
# create an instance of TasksAddTimeSpentModel from a JSON string
tasks_add_time_spent_model_instance = TasksAddTimeSpentModel.from_json(json)
# print the JSON string representation of the object
print(TasksAddTimeSpentModel.to_json())

# convert the object into a dict
tasks_add_time_spent_model_dict = tasks_add_time_spent_model_instance.to_dict()
# create an instance of TasksAddTimeSpentModel from a dict
tasks_add_time_spent_model_from_dict = TasksAddTimeSpentModel.from_dict(tasks_add_time_spent_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


