# from django.forms import ModelForm
# from .models import Order


# class OrderForm(ModelForm):
#     class Meta:
#         model ='Order'
#         fields = '__all__'

from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order  # Corrected line: model = Order, not model = 'Order'
        fields = '__all__'
