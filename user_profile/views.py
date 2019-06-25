from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.shortcuts import redirect, reverse
from django.contrib.auth.models import User
from user_profile.forms import UserProfileModelForm, PersonalProfileModelForm


# Create your views here.


class UserProfileView(TemplateView, LoginRequiredMixin):
    template_name = "user_profile/registration_form.html"
    individual_template="user_profile/individual_registration.html"

    def post(self, request, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user_profile_form'] = user_profile_form = UserProfileModelForm(request.POST, self.request.FILES,
                                                                               instance=request.user.user_profile)
        context['personal_profile_form'] = personal_profile_form = PersonalProfileModelForm(request.POST, self.request.FILES,
                                                                                    instance=request.user.user_profile)
        account_save = request.POST.get('account_save')

        if (account_save=='1'):

            if personal_profile_form.is_valid():

                form_save=personal_profile_form.save(commit=False)
                reg_save=request.POST.get('reg_save')
                form_save.reg_status=reg_save
                form_save.save()
                return redirect(reverse('home'))
            return render(request, self.template_name, context=context)
        else:
            if user_profile_form.is_valid():
                form_save = user_profile_form.save(commit=False)
                reg_save = request.POST.get('reg_save')
                form_save.reg_status = reg_save
                form_save.save()
                return redirect(reverse('home'))
            return render(request, self.template_name, context=context)
        #else:
          #  print(user_profile_form.errors, "++++++")



    def get(self, request, *args, **kwargs):
        usero=request.user
        account_type=usero.first_name
        reg_status=usero.user_profile.reg_status

        if (reg_status==0 and account_type=='business'):
            context = super(UserProfileView, self).get_context_data(**kwargs)
            context['user_profile_form'] = UserProfileModelForm(instance=request.user.user_profile)
            return render(request, self.template_name, context=context)

        elif(reg_status==0 and account_type=='individual'):
            context = super(UserProfileView, self).get_context_data(**kwargs)
            context['user_profile_form'] = PersonalProfileModelForm(instance=request.user.user_profile)
            return render(request, self.individual_template, context=context)

        else:
            return redirect(reverse('home'))

class HomeView(TemplateView, LoginRequiredMixin):
    template_name = "user_profile/profile.html"

    def post(self, request, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['user_profile_form'] = user_profile_form = UserProfileModelForm(request.POST, self.request.FILES,
                                                                               instance=request.user.user_profile)

        if user_profile_form.is_valid():
            user_profile_form.save()
            return redirect(reverse('home'))
        #else:
          #  print(user_profile_form.errors, "++++++")

        return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['user_profile_form'] = UserProfileModelForm(instance=request.user.user_profile)
        return render(request, self.template_name, context=context)





