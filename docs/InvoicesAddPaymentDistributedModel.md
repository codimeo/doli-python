# InvoicesAddPaymentDistributedModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrayofamounts** | **List[str]** | Array with id of invoices with amount to pay for each invoice | 
**datepaye** | **str** | Payment date | 
**paymentid** | **int** | Payment mode Id | 
**closepaidinvoices** | **str** | Close paid invoices | 
**accountid** | **int** | Account Id | 
**num_payment** | **str** | Payment number (optional) | [optional] 
**comment** | **str** | Note private (optional) | [optional] 
**chqemetteur** | **str** | Payment issuer (mandatory if paiementcode &#x3D; &#39;CHQ&#39;) | [optional] 
**chqbank** | **str** | Issuer bank name (optional) | [optional] 
**ref_ext** | **str** | External reference (optional) | [optional] 
**accepthigherpayment** | **bool** | Accept higher payments that it remains to be paid (optional) | [optional] 

## Example

```python
from dolibarr_api.models.invoices_add_payment_distributed_model import InvoicesAddPaymentDistributedModel

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicesAddPaymentDistributedModel from a JSON string
invoices_add_payment_distributed_model_instance = InvoicesAddPaymentDistributedModel.from_json(json)
# print the JSON string representation of the object
print(InvoicesAddPaymentDistributedModel.to_json())

# convert the object into a dict
invoices_add_payment_distributed_model_dict = invoices_add_payment_distributed_model_instance.to_dict()
# create an instance of InvoicesAddPaymentDistributedModel from a dict
invoices_add_payment_distributed_model_from_dict = InvoicesAddPaymentDistributedModel.from_dict(invoices_add_payment_distributed_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


