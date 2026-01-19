# MembersCreateTypeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.members_create_type_model import MembersCreateTypeModel

# TODO update the JSON string below
json = "{}"
# create an instance of MembersCreateTypeModel from a JSON string
members_create_type_model_instance = MembersCreateTypeModel.from_json(json)
# print the JSON string representation of the object
print(MembersCreateTypeModel.to_json())

# convert the object into a dict
members_create_type_model_dict = members_create_type_model_instance.to_dict()
# create an instance of MembersCreateTypeModel from a dict
members_create_type_model_from_dict = MembersCreateTypeModel.from_dict(members_create_type_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


