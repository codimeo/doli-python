# SupplierordersApproveModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idwarehouse** | **int** | Warehouse ID | [optional] 
**secondlevel** | **int** | 1&#x3D;Does not execute triggers, 0&#x3D; execute triggers | [optional] 

## Example

```python
from dolibarr_api.models.supplierorders_approve_model import SupplierordersApproveModel

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierordersApproveModel from a JSON string
supplierorders_approve_model_instance = SupplierordersApproveModel.from_json(json)
# print the JSON string representation of the object
print(SupplierordersApproveModel.to_json())

# convert the object into a dict
supplierorders_approve_model_dict = supplierorders_approve_model_instance.to_dict()
# create an instance of SupplierordersApproveModel from a dict
supplierorders_approve_model_from_dict = SupplierordersApproveModel.from_dict(supplierorders_approve_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


