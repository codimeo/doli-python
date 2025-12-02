# UpdateMulticurrenciesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.update_multicurrencies_model import UpdateMulticurrenciesModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMulticurrenciesModel from a JSON string
update_multicurrencies_model_instance = UpdateMulticurrenciesModel.from_json(json)
# print the JSON string representation of the object
print(UpdateMulticurrenciesModel.to_json())

# convert the object into a dict
update_multicurrencies_model_dict = update_multicurrencies_model_instance.to_dict()
# create an instance of UpdateMulticurrenciesModel from a dict
update_multicurrencies_model_from_dict = UpdateMulticurrenciesModel.from_dict(update_multicurrencies_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


