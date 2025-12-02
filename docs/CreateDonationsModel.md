# CreateDonationsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_donations_model import CreateDonationsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDonationsModel from a JSON string
create_donations_model_instance = CreateDonationsModel.from_json(json)
# print the JSON string representation of the object
print(CreateDonationsModel.to_json())

# convert the object into a dict
create_donations_model_dict = create_donations_model_instance.to_dict()
# create an instance of CreateDonationsModel from a dict
create_donations_model_from_dict = CreateDonationsModel.from_dict(create_donations_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


