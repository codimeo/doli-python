# ProductsAddPurchasePriceModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qty** | **float** | Min quantity for which price is valid | 
**buyprice** | **float** | Purchase price for the quantity min | 
**price_base_type** | **str** | HT or TTC | 
**fourn_id** | **int** | Supplier ID | 
**availability** | **int** | Product availability | 
**ref_fourn** | **str** | Supplier ref | 
**tva_tx** | **float** | New VAT Rate (For example 8.5. Should not be a string) | 
**charges** | **float** | costs affering to product | [optional] 
**remise_percent** | **float** | Discount regarding qty (percent) | [optional] 
**remise** | **float** | Discount regarding qty (amount) | [optional] 
**newnpr** | **int** | Set NPR or not | [optional] 
**delivery_time_days** | **int** | Delay in days for delivery (max). May be &#39;&#39; if not defined. | [optional] 
**supplier_reputation** | **str** | Reputation with this product to the defined supplier (empty, FAVORITE, DONOTORDER) | [optional] 
**localtaxes_array** | **List[str]** | Array with localtaxes info array(&#39;0&#39;&#x3D;&gt;type1,&#39;1&#39;&#x3D;&gt;rate1,&#39;2&#39;&#x3D;&gt;type2,&#39;3&#39;&#x3D;&gt;rate2) (loaded by getLocalTaxesFromRate(vatrate, 0, ...) function). | [optional] 
**newdefaultvatcode** | **str** | Default vat code | [optional] 
**multicurrency_buyprice** | **float** | Purchase price for the quantity min in currency | [optional] 
**multicurrency_price_base_type** | **str** | HT or TTC in currency | [optional] 
**multicurrency_tx** | **float** | Rate currency | [optional] 
**multicurrency_code** | **str** | Currency code | [optional] 
**desc_fourn** | **str** | Custom description for product_fourn_price | [optional] 
**barcode** | **str** | Barcode | [optional] 
**fk_barcode_type** | **int** | Barcode type | [optional] 

## Example

```python
from dolibarr_api.models.products_add_purchase_price_model import ProductsAddPurchasePriceModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsAddPurchasePriceModel from a JSON string
products_add_purchase_price_model_instance = ProductsAddPurchasePriceModel.from_json(json)
# print the JSON string representation of the object
print(ProductsAddPurchasePriceModel.to_json())

# convert the object into a dict
products_add_purchase_price_model_dict = products_add_purchase_price_model_instance.to_dict()
# create an instance of ProductsAddPurchasePriceModel from a dict
products_add_purchase_price_model_from_dict = ProductsAddPurchasePriceModel.from_dict(products_add_purchase_price_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


