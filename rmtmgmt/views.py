from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from rmtmgmt.forms import ResumeManagementForm, \
    RequirementForm, ClientForm
from rmtmgmt.models import Client, Requirement, ResumeManagement
from rolemgmt.models import Role, RoleConfig
import json


@require_http_methods(['GET'])
@login_required(login_url='/user-login/')
def resume_mgmt(request, ):
    """
    Resume Management function's.
    """
    title = "Resume Management"
    resume = ResumeManagement.objects.all()
    return render(request, 'resume_mgmt.html', locals())


@require_http_methods(['GET', 'POST'])
@login_required(login_url='/user-login/')
def add_resume_mgmt(request, ):
    """
    Add Function for resume management,
    this function will be accessed by only specific roles.
    """
    title = "Add Resume Management"
    form = ResumeManagementForm()
    if request.method == "POST":
        form = ResumeManagementForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.status = 1
            f.save()
            return HttpResponseRedirect("/resume-management/")
    return render(request, 'add_resume_mgmt.html', locals())


@require_http_methods(['GET', 'POST'])
@login_required(login_url='/user-login/')
def edit_resume_mgmt(request, res_id=None):
    """
    Edit Resume Management function's.
    """
    title = "Edit Resume Management"
    res = ResumeManagement.objects.get(id=res_id)
    form = ResumeManagementForm(instance=res)
    if request.method == "POST":
        form = ResumeManagementForm(request.POST, request.FILES,
                                    instance=res)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/resume-management/")
    return render(request, 'add_resume_mgmt.html', locals())


@require_http_methods(['GET', ])
@login_required(login_url='/user-login/')
def requirement_mgmt(request, ):
    """
    Requirement Management functionalities.
    """
    title = "Requirement Management"
    req = Requirement.objects.all()
    return render(request, 'requirement_mgmt.html', locals())


@require_http_methods(['GET', 'POST', ])
@login_required(login_url='/user-login/')
def add_requirement_mgmt(request, ):
    """
    Add function for requirement management.
    """
    title = "Add Requirement Management"
    form = RequirementForm()
    if request.method == "POST":
        form = RequirementForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/requirement-management/")
    return render(request, 'add_requirement_mgmt.html', locals())


@require_http_methods(['GET', 'POST', ])
@login_required(login_url='/user-login/')
def edit_requirement_mgmt(request, req_id=None):
    """
    Edit Requirement Management function's.
    """
    title = "Edit Requirement Management"
    req = Requirement.objects.get(id=req_id)
    form = RequirementForm(instance=req)
    if request.method == "POST":
        form = RequirementForm(request.POST, instance=req)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/requirement-management/")
    return render(request, 'add_requirement_mgmt.html', locals())


@require_http_methods(['GET', 'POST', ])
@login_required(login_url='/user-login/')
def add_client_mgmt(request, ):
    """
    Add function for client management.
    """
    title = "Add Client"
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/client-management/")
    return render(request, 'add_client_mgmt.html', locals())


@require_http_methods(['GET', 'POST', ])
@login_required(login_url='/user-login/')
def edit_client_mgmt(request, client_id=None):
    """
    Add function for client management.
    """
    title = "Edit Client"
    client = Client.objects.get(id=client_id)
    form = ClientForm(instance=client)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/client-management/")
    return render(request, 'add_client_mgmt.html', locals())


@require_http_methods(['GET', ])
@login_required(login_url='/user-login/')
def status_client_mgmt(request, client_id=None):
    """
    Activating and deactivating the client services.
    """
    try:
        client = Client.objects.get(id=client_id)
        status = {True: False, False: True}
        client.active = status.get(client.active)
        client.save()
    except Client.DoesNotExist:
        client = None
    return HttpResponseRedirect("/client-management/")


@require_http_methods(['GET', ])
@login_required(login_url='/user-login/')
def client_mgmt(request, ):
    """
    Client Listing function's.
    """
    title = "Client"
    client = Client.objects.all()
    return render(request, 'client_mgmt.html', locals())


@require_http_methods(['GET', ])
@login_required(login_url='/user-login/')
def hr_mgmt(request, ):
    """
    HR Management listing function's.
    """
    title = "HR Management"
    return render(request, 'hr_mgmt.html', locals())


@require_http_methods(['GET', ])
@login_required(login_url='/user-login/')
def role_management(request, status=None):
    """
    Role management Listing function's.
    """
    title = "Role Management"
    user = User.objects.all().exclude(is_superuser=True)
    active_users = user.filter(is_active=True, is_staff=True)
    inactive_users = user.filter(is_active=False, is_staff=False)
    active_users_count = active_users.count()
    inactive_users_count = inactive_users.count()
    role = Role.objects.filter(active=2)
    if status == 'active':
        user_lst = active_users
    elif status == 'inactive':
        user_lst = inactive_users
    else:
        user_lst = []
    return render(request, 'rolemgmt.html', locals())


@require_http_methods(['GET', ])
@login_required(login_url='/user-login/')
def role_management_status(request, status=None, user_id=None):
    """
    Function to activate and deactivate user's.
    """
    change_status = {True: False, False: True}
    user = User.objects.get(id=user_id)
    user.is_active = change_status.get(user.is_active)
    user.is_staff = change_status.get(user.is_staff)
    user.save()
    url_status = {'activate': 'active', 'deactivate': 'inactive'}
    return HttpResponseRedirect(
        '/role-management/{}/'.format(url_status.get(status)))


@require_http_methods(['GET', ])
@login_required(login_url='/user-login/')
def interview_schedule(request, ):
    """
    Every day interview schdule function.
    """
    title = "Interview Schdule"
    return render(request, 'schedule.html', locals())


@require_http_methods(['GET', ])
@login_required(login_url='/user-login/')
def approvals(request, ):
    """
    Admin approval function's.
    """
    title = "Approval"
    return render(request, 'approvals.html', locals())


@require_http_methods(['GET', ])
@login_required(login_url='/user-login/')
def update_role(request, ):
    """
    Update the user role.
    """
    resp, success = {}, False
    role = request.GET.get('role')
    user = request.GET.get('user')
    if role and user:
        try:
            role_obj = Role.objects.get(id=int(role))
            user_obj = User.objects.get(id=int(user))
            role_conf, created = RoleConfig.objects.get_or_create(
                user=user_obj)
            role_conf.role = role_obj
            role_conf.save()
            success = True
        except (Role.DoesNotExist, User.DoesNotExist):
            success = False
    resp['success'] = success
    return HttpResponse(json.dumps(resp),
                        content_type="application/json")

