from collections import namedtuple

from django.db import models

from .validators import validate_file_extension
from .tasks import send_invitation_task


class Authenticator(models.Model):
    file = models.FileField(validators=[validate_file_extension])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Authenticator, self).save()
        self.auth_users_from_file(self.id)

    @staticmethod
    def auth_users_from_file(authenticator_id):
        Person = namedtuple('Person', 'first_name last_name email')
        file = Authenticator.objects.get(id=authenticator_id).file
        for line in file.readlines():
            line = str(line, 'utf-8')
            person = Person(*line.split())
            send_invitation_task.delay(person.first_name, person.last_name,
                                       person.email)
