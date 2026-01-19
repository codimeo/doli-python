# ProductsAddVariantByProductRefModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weight_impact** | **float** | Weight impact of variant | 
**price_impact** | **float** | Price impact of variant | 
**price_impact_is_percent** | **bool** | Price impact in percent (true or false) | 
**features** | **List[str]** | List of attributes pairs id_attribute-&gt;id_value. Example: array(id_color&#x3D;&gt;id_Blue, id_size&#x3D;&gt;id_small, id_option&#x3D;&gt;id_val_a, ...) | 

## Example

```python
from dolibarr_api.models.products_add_variant_by_product_ref_model import ProductsAddVariantByProductRefModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsAddVariantByProductRefModel from a JSON string
products_add_variant_by_product_ref_model_instance = ProductsAddVariantByProductRefModel.from_json(json)
# print the JSON string representation of the object
print(ProductsAddVariantByProductRefModel.to_json())

# convert the object into a dict
products_add_variant_by_product_ref_model_dict = products_add_variant_by_product_ref_model_instance.to_dict()
# create an instance of ProductsAddVariantByProductRefModel from a dict
products_add_variant_by_product_ref_model_from_dict = ProductsAddVariantByProductRefModel.from_dict(products_add_variant_by_product_ref_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


