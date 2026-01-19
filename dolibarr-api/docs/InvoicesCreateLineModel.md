# InvoicesCreateLineModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | InvoiceLine data | [optional] 

## Example

```python
from dolibarr_api.models.invoices_create_line_model import InvoicesCreateLineModel

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicesCreateLineModel from a JSON string
invoices_create_line_model_instance = InvoicesCreateLineModel.from_json(json)
# print the JSON string representation of the object
print(InvoicesCreateLineModel.to_json())

# convert the object into a dict
invoices_create_line_model_dict = invoices_create_line_model_instance.to_dict()
# create an instance of InvoicesCreateLineModel from a dict
invoices_create_line_model_from_dict = InvoicesCreateLineModel.from_dict(invoices_create_line_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


