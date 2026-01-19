# UpdateUsersModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Datas | [optional] 

## Example

```python
from dolibarr_api.models.update_users_model import UpdateUsersModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUsersModel from a JSON string
update_users_model_instance = UpdateUsersModel.from_json(json)
# print the JSON string representation of the object
print(UpdateUsersModel.to_json())

# convert the object into a dict
update_users_model_dict = update_users_model_instance.to_dict()
# create an instance of UpdateUsersModel from a dict
update_users_model_from_dict = UpdateUsersModel.from_dict(update_users_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


