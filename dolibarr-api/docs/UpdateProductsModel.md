# UpdateProductsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.update_products_model import UpdateProductsModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProductsModel from a JSON string
update_products_model_instance = UpdateProductsModel.from_json(json)
# print the JSON string representation of the object
print(UpdateProductsModel.to_json())

# convert the object into a dict
update_products_model_dict = update_products_model_instance.to_dict()
# create an instance of UpdateProductsModel from a dict
update_products_model_from_dict = UpdateProductsModel.from_dict(update_products_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


