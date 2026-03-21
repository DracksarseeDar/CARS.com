from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from . import forms, models

class RegisterView(generic.CreateView):
    form_class = forms.CustomRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login') 

class AuthLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('congratulation')


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('login') 


class CongView(generic.ListView):
    template_name = 'cong.html'
    model = models.CustomUser
    context_object_name = 'user' 
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

# def register_view(request):
#     if request.method == 'POST':
#         form = forms.CustomRegisterForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/login/')
#     else:
#         form = forms.CustomRegisterForm()
    
#     return render(
#         request,
#         'register.html',
#         {
#             'form': form,
#         }
#     )

# def auth_login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('/congratulation/')
#     else:
#         form = AuthenticationForm()
    
#     return render(
#         request,
#         'login.html',
#         {
#             "form": form,
#         }
#     )

# def auth_logout_view(request):
#     logout(request)
#     return redirect('/login/')

# def cong_view(request):
    
#     users_list = models.CustomUser.objects.all() 
#     return render(
#         request,
#         'cong.html',
#         {
#             'user': users_list
#         }
#     )