
from django.contrib.auth.models import User, Permission, Group
from django.db import models
from django.db.models import Q

from sweettooth.extensions.models import ExtensionVersion, STATUSES

def get_all_reviewers():
    perm = Permission.objects.get(codename="can-review-extensions")

    # Dark magic to get all the users with a specific permission
    # Thanks to <schinckel> in #django
    groups = Group.objects.filter(permissions=perm)
    return User.objects.filter(Q(is_superuser=True)|Q(user_permissions=perm)|Q(groups__in=groups)).distinct()

class CodeReview(models.Model):
    reviewer = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank=True)
    version = models.ForeignKey(ExtensionVersion, related_name="reviews")
    new_status = models.PositiveIntegerField(choices=STATUSES.items(), null=True)
    auto = models.BooleanField(default=False)

    class Meta:
        permissions = (
            ("can-review-extensions", "Can review extensions"),
            ("trusted", "Trusted author"),
        )
