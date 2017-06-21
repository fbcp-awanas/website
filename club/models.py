from django.db import models
import people

class Group(models.Model):
    CLUBLIST = (
        ('A', 'Awanas'),
        ('P', 'Puggles'),
        ('C', 'Cubbies'),
        ('S', 'Sparks'),
        ('T', 'Truth & Training')
        )
    
    name = models.CharField(max_length=20,
                            help_text="What should this club be called?")
    club = models.CharField(max_length=1,
                            choices=CLUBLIST,
                            default='A')
    age = models.CharField(max_length=10,
                           help_text="Age range for this group.")
    grades = models.CharField(max_length=10,
                              help_text="Grades included in this group.")
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