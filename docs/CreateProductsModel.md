# CreateProductsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_products_model import CreateProductsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProductsModel from a JSON string
create_products_model_instance = CreateProductsModel.from_json(json)
# print the JSON string representation of the object
print(CreateProductsModel.to_json())

# convert the object into a dict
create_products_model_dict = create_products_model_instance.to_dict()
# create an instance of CreateProductsModel from a dict
create_products_model_from_dict = CreateProductsModel.from_dict(create_products_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


