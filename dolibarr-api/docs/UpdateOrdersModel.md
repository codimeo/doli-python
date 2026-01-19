# UpdateOrdersModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.update_orders_model import UpdateOrdersModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrdersModel from a JSON string
update_orders_model_instance = UpdateOrdersModel.from_json(json)
# print the JSON string representation of the object
print(UpdateOrdersModel.to_json())

# convert the object into a dict
update_orders_model_dict = update_orders_model_instance.to_dict()
# create an instance of UpdateOrdersModel from a dict
update_orders_model_from_dict = UpdateOrdersModel.from_dict(update_orders_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


