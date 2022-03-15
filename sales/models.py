from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.urls import reverse

class Party(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Party Name')
    phone = models.CharField(max_length=15, blank=True, verbose_name='Party Contact Number')
    address_line1 = models.CharField(max_length=100, blank=True, verbose_name='Address Line 1')
    address_line2 = models.CharField(max_length=100, blank=True, verbose_name='Address Line 2')
    payment_recieved = models.DecimalField(default=0.0, verbose_name='Payment Recieved', max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail-party', kwargs={'pk':self.pk})

    @property
    def sale_amount(self):
        sale_amt = 0
        invoices = Invoice.objects.filter(party_name = self)
        for invoice in invoices:
            sale_amt += invoice.total
        return sale_amt
    
    @property
    def balance(self):
        return self.sale_amount-self.payment_recieved
    
class StockItem(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Enter Stock Item Name')
    choices = (('kg', 'kg'), ('pc', 'pc'), ('mtr', 'mtr'))
    per = models.CharField(max_length=10, choices=choices, blank=True, verbose_name='Enter Sale Method')
    hsncode = models.CharField(max_length=5, blank=True, verbose_name='Enter HSN/SAC Code')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-stock-item')

class Invoice(models.Model):
    date = models.DateField(default=None, blank=True)
    disp_thru = models.CharField(max_length=20, default=None, blank=True, verbose_name='Dispatched Through')
    party_name = models.ForeignKey(Party, on_delete=DO_NOTHING)
    bales = models.CharField(max_length=20, default=None, blank=True)
    delivery = models.CharField(max_length=20, blank=True, default=None, verbose_name='Destination')

    def __str__(self):
        return (self.party_name.name + '-' + str(self.date) + '/' + str(self.id))

    def get_absolute_url(self):
        return reverse('detail-invoice', kwargs={'pk':self.pk})

    @property
    def total(self):
        total = 0
        for item in InvoiceItem.objects.filter(invno=self.id):
            total+=item.price
        return total

class InvoiceItem(models.Model):
    invno = models.ForeignKey(Invoice, blank=True, on_delete=DO_NOTHING, default=None)
    stockitem = models.ForeignKey(StockItem, blank = True, on_delete=DO_NOTHING)
    rate = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=1000, blank = True)

    @property
    def price(self):
        return self.rate * self.quantity
    
    def get_absolute_url(self):
        x = int(str(self.invno).split("/", 1)[1])
        return reverse('detail-invoice', kwargs={'pk':x})