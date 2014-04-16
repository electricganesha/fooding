from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    chef = models.ForeignKey(User, related_name='event_chef')
    guests = models.ManyToManyField(User, related_name='event_guests')
    #reviews = models.ForeignKey('Review')
    creation_timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.description


class Review(models.Model):
    comment = models.CharField(max_length=500)
    event = models.ForeignKey(Event)
    reviewer = models.ForeignKey(User)
    review_timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.comment
    def reviewer_comments_event(self, text):
        comment = text
        sender = review.reviewer
        event = review.event

        notify = Notify()
        notify.event = event
        notify.sender = sender
        notify.user = event.chef
        notify.text = text
        notify.save()

class Likes(models.Model):
    event = models.ForeignKey(Event)
    liker = models.ForeignKey(User, related_name='event_liker')

    def __unicode__(self):
        return '%s' % (self.liker)

class Notify(models.Model):
    event = models.ForeignKey(Event)
    sender = models.ForeignKey(User, related_name="sender")
    user = models.ForeignKey(User, related_name="userid")
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text