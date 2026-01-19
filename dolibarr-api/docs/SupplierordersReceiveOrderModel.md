# SupplierordersReceiveOrderModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closeopenorder** | **int** | Close order if everything is received | [optional] 
**comment** | **str** | Comment | [optional] 
**lines** | **List[str]** | Array of product dispatches | 

## Example

```python
from dolibarr_api.models.supplierorders_receive_order_model import SupplierordersReceiveOrderModel

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierordersReceiveOrderModel from a JSON string
supplierorders_receive_order_model_instance = SupplierordersReceiveOrderModel.from_json(json)
# print the JSON string representation of the object
print(SupplierordersReceiveOrderModel.to_json())

# convert the object into a dict
supplierorders_receive_order_model_dict = supplierorders_receive_order_model_instance.to_dict()
# create an instance of SupplierordersReceiveOrderModel from a dict
supplierorders_receive_order_model_from_dict = SupplierordersReceiveOrderModel.from_dict(supplierorders_receive_order_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


