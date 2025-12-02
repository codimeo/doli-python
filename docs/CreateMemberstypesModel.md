# CreateMemberstypesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_memberstypes_model import CreateMemberstypesModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMemberstypesModel from a JSON string
create_memberstypes_model_instance = CreateMemberstypesModel.from_json(json)
# print the JSON string representation of the object
print(CreateMemberstypesModel.to_json())

# convert the object into a dict
create_memberstypes_model_dict = create_memberstypes_model_instance.to_dict()
# create an instance of CreateMemberstypesModel from a dict
create_memberstypes_model_from_dict = CreateMemberstypesModel.from_dict(create_memberstypes_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


