from django import forms
from models import ResumeManagement, Client, \
    Requirement, RESUME_STATUS

RS = {
    1: ((2, 'Technical Interview'), ),
    2: ((3, 'HR Interview'), ),
    3: ((4, 'Conditional Offer Letter'), ),
    4: ((5, 'Client Short Listing'), ),
    5: ((6, 'Client Interview Scheduled'), ),
    6: ((7, 'Client Interview Done'), ),
    7: ((8, 'Client Shortlisted'), ),
}

INTERVIEW_STATUS = (
    (2, 'Selected'),
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
                  'notice_period', 'current_location',
                  'remarks', 'resume', )


class ISForm(forms.Form):
    """
    Interview schedule and status changing form.
    """
    def __init__(self, *args, **kwargs):
        resume = kwargs.pop("resume_id")
        resume = ResumeManagement.objects.get(id=int(resume))
        super(ISForm, self).__init__(*args, **kwargs)
        self.fields['status'].choices = RS.get(resume.status)
        for label in self.fields:
            self.fields[label].widget.attrs['class'] = 'form-control input-sm'

    status = forms.ChoiceField(required=True,
                               choices=RESUME_STATUS)
    scheduled_date = forms.DateTimeField(required=True)
    remarks = forms.CharField(required=True)


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
