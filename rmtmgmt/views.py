from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph
from dateutil.parser import parse
import datetime
import os

from rmtmgmt.forms import ResumeManagementForm, \
    RequirementForm, ClientForm, ISForm, \
    ISUpdateForm, CTCUpdateForm
from rmtmgmt.models import Client, Requirement, \
    ResumeManagement, InterviewSchedule, \
    HRManagement
from rolemgmt.models import Role, RoleConfig
import json


def send_email_rmt(resume, email, content):
    """
    sending email based in resume status.
    """
    sender = "felix.stephen@brisatech.com"
    to = "felix.stephen@brisatech.com"
    subject = "Technical Interview"
    message = "Hi, Interview scheduled at 2 PM."
    email = EmailMessage(subject, message, sender, [to])
    email.attach_file("/home/felsen/questions.txt")
    email.send()


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
            f = form.save(commit=False)
            f.created_by = request.user
            f.save()
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
    hrmgmt = HRManagement.objects.all()
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
    schedule = InterviewSchedule.objects.filter(
        status=1,
    ).exclude(candidate__status=4)
    return render(request, 'schedule.html', locals())


@require_http_methods(['GET', ])
@login_required(login_url='/user-login/')
def approvals(request, ):
    """
    Admin approval function's.
    """
    title = "Approval"
    approval = HRManagement.objects.all()
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


@require_http_methods(['GET', 'POST', ])
@login_required(login_url='/user-login/')
def update_resume_status(request, resume_id=None, req_id=None):
    """
    Updating the resume status / interview schedule.
    """
    title = "Update Interview Schedule"
    form = ISForm(resume_id=resume_id)
    if request.method == "POST":
        data = request.POST.copy()
        if data.get("resume_status") and data.get("interview_status") \
           and data.get("remarks"):
            try:
                resume = ResumeManagement.objects.get(id=int(resume_id))
                resume.status = int(data.get("resume_status"))
                resume.save()

                req = Requirement.objects.get(id=int(req_id))
                schedule = InterviewSchedule.objects.create(
                    candidate=resume,
                    requirement=req,
                )
                schedule.scheduled_by = request.user
                schedule.approved_by = request.user
                schedule.status = int(data.get("interview_status"))
                schedule.resume_status = int(data.get("resume_status"))
                schedule.remarks1 = data.get("remarks")
                schedule.save()

#                send_email_rmt(resume, data.get("email"), data.get("remarks"))

                if resume.status == 4:
                    HRManagement.objects.create(
                        resume=resume,
                        approval_status=1,
                        created_by=request.user,
                    )
            except Exception as e:
                pass
            return HttpResponseRedirect("/resume-management/")
    return render(request, 'is_status.html', locals())


@require_http_methods(['GET', 'POST', ])
@login_required(login_url='/user-login/')
def update_schedule(request, scheduled_id=None, req_id=None):
    """
    This function is for updating the interview status.
    """
    title = "Update Interview Status"
    form = ISUpdateForm()
    if request.method == "POST":
        form = ISUpdateForm(request.POST)
        if form.is_valid():
            try:
                candidate = ResumeManagement.objects.get(id=int(scheduled_id))
                isu = InterviewSchedule.objects.get(
                    candidate__id=int(scheduled_id),
                    requirement__id=int(req_id),
                    resume_status=candidate.status,
                )
                isu.status = request.POST.get("status")
                isu.remarks2 = request.POST.get("remarks")
                isu.save()
            except InterviewSchedule.DoesNotExist:
                pass
            return HttpResponseRedirect("/resume-management/")
    return render(request, "update_scheduled.html", locals())


@require_http_methods(['GET', ])
@login_required(login_url='/user-login/')
def interview_history(request, resume_id=None, req_id=None):
    """
    Function for all the interview status history.
    """
    title = "Interview History"
    history = InterviewSchedule.objects.filter(
        candidate__id=resume_id,
        requirement__id=req_id).order_by("resume_status")
    return render(request, "interview_history.html", locals())


