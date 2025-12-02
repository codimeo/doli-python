# UpdatePartnershipsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.update_partnerships_model import UpdatePartnershipsModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePartnershipsModel from a JSON string
update_partnerships_model_instance = UpdatePartnershipsModel.from_json(json)
# print the JSON string representation of the object
print(UpdatePartnershipsModel.to_json())

# convert the object into a dict
update_partnerships_model_dict = update_partnerships_model_instance.to_dict()
# create an instance of UpdatePartnershipsModel from a dict
update_partnerships_model_from_dict = UpdatePartnershipsModel.from_dict(update_partnerships_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


