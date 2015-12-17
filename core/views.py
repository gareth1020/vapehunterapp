from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
import core.models as coremodels
from sitegate.decorators import sitegate_view, signup_view, signin_view
from sitegate.signup_flows.classic import ClassicWithEmailSignup
from sitegate.signin_flows.classic import ClassicSignin

# Create your views here.

class LandingView(TemplateView):
	template_name = "base/index.html"

class EliquidListView(ListView):
	model = coremodels.Eliquid
	template_name = 'eliquids/list.html'
	paginate_by = 10

class SearchListView(EliquidListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
	return coremodels.Eliquid.objects.filter(search_var__icontains=incoming_query_string).order_by('-score', 'title')

class EliquidDetailView(DetailView):
	model = coremodels.Eliquid
	template_name = 'eliquids/detail.html'
	context_object_name = 'eliquid'

	def get_context_data(self, **kwargs):
		context = super(EliquidDetailView, self).get_context_data(**kwargs)
		eliquid = coremodels.Eliquid.objects.get(id=self.kwargs['pk'])
		if self.request.user.is_authenticated():
			user_reviews = coremodels.Review.objects.filter(eliquid=eliquid, user=self.request.user)
			if user_reviews.count() > 0:
				context['user_review'] = user_reviews[0]
			else:
				context['user_review'] = None

		return context

class EliquidCreateView(CreateView):
	model = coremodels.Eliquid
	template_name = 'base/form.html'
	fields = "__all__"

class EliquidUpdateView(UpdateView):
	model = coremodels.Eliquid
	template_name = 'base/form.html'
	fields = "__all__"

class ReviewCreateView(CreateView):
	model = coremodels.Review
	template_name = 'base/form.html'
	fields =['description', 'rating']

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.eliquid = coremodels.Eliquid.objects.get(id=self.kwargs['pk'])
		return super(ReviewCreateView, self).form_valid(form)

	def get_success_url(self):
		return self.object.eliquid.get_absolute_url()


class ReviewUpdateView(UpdateView):
	model = coremodels.Review
	template_name = 'base/form.html'
	fields =['description', 'rating']

	def get_object(self):
		return coremodels.Review.objects.get(eliquid__id=self.kwargs['pk'], user=self.request.user)

	def get_success_url(self):
		return self.object.eliquid.get_absolute_url()


@signup_view(flow=ClassicWithEmailSignup, widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3')
def newuser(request):
    return render(request, 'base/newuser.html', {'title': 'Sign up'})

@signin_view(flow=ClassicSignin, widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3')
def login(request):
	return render(request, 'base/login.html', {'title': 'Sign in'})