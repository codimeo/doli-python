# OrdersCloseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notrigger** | **int** | Disabled triggers | [optional] 

## Example

```python
from dolibarr_api.models.orders_close_model import OrdersCloseModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersCloseModel from a JSON string
orders_close_model_instance = OrdersCloseModel.from_json(json)
# print the JSON string representation of the object
print(OrdersCloseModel.to_json())

# convert the object into a dict
orders_close_model_dict = orders_close_model_instance.to_dict()
# create an instance of OrdersCloseModel from a dict
orders_close_model_from_dict = OrdersCloseModel.from_dict(orders_close_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


