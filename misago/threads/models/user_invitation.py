from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class UserInvitation(models.Model):
    invited_email = models.CharField(max_length=64)
    invitor_id = models.PositiveIntegerField()
    created_on = models.DateTimeField(db_index=True)
    updated_on = models.DateTimeField()


    class Meta:
        indexes = [
            models.Index(fields=['invited_email']),
        ]

    def __str__(self):
        return '%s...' % self.invited_email
