from django import forms
from models import ResumeManagement, Client, \
    Requirement, INTERVIEW_STATUS


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
                  'resume', 'remarks',)


class ISForm(forms.ModelForm):
    """
    Interview schedule and status changing form.
    """
    def __init__(self, *args, **kwargs):
        super(ISForm, self).__init__(*args, **kwargs)
        for lable in self.fields:
            self.fields['label'].widget.attrs['class'] \
                = 'form-control input-sm'

    status = forms.ChoiceField(required=True,
                               choices=INTERVIEW_STATUS)
    scheduled_date = forms.DateTimeField(required=True)
    remarks = forms.CharField(required=True)

