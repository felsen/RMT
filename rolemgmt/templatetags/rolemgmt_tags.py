from django import template
from rolemgmt.models import RoleConfig, Role
from rmtmgmt.models import UserProfile
from django.core.exceptions import MultipleObjectsReturned
register = template.Library()


@register.filter
def get_user_menus(request):
    try:
        rconf = RoleConfig.objects.get(user=request.user)
        rconf = rconf.get_user_menus().order_by("order")
    except (RoleConfig.DoesNotExist, AttributeError):
        rconf = []
    return rconf


@register.filter
def get_role(user):
    try:
        role = RoleConfig.objects.get(user=user)
        role = role.role.name
    except RoleConfig.DoesNotExist:
        role = ""
    return role


@register.filter(name='mobile')
def get_user_mobile(user):
    try:
        up = UserProfile.objects.get(user=user)
        up = up.mobile
    except UserProfile.DoesNotExist:
        up = None
    except MultipleObjectsReturned:
        up = None
    return up


@register.assignment_tag
def selected(user, role):
    available = False
    try:
        RoleConfig.objects.get(user=user, role=role)
        available = True
    except (RoleConfig.DoesNotExist):
        available = False
    return available

