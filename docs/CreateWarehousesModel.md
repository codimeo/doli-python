# CreateWarehousesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_warehouses_model import CreateWarehousesModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWarehousesModel from a JSON string
create_warehouses_model_instance = CreateWarehousesModel.from_json(json)
# print the JSON string representation of the object
print(CreateWarehousesModel.to_json())

# convert the object into a dict
create_warehouses_model_dict = create_warehouses_model_instance.to_dict()
# create an instance of CreateWarehousesModel from a dict
create_warehouses_model_from_dict = CreateWarehousesModel.from_dict(create_warehouses_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


