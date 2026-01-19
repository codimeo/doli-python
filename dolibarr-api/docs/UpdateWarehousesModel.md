# UpdateWarehousesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.update_warehouses_model import UpdateWarehousesModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWarehousesModel from a JSON string
update_warehouses_model_instance = UpdateWarehousesModel.from_json(json)
# print the JSON string representation of the object
print(UpdateWarehousesModel.to_json())

# convert the object into a dict
update_warehouses_model_dict = update_warehouses_model_instance.to_dict()
# create an instance of UpdateWarehousesModel from a dict
update_warehouses_model_from_dict = UpdateWarehousesModel.from_dict(update_warehouses_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


