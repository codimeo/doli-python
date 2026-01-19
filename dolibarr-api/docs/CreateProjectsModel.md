# CreateProjectsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_projects_model import CreateProjectsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectsModel from a JSON string
create_projects_model_instance = CreateProjectsModel.from_json(json)
# print the JSON string representation of the object
print(CreateProjectsModel.to_json())

# convert the object into a dict
create_projects_model_dict = create_projects_model_instance.to_dict()
# create an instance of CreateProjectsModel from a dict
create_projects_model_from_dict = CreateProjectsModel.from_dict(create_projects_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


