from django_messages.models import Message
from tastypie.authorization import Authorization
from tastypie.serializers import Serializer
from traveller.api import UserResource, TravellerResource

__author__ = 'danielqiu'

from tastypie.resources import ModelResource
from tastypie import fields

from tastypie.paginator import Paginator

class SentMessageAuthorization(Authorization):

    def read_list(self, object_list, bundle):
        return object_list.filter(sender=bundle.request.user)




class SentMessageResource(ModelResource):

    messageSubject = fields.CharField(attribute='subject')
    messageBody = fields.CharField(attribute='body')

    class Meta:
        queryset = Message.objects.all()
        resource_name = 'sent_message'
        authorization = SentMessageAuthorization()
        fields=['messageSubject', 'messageBody']

    def dehydrate(self, bundle):
        bundle.data['senderName'] = bundle.obj.sender.username
        bundle.data['recipientName'] = bundle.obj.recipient.username
        bundle.data['senderURL'] = bundle.obj.sender.profile.get_absolute_url()
        bundle.data['recipientURL'] = bundle.obj.recipient.profile.get_absolute_url()
        bundle.data['userAvatarImg'] = bundle.obj.recipient.profile.get_avatar_url(50)
        bundle.data['messageURL'] = bundle.obj.get_absolute_url()
        bundle.data['messageID'] = bundle.obj.id
        return bundle



class ReceivedMessageAuthorization(Authorization):

    def read_list(self, object_list, bundle):
        return object_list.filter(recipient=bundle.request.user)


class ReceivedMessageResource(ModelResource):

    messageSubject = fields.CharField(attribute='subject')
    messageBody = fields.CharField(attribute='body')

    class Meta:
        queryset = Message.objects.all()
        resource_name = 'received_message'
        authorization = ReceivedMessageAuthorization()
        fields=['messageSubject', 'messageBody']

    def dehydrate(self, bundle):
        bundle.data['senderName'] = bundle.obj.sender.username
        bundle.data['recipientName'] = bundle.obj.recipient.username
        bundle.data['senderURL'] = bundle.obj.sender.profile.get_absolute_url()
        bundle.data['recipientURL'] = bundle.obj.recipient.profile.get_absolute_url()
        bundle.data['userAvatarImg'] = bundle.obj.sender.profile.get_avatar_url(50)
        bundle.data['messageURL'] = bundle.obj.get_absolute_url()
        bundle.data['messageID'] = bundle.obj.id
        return bundle
