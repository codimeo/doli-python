# UsersCreateUserNotificationByCodeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.users_create_user_notification_by_code_model import UsersCreateUserNotificationByCodeModel

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateUserNotificationByCodeModel from a JSON string
users_create_user_notification_by_code_model_instance = UsersCreateUserNotificationByCodeModel.from_json(json)
# print the JSON string representation of the object
print(UsersCreateUserNotificationByCodeModel.to_json())

# convert the object into a dict
users_create_user_notification_by_code_model_dict = users_create_user_notification_by_code_model_instance.to_dict()
# create an instance of UsersCreateUserNotificationByCodeModel from a dict
users_create_user_notification_by_code_model_from_dict = UsersCreateUserNotificationByCodeModel.from_dict(users_create_user_notification_by_code_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


