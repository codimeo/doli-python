# ProductsAddAttributesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | Reference of Attribute | 
**label** | **str** | Label of Attribute | 
**ref_ext** | **str** | Reference of Attribute | [optional] 

## Example

```python
from dolibarr_api.models.products_add_attributes_model import ProductsAddAttributesModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsAddAttributesModel from a JSON string
products_add_attributes_model_instance = ProductsAddAttributesModel.from_json(json)
# print the JSON string representation of the object
print(ProductsAddAttributesModel.to_json())

# convert the object into a dict
products_add_attributes_model_dict = products_add_attributes_model_instance.to_dict()
# create an instance of ProductsAddAttributesModel from a dict
products_add_attributes_model_from_dict = ProductsAddAttributesModel.from_dict(products_add_attributes_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


