# ShipmentsCloseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notrigger** | **int** | Disabled triggers | [optional] 

## Example

```python
from dolibarr_api.models.shipments_close_model import ShipmentsCloseModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentsCloseModel from a JSON string
shipments_close_model_instance = ShipmentsCloseModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentsCloseModel.to_json())

# convert the object into a dict
shipments_close_model_dict = shipments_close_model_instance.to_dict()
# create an instance of ShipmentsCloseModel from a dict
shipments_close_model_from_dict = ShipmentsCloseModel.from_dict(shipments_close_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


