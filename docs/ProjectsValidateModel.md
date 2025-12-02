# ProjectsValidateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notrigger** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.projects_validate_model import ProjectsValidateModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsValidateModel from a JSON string
projects_validate_model_instance = ProjectsValidateModel.from_json(json)
# print the JSON string representation of the object
print(ProjectsValidateModel.to_json())

# convert the object into a dict
projects_validate_model_dict = projects_validate_model_instance.to_dict()
# create an instance of ProjectsValidateModel from a dict
projects_validate_model_from_dict = ProjectsValidateModel.from_dict(projects_validate_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


