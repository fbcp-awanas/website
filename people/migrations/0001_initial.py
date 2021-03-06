# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 04:38
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=15)),
                ('cpp', models.NullBooleanField(verbose_name='Child Protective Policy')),
                ('position', models.CharField(blank=True, choices=[('Com', 'Commander'), ('Sec', 'Secretary'), ('Admin', 'Admin Helper'), ('Lead', 'Leader'), ('AL', 'Assistant Leader'), ('Student', 'Student Helper'), ('Direct', 'Director'), ('GameLead', 'Game Leader'), ('GameAs', 'Game Assistant'), ('GameStu', 'Game Student Helper'), ('Listener', 'Listener'), ('StoreShop', 'Store Shopper'), ('StoreCoor', 'Store Coordinator'), ('StoreHelp', 'Store Helper'), ('StoreWrap', 'Store Wrapper'), ('Float', 'Floater')], max_length=9, null=True)),
                ('group', models.CharField(blank=True, choices=[('A', 'Awanas'), ('P', 'Puggles'), ('C', 'Cubbies'), ('S', 'Sparks'), ('T', 'Truth & Training')], max_length=2, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('grade', models.IntegerField(choices=[(0, 'Kindergarten'), (1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth'), (6, 'Sixth')])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('allergies', models.TextField(blank=True, null=True)),
                ('medications', models.TextField(blank=True, null=True)),
                ('special_instructions', models.TextField(blank=True, null=True)),
                ('photo_release', models.NullBooleanField()),
                ('medical_release', models.BooleanField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('group', models.CharField(choices=[('A', 'Awanas'), ('P', 'Puggles'), ('C', 'Cubbies'), ('S', 'Sparks'), ('T', 'Truth & Training')], max_length=2, null=True)),
                ('guest', models.BooleanField()),
                ('color', models.CharField(blank=True, choices=[('R', 'Red'), ('B', 'Blue'), ('Y', 'Yellow'), ('G', 'Green')], max_length=1, null=True)),
            ],
            options={
                'verbose_name_plural': 'children',
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(help_text='Street number and name', max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(choices=[('TX', 'Texas'), ('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'District of Columbia'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MO', 'Missouri'), ('MS', 'Mississippi'), ('MT', 'Montana'), ('NA', 'National'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('NE', 'Nebraska'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NV', 'Nevada'), ('NY', 'New York'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming')], default='TX', max_length=2)),
                ('zip', models.CharField(help_text='Five-digit zip code', max_length=5)),
                ('ICEContactName', models.CharField(max_length=150, verbose_name='Emergency Contact Name')),
                ('ICEContactPhone', models.CharField(max_length=20, verbose_name='Emergency Contact Phone#')),
                ('pickup', models.TextField(help_text='Enter names of people other than parents approved for pick-up, one per line', verbose_name='Approved for pickup')),
                ('attend_church', models.BooleanField(default=False, help_text='Does the family attend church?')),
                ('church_name', models.CharField(blank=True, help_text='What church does the family attend (if yes to the above)?', max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, help_text='Family identifier. Leave blank to generate one from child/parent names.', null=True, unique=True, verbose_name='Family Name')),
            ],
            options={
                'verbose_name_plural': 'families',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.CharField(help_text='Street number and name', max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(choices=[('TX', 'Texas'), ('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'District of Columbia'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MO', 'Missouri'), ('MS', 'Mississippi'), ('MT', 'Montana'), ('NA', 'National'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('NE', 'Nebraska'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NV', 'Nevada'), ('NY', 'New York'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming')], default='TX', max_length=2)),
                ('zip', models.CharField(help_text='Five-digit zip code', max_length=5)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('prefer_phone', models.BooleanField()),
                ('prefer_email', models.BooleanField()),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='people.Family')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='child',
            name='family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='people.Family'),
        ),
        migrations.AddField(
            model_name='child',
            name='guest_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='guests', to='people.Child'),
        ),
        migrations.AddField(
            model_name='leader',
            name='parent',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='people.Parent'),
        ),
        migrations.AddField(
            model_name='leader',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Clubber',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
            },
            bases=('people.child',),
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
            },
            bases=('people.child',),
        ),
    ]
