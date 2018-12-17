from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Order, Good

from .forms import CustomerForm, OrderForm, GoodForm
##########################
def create_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm()
    return render(request, 'blog/customer_edit.html', {'form': form})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'blog/customer_detail.html', {'customer': customer})

def customer_list(request):
    customers = Customer.objects.order_by('name')
    return render(request, 'blog/customer_list.html', {'customers': customers})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('customer_list')
"""
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            post.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'blog/customer_edit.html', {'form': form})
"""
##########################
def add_order_to_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.cust_id = customer
            order.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = OrderForm()
    return render(request, 'blog/add_order_to_customer.html', {'form': form})
##########################
def good_create(request):
    if request.method == "POST":
        form = GoodForm(request.POST)
        if form.is_valid():
            good = form.save(commit=False)
            good.save()
            return redirect('good_detail', pk=good.pk)
    else:
        form = GoodForm()
    return render(request, 'blog/good_edit.html', {'form': form})

def good_detail(request, pk):
    good = get_object_or_404(Good, pk=pk)
    return render(request, 'blog/good_detail.html', {'good': good})

def good_list(request):
    goods = Good.objects.order_by('name')
    return render(request, 'blog/good_list.html', {'goods': goods})

def good_buy(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'blog/good_buy.html', {'order':order})

##########################
def bucket(request):
    orders = Order.objects.order_by('cust_id')
    return render(request, 'blog/bucket.html', {'orders':orders})

def checked_and_delivered(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('bucket')
##########################
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

"""
def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('')
	else:
		form = UserCreationForm()
		args = {'form':form}
		return render(request, 'blog/reg_form.html', args)
"""
def view_spec_list(request, number, pk):
    if number == 1:
        goods = Good.objects.get(name='apelsin')
        return render(request, 'blog/spec_num_list.html', {'goods': goods})
    if number == 2;
        posts = Post.objects.order_by('published_date')[0:1].get()
        return render(request, 'blog/post_draft_list.html', {'posts': posts})
    if number == 3:
        customers = Customer.objects.get(name__exact="Sergey")
        return render(request, 'blog/spec_num_list.html', {'customers': customers})
    if number == 4:
        entries = Entry.objects.select_related().get(id=pk)
        return render(request, 'blog/spec_num_list.html', {'entries': entries})
