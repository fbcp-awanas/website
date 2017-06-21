from setup import *
import datetime

#TODO: Add dummy groups

families = [
    {'attend_church': True, 'city': 'Garland', 'address': '3430 Rockcrest Drive', 'slug': 'Owen', 'ICEContactPhone': '(214) 686-5808', 'zip': '75044', 'ICEContactName': 'Jeremy Welch', 'church_name': 'FBC Plano', 'pickup': '', 'state': 'TX'},
    {'attend_church': True, 'city': 'Garland', 'address': '5442 Round Rock Road', 'slug': 'Welch', 'ICEContactPhone': '907-232-3672', 'zip': '75044', 'ICEContactName': 'Sarah Munson', 'church_name': 'FBC Plano', 'pickup': 'Sarah Munson\r\nBarbara Boswell', 'state': 'TX'},
    ]

for f in families:
    Family.objects.update_or_create(**f)

owen_id = Family.objects.get(slug='Owen').id
welch_id = Family.objects.get(slug='Welch').id

parents = [
    {'last_name': 'Owen', 'phone': '(469) 323-3536', 'prefer_email': True, 'email': 'jennifer@o1family.com', 'zip': '75044', 'state': 'TX', 'prefer_phone': True, 'family_id': owen_id, 'city': 'Garland', 'first_name': 'Jennifer', 'address': '3430 Rockcrest Drive'}, 
    {'last_name': 'Welch', 'phone': '2146865808', 'prefer_email': True, 'email': 'j@boswelch.com', 'zip': '75044', 'state': 'TX', 'prefer_phone': True, 'family_id': welch_id, 'city': 'Garland', 'first_name': 'Jeremy', 'address': '5442 Round Rock Road'}, 
    {'last_name': 'Welch', 'phone': '2146865807', 'prefer_email': False, 'email': 'l@boswelch.com', 'zip': '75044', 'state': 'TX', 'prefer_phone': True, 'family_id': welch_id, 'city': 'Garland', 'first_name': 'Linnea', 'address': '5442 Round Rock Road'}, 
    {'last_name': 'Owen', 'phone': '2148642707', 'prefer_email': True, 'email': 'scott@o1family.com', 'zip': '75044', 'state': 'TX', 'prefer_phone': False, 'family_id': owen_id, 'city': 'Garland', 'first_name': 'Scott', 'address': '3430 Rockcrest Drive'}
    ]

for p in parents:
    Parent.objects.update_or_create(**p)

children = [
    {'last_name': 'Owen', 'allergies': '', 'photo_release': True, 'guest_of_id': None, 'group_id': 1, 'dob': datetime.date(2010, 11, 28), 'special_instructions': '', 'first_name': 'Samantha', 'color': None, 'notes': '', 'gender': 'F', 'grade': 1, 'medical_release': True, 'family_id': owen_id, 'medications': '', 'guest': False}, 
    {'last_name': 'Owen', 'allergies': '', 'photo_release': True, 'guest_of_id': None, 'group_id': 1, 'dob': datetime.date(2008, 3, 20), 'special_instructions': '', 'first_name': 'Dalton', 'color': None, 'notes': '', 'gender': 'M', 'grade': 4, 'medical_release': True, 'family_id': owen_id, 'medications': '', 'guest': False}, 
    {'last_name': 'Welch', 'allergies': '', 'photo_release': True, 'guest_of_id': 'Samantha Owen', 'group_id': 1, 'dob': datetime.date(2012, 4, 7), 'special_instructions': '', 'first_name': 'Eleanor', 'color': None, 'notes': '', 'gender': 'F', 'grade': 0, 'medical_release': True, 'family_id': welch_id, 'medications': '', 'guest': True}, 
    {'last_name': 'Owen', 'allergies': '', 'photo_release': True, 'guest_of_id': None, 'group_id': 1, 'dob': datetime.date(2006, 8, 19), 'special_instructions': '', 'first_name': 'Alysa', 'color': None, 'notes': '', 'gender': 'F', 'grade': 6, 'medical_release': True, 'family_id': owen_id, 'medications': '', 'guest': False}, 
    {'last_name': 'Owen', 'allergies': '', 'photo_release': True, 'guest_of_id': None, 'group_id': 1, 'dob': datetime.date(2013, 3, 2), 'special_instructions': '', 'first_name': 'Liam', 'color': None, 'notes': '', 'gender': 'F', 'grade': -1, 'medical_release': True, 'family_id': owen_id, 'medications': '', 'guest': False}, 
    ]

for c in children:
    if c['guest']:
        c['guest_of_id'] = Child.objects.get(first_name=c['guest_of_id'].split()[0], last_name=c['guest_of_id'].split()[1]).id
    Child.objects.update_or_create(**c)

leaders = [
    {'last_name': 'Welch', 'password': 'pbkdf2_sha256$36000$ql4qSrqWe0ua$CWNnJbT3cpjVYbQOVG5aYtK68JRYLIcRR7bhHvEDbCQ=', 'parent_id': None, 'email': 'j@adhddos.com', 'city': 'Garland', 'is_active': True, 'state': 'TX', 'position': 'Web', 'phone': '(214) 686-5808', 'is_staff': True, 'first_name': 'Jeremy', 'address': '5442 Round Rock Road', 'cpp': None, 'group': 'A', 'is_superuser': True, 'username': 'jwelch-a', 'zip': '75044'}, 
    {'last_name': 'Owen', 'password': 'pbkdf2_sha256$36000$ce6WwR29XGQz$S7DRvBqsmj4tDAu3ZfWCIFrEnjHBMu+5Aqw3W8hKAcQ=', 'parent_id': None, 'email': 'jennifer@o1family.com', 'city': 'Garland', 'is_active': True, 'state': 'TX', 'position': 'Lead', 'phone': '(469) 323-4936', 'is_staff': True, 'first_name': 'Jennifer', 'address': '3430 Rockcrest Drive', 'cpp': True, 'group': 'A', 'is_superuser': True, 'username': 'jowen-a', 'zip': '75044'},
    {'last_name': 'Owen', 'password': 'pbkdf2_sha256$36000$ce6WwR29XGQz$S7DRvBqsmj4tDAu3ZfWCIFrEnjHBMu+5Aqw3W8hKAcQ=', 'parent_id': True, 'email': 'jennifer@o1family.com', 'city': 'Garland', 'is_active': True, 'state': 'TX', 'position': 'Lead', 'phone': '(469) 323-4936', 'is_staff': False, 'first_name': 'Jennifer', 'address': '3430 Rockcrest Drive', 'cpp': True, 'group': 'A', 'is_superuser': False, 'username': 'jowen', 'zip': '75044'}
]

for l in leaders:
    if l['parent_id']:
        l['parent_id'] = Parent.objects.get(first_name=l['first_name'], last_name=l['last_name']).id
    Leader.objects.update_or_create(**l)