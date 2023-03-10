from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet
from django.core.paginator import Paginator

from .decorators import status_validator
from .models import User, Account, VacationRequest
from .forms import VacationRequestForm

@login_required(login_url='login_user')
@status_validator
def home(request):
    user = get_object_or_404(User, pk=request.user.id)
    account = get_object_or_404(Account, user_id=request.user.id)
    if account.status is None:
        return render(request, 'vacation_management_app/no_permission.html')
    return render(request, 'vacation_management_app/home.html', {'user': user, 'account': account})


@login_required(login_url='login_user')
@status_validator
def vacation_request(request):
    form = VacationRequestForm(request.POST or None)
    account = get_object_or_404(Account, user_id=request.user.id)
    if account.status == Account.VIEWER:
        if request.method == "POST":
            messages.error(request, "Viewers are not allowed to send requests")
        return render(request, 'vacation_management_app/vacation_request.html', {'form': form, 'unavalaible': True})
    if request.method == "POST":
        if form.is_valid():
            try:
                form.clean_dates()
                form.save(user=request.user, account=account)
                messages.success(request, "Your request is submitted")
                return redirect('home')
            except ValidationError as e:
                messages.error(request, e.message)
        else:
            messages.error(request, "Something went wrong. Try again")
    return render(request, 'vacation_management_app/vacation_request.html', {'form': form})


@login_required(login_url='login_user')
@status_validator
def requests_list(request):
    statuses = {
        VacationRequest.WAITING: VacationRequest.WAITING,
        VacationRequest.APPROVED: VacationRequest.APPROVED,
        VacationRequest.REJECTED: VacationRequest.REJECTED,
        VacationRequest.CANCELLED: VacationRequest.CANCELLED,
    }
    leaveTypes = {
        VacationRequest.CASUAL: VacationRequest.CASUAL,
        VacationRequest.MEDICAL: VacationRequest.MEDICAL,
        VacationRequest.OPTIONAL: VacationRequest.OPTIONAL,
        VacationRequest.REGIONAL: VacationRequest.REGIONAL,
    }

    filtered_requests = QuerySet
    filtered_status = str()
    filtered_leaveType = str()
    if 'status' in request.GET:
        if request.GET['status'] in statuses.values():
            filtered_status = request.GET['status']
            filtered_requests = VacationRequest.objects.filter(
                user_id=request.user.id, status=filtered_status).order_by('-id')
    if 'leave_type' in request.GET:
        if request.GET['leave_type'] in leaveTypes.values():
            filtered_leaveType = request.GET['leave_type']
            filtered_requests = VacationRequest.objects.filter(
                user_id=request.user.id, leave_type=filtered_leaveType).order_by('-id')

    if filtered_requests == QuerySet:
        filtered_requests = VacationRequest.objects.filter(
            user_id=request.user.id).order_by('-id')
    amount_of_items = 3
    paginator = Paginator(filtered_requests, amount_of_items)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if page_number is None:
        page_number = 1
    requests = list(zip([x for x in range((amount_of_items * int(page_number)) -
                                          amount_of_items + 1, amount_of_items * int(page_number) + 1)], page_obj))
    return render(request, 'vacation_management_app/requests_list.html', {'requests': requests, 'statuses': statuses, 'leaveTypes': leaveTypes, 'page_obj': page_obj, 'filtered_status': filtered_status, 'filtered_leaveType': filtered_leaveType})


@login_required(login_url='login_user')
@status_validator
def users_list(request):
    users =  User.objects.all().values()
    print(">>>>>>>>>>>>>")
    print(User.objects.all().values())
    return render(user, 'vacation_management_app/users_list.html',{'users': users})