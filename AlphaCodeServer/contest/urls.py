from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('contest/<cname>',views.disp_contest_pg),
    # path('round1',views.quiz),
    # path('round2',views.quiz2),
    path('contest/<cname>/getQuestion/<int:qno>',views.getQuestion),
    # path('saveResponse/<qno>',views.saveResponse)
]
