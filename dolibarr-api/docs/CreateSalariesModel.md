# CreateSalariesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_salaries_model import CreateSalariesModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSalariesModel from a JSON string
create_salaries_model_instance = CreateSalariesModel.from_json(json)
# print the JSON string representation of the object
print(CreateSalariesModel.to_json())

# convert the object into a dict
create_salaries_model_dict = create_salaries_model_instance.to_dict()
# create an instance of CreateSalariesModel from a dict
create_salaries_model_from_dict = CreateSalariesModel.from_dict(create_salaries_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


