# InvoicesUpdateLineModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | InvoiceLine data | [optional] 

## Example

```python
from dolibarr_api.models.invoices_update_line_model import InvoicesUpdateLineModel

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicesUpdateLineModel from a JSON string
invoices_update_line_model_instance = InvoicesUpdateLineModel.from_json(json)
# print the JSON string representation of the object
print(InvoicesUpdateLineModel.to_json())

# convert the object into a dict
invoices_update_line_model_dict = invoices_update_line_model_instance.to_dict()
# create an instance of InvoicesUpdateLineModel from a dict
invoices_update_line_model_from_dict = InvoicesUpdateLineModel.from_dict(invoices_update_line_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


