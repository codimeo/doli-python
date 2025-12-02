# ProductsAddSubproductsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subproduct_id** | **int** | ID of child product/service | 
**qty** | **float** | Quantity | 
**incdec** | **int** | 1&#x3D;Increase/decrease stock of child when parent stock increases/decreases | [optional] 

## Example

```python
from dolibarr_api.models.products_add_subproducts_model import ProductsAddSubproductsModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsAddSubproductsModel from a JSON string
products_add_subproducts_model_instance = ProductsAddSubproductsModel.from_json(json)
# print the JSON string representation of the object
print(ProductsAddSubproductsModel.to_json())

# convert the object into a dict
products_add_subproducts_model_dict = products_add_subproducts_model_instance.to_dict()
# create an instance of ProductsAddSubproductsModel from a dict
products_add_subproducts_model_from_dict = ProductsAddSubproductsModel.from_dict(products_add_subproducts_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


