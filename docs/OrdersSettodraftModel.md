# OrdersSettodraftModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idwarehouse** | **int** | Warehouse ID to use for stock change (Used only if option STOCK_CALCULATE_ON_VALIDATE_ORDER is on) | [optional] 

## Example

```python
from dolibarr_api.models.orders_settodraft_model import OrdersSettodraftModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersSettodraftModel from a JSON string
orders_settodraft_model_instance = OrdersSettodraftModel.from_json(json)
# print the JSON string representation of the object
print(OrdersSettodraftModel.to_json())

# convert the object into a dict
orders_settodraft_model_dict = orders_settodraft_model_instance.to_dict()
# create an instance of OrdersSettodraftModel from a dict
orders_settodraft_model_from_dict = OrdersSettodraftModel.from_dict(orders_settodraft_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


