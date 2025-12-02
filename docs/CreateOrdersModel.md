# CreateOrdersModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_orders_model import CreateOrdersModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrdersModel from a JSON string
create_orders_model_instance = CreateOrdersModel.from_json(json)
# print the JSON string representation of the object
print(CreateOrdersModel.to_json())

# convert the object into a dict
create_orders_model_dict = create_orders_model_instance.to_dict()
# create an instance of CreateOrdersModel from a dict
create_orders_model_from_dict = CreateOrdersModel.from_dict(create_orders_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


