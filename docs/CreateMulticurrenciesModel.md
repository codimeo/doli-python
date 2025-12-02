# CreateMulticurrenciesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_multicurrencies_model import CreateMulticurrenciesModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMulticurrenciesModel from a JSON string
create_multicurrencies_model_instance = CreateMulticurrenciesModel.from_json(json)
# print the JSON string representation of the object
print(CreateMulticurrenciesModel.to_json())

# convert the object into a dict
create_multicurrencies_model_dict = create_multicurrencies_model_instance.to_dict()
# create an instance of CreateMulticurrenciesModel from a dict
create_multicurrencies_model_from_dict = CreateMulticurrenciesModel.from_dict(create_multicurrencies_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


