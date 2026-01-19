# UpdateContactsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.update_contacts_model import UpdateContactsModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateContactsModel from a JSON string
update_contacts_model_instance = UpdateContactsModel.from_json(json)
# print the JSON string representation of the object
print(UpdateContactsModel.to_json())

# convert the object into a dict
update_contacts_model_dict = update_contacts_model_instance.to_dict()
# create an instance of UpdateContactsModel from a dict
update_contacts_model_from_dict = UpdateContactsModel.from_dict(update_contacts_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


