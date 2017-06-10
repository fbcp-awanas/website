from django.db import models
from django.template.defaultfilters import slugify
import datetime as dt
from django.utils import timezone

# Field Type Reference:
# https://docs.djangoproject.com/en/1.11/ref/models/fields/



## Abstract Models
class Person(models.Model):
    """ Abstract class defining name fields """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    @property
    def full_name(self):
        return "{s.first_name s.last_name}".format(s=self)

    def __str__(self):
        return self.full_name

    class Meta:
        abstract = True


class Contact(models.Model):
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
    email = models.EmailField()

    class Meta:
        abstract = True


## Functional Models
# People
class Family(Contact):
    ICEContactName = models.CharField(max_length=150,
                                      verbose_name="Emergency Contact Name")
    ICEContactPhone = models.CharField(max_length=20,
                                       verbose_name="Emergency Contact Phone#")
    pickup = models.TextField(help_text="Enter names of people other than parents approved for pick-up, one per line",
                              verbose_name="Approved for pickup")
    attend_church = models.BooleanField(help_text="Does the family attend church?")
    church_name = models.CharField(max_length=100,
                                   help_text="What church does the family attend (if yes to the above)?")
    #TODO: Slug for families - based on last name of first child added?
    #slug = models.SlugField(unique=True)

    # Don't need these at the family level
    phone = None
    email = None

    class Meta:
        verbose_name_plural = "families"

    def get_clubbers(self):
        """ get list of Clubbers objects that match """
        return Clubber.objects.filter(family=self)

    def get_parents(self):
        """ get list of parents for the family """
        return Parent.objects.filter(family=self)

    def get_contacts(self):
        """ Get the preferred contact information for parents in this family """
        #TODO: Family.get_contacts()
        pass

    def get_family(self):
        """ Parents + clubbers """
        return self.get_clubbers() + self.get_parents()

    def balancesheet(self):
        """ Get all finance info matching the family """
        #TODO: family.balancesheet()
        pass


class Clubber(Person):
    family = models.ForeignKey('Family')
    club = models.ForeignKey('Club')
    dob = models.DateField(verbose_name="Date of Birth")
    grade = models.IntegerField()
    gender = models.CharField(max_length=1,
                              choices = (("M", "Male"),
                                         ("F", "Female"))
                             )
    allergies = models.TextField()
    special_instructions = models.TextField()
    # Using NullBool to represent the three states - (not turned in|not allowed|allowed)
    photo_release = models.NullBooleanField()
    medical_release = models.BooleanField()
    notes = models.TextField()
    color = models.CharField(max_length=50)

    @property
    def age(self):
        """ Figure out age from dob """
        return (dt.date.today() - self.dob).days // 365

    def get_points(self):
        """ Get point tally from points table """
        pass

    def add_points(self, points, reason, leader):
        """ Add points to points table """
        pass

    def assign_book(self, book):
        """ Assign a new book into the activity table """
        # Query to get all sections of the handbook
        # Create rows in the activity table for each section, marked incomplete
        pass

    def give_award(self):
        pass

    def add_visitor(self, first, last):
        """ Add a visitor entry and assign points for it """
        today = dt.date.today()
        v = Visitor.objects.create(first_name=first,
                                   last_name=last,
                                   guest_of=self,
                                   date=today)
        self.assign_points(1, "Visitor {v.full_name} on {d}".format(v=v, d=today))


class Parent(Person, Contact):
    family = models.ForeignKey('Family')
    prefer_phone = models.BooleanField()
    prefer_email = models.BooleanField()


class Visitor(Person):
    guest_of = models.ForeignKey('Clubber')
    date = models.DateField(default=dt.date.today())


