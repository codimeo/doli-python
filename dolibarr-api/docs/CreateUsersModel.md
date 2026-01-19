# CreateUsersModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | New user data | [optional] 

## Example

```python
from dolibarr_api.models.create_users_model import CreateUsersModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUsersModel from a JSON string
create_users_model_instance = CreateUsersModel.from_json(json)
# print the JSON string representation of the object
print(CreateUsersModel.to_json())

# convert the object into a dict
create_users_model_dict = create_users_model_instance.to_dict()
# create an instance of CreateUsersModel from a dict
create_users_model_from_dict = CreateUsersModel.from_dict(create_users_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


