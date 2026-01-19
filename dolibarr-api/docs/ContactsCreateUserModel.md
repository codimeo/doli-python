# ContactsCreateUserModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.contacts_create_user_model import ContactsCreateUserModel

# TODO update the JSON string below
json = "{}"
# create an instance of ContactsCreateUserModel from a JSON string
contacts_create_user_model_instance = ContactsCreateUserModel.from_json(json)
# print the JSON string representation of the object
print(ContactsCreateUserModel.to_json())

# convert the object into a dict
contacts_create_user_model_dict = contacts_create_user_model_instance.to_dict()
# create an instance of ContactsCreateUserModel from a dict
contacts_create_user_model_from_dict = ContactsCreateUserModel.from_dict(contacts_create_user_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


