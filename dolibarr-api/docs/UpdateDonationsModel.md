# UpdateDonationsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.update_donations_model import UpdateDonationsModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDonationsModel from a JSON string
update_donations_model_instance = UpdateDonationsModel.from_json(json)
# print the JSON string representation of the object
print(UpdateDonationsModel.to_json())

# convert the object into a dict
update_donations_model_dict = update_donations_model_instance.to_dict()
# create an instance of UpdateDonationsModel from a dict
update_donations_model_from_dict = UpdateDonationsModel.from_dict(update_donations_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


