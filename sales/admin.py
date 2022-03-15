from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Party)
admin.site.register(StockItem)
admin.site.register(InvoiceItem)
admin.site.register(Invoice)