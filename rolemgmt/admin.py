from django.contrib import admin
from models import Menu, Role, RoleConfig, RoleMenu


admin.site.register(Menu)
admin.site.register(Role)
admin.site.register(RoleMenu)
admin.site.register(RoleConfig)
