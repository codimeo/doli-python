# SupplierinvoicesUpdateLineModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | InvoiceLine data | [optional] 

## Example

```python
from dolibarr_api.models.supplierinvoices_update_line_model import SupplierinvoicesUpdateLineModel

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierinvoicesUpdateLineModel from a JSON string
supplierinvoices_update_line_model_instance = SupplierinvoicesUpdateLineModel.from_json(json)
# print the JSON string representation of the object
print(SupplierinvoicesUpdateLineModel.to_json())

# convert the object into a dict
supplierinvoices_update_line_model_dict = supplierinvoices_update_line_model_instance.to_dict()
# create an instance of SupplierinvoicesUpdateLineModel from a dict
supplierinvoices_update_line_model_from_dict = SupplierinvoicesUpdateLineModel.from_dict(supplierinvoices_update_line_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


