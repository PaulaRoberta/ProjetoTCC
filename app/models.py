import datetime
from django.utils import timezone
from django.db.models import (Model, CharField, ForeignKey,
                                                   DateTimeField)

class UserType(Model):
    type_user =CharField(max_length=120)

    def __str__(self):
        return self.type_user

class User(Model):
    user_type = ForeignKey(UserType)
    name = CharField(max_length=120, null=True)
    email = CharField(max_length=120, null=True)
    identify = CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

class Location(Model):
    name = CharField(max_length=120, null=True)
    description = CharField(max_length=200, null=True)
    user = ForeignKey(User, null=True)

    def __str__(self):
        return self.name

class Entity(Model):
    name = CharField(max_length=120)
    location = ForeignKey(Location)
    serie_number = CharField(max_length=120, unique=True, null=True)
    maker = CharField(max_length=120, null=True)
    model = CharField(max_length=120, null=True)
    created_at = DateTimeField(default=timezone.now())
    description = CharField(max_length=400, null=True)
    image = CharField(max_length=300, null=True)

    def __str__(self):
        return self.name

class Event(Model):
    description = CharField(max_length=200, null=True)
    user = ForeignKey(User, null=True)
    entity = ForeignKey(Entity, null=True)
    created_at = DateTimeField(default=timezone.now())
    resolved_at = DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Entity #%s" % self.id


class Midias(Model):
    entity = ForeignKey(Entity, null=True)
    file = CharField(max_length=120, null=True)
    link = CharField(max_length=120, null=True)


    def __str__(self):
        return "Entity #%s" % self.id



class Comment(Model):
    event = ForeignKey(Event, null=True)
    Comment = CharField(max_length=200, null=True)
    user = ForeignKey(User, null=True)
    created_at = DateTimeField(default=timezone.now())

    def __str__(self):
        return "Event #%s" % self.id

class FAQ(Model):
    entity = ForeignKey(Entity, null=True)
    ask = CharField(max_length=200, null=True)
    answer = CharField(max_length=200, null=True)
    asked_at = DateTimeField(default=timezone.now())
    answered_at = DateTimeField(auto_now=True)

    def __str__(self):
        return "FAQ #%s" % self.id
