# TasksUpdateTimeSpentModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Date (YYYY-MM-DD HH:MI:SS in GMT) | 
**duration** | **int** | Duration in seconds (3600 &#x3D; 1h) | 
**user_id** | **int** | User (Use 0 for connected user) | [optional] 
**note** | **str** | Note | [optional] 

## Example

```python
from dolibarr_api.models.tasks_update_time_spent_model import TasksUpdateTimeSpentModel

# TODO update the JSON string below
json = "{}"
# create an instance of TasksUpdateTimeSpentModel from a JSON string
tasks_update_time_spent_model_instance = TasksUpdateTimeSpentModel.from_json(json)
# print the JSON string representation of the object
print(TasksUpdateTimeSpentModel.to_json())

# convert the object into a dict
tasks_update_time_spent_model_dict = tasks_update_time_spent_model_instance.to_dict()
# create an instance of TasksUpdateTimeSpentModel from a dict
tasks_update_time_spent_model_from_dict = TasksUpdateTimeSpentModel.from_dict(tasks_update_time_spent_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


