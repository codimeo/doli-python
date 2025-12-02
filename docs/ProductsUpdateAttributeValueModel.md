# ProductsUpdateAttributeValueModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | 

## Example

```python
from dolibarr_api.models.products_update_attribute_value_model import ProductsUpdateAttributeValueModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsUpdateAttributeValueModel from a JSON string
products_update_attribute_value_model_instance = ProductsUpdateAttributeValueModel.from_json(json)
# print the JSON string representation of the object
print(ProductsUpdateAttributeValueModel.to_json())

# convert the object into a dict
products_update_attribute_value_model_dict = products_update_attribute_value_model_instance.to_dict()
# create an instance of ProductsUpdateAttributeValueModel from a dict
products_update_attribute_value_model_from_dict = ProductsUpdateAttributeValueModel.from_dict(products_update_attribute_value_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