class Leader(Person, Contact):
    POSITIONS = (
        ('Com', 'Commander'),
        ('Sec', 'Secretary'),
        ('PugLead', 'Puggles Leader'),
        ('PugAs', 'Puggles Assitant'),
        ('PugStu', 'Puggles Student Helper'),
        ('CubDir', 'Cubbies Director'),
        ('CubLead', 'Cubbies Leader'),
        ('CubAs', 'Cubbies Assitant'),
        ('CubStu', 'Cubbies Student Helper'),
        ('SpkDir', 'Sparks Director'),
        ('SpkLead', 'Sparks Leader'),
        ('SpkAs', 'Sparks Assitant'),
        ('SpkStu', 'Sparks Student Helper'),
        ('TTDir', 'T&T Director'),
        ('TTLead', 'T&T Leader'),
        ('TTAs', 'T&T Assitant'),
        ('TTStu', 'T&T Student Helper'),
        ('GameLead', 'Game Leader'),
        ('GameAs', 'Game Assistant'),
        ("GameStu", 'Game Student Helper'),
        ('Listener', 'Listener'),
        ('StoreShop', 'Store Shopper'),
        ('StoreCoor', 'Store Coordinator'),
        ('StoreHelp', 'Store Helper'),
        ('StoreWrap', 'Store Wrapper'),
        ('Float', 'Floater')
    )
    #TODO: add ability to have multiple leader positions
    
    cpp = models.NullBooleanField()
    position = models.CharField(max_length=9,
                                choices=POSITIONS)
    club = models.ForeignKey('Club')
    # group =
    # schedule =

    def check_in(self):
        """ Check in on the leader attendance table """
        #TODO: Leader.check_in()
        pass


# Organization
class Club(models.Model):
    name = models.CharField(max_length=10)

    def list_awards(self):
        """ Get a list of awards that need to be delivered for this club """
        #TODO: Club.list_awards()
        pass

    def list_clubbers(self):
        """ List clubbers for this club """
        return Clubber.objects.filter(club=self)

    def get_attendance(self, date=False):
        """ Pull all items from the attendance table for this club's clubbers """
        clubbers = self.list_clubbers()
        #TODO: Club.get_attendance()
        # if date:
        #   # Get one day's records
        # else:
        #   # Get all records
        pass


class Handbook(models.Model):
    name = models.CharField(max_length=100)
    club = models.ForeignKey('Club')
    inventory_number = models.ForeignKey('Inventory',
                                         to_field='item_num')
    # verses =
    # extra_credit =
    # entrance_book =

    @property
    def sections(self):
        # Not sure if this is going to work
        # https://docs.djangoproject.com/en/1.11/topics/db/queries/#backwards-related-objects
        return self.section_set.all()


class Section(models.Model):
    name = models.CharField(max_length=100)
    handbook = models.ForeignKey('Handbook')
    #content =
    #in_order =
    points = models.IntegerField(default=1)


class Inventory(models.Model):
    item_num = models.IntegerField(unique=True)
    quantity = models.IntegerField()
    club = models.ForeignKey('Club')
    category = models.CharField(max_length=50)
    order_threshold = models.IntegerField()
    description = models.CharField(max_length=50)
    picture = models.FileField()
    price = models.DecimalField(max_digits=5, decimal_places=2,
                                help_text="Unit price")


# Running tallies
class Awards(models.Model):
    clubber = models.ForeignKey('clubber')
    description = models.TextField()
    date_awarded = models.DateField()
    # When this is set to a non-None/non-False value, it serves as both a checkbox and a datestamp
    delivered = models.DateField(blank=True, null=True, default=None)


class Points(models.Model):
    #TODO: List of point reasons?
    clubber = models.ForeignKey('Clubber')
    date = models.DateField(default=dt.date.today())
    leader = models.ForeignKey('Leader')
    points = models.IntegerField(default=1,
                                 help_text="How many points?")
    reason = models.CharField(max_length=50)


class Activity(models.Model):
    clubber = models.ForeignKey('Clubber')
    section = models.ForeignKey('Section')
    complete = models.DateField(default=None,
                            null=True, blank=True,
                            help_text="When was this module completed?")
    leader = models.ForeignKey('Leader',
                               default=None,
                               null=True, blank=True,
                               help_text="Who signed off on this activity?")


class Attendance(models.Model):
    STATUS = (('A', 'Absent'),
              ('P', 'Present'),
              ('O', 'On Time'),
              ('E', 'Excused'))
    clubber = models.ForeignKey('Clubber',
                                unique_for_date='date')
    date = models.DateTimeField(default=dt.date.today())
    time = models.TimeField(defalt=timezone.now())
    status = models.CharField(max_length=1,
                              choices=STATUS)
    ontime = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "attendance"


class Finance(models.Model):
    #TODO: List of methods?
    METHODS = (('CA', 'Cash'),
               ('CH', 'Check'),
               ('CC', 'Credit Card'))
    family = models.ForeignKey('Family')
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=200)
    date = models.DateField(default=dt.date.today())
    method = models.CharField(max_length=2,
                              choices=METHODS)


class Expense(models.Model):
    #TODO: List of categories?
    date = models.DateField()
    receipt_date = models.DateField()
    receipt_store = models.CharField(max_length=100)
    items = models.TextField()
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payee = models.CharField(max_length=50)