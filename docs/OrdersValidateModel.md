# OrdersValidateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idwarehouse** | **int** | Warehouse ID | [optional] 
**notrigger** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.orders_validate_model import OrdersValidateModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersValidateModel from a JSON string
orders_validate_model_instance = OrdersValidateModel.from_json(json)
# print the JSON string representation of the object
print(OrdersValidateModel.to_json())

# convert the object into a dict
orders_validate_model_dict = orders_validate_model_instance.to_dict()
# create an instance of OrdersValidateModel from a dict
orders_validate_model_from_dict = OrdersValidateModel.from_dict(orders_validate_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


