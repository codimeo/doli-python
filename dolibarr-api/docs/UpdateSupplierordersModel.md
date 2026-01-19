# UpdateSupplierordersModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.update_supplierorders_model import UpdateSupplierordersModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSupplierordersModel from a JSON string
update_supplierorders_model_instance = UpdateSupplierordersModel.from_json(json)
# print the JSON string representation of the object
print(UpdateSupplierordersModel.to_json())

# convert the object into a dict
update_supplierorders_model_dict = update_supplierorders_model_instance.to_dict()
# create an instance of UpdateSupplierordersModel from a dict
update_supplierorders_model_from_dict = UpdateSupplierordersModel.from_dict(update_supplierorders_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


