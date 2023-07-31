from django.db import models
from userprofile.models import Address
from variant.models import VariantImage,Variant
from user.models import CustomUser
from datetime import timedelta
# # Create your models here.


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null= False)
    payment_id = models.CharField(max_length=250, null=True)
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    orderstatuses = {
        ('Pending','Pending'),
        ('Processing','Processing'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled'),
        ('Return', 'Return')
       
    }
    od_status = models.CharField(max_length=150,choices=orderstatuses, default='Pending')
    @property
    def expected_delivery(self):
        return self.created_at + timedelta(days=3)

    def __str__(self):
        return f"{self.id, self.tracking_no}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    orderstatuses = {
        ('Pending','Pending'),
        ('Processing','Processing'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled'),
        ('Return', 'Return')
    }
    status = models.CharField(max_length=150,choices=orderstatuses, default='Pending')

    def __str__(self):
        return f"{self.order.id, self.order.tracking_no}"
         