@require_http_methods(['GET', ])
@login_required(login_url='/user-login/')
def update_approval_status(request):
    """
    Update the COL approval status by Admin.
    """
    resp, success = {}, False
    status, user = request.GET.get("status"), request.GET.get("user")
    remarks = request.GET.get("remarks")
    if status and user and remarks:
        try:
            approval = HRManagement.objects.get(id=int(user))
            approval.approval_status = int(status)
            approval.remarks = remarks
            approval.approved_by = request.user
            approval.save()
            isu = InterviewSchedule.objects.get(candidate=approval.resume)
            isu.status = status
            isu.save()
            InterviewScheduleHistory.objects.create(
                ischedule=isu,
                resume_status=isu.candidate.status,
                interview_status=status,
                remarks=remarks,
                date=datetime.datetime.now(),
            )
            success = True
        except (HRManagement.DoesNotExist,
                InterviewSchedule.DoesNotExist,
                AttributeError):
            approval = None
    resp["success"] = success
    return HttpResponse(json.dumps(resp), content_type="application/json")


@require_http_methods(['GET', 'POST'])
@login_required(login_url='/user-login/')
def update_salary_details(request, hrmgmt_id=None):
    """
    Update the candidate joining_date and offered_ctc.
    """
    form = CTCUpdateForm()
    if request.method == "POST":
        data = request.POST.copy()
        salary = data.get("offered_ctc")
        joining = parse(data.get("joining_date"))
        if salary and joining:
            try:
                hr = HRManagement.objects.get(id=int(hrmgmt_id))
                hr.offered_ctc = salary
                hr.joining_date = joining
                hr.save()
            except Exception as e:
                pass
            return HttpResponseRedirect("/hr-management/")
    return render(request, 'salary.html', locals())


@require_http_methods(['GET', ])
@login_required(login_url='/user-login/')
def reports(request, status=None):
    """
    This is the function will track the reports.
    """
    title = "Reports"
    if status == "resume":
        resume_status = Requirement.objects.all()
    elif status == "requirement":
        requirement_status = Requirement.objects.all()
    return render(request, 'reports.html', locals())


def createParagraph(c, text, x, y):
    """
    Creating the paragraph text.
    """
    style = getSampleStyleSheet()
    width, height = letter
    p = Paragraph(text, style=style["Normal"])
    p.wrapOn(c, width, height)
    p.drawOn(c, x, y, mm)


def createBulletListParagraph(c, text, x, y):
    """
    Creating the bullet text line.
    """
    style = getSampleStyleSheet()
    width, height = letter
    p = Paragraph(text, style=style["Normal"], bulletText='&bull')
    p.wrapOn(c, width, height)
    p.drawOn(c, x, y, mm)


