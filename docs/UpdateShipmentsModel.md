# UpdateShipmentsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.update_shipments_model import UpdateShipmentsModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShipmentsModel from a JSON string
update_shipments_model_instance = UpdateShipmentsModel.from_json(json)
# print the JSON string representation of the object
print(UpdateShipmentsModel.to_json())

# convert the object into a dict
update_shipments_model_dict = update_shipments_model_instance.to_dict()
# create an instance of UpdateShipmentsModel from a dict
update_shipments_model_from_dict = UpdateShipmentsModel.from_dict(update_shipments_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


