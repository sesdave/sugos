from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from home.forms import HomeForm,MessageForm
from home.models import Post, Friend, UserMessage


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        usermes=UserMessage.objects.filter(sent_from=request.user)
        #busermes = UserMessage.objects.all()
        message=UserMessage.objects.all().order_by('-time_sent')
        nav_menu_message=UserMessage.objects.values('sent_from').distinct()
        #nav_menu_message = (UserMessage.objects.filter(sent_from=request.user) | UserMessage.objects.filter(to_who=request.user)).order_by('-time_sent')
        users = User.objects.exclude(id=request.user.id)
        friend, created = Friend.objects.get_or_create(current_user=request.user)
        friends = friend.users.all()
        user_array=[]
        for dic in nav_menu_message:
            for val,cal in dic.items():
                new_user = User.objects.get(id=cal)
                user_array.append(new_user)

        args = {
            'form': form, 
            'posts': posts,
            'users': users, 
            'friends': friends,
            'messages': message, 
            'usermes':usermes, 
            'user_array':user_array, 
            'nav_menu_message':nav_menu_message
        }
        return render(request, self.template_name, args) 

    def post(self, request):
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

        text = form.cleaned_data['post']
        form = HomeForm()
        return redirect('home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

class MessageView(TemplateView):
    template_name = 'home/message.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        friend, created = Friend.objects.get_or_create(current_user=request.user)
        friends = friend.users.all()

        args = {
            'form': form, 'posts': posts, 'users': users, 'friends': friends
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

        text = form.cleaned_data['post']
        form = HomeForm()
        return redirect('home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home')

def view_profile_with_pk(request, pk=None):
    user=User.object.get(pk=pk)
    args={
        'users':user
    }
    return render(request,'home/profile', args)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    posts = Post.objects.all().order_by('-created')
    friend, created = Friend.objects.get_or_create(current_user=user)
    friends = friend.users.all()
    args = {'user': user, 'posts':posts, 'friends': friends}
    return render(request, 'home/personal_profile.html', args)

class MessageHome(TemplateView):
    template_name = 'home/message.html'

    def get(self, request, pk):
        form = MessageForm()
        shared_user = User.objects.get(id=pk)
        #messages = UserMessage.objects.filter(to_who=pk, sent_from=request.user.pk)
        messages = (UserMessage.objects.filter(sent_from=request.user.pk, to_who=pk) | UserMessage.objects.filter(
            sent_from=pk, to_who=request.user.pk)).order_by('-time_sent')
        args = {'messages': messages,
                'shared_user': shared_user,
                'form':form
                }


        return render(request, self.template_name, args)

    def post(self, request, pk):
        sent_from = request.POST.get('sent_from')
        sent_user=User.objects.get(pk=sent_from)
        to_who = request.POST.get('to_who')
        message = request.POST.get('message')
        to_user = User.objects.get(pk=to_who)
        form = MessageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.sent_from = sent_user
            post.message = message
            post.to_who = to_user
            post.save()

        form = MessageForm()
        return redirect('view_message', pk=pk)

        args = {
                'form':form,
                }
        return render(request, self.template_name, args)



