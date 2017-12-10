#from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import *
from django.contrib.auth import *
from rest_framework.permissions import AllowAny
from django.template import RequestContext
from django.shortcuts import *

# Import models
from django.contrib.auth.models import *
from api.models import *
from api.forms import DocumentForm


#REST API
from rest_framework import viewsets, filters, parsers, renderers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.authentication import *

#filters
#from filters.mixins import *

from api.pagination import *
import json, datetime, pytz
from django.core import serializers


def home(request):
   """
   Send requests to / to the ember.js clientside app
   """
   return render_to_response('ember/index.html',
               {}, RequestContext(request))

class ChurchEventDetail(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get(self, request, pk, format=None):
        events = ChurchEvent.objects.get(pk=pk)
        json_data = serializers.serialize('json', [events])
        content = {'events': json_data}
        return HttpResponse(json_data, content_type='json')

    def delete(self, request, pk, format=None):
        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == "basic":
                    uname, passwd = base64.b64decode(auth[1]).split(':')
                    user = authenticate(username=uname, password=passwd)
                    if user is not None and user.is_active:
                        ChurchEvent.objects.get(pk=pk).delete()
                        return Response({'success': True}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == "basic":
                    uname, passwd = base64.b64decode(auth[1]).split(':')
                    user = authenticate(username=uname, password=passwd)
                    if user is not None and user.is_active:
                        event = ChurchEvent.objects.get(pk=pk)
                        event.title = request.data.get('title')
                        event.starttime = request.data.get('starttime')
                        event.endtime = request.data.get('endtime')
                        event.description = request.data.get('description')
                        event.address = request.data.get('address')


                        try:
                            event.clean_fields()
                        except ValidationError as e:
                            print e
                            return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)

                        event.save()
                        return Response({'success': True}, status=status.HTTP_200_OK)

class ChurchEventList(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get(self, request, format=None):
        events = ChurchEvent.objects.all()
        json_data = serializers.serialize('json', events)
        content = {'events': json_data}
        return HttpResponse(json_data, content_type='json')

    def post(self, request, *args, **kwargs):
        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == "basic":
                    uname, passwd = base64.b64decode(auth[1]).split(':')
                    user = authenticate(username=uname, password=passwd)
                    if user is not None and user.is_active:
                        print 'REQUEST DATA'
                        print str(request.data)

                        title = request.data.get('title')
                        starttime = request.data.get('starttime')
                        endtime = request.data.get('endtime')
                        description = request.data.get('description')
                        address = request.data.get('address')


                        newEvent = ChurchEvent(
                            title=title,
                            starttime=starttime,
                            endtime=endtime,
                            description=description,
                            address = address
                        )

                        try:
                            newEvent.clean_fields()
                        except ValidationError as e:
                            print e
                            return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)

                        newEvent.save()
                        return Response({'success': True}, status=status.HTTP_200_OK)

class AlertDetail(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )
    def form_response(self, isauthenticated, userid, username, error=""):
        data = {
            'isauthenticated': isauthenticated,
            'userid': userid,
            'username': username
        }
        if error:
            data['message'] = error

        return Response(data)

    def get(self, request, pk, format=None):
        alerts = Alert.objects.get(pk=pk)
        json_data = serializers.serialize('json', [alerts])
        content = {'alerts': json_data}
        return HttpResponse(json_data, content_type='json')

    def delete(self, request, pk, format=None):

        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == "basic":
                    uname, passwd = base64.b64decode(auth[1]).split(':')
                    user = authenticate(username=uname, password=passwd)
                    if user is not None and user.is_active:
                        Alert.objects.get(pk=pk).delete()
                        return Response({'success': True}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):

        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == "basic":
                    uname, passwd = base64.b64decode(auth[1]).split(':')
                    user = authenticate(username=uname, password=passwd)
                    if user is not None and user.is_active:
                        alert = Alert.objects.get(pk=pk)
                        alert.text = request.data.get('text')
                        alert.startdate = request.data.get('startdate')
                        alert.enddate = request.data.get('enddate')
                        try:
                            alert.clean_fields()
                        except ValidationError as e:
                            print e
                            return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)

                        alert.save()
                        return Response({'success': True}, status=status.HTTP_200_OK)

class AlertList(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get(self, request, format=None):
        alert = Alert.objects.filter(startdate__lt=datetime.datetime.now(), enddate__gt=datetime.datetime.now())
        json_data = serializers.serialize('json', alert)
        content = {'alert': json_data}
        return HttpResponse(json_data, content_type='json')

    def post(self, request, *args, **kwargs):

        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == "basic":
                    uname, passwd = base64.b64decode(auth[1]).split(':')
                    user = authenticate(username=uname, password=passwd)
                    if user is not None and user.is_active:
                        print 'REQUEST DATA'
                        print str(request.data)

                        text = request.data.get('text')
                        startdate = request.data.get('startdate')
                        enddate = request.data.get('enddate')

                        newAlert = Alert(
                            text=text,
                            startdate=startdate,
                            enddate=enddate
                        )

                        try:
                            newAlert.clean_fields()
                        except ValidationError as e:
                            print e
                            return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)

                        newAlert.save()
                        return Response({'success': True}, status=status.HTTP_200_OK)

class SermonDetail(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get(self, request, pk, format=None):
        sermons = Sermon.objects.get(pk=pk)
        json_data = serializers.serialize('json', [sermons])
        content = {'sermons': json_data}
        return HttpResponse(json_data, content_type='json')

    def delete(self, request, pk, format=None):
        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == "basic":
                    uname, passwd = base64.b64decode(auth[1]).split(':')
                    user = authenticate(username=uname, password=passwd)
                    if user is not None and user.is_active:
                        Sermon.objects.get(pk=pk).delete()
                        return Response({'success': True}, status=status.HTTP_200_OK)

class SermonList(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.MultiPartParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get(self, request, format=None):
        sermons = Sermon.objects.all()
        json_data = serializers.serialize('json', sermons)
        content = {'sermons': json_data}
        return HttpResponse(json_data, content_type='json')

    def post(self, request, *args, **kwargs):
        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == "basic":
                    uname, passwd = base64.b64decode(auth[1]).split(':')
                    user = authenticate(username=uname, password=passwd)
                    if user is not None and user.is_active:
                        form = DocumentForm(request.POST, request.FILES)
                        if form.is_valid():
                            try:
                                form.save()
                                return Response({'success': True}, status=status.HTTP_200_OK)
                            except ValidationError as e:
                                print e
                                return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)



