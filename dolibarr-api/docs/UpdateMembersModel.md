# UpdateMembersModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Datas | [optional] 

## Example

```python
from dolibarr_api.models.update_members_model import UpdateMembersModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMembersModel from a JSON string
update_members_model_instance = UpdateMembersModel.from_json(json)
# print the JSON string representation of the object
print(UpdateMembersModel.to_json())

# convert the object into a dict
update_members_model_dict = update_members_model_instance.to_dict()
# create an instance of UpdateMembersModel from a dict
update_members_model_from_dict = UpdateMembersModel.from_dict(update_members_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


