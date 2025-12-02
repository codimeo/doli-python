# DonationsValidateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idwarehouse** | **int** | Warehouse ID | [optional] 
**notrigger** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.donations_validate_model import DonationsValidateModel

# TODO update the JSON string below
json = "{}"
# create an instance of DonationsValidateModel from a JSON string
donations_validate_model_instance = DonationsValidateModel.from_json(json)
# print the JSON string representation of the object
print(DonationsValidateModel.to_json())

# convert the object into a dict
donations_validate_model_dict = donations_validate_model_instance.to_dict()
# create an instance of DonationsValidateModel from a dict
donations_validate_model_from_dict = DonationsValidateModel.from_dict(donations_validate_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


