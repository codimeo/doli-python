# UpdateSalariesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.update_salaries_model import UpdateSalariesModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSalariesModel from a JSON string
update_salaries_model_instance = UpdateSalariesModel.from_json(json)
# print the JSON string representation of the object
print(UpdateSalariesModel.to_json())

# convert the object into a dict
update_salaries_model_dict = update_salaries_model_instance.to_dict()
# create an instance of UpdateSalariesModel from a dict
update_salaries_model_from_dict = UpdateSalariesModel.from_dict(update_salaries_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


