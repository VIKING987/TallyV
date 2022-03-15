from . import views
from django.urls import path

urlpatterns = [
    path('', views.LoginView.as_view(), name = 'login'),
    path('home', views.home, name = 'home'),
    path('signout', views.signout, name = 'signout'),

    path('create-party', views.PartyCreateView.as_view(), name='create-party'),
    path('detail-party/<int:pk>', views.PartyDetailView.as_view(), name = 'detail-party'),
    path('list-party', views.PartyListView.as_view(), name = 'list-party'),
    path('update-party/<int:pk>', views.PartyUpdateView.as_view(), name = 'update-party'),
    path('update-payment/<int:pk>', views.PartyPaymentUpdateView.as_view(), name = 'update-payment'),

    path('create-stock-item', views.StockItemCreateView.as_view(), name='create-stock-item'),
    path('list-stock-item', views.StockItemListView.as_view(), name = 'list-stock-item'),
    path('update-stock-item/<int:pk>', views.StockItemUpdateView.as_view(), name = 'update-stock-item'),

    path('create-invoice', views.InvoiceCreateView.as_view(), name='create-invoice'),
    path('detail-invoice/<int:pk>', views.InvoiceDetailView.as_view(), name='detail-invoice'),
    path('update-invoice/<int:pk>', views.InvoiceUpdateView.as_view(), name='update-invoice'),
    path('create-invoiceitem/<int:pk>', views.InvoiceItemCreateView.as_view(), name='create-invoiceitem'),
    path('update-invoiceitem/<int:pk>', views.InvoiceItemUpdateView.as_view(), name='update-invoiceitem'),
    path('delete-invoiceitem/<int:pk>', views.InvoiceItemDeleteView.as_view(), name='delete-invoiceitem'),
    path('print-invoice/<int:pk>', views.invoiceView, name='print-invoice'),
]