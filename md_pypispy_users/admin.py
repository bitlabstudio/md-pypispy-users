"""Admin classes for the ``md-pypispy-users`` app."""
from django.contrib import admin

from md_pypispy_users.models import UserCount


admin.site.register(UserCount)
