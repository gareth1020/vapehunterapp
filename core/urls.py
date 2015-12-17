from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as coreviews
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',

 url(r'^$', coreviews.LandingView.as_view()),
 url(r'eliquid/$', coreviews.EliquidListView.as_view()),
 url(r'eliquid/(?P<pk>\d+)/detail/$', coreviews.EliquidDetailView.as_view(), name='eliquids_list'),
 url(r'eliquid/create/$', login_required(coreviews.EliquidCreateView.as_view())),
 url(r'search/$', coreviews.SearchListView.as_view()),
 url(r'eliquid/(?P<pk>\d+)/update/$', login_required(coreviews.EliquidUpdateView.as_view()), name='eliquids_update'),
 url(r'eliquid/(?P<pk>\d+)/review/create/$', login_required(coreviews.ReviewCreateView.as_view()), name='review_create'),
 url(r'eliquid/(?P<pk>\d+)/review/update/$', login_required(coreviews.ReviewUpdateView.as_view()), name='review_update'),
 url(r'login/newuser/$', coreviews.newuser),
 url(r'login/$', coreviews.login),
)