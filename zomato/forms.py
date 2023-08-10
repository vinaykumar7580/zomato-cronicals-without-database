from django import forms
# from .views import menu

class NewDishForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(decimal_places=2)
    availability = forms.BooleanField(required=False)



class OrderForm(forms.Form):
    def __init__(self, menu_choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_name'] = forms.CharField(max_length=100)
        self.fields['selected_dishes'] = forms.MultipleChoiceField(choices=menu_choices)



class UpdateStatusForm(forms.Form):
    STATUS_CHOICES = [
        ('preparing', 'Preparing'),
        ('ready', 'Ready for Pickup'),
        ('delivered', 'Delivered'),
    ]
    new_status = forms.ChoiceField(choices=STATUS_CHOICES)
