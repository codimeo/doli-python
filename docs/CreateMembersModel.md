# CreateMembersModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_members_model import CreateMembersModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMembersModel from a JSON string
create_members_model_instance = CreateMembersModel.from_json(json)
# print the JSON string representation of the object
print(CreateMembersModel.to_json())

# convert the object into a dict
create_members_model_dict = create_members_model_instance.to_dict()
# create an instance of CreateMembersModel from a dict
create_members_model_from_dict = CreateMembersModel.from_dict(create_members_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


