# CreateSupplierinvoicesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_supplierinvoices_model import CreateSupplierinvoicesModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSupplierinvoicesModel from a JSON string
create_supplierinvoices_model_instance = CreateSupplierinvoicesModel.from_json(json)
# print the JSON string representation of the object
print(CreateSupplierinvoicesModel.to_json())

# convert the object into a dict
create_supplierinvoices_model_dict = create_supplierinvoices_model_instance.to_dict()
# create an instance of CreateSupplierinvoicesModel from a dict
create_supplierinvoices_model_from_dict = CreateSupplierinvoicesModel.from_dict(create_supplierinvoices_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


