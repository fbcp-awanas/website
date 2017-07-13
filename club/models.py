from django.db import models
from django.utils.translation import gettext_lazy as _
import people

CLUBLIST = (
    ('A', 'Awanas'),
    ('P', 'Puggles'),
    ('C', 'Cubbies'),
    ('S', 'Sparks'),
    ('T', 'Truth & Training')
)


class Group(models.Model):
    name = models.CharField(max_length=20,
                            help_text="What should this club be called?")
    club = models.CharField(max_length=1,
                            choices=CLUBLIST,
                            default='A')
    age = models.CharField(max_length=10,
                           help_text="Age range for this group.",
                           blank=True, null=True)
    grades = models.CharField(max_length=10,
                              help_text="Grades included in this group.",
                              blank=True, null=True)
    leaders = models.ManyToManyField('people.Leader',
                                     related_name='group',
                                     blank=True)

    def list_awards(self):
        """ Get a list of all of the outstanding awards for this group """
        pass

    def list_clubbers(self):
        """ Quick interface to pull a list of clubbers assigned to this group """
        pass

    def get_attendance(self):
        """ View attendance by clubber for a given group """
        pass

    def __str__(self):
        return self.name


class Handbook(models.Model):
    name = models.CharField(max_length=30,
                            help_text="Name of the handbook")
    club = models.CharField(max_length=1,
                            choices=CLUBLIST,
                            help_text="What club is this book for?")
    entrance_book = models.BooleanField(default=False,
                                        help_text="Is this an entrance book?")
    # Need to know what these should be
    # extra_credit = 
    # verses = 
    inventory_number = models.IntegerField(help_text="Inventory number for this book",
                                           blank=True, null=True)

    def get_sections(self):
        return self.sections.select_related()

    def __str__(self):
        return (self.name)


class Section(models.Model):
    name = models.CharField(max_length=30,
                            help_text="Name of the section")
    book = models.name = models.ForeignKey('Handbook',
                                           related_name='sections',
                                           on_delete=models.CASCADE)
    content = models.TextField(help_text="What's in this section?",
                               blank=True, null=True)
    in_order = models.BooleanField(default=False,
                                   help_text="Does the section have to be done in order?")
    points = models.IntegerField(help_text="How many points is the section worth?",
                                 default=1)

    def __str__(self):
        return ('{}: {}'.format(self.book.name, self.name))
