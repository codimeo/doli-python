# MembersUpdateTypeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Datas | [optional] 

## Example

```python
from dolibarr_api.models.members_update_type_model import MembersUpdateTypeModel

# TODO update the JSON string below
json = "{}"
# create an instance of MembersUpdateTypeModel from a JSON string
members_update_type_model_instance = MembersUpdateTypeModel.from_json(json)
# print the JSON string representation of the object
print(MembersUpdateTypeModel.to_json())

# convert the object into a dict
members_update_type_model_dict = members_update_type_model_instance.to_dict()
# create an instance of MembersUpdateTypeModel from a dict
members_update_type_model_from_dict = MembersUpdateTypeModel.from_dict(members_update_type_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