@require_http_methods(['GET', ])
def generate_col_letter(request, hrmgmt_id=None):
    """
    Generate COL Letter for candidate.
    """
    hr, first_name, last_name, offered_ctc, joining_date, ref_id \
        = "", "", "", "", "", ""
    try:
        hr = HRManagement.objects.get(id=int(hrmgmt_id))
    except HRManagement.DoesNotExist:
        hr = hr
    if hr:
        client = hr.resume.requirement.client.name
        first_name = hr.resume.first_name
        last_name = hr.resume.last_name
        offered_ctc = hr.offered_ctc
        joining_date = hr.joining_date.strftime("%d/%m/%Y")
        s = "{}".format(client)
        ref_id = "Brisa/{}/{}/{}/{}".format("".join([i[0] for i in s.split()]),
                                            datetime.datetime.now().strftime("%b%Y"),
                                            "NE", 0)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}_{}_offer"'.format(first_name, last_name)
    p = canvas.Canvas(response)
    path = os.getcwd()
    image_path = os.path.abspath(path + "/static/images/logo.png")
    p.drawImage(image_path, 10, 770, width=155, height=60, mask=None)

    ptext = """<font name=Times-Bold color=black size=14>Brisa Technologies Pvt.Ltd.</font>"""
    createParagraph(p, ptext, 420, 815)
    ptext = """<font name=Times color=black size=12>No.90, 27th Main,</font>"""
    createParagraph(p, ptext, 420, 803)
    ptext = """<font name=Times color=black size=12>HSR Layout,Sector-1,</font>"""
    createParagraph(p, ptext, 420, 791)
    ptext = """<font name=Times color=black size=12>Bangalore-560 102</font>"""
    createParagraph(p, ptext, 420, 779)
    ptext = """<font name=Times color=black size=12>Phone:+91-80-42134897</font>"""
    createParagraph(p, ptext, 420, 767)
    ptext = """<font name=Times color=black size=12>website:www.brisa-tech.com</font>"""
    createParagraph(p, ptext, 420, 755)
    p.line(10, 740, 580, 740)
    ref_id = ref_id
    ptext = """<font name=Times-Bold color=black size=12>Ref: {}</font>""".format(ref_id)
    createParagraph(p, ptext, 50, 710)

    name = "{} {},".format(first_name, last_name)
    ptext = """<font name=Times-Bold color=black size=12>Dear {}</font>""".format(name)
    createParagraph(p, ptext, 50, 670)
    gen_date = datetime.datetime.now().strftime("%d/%m/%Y")
    ptext = """<font name=Times-Bold color=black size=12>{}</font>""".format(str(gen_date))
    createParagraph(p, ptext, 480, 710)
    p.drawString(50, 630, "As per our discussion with you, please find below the terms and conditions of your conditional")
    p.drawString(50, 605, "offer from Brisa Technologies Pvt. Ltd., Bangalore.")
    salary = offered_ctc
    ptext = """<bullet>&bull</bullet><font name=times-roman color=black size=14>Annual CTC would be INR {} /- per annum.</font> """.format(salary)
    createBulletListParagraph(p, ptext, 100, 570)
    ptext = """<bullet>&bull</bullet><font name=times-roman  size=14>Your Tentative Joining Date with Brisa Technologies would be {}.</font> """.format(joining_date)
    createBulletListParagraph(p, ptext, 100, 545)
    ptext = """<font name=Times-Bold color=black size=14>If your profile is shortlisted by our client, you will have to attend Face to</font>"""
    createParagraph(p, ptext, 50, 490)
    ptext = """<font name=Times-Bold color=black size=14>Face Interview during weekdays without fail.</font>"""
    createParagraph(p, ptext, 50, 465)
    p.drawString(50, 435, "We will extend a final offer of employment, subject to you clearing a series of internal and ")
    p.drawString(50, 420, "client interviews and your final selection. Please note that this is a conditional offer and does not ")
    p.drawString(50, 405, "constitute a contract of employment, with validity of 7 working days starting from date of issue.")
    stringLine = """Kindly send us an acknowledgment and confirm based on which we can process your CV """
    ptext = """<u><font name=Times-Bold color=black size=14>{}</font></u>""".format(stringLine)
    createParagraph(p, ptext, 50, 380)
    ptext = """<u><font name=Times-Bold color=black size=14>further to our client.</font></u>"""
    createParagraph(p, ptext, 50, 365)
    p.drawString(50,310,"For any clarification please feel free to call us at 080-42134897. ")
    ptext = """<font name=Times-Bold color=black size=14>Thanks! </font>"""
    createParagraph(p, ptext, 50, 240)
    ptext = """<font name=Times-Bold color=black size=14>HR Manager</font>"""
    createParagraph(p, ptext, 50, 220)
    ptext = """<font name=Times-Bold color=black size=14> Brisa Technologies Pvt. Ltd., Bangalore.</font>"""
    createParagraph(p, ptext, 50, 200)
    p.save()
    return response

