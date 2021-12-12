from django.db import models
from django.contrib.auth.models import User

# class Question(models.Model):
#     Qnum = models.CharField(max_length = 100)
#     Qtext = models.TextField()

#     def __str__(self):
#         return self.Qnum

# class Member(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     status = models.BooleanField(default=False)
#     purchase_date = models.DateTimeField(auto_now_add=True)
#     validity = models.DateTimeField()
#     is_active = models.BooleanField()

#     def __str__(self):
#         return str(self.user)


class Package(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    validity_in_months = models.IntegerField(default=0)
    description = models.TextField(max_length=400)

    def __str__(self):
        return str(self.id)


class OrderDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    customer_email = models.EmailField(verbose_name='Customer Email')
    product = models.ForeignKey(
        to=Package, verbose_name='Product', on_delete=models.PROTECT)
    amount = models.IntegerField(verbose_name='Amount')
    stripe_payment_intent = models.CharField(max_length=200)
    has_paid = models.BooleanField(
        default=False, verbose_name='Payment Status')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
