from email.message import EmailMessage
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProfileSerializer
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.urls import reverse_lazy
from .forms import PasswordResetForm

# Create your views here.
@api_view(['POST'])
def follow(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    
    if user.followers.filter(pk=request.user.pk).exists():
        user.followers.remove(request.user)
    else:
        request.user.followings.add(user)

    serializers = ProfileSerializer(user)

    return Response(serializers.data)


@api_view(['GET'])
def profile(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


# @api_view(['POST'])
# def ForgotID(request):
#     email = request.get('email')

#     try:
#         user = get_object_or_404(get_user_model(), email = email)
#         if user is not None:
#             method_email = EmailMessage(
#                 '아이디 찾기 결과'
#                 f'회원님의 아이디는 {str(user.username)}입니다.',
#                 settings.EMAIL_HOST_USER,
#                 [email],
#             )
#             method_email.send(fail_silently=False)
#             return Response(True)
#     except:
#         return Response(False)
#     return Response(False)


# class MyPasswordResetView(PasswordResetView):
#     template_name = 'accounts/password_reset.html'
#     success_url = reverse_lazy('password_reset_done')
#     form_class = PasswordResetForm
#     # email_template_name = 'registration/password_reset_email.html'


# class MyPasswordResetDoneView(PasswordResetDoneView):
#     """
#     비밀번호 초기화 - 메일 전송 완료
#     """
#     template_name = 'accounts/password_reset_done.html'


# class MyPasswordResetConfirmView(PasswordResetConfirmView):
#     """
#     비밀번호 초기화 - 새로운 비밀번호 입력
#     """
#     template_name = 'accounts/password_reset_confirm.html'