# UpdateCategoriesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.update_categories_model import UpdateCategoriesModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCategoriesModel from a JSON string
update_categories_model_instance = UpdateCategoriesModel.from_json(json)
# print the JSON string representation of the object
print(UpdateCategoriesModel.to_json())

# convert the object into a dict
update_categories_model_dict = update_categories_model_instance.to_dict()
# create an instance of UpdateCategoriesModel from a dict
update_categories_model_from_dict = UpdateCategoriesModel.from_dict(update_categories_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


