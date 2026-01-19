# ProductsUpdateAttributesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.products_update_attributes_model import ProductsUpdateAttributesModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsUpdateAttributesModel from a JSON string
products_update_attributes_model_instance = ProductsUpdateAttributesModel.from_json(json)
# print the JSON string representation of the object
print(ProductsUpdateAttributesModel.to_json())

# convert the object into a dict
products_update_attributes_model_dict = products_update_attributes_model_instance.to_dict()
# create an instance of ProductsUpdateAttributesModel from a dict
products_update_attributes_model_from_dict = ProductsUpdateAttributesModel.from_dict(products_update_attributes_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


