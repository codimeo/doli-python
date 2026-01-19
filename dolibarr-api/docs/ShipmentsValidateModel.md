# ShipmentsValidateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notrigger** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.shipments_validate_model import ShipmentsValidateModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentsValidateModel from a JSON string
shipments_validate_model_instance = ShipmentsValidateModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentsValidateModel.to_json())

# convert the object into a dict
shipments_validate_model_dict = shipments_validate_model_instance.to_dict()
# create an instance of ShipmentsValidateModel from a dict
shipments_validate_model_from_dict = ShipmentsValidateModel.from_dict(shipments_validate_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


