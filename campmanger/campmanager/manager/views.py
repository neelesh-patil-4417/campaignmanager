from django.shortcuts import render
from rest_framework.decorators import api_view
from manager.models import subscriber
from manager.serializer import unsubscriber_serializer
from rest_framework.response import Response
# from django.contrib.auth.models import subscriber
import pdb
from manager.models import subscriber
# Create your views here.



#end point to unsubscribe the user
@api_view(['POST'])
def unsubscribe(request):
    email = request.data["email"]
    person = subscriber.objects.filter(emailid = str(email))
    if person:
        person = subscriber.objects.get(emailid = email)
        person.isactive = False
        person.issubscribed = False
        person.save()
        return Response({"msg":f"The user {person.first_name} has successfully subscribed"})
    else:
        return Response({"msg":"The user doesnot exist"})



from django.core.mail import send_mail
@api_view(["GET"])
def send_email(request):
    # 'Subject', 'preview_text', 'article_url', 'html_content', 'plain_text_content', 'published_date'.
    subject = "Campaign Manager"
    message = "Save Water Drink BEER"
    from_email = "nileshppatil68@gmail.com"
    recipient_list = ["np6160287@gmail.com"]

    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)

    return Response({"msg":"Message sent"})