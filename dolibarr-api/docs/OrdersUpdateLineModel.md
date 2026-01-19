# OrdersUpdateLineModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | OrderLine data | [optional] 

## Example

```python
from dolibarr_api.models.orders_update_line_model import OrdersUpdateLineModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersUpdateLineModel from a JSON string
orders_update_line_model_instance = OrdersUpdateLineModel.from_json(json)
# print the JSON string representation of the object
print(OrdersUpdateLineModel.to_json())

# convert the object into a dict
orders_update_line_model_dict = orders_update_line_model_instance.to_dict()
# create an instance of OrdersUpdateLineModel from a dict
orders_update_line_model_from_dict = OrdersUpdateLineModel.from_dict(orders_update_line_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


