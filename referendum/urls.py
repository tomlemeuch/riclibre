from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from referendum.forms import CustomLoginForm, CustomPasswordResetForm, CustomSetPasswordForm, CustomPasswordChangeForm
from referendum.views import IndexView, SignupView, SignupConfirmView, AccountActivationView, \
    AskAccountActivationView, ReferendumDetailView, ReferendumVoteView, ReferendumListView, CategoryView, \
    ReferendumCreateView, \
    MyReferendumsView, ReferendumUpdateView, CustomPasswordResetView, VoteControlView, InProgressReferendumListView, \
    FavoritesReferendumListView, OverReferendumListView, UserVotedForReferendumListView, VoteConfirmedView
from referendum.views.account import AccountView
from referendum.views.comment import CommentCreateView, CommentUpdateView
from referendum.views.contact import ContactView
from referendum.views.legal import LegalView
from referendum.views.like import LikeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('legal', LegalView.as_view(), name='legal'),
    path('contact', ContactView.as_view(), name='contact'),
    path('account/<pk>', AccountView.as_view(), name='account'),
    path('signup', SignupView.as_view(), name='signup'),
    path('signup-confirm', SignupConfirmView.as_view(), name='signup_confirm'),
    path('ask-account-activation/', AskAccountActivationView.as_view(), name='ask_account_activation'),
    path('account-activation/<uidb64>/<token>/', AccountActivationView.as_view(), name='account_activation'),
    path('login', LoginView.as_view(redirect_authenticated_user=True, authentication_form=CustomLoginForm),
         name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('password_change', PasswordChangeView.as_view(
        template_name='registration/custom_password_change_form.html', form_class=CustomPasswordChangeForm),
         name='password_change'),
    path('password_change/done',
         PasswordChangeDoneView.as_view(template_name='registration/custom_password_change_done.html'),
         name='password_change_done'),
    path('password_reset',
         CustomPasswordResetView.as_view(template_name='registration/custom_password_reset_form.html',
                                         form_class=CustomPasswordResetForm),
         name='password_reset'),
    path('password_reset/done',
         PasswordResetDoneView.as_view(template_name='registration/custom_password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='registration/custom_password_reset_confirm.html', form_class=CustomSetPasswordForm),
         name='password_reset_confirm'),
    path('reser/done',
         PasswordResetCompleteView.as_view(template_name='registration/custom_password_reset_complete.html'),
         name='password_reset_complete'),

    path('referendums', ReferendumListView.as_view(), name='referendum_list'),
    path('my-referendums', MyReferendumsView.as_view(), name='my_referendums'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('in-progress', InProgressReferendumListView.as_view(), name='in_progress'),
    path('over', OverReferendumListView.as_view(), name='over'),
    path('favorites', FavoritesReferendumListView.as_view(), name='favorites'),
    path('voted', UserVotedForReferendumListView.as_view(), name='voted'),

    path('add-referendum', ReferendumCreateView.as_view(), name='referendum_create'),

    path('referendum/<slug>', ReferendumDetailView.as_view(), name='referendum'),
    path('referendum/<slug>/update', ReferendumUpdateView.as_view(), name='referendum_update'),
    path('referendum/<slug>/like', LikeView.as_view(), name='like'),
    path('referendum/<slug>/vote', VoteControlView.as_view(), name='vote_control'),
    path('referendum/<slug>/vote-confirmed', VoteConfirmedView.as_view(), name='vote_confirmed'),
    path('vote/<token>',
         permission_required('referendum.is_citizen', raise_exception=True)(ReferendumVoteView.as_view()),
         name='vote'),
    path('comment/create', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<pk>/update', CommentUpdateView.as_view(), name='comment_update'),
]
