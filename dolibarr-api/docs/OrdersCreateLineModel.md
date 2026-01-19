# OrdersCreateLineModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | OrderLine data | [optional] 

## Example

```python
from dolibarr_api.models.orders_create_line_model import OrdersCreateLineModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersCreateLineModel from a JSON string
orders_create_line_model_instance = OrdersCreateLineModel.from_json(json)
# print the JSON string representation of the object
print(OrdersCreateLineModel.to_json())

# convert the object into a dict
orders_create_line_model_dict = orders_create_line_model_instance.to_dict()
# create an instance of OrdersCreateLineModel from a dict
orders_create_line_model_from_dict = OrdersCreateLineModel.from_dict(orders_create_line_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


