# ProductsAddAttributeValueModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | Reference of Attribute value | 
**value** | **str** | Value of Attribute value | 

## Example

```python
from dolibarr_api.models.products_add_attribute_value_model import ProductsAddAttributeValueModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsAddAttributeValueModel from a JSON string
products_add_attribute_value_model_instance = ProductsAddAttributeValueModel.from_json(json)
# print the JSON string representation of the object
print(ProductsAddAttributeValueModel.to_json())

# convert the object into a dict
products_add_attribute_value_model_dict = products_add_attribute_value_model_instance.to_dict()
# create an instance of ProductsAddAttributeValueModel from a dict
products_add_attribute_value_model_from_dict = ProductsAddAttributeValueModel.from_dict(products_add_attribute_value_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


