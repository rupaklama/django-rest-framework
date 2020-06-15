from django.db import models


# Create your models here.

class Profession(models.Model):
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.description


class DataSheet(models.Model):
    description = models.CharField(max_length=50)
    historical_data = models.TextField()

    def __str__(self):
        return self.description


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True)
    address = models.CharField(max_length=50)
    professions = models.ManyToManyField(Profession)
    data_sheet = models.OneToOneField(DataSheet, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)

    # using properties to add extra information to the serializer
    @property
    def status_message(self):  # custom method to return string instead of boolean
        if self.active:
            return "Customer is active"
        else:
            return "Customer is not active"

    # count of professions, this is added as an extra data to the serializer
    def num_professions(self):
        return self.professions.all().count()

    def __str__(self):
        return self.name


class Document(models.Model):
    # choices
    PP = 'PP'
    ID = 'ID'
    OT = 'OT'

    # creating list
    DOC_TYPES = (  # constant
        (PP, 'Passport'),
        (ID, 'Identity card'),
        (OT, 'Others')
    )

    # passing above values
    document_type = models.CharField(choices=DOC_TYPES, max_length=2)  # choices are two letters
    doc_number = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.doc_number
