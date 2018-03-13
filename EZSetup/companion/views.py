# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("""<html><head><style>h1{font-family: "Ludica Console", monospace, serif;}h2{font-family: "Ludica Console", monospace, serif;}p{font-family: "Ludica Console", monospace, serif;}</style></head><body><div align="center"><img src="https://lh3.googleusercontent.com/z8Z5LQQvbHTnGILkg0uIgSOK0hZP6r44WfxUnIwKwTwltL7hUQbGkMhhP0u8zNwEeGI=w300"/></div><br><h1 align="center">Hi! I'm Sabrina!</h1><br><div align="center"><h2>I'm here to help!</h2><p>I can have conversations with you, about anything!</p><p>I can get weather or calendar information for you.</p><p>I am great at remembering things for you!</p><p>Finally, I can dial phone numbers for you and text.</p><br><p>All on this little device you purchased! That's great, right?</p><br><h2>But, if you want me to help out, click <a href="http://192.168.1.139:5555/wifi">here</a> to set me up with your WiFi!</h2></div></body></html>""")
