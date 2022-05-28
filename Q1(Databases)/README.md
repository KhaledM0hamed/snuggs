### A. Retrieve the product Ids and names of the top 5 highest selling products

```sql
select task_product.id, task_product.productName
from task_order_products
Inner Join task_product on task_order_products.product_id = task_product.id
group by productName
order by count(productName) desc
limit 5
```
---
### B. Retrieve the top 5 customer names and emails that have spent the most sum of money (Amount in the order table)
```sql
select task_customer.name, task_customer.email
from task_order
INNER JOIN task_customer on task_order.customer_id = task_customer.id
group by customer_id
order by sum(task_order.amount) desc
limit 5
```
---
### C. Retrieve the top 5 customer names and emails that have made the most total count of orders
```sql
select task_customer.name, task_customer.email
from task_order
INNER JOIN task_customer on task_order.customer_id = task_customer.id
group by customer_id
order by count(task_order.id) desc
limit 5
```
