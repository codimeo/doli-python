# UpdateProjectsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Datas | [optional] 

## Example

```python
from dolibarr_api.models.update_projects_model import UpdateProjectsModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectsModel from a JSON string
update_projects_model_instance = UpdateProjectsModel.from_json(json)
# print the JSON string representation of the object
print(UpdateProjectsModel.to_json())

# convert the object into a dict
update_projects_model_dict = update_projects_model_instance.to_dict()
# create an instance of UpdateProjectsModel from a dict
update_projects_model_from_dict = UpdateProjectsModel.from_dict(update_projects_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


