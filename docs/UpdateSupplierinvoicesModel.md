# UpdateSupplierinvoicesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.update_supplierinvoices_model import UpdateSupplierinvoicesModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSupplierinvoicesModel from a JSON string
update_supplierinvoices_model_instance = UpdateSupplierinvoicesModel.from_json(json)
# print the JSON string representation of the object
print(UpdateSupplierinvoicesModel.to_json())

# convert the object into a dict
update_supplierinvoices_model_dict = update_supplierinvoices_model_instance.to_dict()
# create an instance of UpdateSupplierinvoicesModel from a dict
update_supplierinvoices_model_from_dict = UpdateSupplierinvoicesModel.from_dict(update_supplierinvoices_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


