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



    class Meta:
        queryset = Message.objects.all()
        resource_name = 'sent_message'
        authorization = SentMessageAuthorization()



class ReceivedMessageAuthorization(Authorization):

    def read_list(self, object_list, bundle):
        return object_list.filter(recipient=bundle.request.user)


class ReceivedMessageResource(ModelResource):

    sender = fields.ForeignKey(TravellerResource, "sender")
    recipient = fields.ForeignKey(TravellerResource, "recipient")

    class Meta:
        queryset = Message.objects.all()
        resource_name = 'received_message'
        authorization = ReceivedMessageAuthorization()


    #     creator = fields.ForeignKey(TravellerResource, 'creator')
    # participants = fields.ManyToManyField(TravellerResource, 'participants')