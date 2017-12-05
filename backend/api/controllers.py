#from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import *
from django.contrib.auth import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
#from django.shortcuts import render_to_response
from django.template import RequestContext
from django_filters.rest_framework import DjangoFilterBackend


from django.shortcuts import *

# Import models
from django.db import models
from django.contrib.auth.models import *
from api.models import *

#REST API
from rest_framework import viewsets, filters, parsers, renderers
from django.http import Http404
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
import requests
import bleach


def home(request):
   """
   Send requests to / to the ember.js clientside app
   """
   return render_to_response('ember/index.html',
               {}, RequestContext(request))

def xss_example(request):
  """
  Send requests to xss-example/ to the insecure client app
  """
  return render_to_response('dumb-test-app/index.html',
              {}, RequestContext(request))

class Register(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        # Login
        username = request.POST.get('username') #you need to apply validators to these
        print username
        password = request.POST.get('password') #you need to apply validators to these
        email = request.POST.get('email') #you need to apply validators to these
        gender = request.POST.get('gender') #you need to apply validators to these
        age = request.POST.get('age') #you need to apply validators to these
        educationlevel = request.POST.get('educationlevel') #you need to apply validators to these
        city = request.POST.get('city') #you need to apply validators to these
        state = request.POST.get('state') #you need to apply validators to these

        print request.POST.get('username')
        if User.objects.filter(username=username).exists():
            return Response({'username': 'Username is taken.', 'status': 'error'})
        elif User.objects.filter(email=email).exists():
            return Response({'email': 'Email is taken.', 'status': 'error'})

        #especially before you pass them in here
        newuser = User.objects.create_user(email=email, username=username, password=password)
        newprofile = Profile(user=newuser, gender=gender, age=age, educationlevel=educationlevel, city=city, state=state)
        newprofile.save()

        return Response({'status': 'success', 'userid': newuser.id, 'profile': newprofile.id})

class Session(APIView):
    permission_classes = (AllowAny,)
    def form_response(self, isauthenticated, userid, username, error=""):
        data = {
            'isauthenticated': isauthenticated,
            'userid': userid,
            'username': username
        }
        if error:
            data['message'] = error

        return Response(data)

    def get(self, request, *args, **kwargs):
        # Get the current user
        if request.user.is_authenticated():
            return self.form_response(True, request.user.id, request.user.username)
        return self.form_response(False, None, None)

    def post(self, request, *args, **kwargs):
        # Login
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return self.form_response(True, user.id, user.username)
            return self.form_response(False, None, None, "Account is suspended")
        return self.form_response(False, None, None, "Invalid username or password")

    def delete(self, request, *args, **kwargs):
        # Logout
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

class Events(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def post(self, request, *args, **kwargs):
        print 'REQUEST DATA'
        print str(request.data)

        eventtype = bleach.clean(request.data.get('eventtype'))
        if eventtype != request.data.get('eventtype'):
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)
        timestamp = int(request.data.get('timestamp'))
        userid = request.data.get('userid')
        requestor = request.META['REMOTE_ADDR']

        newEvent = Event(
            eventtype=eventtype,
            timestamp=datetime.datetime.fromtimestamp(timestamp/1000, pytz.utc),
            userid=userid,
            requestor=requestor
        )

        try:
            newEvent.clean_fields()
        except ValidationError as e:
            print e
            return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)

        newEvent.save()
        print 'New Event Logged from: ' + requestor
        return Response({'success': True}, status=status.HTTP_200_OK)

    def get(self, request, format=None):
        events = Event.objects.all()
        json_data = serializers.serialize('json', events)
        content = {'events': json_data}
        return HttpResponse(json_data, content_type='json')

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

class BreedDetail(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get(self, request, pk, format=None):
        breeds = Breed.objects.get(pk=pk)
        json_data = serializers.serialize('json', [breeds])
        content = {'breeds': json_data}
        return HttpResponse(json_data, content_type='json')

    def put(self, request, pk, format=None):
        breed = Breed.objects.get(pk=pk)
        breed.name = request.data.get('name')
        breed.size = request.data.get('size')
        breed.friendliness = int(request.data.get('friendliness'))
        breed.trainability = int(request.data.get('trainability'))
        breed.sheddingamount = int(request.data.get('sheddingamount'))
        breed.exerciseneeds = int(request.data.get('exerciseneeds'))

        try:
            breed.clean_fields()
        except ValidationError as e:
            print e
            return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)

        breed.save()
        return Response({'success': True}, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        Breed.objects.get(pk=pk).delete()
        return Response({'success': True}, status=status.HTTP_200_OK)

class BreedList(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get(self, request, format=None):
        breeds = Breed.objects.all()
        json_data = serializers.serialize('json', breeds)
        content = {'breeds': json_data}
        return HttpResponse(json_data, content_type='json')

    def post(self, request, *args, **kwargs):
        print 'REQUEST DATA'
        print str(request.data)

        name = request.data.get('name')
        size = request.data.get('size')
        friendliness = int(request.data.get('friendliness'))
        trainability = int(request.data.get('trainability'))
        sheddingamount = int(request.data.get('sheddingamount'))
        exerciseneeds = int(request.data.get('exerciseneeds'))


        newBreed = Breed(
            name=name,
            size=size,
            friendliness=friendliness,
            trainability=trainability,
            sheddingamount=sheddingamount,
            exerciseneeds=exerciseneeds
        )

        try:
            newBreed.clean_fields()
        except ValidationError as e:
            print e
            return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)

        newBreed.save()
        return Response({'success': True}, status=status.HTTP_200_OK)

class ActivateIFTTT(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def post(self,request):
        print 'REQUEST DATA'
        print str(request.data)

        eventtype = bleach.clean(request.data.get('eventtype'))
        timestamp = int(request.data.get('timestamp'))
        requestor = request.META['REMOTE_ADDR']
        api_key = ApiKey.objects.all().first()
        event_hook = "test"

        if eventtype != request.data.get('eventtype'):
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)

        print "Creating New event"

        newEvent = Event(
            eventtype=eventtype,
            timestamp=datetime.datetime.fromtimestamp(timestamp/1000, pytz.utc),
            userid=str(api_key.owner),
            requestor=requestor
        )

        print newEvent
        print "Sending Device Event to IFTTT hook: " + str(event_hook)

        #send the new event to IFTTT and print the result
        event_req = requests.post('https://maker.ifttt.com/trigger/'+str(event_hook)+'/with/key/'+api_key.key, data= {
            'value1' : timestamp,
            'value2':  "\""+str(eventtype)+"\"",
            'value3' : "\""+str(requestor)+"\""
        })
        print event_req.text

        #check that the event is safe to store in the databse
        try:
            newEvent.clean_fields()
        except ValidationError as e:
            print e
            return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)

        #log the event in the DB
        newEvent.save()
        print 'New Event Logged'
        return Response({'success': True}, status=status.HTTP_200_OK)
