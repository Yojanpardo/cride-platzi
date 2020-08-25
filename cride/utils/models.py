"""Django models utilities"""

# Django
from django.db import models


class CRideModel(models.Model):
    """Comparte Ride base model.

    CRideModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + modified (DateTime): Store the datetime the object was modified
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was modified.'
    )

    class Meta:
        """Meta options"""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']


""" Example:
class Student(CRideModel):
    name = models.CharField()

    class Meta(CRideModel.META):
        db_table = 'students_table'


class Person(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()


class Student(Person):
    class Meta:
        proxy = True

    code = models.UUIDField(unique=True, default=uuid.uuid4)

    def study(self, subject):
        print('{} is studying {}'.format(self.first_name, subject))
"""
