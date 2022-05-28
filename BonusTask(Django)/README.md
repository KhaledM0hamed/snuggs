### Customer Model
```python 
class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=90)
    
    def __str__(self):
        return "%s %s %s" % (self.name, self.email, self.address)
```
---
### Product Model 
```python 
class Product(models.Model):
    productName = models.CharField(max_length=30)

    def __str__(self):
        return "%s" % self.productName
```
---
### Order Model 
```python 
class Order(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.amount
```