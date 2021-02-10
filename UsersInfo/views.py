import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Schema
from .forms import SchemaForm, UserRegisterForm, UserLoginForm
from django.views.generic import UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class UpdateScheme(LoginRequiredMixin, UpdateView):
    model = Schema
    template_name = 'newSchemas.html'
    form_class = SchemaForm


class DeleteSchema(DeleteView, LoginRequiredMixin):
    model = Schema
    template_name = 'deleteSchema.html'
    success_url = '/home'


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'incorrect data')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'Auth/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('/home')


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your account has been successfully registered')
            return redirect('/login')
        else:
            messages.error(request, 'incorrect data')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'Auth/register.html', context)


def index(request):
    items = Schema.objects.order_by('id')
    context = {'username': request.user.username, 'items': items}
    return render(request, 'index.html', context)


def schemas(request):
    items = Schema.objects.order_by('id')
    context = {'username': request.user.username, 'items': items}
    return render(request, 'dataSets.html', context)


@login_required
def add_new_schema(request):
    error = ''
    if request.method == 'POST':
        form = SchemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            error = 'wrong data'
    form = SchemaForm()
    context = {'form': form, 'error': error, 'username': request.user.username}
    return render(request, 'newSchemas.html', context)


@login_required
def export_to_csv(request, pk):
    schema_id = pk
    name_schema = Schema.objects.get(id=schema_id)
    filename = str(name_schema)
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Name schema', 'First name', 'Last name', 'Phone number', 'Email', 'Address', 'Age', 'Job', 'Company'])
    for user_form in Schema.objects.filter(id=schema_id).values_list('name_schema', 'first_name', 'last_name', 'phone_number', 'email',
                                                                     'address', 'age', 'job', 'company'):
        writer.writerow(user_form)
    response['Content-Disposition'] = f'attachment; filename = {filename}.csv'
    return response
