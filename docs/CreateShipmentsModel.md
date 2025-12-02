# CreateShipmentsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_shipments_model import CreateShipmentsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShipmentsModel from a JSON string
create_shipments_model_instance = CreateShipmentsModel.from_json(json)
# print the JSON string representation of the object
print(CreateShipmentsModel.to_json())

# convert the object into a dict
create_shipments_model_dict = create_shipments_model_instance.to_dict()
# create an instance of CreateShipmentsModel from a dict
create_shipments_model_from_dict = CreateShipmentsModel.from_dict(create_shipments_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


