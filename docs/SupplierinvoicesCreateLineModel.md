# SupplierinvoicesCreateLineModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | supplier invoice line data | [optional] 

## Example

```python
from dolibarr_api.models.supplierinvoices_create_line_model import SupplierinvoicesCreateLineModel

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierinvoicesCreateLineModel from a JSON string
supplierinvoices_create_line_model_instance = SupplierinvoicesCreateLineModel.from_json(json)
# print the JSON string representation of the object
print(SupplierinvoicesCreateLineModel.to_json())

# convert the object into a dict
supplierinvoices_create_line_model_dict = supplierinvoices_create_line_model_instance.to_dict()
# create an instance of SupplierinvoicesCreateLineModel from a dict
supplierinvoices_create_line_model_from_dict = SupplierinvoicesCreateLineModel.from_dict(supplierinvoices_create_line_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


