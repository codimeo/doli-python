# SupplierordersValidateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idwarehouse** | **int** | Warehouse ID | [optional] 
**notrigger** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.supplierorders_validate_model import SupplierordersValidateModel

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierordersValidateModel from a JSON string
supplierorders_validate_model_instance = SupplierordersValidateModel.from_json(json)
# print the JSON string representation of the object
print(SupplierordersValidateModel.to_json())

# convert the object into a dict
supplierorders_validate_model_dict = supplierorders_validate_model_instance.to_dict()
# create an instance of SupplierordersValidateModel from a dict
supplierorders_validate_model_from_dict = SupplierordersValidateModel.from_dict(supplierorders_validate_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


