from django import forms
from django.core.exceptions import ValidationError
from models import ResumeManagement, Client, \
    Requirement, RESUME_STATUS

RS = {
    1: ((2, 'Technical Interview'), ),
    2: ((3, 'HR Interview'), ),
    3: ((4, 'Conditional Offer Letter'), ),
    4: ((5, 'Client Short Listing'), ),
    5: ((6, 'Client Interview Schedule'), ),
    6: ((7, 'Client Interview Done'), ),
    7: ((8, 'Client Shortlisted'), ),
    8: ((9, 'Joining'), )
}

INTERVIEW_STATUS = (
    (2, 'Selected'),
    (3, 'Rejected'),
)

INTERVIEW_NEW_STATUS = (
    (1, 'Schedule'),
    (2, 'Selected'),
    (3, 'Rejected'),
)

INTERVIEW_APPROVAL_STATUS = (
    (2, 'Approval'),
    (3, 'Rejected'),
)


class ClientForm(forms.ModelForm):
    """
    Client model form fields are defined here.
    """
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for label in self.fields:
            self.fields[label].widget.attrs['class'] = 'form-control input-sm'

    class Meta:
        model = Client
        fields = ('name', 'location', 'desc', )
        exclude = ('active', )


class RequirementForm(forms.ModelForm):
    """
    Client Requirement form fields are defined here.
    """
    def __init__(self, *args, **kwargs):
        super(RequirementForm, self).__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.filter(active=True)
        for label in self.fields:
            self.fields[label].widget.attrs['class'] = 'form-control input-sm'

    class Meta:
        model = Requirement
        fields = ('client', 'name', 'position_name',
                  'skills', 'duration', 'no_of_position',
                  'open_position', 'location', 'min_exp',
                  'annual_billing', 'desc', 'remarks',
                  'position_status', )


class ResumeManagementForm(forms.ModelForm):
    """
    Resume management form fields are defined here.
    """
    def __init__(self, *args, **kwargs):
        super(ResumeManagementForm, self).__init__(*args, **kwargs)
        for label in self.fields:
            self.fields[label].widget.attrs['class'] = 'form-control input-sm'

    class Meta:
        model = ResumeManagement
        fields = ('requirement', 'first_name', 'last_name', 'email',
                  'mobile', 'skills', 'experience', 'dob', 'ctc', 'ectc',
                  'notice_period', 'current_location', 'remarks', 'resume', )

    def clean_email(self, ):
        email = self.cleaned_data.get("email")
        resume = ResumeManagement.objects.filter(
            email=email).exclude(freeze=True).exists()
        if resume:
            raise ValidationError("Email already exists.!")
        return email

    def clean_mobile(self, ):
        mobile = self.cleaned_data.get("mobile")
        resume = ResumeManagement.objects.filter(
            mobile=mobile).exclude(freeze=True).exists()
        if resume:
            raise ValidationError("Mobile Number already exists.!")
        return mobile


class ISNForm(forms.Form):
    """
    Interview schedule new form for after the status 6.
    """
    def __init__(self, *args, **kwargs):
        resume = kwargs.pop('resume_id')
        resume = ResumeManagement.objects.get(id=int(resume))
        super(ISNForm, self).__init__(*args, **kwargs)
        self.fields['resume_status'].choices = RS.get(resume.status)
        if resume.status == 6:
            self.fields['interview_status'].choices = INTERVIEW_STATUS
        if resume.status == 8:
            self.fields['interview_status'].choices = INTERVIEW_APPROVAL_STATUS
        for label in self.fields:
            self.fields[label].widget.attrs['class'] = 'form-control input-sm'

    resume_status = forms.ChoiceField(required=True,
                                      choices=RESUME_STATUS)
    interview_status = forms.ChoiceField(required=True,
                                         choices=INTERVIEW_NEW_STATUS)
    remarks = forms.CharField(required=True)
    date = forms.DateTimeField(label="Date", required=True)

    class Meta:
        fields = ("resume_status", "interview_status", "date", "remarks", )


class ISForm(forms.Form):
    """
    Interview schedule and status changing form.
    """
    def __init__(self, *args, **kwargs):
        resume = kwargs.pop("resume_id")
        resume = ResumeManagement.objects.get(id=int(resume))
        super(ISForm, self).__init__(*args, **kwargs)
        self.fields['resume_status'].choices = RS.get(resume.status)
        if resume.status == 3:
            self.fields['interview_status'].choices = INTERVIEW_APPROVAL_STATUS
        for label in self.fields:
            self.fields[label].widget.attrs['class'] = 'form-control input-sm'

    resume_status = forms.ChoiceField(required=True,
                                      choices=RESUME_STATUS)
    interview_status = forms.ChoiceField(required=True,
                                         choices=INTERVIEW_STATUS)
    remarks = forms.CharField(required=True)

    class Meta:
        fields = ("resume_status", "interview_status", "remarks", )


class ISUpdateForm(forms.Form):
    """
    Update the interview status.
    """
    def __init__(self, *args, **kwargs):
        super(ISUpdateForm, self).__init__(*args, **kwargs)
        for label in self.fields:
            self.fields[label].widget.attrs['class'] = 'form-control input-sm'

    status = forms.ChoiceField(required=True,
                               choices=INTERVIEW_STATUS)
    remarks = forms.CharField(required=True)


class CTCUpdateForm(forms.Form):
    """
    Update joining date and CTC for approved candidate.
    """
    def __init__(self, *args, **kwargs):
        super(CTCUpdateForm, self).__init__(*args, **kwargs)
        for label in self.fields:
            self.fields[label].widget.attrs["class"] = "form-control input-sm"

    offered_ctc = forms.IntegerField(label="Offered CTC", required=True)
    joining_date = forms.DateTimeField(label="Joining Date", required=True)

