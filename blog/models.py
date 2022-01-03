from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField


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

    def __str__(self):
        return str(self.created_on)


class Discipline(models.Model):
    discipline_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.discipline_name)


DISCIPLINE_CHOICES = (
    ('MECHANICAL', 'MECHANICAL'),
    ('CHEMICAL', 'CHEMICAL'),
    ('CIVIL', 'CIVIL'),
    ('ELECTRICAL AND COMPUTER SCIENCE', 'ELECTRICAL AND COMPUTER SCIENCE'),
    ('ENVIRONMENTAL', 'ENVIRONMENTAL'),
    ('INDUSTRIAL', 'INDUSTRIAL'),
    ('OTHERS', 'OTHERS')
)


APPEARING_YEAR = (
    ('THIS YEAR', 'THIS YEAR'),
    ('NEXT YEAR', 'NEXT YEAR'),
    ('NEXT TO NEXT YEAR', 'NEXT TO NEXT YEAR'),
    ('NOT PLANNING TO GIVE FE EXAMS', 'NOT PLANNING TO GIVE FE EXAMS'),
)


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    country = CountryField()
    discipline = models.ForeignKey(
        Discipline, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    order_details = models.ForeignKey(
        OrderDetail, on_delete=models.PROTECT, blank=True, null=True)
    purchase_time = models.DateTimeField(null=True, blank=True)
    package_expiration_time = models.DateTimeField(null=True, blank=True)
    appearing_year = models.CharField(
        choices=APPEARING_YEAR, max_length=100, blank=True)

    def __str__(self):
        return str(self.user.username)


class ThoughtData(models.Model):
    quote = models.CharField(max_length=800)
    author = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.id)
