from django.db import models
from django.template.defaultfilters import slugify
import datetime as dt
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import itertools

# Create your models here.

GROUPLIST = (
    ('A', 'Awanas'),
    ('P', 'Puggles'),
    ('C', 'Cubbies'),
    ('S', 'Sparks'),
    ('T', 'Truth & Training')
    )

class A_Person(models.Model):
    """ Abstract class defining name fields """

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    @property
    def full_name(self):
        return "{s.first_name} {s.last_name}".format(s=self)

    def __str__(self):
        return self.full_name
    __str__.short_description = 'Full Name'
    __str__.admin_order_field = 'last_name'

    class Meta:
        abstract = True


class A_Contact(models.Model):
    """ Abstract class defining address/phone/email fields """

    STATES = (
        ('TX', 'Texas'),
        ('AK', 'Alaska'),
        ('AL', 'Alabama'),
        ('AR', 'Arkansas'),
        ('AZ', 'Arizona'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DC', 'District of Columbia'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('GU', 'Guam'),
        ('HI', 'Hawaii'),
        ('IA', 'Iowa'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('MA', 'Massachusetts'),
        ('MD', 'Maryland'),
        ('ME', 'Maine'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MO', 'Missouri'),
        ('MS', 'Mississippi'),
        ('MT', 'Montana'),
        ('NA', 'National'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('NE', 'Nebraska'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NV', 'Nevada'),
        ('NY', 'New York'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('PR', 'Puerto Rico'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('UT', 'Utah'),
        ('VA', 'Virginia'),
        ('VT', 'Vermont'),
        ('WA', 'Washington'),
        ('WI', 'Wisconsin'),
        ('WV', 'West Virginia'),
        ('WY', 'Wyoming')
    )

    address = models.CharField(max_length=50,
                               help_text="Street number and name")
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2,
                             choices=STATES,
                             default="TX")
    zip = models.CharField(max_length=5,
                           help_text="Five-digit zip code")
    phone = models.CharField(max_length=15)
    
    class Meta:
        abstract = True


class Child(A_Person):
    COLORS = (('R', 'Red'),
              ('B', 'Blue'),
              ('Y', 'Yellow'),
              ('G', 'Green')
              )
    
    GRADES = [(i, v) for i, v in enumerate(['Kindergarten', 
                                            'First', 
                                            'Second', 
                                            'Third', 
                                            'Fourth', 
                                            'Fifth', 
                                            'Sixth'])]
    
    family = models.ForeignKey('Family',
                               on_delete=models.CASCADE,
                               null=True,
                               related_name='children')
    dob = models.DateField(verbose_name="Date of Birth")
    grade = models.IntegerField(choices=GRADES)
    gender = models.CharField(max_length=1,
                              choices=(("M", "Male"),
                                       ("F", "Female"))
                             )
    allergies = models.TextField(blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    special_instructions = models.TextField(blank=True, null=True)
    # Using NullBool to represent the three states - (not turned in|not allowed|allowed)
    photo_release = models.NullBooleanField()
    medical_release = models.BooleanField()
    notes = models.TextField(blank=True, null=True)
    #TODO: Foreign key map to club.group
    group = models.CharField(max_length=2,
                             choices=GROUPLIST,
                             null=True)
    guest = models.BooleanField()
    guest_of = models.ForeignKey('self',
                                 related_name='guests',
                                 blank=True, null=True,
                                 on_delete=models.PROTECT)
    color = models.CharField(max_length=1,
                             blank=True, null=True,
                             choices=COLORS)

    class Meta:
        verbose_name_plural = 'children'
    
    def age(self):
        """ Figure out age from dob """
        if self.pk:
            return (dt.date.today() - self.dob).days // 365
        else:
            return '-'
        
    age.admin_order_field = 'dob'

    def get_points(self):
        """ Get point tally from points table """
        #TODO: Child.get_points()
        pass

    def add_points(self, points, reason, leader):
        """ Add points to points table """
        #TODO: Child.add_points()
        pass

    def assign_book(self, book):
        """ Assign a new book into the activity table """
        #TODO: Child.assign_book()
        # Query to get all sections of the handbook
        # Create rows in the activity table for each section, marked incomplete
        pass

    def give_award(self):
        #TODO: Child.give_award()
        pass

# Proxy models and managers for Clubber/Visitor types
class ClubberManager(models.Manager):
    def get_queryset(self):
        return super(ClubberManager, self).get_queryset().filter(guest=False)


class VisitorManager(models.Manager):
    def get_queryset(self):
        return super(VisitorManager, self).get_queryset().filter(guest=True)


class Clubber(Child):
    objects = ClubberManager()
    
    class Meta:
        proxy = True


class Visitor(Child):
    objects = VisitorManager()
    class Meta:
        proxy = True


class Parent(A_Person, A_Contact):
    family = models.ForeignKey('Family',
                               related_name='parents')
    email = models.EmailField()                           
    prefer_phone = models.BooleanField()
    prefer_email = models.BooleanField()


class Family(A_Contact):
    ICEContactName = models.CharField(max_length=150,
                                      verbose_name="Emergency Contact Name")
    ICEContactPhone = models.CharField(max_length=20,
                                       verbose_name="Emergency Contact Phone#")
    pickup = models.TextField(help_text="Enter names of people other than parents approved for pick-up, one per line",
                              verbose_name="Approved for pickup",
                              blank=True)
    attend_church = models.BooleanField(help_text="Does the family attend church?",
                                        default=False)
    church_name = models.CharField(max_length=100,
                                   help_text="What church does the family attend (if yes to the above)?",
                                   blank=True, null=True,)
    slug = models.SlugField(unique=True,
                            blank=True, null=True,
                            verbose_name='Family Name',
                            help_text='Family identifier. Leave blank to generate one from child/parent names.')

    # Don't need these at the family level
    phone = None

    class Meta:
        verbose_name_plural = "families"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            value = 'family'
            if self.children.select_related():
                value = self.children.select_related()[0].last_name
            elif self.parents.select_related():
                value = self.parents.select_related()[0].last_name

            self.slug = orig = value
            for x in itertools.count(1):
                if not Family.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '{o}-{x}'.format(o=orig, x=x)
            
        super(Family, self).save(*args, **kwargs)

    def children_short(self):
        return [c.first_name[0] for c in self.children.select_related()]
    children_short.short_description = 'Children'

    def parents_short(self):
        return [p.first_name[0] for p in self.parents.select_related()]
    parents_short.short_description = 'Parents'

    def get_contacts(self):
        """ 
        Get the preferred contact information for parents in this family 
        Return value is a dict containing two elements, 'phone' and 'email,
          both lists of contact methods for this family
        """
        contacts = {
            'email': [],
            'phone': []
            }
        for parent in self.parents.select_related():
            if parent.prefer_email:
                contacts['email'].append(parent.email)
            if parent.prefer_phone:
                contacts['phone'].append(parent.phone)
        return contacts     

    @property
    def family(self):
        """ Parents + clubbers """
        return {
            'children': self.children.select_related(),
            'parents': self.parents.select_related()
        }

    # def balancesheet(self):
    #     """ Get all finance info matching the family """
    #     #TODO: family.balancesheet()
    #     pass

    def __str__(self):
        return '{} ({})'.format(self.slug, ','.join(self.children_short()))


class Leader(AbstractUser, A_Contact):
    POSITIONS = (
        ('Com', 'Commander'),
        ('Sec', 'Secretary'),
        ('Admin', 'Admin Helper'),
        ('Lead', 'Leader'),
        ('AL', 'Assistant Leader'),
        ('Student', 'Student Helper'),
        ('Direct', 'Director'),
        ('GameLead', 'Game Leader'),
        ('GameAs', 'Game Assistant'),
        ("GameStu", 'Game Student Helper'),
        ('Listener', 'Listener'),
        ('StoreShop', 'Store Shopper'),
        ('StoreCoor', 'Store Coordinator'),
        ('StoreHelp', 'Store Helper'),
        ('StoreWrap', 'Store Wrapper'),
        ('Float', 'Floater'),
        ('Web', 'Webmaster')
    )
    #TODO: add ability to have multiple leader positions
    
    parent = models.OneToOneField(Parent,
                                  on_delete=models.PROTECT,
                                  blank=True, null=True)
    # {None: No Data, True: Received, False: Not possible}
    cpp = models.NullBooleanField(verbose_name="Child Protective Policy")
    position = models.CharField(max_length=9,
                                choices=POSITIONS,
                                null=True, blank=True)
    #TODO: Foreign key map to club.group
    group = models.CharField(max_length=2,
                             choices=GROUPLIST,
                             null=True, blank=True)
    #TODO: What does this need to be?
    # schedule = 

    def check_in(self):
        """ Check in on the leader attendance table """
        #TODO: Leader.check_in()
        pass

    def __str__(self):
        return self.get_full_name() or self.username

    class Meta:
        verbose_name_plural = "leaders"
