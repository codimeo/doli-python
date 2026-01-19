# CreateContactsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_contacts_model import CreateContactsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContactsModel from a JSON string
create_contacts_model_instance = CreateContactsModel.from_json(json)
# print the JSON string representation of the object
print(CreateContactsModel.to_json())

# convert the object into a dict
create_contacts_model_dict = create_contacts_model_instance.to_dict()
# create an instance of CreateContactsModel from a dict
create_contacts_model_from_dict = CreateContactsModel.from_dict(create_contacts_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


