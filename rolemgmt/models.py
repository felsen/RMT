from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Base(models.Model):
    """
    This is the base models, which is used for common field's:
    """
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Menu(Base):
    """
    All the menus which is required for RMT:
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField("SEO friendly URL, use alphabets and hyphen",
                            blank=True, null=True)
    parent = models.ForeignKey("self", blank=True, null=True)
    link = models.CharField("Link", max_length=100, blank=True, null=True)
    active = models.IntegerField(default=2)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "1. Menus"

    def __unicode__(self, ):
        return "{} - {}".format(self.name, self.slug)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.link = self.slug
        super(Menu, self).save(*args, **kwargs)


class Role(Base):
    """
    Defining all the roles required for RMT:
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField("SEO friendly URL, use alphabets and hyphen",
                            blank=True, null=True)
    link = models.CharField("Link", max_length=100, blank=True, null=True)
    active = models.IntegerField(default=2)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "2. Roles"

    def __unicode__(self, ):
        return "{} - {}".format(self.name, self.slug)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.link = self.slug
        super(Role, self).save(*args, **kwargs)


class RoleMenu(Base):
    """
    Menu will be defined for each role's:
    """
    role = models.ForeignKey(Role)
    menu = models.ManyToManyField(Menu, blank=True, null=True)
    active = models.IntegerField(default=2)

    class Meta:
        verbose_name_plural = "3. Role Menus"

    def __unicode__(self, ):
        return "{}".format(self.role.name)


class RoleConfig(Base):
    """
    Defining each user with the specific roles and the permitted to
    access menu's:
    """
    user = models.ForeignKey(User)
    role = models.ForeignKey(Role, blank=True, null=True)
    active = models.IntegerField(default=2)

    class Meta:
        verbose_name_plural = "4. Role Configurations"

    def __unicode__(self, ):
        return "{}".format(self.user.get_full_name())

    def get_user_menus(self, ):
        if self.user.is_active and self.user.is_staff:
            rmenu = RoleMenu.objects.get(role=self.role)
            return rmenu.menu.all()
        return []

