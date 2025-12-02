# SupplierordersMakeOrderModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **int** | Date (unix timestamp in sec) | 
**method** | **int** | Method | 
**comment** | **str** | Comment | [optional] 

## Example

```python
from dolibarr_api.models.supplierorders_make_order_model import SupplierordersMakeOrderModel

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierordersMakeOrderModel from a JSON string
supplierorders_make_order_model_instance = SupplierordersMakeOrderModel.from_json(json)
# print the JSON string representation of the object
print(SupplierordersMakeOrderModel.to_json())

# convert the object into a dict
supplierorders_make_order_model_dict = supplierorders_make_order_model_instance.to_dict()
# create an instance of SupplierordersMakeOrderModel from a dict
supplierorders_make_order_model_from_dict = SupplierordersMakeOrderModel.from_dict(supplierorders_make_order_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


