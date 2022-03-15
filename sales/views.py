from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin

from . forms import *
from . models import *
from . num2wrd import number_to_word
""" import weasyprint
import os
os.add_dll_directory(r"E:\Apps\GTK3-Runtime Win64\bin") """

# Create your views here.

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'sales/login.html'
    success_url = 'home'

    def form_valid(self, form):
        form_data = form.cleaned_data
        user = authenticate(username = form_data['username'], password = form_data['password'])
        if user is not None:
            auth_login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, "Invalid Credentials!!")
            return redirect('login')


@login_required(login_url = 'login')
def home(request):
    return render(request, 'sales/home.html')

def signout(request):
    if request.user.is_anonymous:
        pass
    else:
        logout(request)
        messages.success(request, "You Have Been Successfully Logged Out!!")
    return redirect('login')

class PartyCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Party
    form_class = PartyCreateForm

class PartyDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Party
    def get_context_data(self, *args, **kwargs):
        context = super(PartyDetailView, self).get_context_data(*args, **kwargs)
        party_name = Party.objects.get(name = self.object).id
        context['inv_list'] = Invoice.objects.filter(party_name = party_name)
        return context

class PartyListView(ListView):
    model = Party
    ordering = ['name']
    paginate_by = 10

class PartyUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Party
    fields = ['phone', 'address_line1', 'address_line2']

class PartyPaymentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Party
    fields = ['payment_recieved']

class StockItemCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = StockItem
    form_class = StockItemCreateForm

class StockItemListView(ListView):
    model = StockItem
    ordering = ['name']
    paginate_by = 10

class StockItemUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = StockItem
    fields = ['per', 'hsncode']

class InvoiceCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Invoice
    form_class = InvoiceForm

class InvoiceUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Invoice
    fields = ['party_name', 'date', 'disp_thru', 'bales', 'delivery']

class InvoiceDetailView(DetailView):
    # login_url = 'login'
    model = Invoice
    def get_context_data(self, *args, **kwargs):
        context = super(InvoiceDetailView, self).get_context_data(*args, **kwargs)
        invno = Invoice.objects.get(id = self.object.id).id
        context['inv_list'] = InvoiceItem.objects.filter(invno = invno)
        return context

class InvoiceItemCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = InvoiceItem
    form_class = InvoiceItemForm
    
    def form_valid(self, form):
        form.instance.invno = Invoice.objects.get(id = self.request.path.split('/')[-1])
        return super().form_valid(form)

class InvoiceItemUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = InvoiceItem
    fields = ['rate', 'quantity', 'description']

class InvoiceItemDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = InvoiceItem
    
    def get_success_url(self):
        x = int(str(self.object.invno).split("/", 1)[1])
        return reverse('detail-invoice', kwargs={'pk':x})

#@login_required(login_url = 'login')
def invoiceView(request, pk):
    invoice = Invoice.objects.get(id=pk)
    invoiceitems = InvoiceItem.objects.filter(invno = pk)
    """ weasyprint.HTML('sales/invoice.html', {'invoice':invoice, 'invoiceitems':invoiceitems, 'num2wrd':number_to_word(invoice.total)}).write_pdf(f'D:/ATC/Party/{invoice.party_name}/{invoice}.pdf') """
    return render(request, 'sales/invoice.html',{'invoice':invoice, 'invoiceitems':invoiceitems, 'num2wrd':number_to_word(invoice.total)})