# CreateSupplierordersModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_supplierorders_model import CreateSupplierordersModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupplierordersModel from a JSON string
create_supplierorders_model_instance = CreateSupplierordersModel.from_json(json)
# print the JSON string representation of the object
print(CreateSupplierordersModel.to_json())

# convert the object into a dict
create_supplierorders_model_dict = create_supplierorders_model_instance.to_dict()
# create an instance of CreateSupplierordersModel from a dict
create_supplierorders_model_from_dict = CreateSupplierordersModel.from_dict(create_supplierorders_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


