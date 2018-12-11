from django import forms

from .models import Post, Customer, Order, Good

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CustomerForm(forms.ModelForm):

	class Meta:
		model = Customer
		fields = ('name','phone_number','email','organization',)

class OrderForm(forms.ModelForm):

	class Meta:
		model = Order
		fields = ('form_of_payment','address','date_completed','delivery_type','notes')

class GoodForm(forms.ModelForm):

	class Meta:
		model = Good
		fields = ('name', 'description',)