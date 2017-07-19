from django.db import models
from rolemgmt.models import Base
from django.contrib.auth.models import User


POSITION_STATUS = (
    (1, 'OPEN'), (2, 'HOLD'), (3, 'RESUME'), (4, 'CLOSED'),
)

RESUME_STATUS = (
    (1, 'Line Up'),
    (2, 'Technical Interview'),
    (3, 'HR Interview'),
    (4, 'Conditional Offer Letter'),
    (5, 'Client Short Listing'),
    (6, 'Client Interview Scheduled'),
    (7, 'Client Interview Done'),
    (8, 'Client Shortlisted'),
    (9, 'Joined'),
)

APPROVAL_STATUS = (
    (1, 'Pending'),
    (2, 'Approved'),
    (3, 'Rejected'),
)

# INTERVIEW_STATUS = (
#     (1, 'Scheduled'),
#     (2, 'Participated'),
#     (3, 'Not Participated'),
#     (4, 'Selected'),
#     (5, 'Rejected'),
#     (6, 'Re-Scheduled'),
# )

INTERVIEW_STATUS = (
    (1, 'Scheduled'),
    (2, 'Selected'),
    (3, 'Rejected'),
)


class UserProfile(Base):
    """
    Registered user profile table structure.
    """
    user = models.ForeignKey(User, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self, ):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class Client(Base):
    """
    This table will store the basic client details.
    """
    name = models.CharField("Client Name", max_length=100, unique=True)
    desc = models.TextField("About Client", blank=True,
                            null=True, max_length=500)
    location = models.CharField("Client Location", max_length=100)
    active = models.BooleanField(default=True)
    # created_by = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self, ):
        return "{} - {}".format(self.name, self.location)


class Requirement(Base):
    """
    Capture all the client requirement details.
    """
    client = models.ForeignKey(Client, blank=True, null=True)
    name = models.CharField("Group Name", max_length=100)
    position_name = models.CharField("Position Name", max_length=100)
    desc = models.TextField("About Position", max_length=500,
                            blank=True, null=True)
    skills = models.CharField("Primary Skills", max_length=200,
                              help_text="Ex: Python, Django, etc,..")
    duration = models.CharField("Duration", max_length=20,
                                help_text="Ex: 0 M / 0 Y")
    no_of_position = models.PositiveIntegerField(blank=True, null=True,
                                                 verbose_name="No of Position")
    open_position = models.PositiveIntegerField(blank=True, null=True,
                                                verbose_name="Open Position")
    location = models.CharField("Location", max_length=200)
    position_status = models.IntegerField(choices=POSITION_STATUS)
    min_exp = models.CharField("Minimum Experience", max_length=50,
                               help_text="Ex: 0 M / 0 Y")
    annual_billing = models.CharField("Annual Billing(INR)", max_length=100,
                                      help_text="Ex: 0.0 L")
    remarks = models.TextField(max_length=500, blank=True, null=True)
    created_by = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self, ):
        return "{} - {}".format(self.client.name,
                                self.position_name, )


class ResumeManagement(Base):
    """
    Candidate profile details table.
    """
    requirement = models.ForeignKey(Requirement, verbose_name="Requirement")
    first_name = models.CharField("First Name", max_length=100, )
    last_name = models.CharField("Last Name", max_length=100, )
    email = models.EmailField("Email", blank=True, null=True,
                              help_text="example@domain.com")
    mobile = models.CharField("Mobile Number", max_length=50,
                              blank=True, null=True,
                              help_text="Only 10 digits. Ex: 0000000000")
    skills = models.CharField("Skills", max_length=200,
                              blank=True, null=True,
                              help_text="Ex: Python, Django, etc,...")
    experience = models.CharField("Year's of Experience",
                                  max_length=50, blank=True, null=True,
                                  help_text="Ex: 0 M / 0 Y / 0.0 Y")
    dob = models.DateField(blank=True, null=True,
                           verbose_name="Date of Birth",
                           help_text="Ex: MM/DD/YYYY")
    ctc = models.CharField("CTC", max_length=20, help_text="Ex: 0.0 L")
    ectc = models.CharField("ECTC", max_length=20, help_text="Ex: 0.0 L")
    notice_period = models.CharField("Notice Period", max_length=20,
                                     blank=True, null=True,
                                     help_text="Ex: 0 D / 0 M")
    current_location = models.CharField("Current Location", max_length=100,
                                        blank=True, null=True)
    status = models.IntegerField(choices=RESUME_STATUS)
    remarks = models.TextField(max_length=500, blank=True, null=True)
    resume = models.FileField(upload_to='static/uploads/',
                              blank=True, null=True)
    # created_by = models.ForeignKey(User, blank=True, null=True)
    # is_blocked = models.BooleanField(default=False)

    def __unicode__(self, ):
        return "{} {}".format(self.first_name, self.last_name)

    def get_is_status(self, ):
        try:
            isstatus = InterviewSchedule.objects.get(candidate=self)
        except Exception:
            isstatus = ""
        return isstatus

    def get_resume_history(self, ):
        return InterviewScheduleHistory.objects.filter(
            ischedule__candidate=self)


class HRManagement(Base):
    """
    Detailing conditional offer letter.
    """
    resume = models.ForeignKey(ResumeManagement, blank=True, null=True)
    offered_ctc = models.CharField("Offered CTC", max_length=50,
                                   blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    remarks = models.TextField(max_length=500, blank=True, null=True)
    approval_status = models.IntegerField(choices=APPROVAL_STATUS,
                                          blank=True, null=True)
    created_by = models.ForeignKey(User, blank=True, null=True,
                                   related_name="%(class)s_related_to_created")
    approved_by = models.ForeignKey(
        User, blank=True, null=True,
        related_name="%(class)s_related_to_approved")

    def __unicode__(self, ):
        return "{} {}".format(self.resume.first_name, self.resume.email)


class InterviewSchedule(Base):
    """
    Here we are tracking all the interview schedule's.
    """
    candidate = models.ForeignKey(ResumeManagement, blank=True, null=True)
    requirement = models.ForeignKey(Requirement, blank=True, null=True)
    scheduled_by = models.ForeignKey(User, blank=True, null=True)
    scheduled_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=INTERVIEW_STATUS,
                                 blank=True, null=True)

    def __unicode__(self, ):
        return "{}".format(self.candidate.first_name)


class InterviewScheduleHistory(Base):
    """
    All the interview schedule history details has stored.
    """
    ischedule = models.ForeignKey(InterviewSchedule,
                                  blank=True, null=True)
    resume_status = models.IntegerField(choices=RESUME_STATUS,
                                        blank=True, null=True)
    interview_status = models.IntegerField(choices=INTERVIEW_STATUS,
                                           blank=True, null=True)
    remarks = models.TextField(max_length=500,
                               blank=True, null=True)
    date = models.DateTimeField(blank=True,
                                null=True)

    def __unicode__(self, ):
        return "{}".format(self.ischedule.scheduled_by.get_full_name())

