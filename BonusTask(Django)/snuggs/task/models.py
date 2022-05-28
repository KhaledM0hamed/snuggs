from django.db import models


# Create your models here.
class Customer(models.Model):
    # customer2 = Customer(name="khaled2", email="khaled2@dfsa.com", address="shit")
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=90)

    def __str__(self):
        return "%s %s %s" % (self.name, self.email, self.address)


class Product(models.Model):
    # product1 = Product(productName="product1")
    productName = models.CharField(max_length=30)

    def __str__(self):
        return "%s" % self.productName


class Order(models.Model):
    # order1 = Order(amount=100, customer=customer1, products.add(product1))
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.amount
