# System imports
from django.conf import settings
# Local source tree imports
from django.db import models

class StockProfile(models.Model):
    """
        A simple representation of a Stock.

        Attributes:
            :title: A String, the Stocks title.
            :stock_list: A Many-to-One relationship to StockList.
    """
    title = models.CharField(max_length=255)
    stock_list = models.ForeignKey('StockList', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class StockList(models.Model):
    """
        This model is a list for containing StockProfile objects.

        Attributes:
            :name: A String, the name of the list.
            :length: An int, the number of StockProfile objects.
    """
    name = models.CharField(max_length=255)
    length = models.PositiveIntegerField(default=0)

    def __len__(self):
        return self.length

    def __str__(self):
        return self.name
