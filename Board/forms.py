from django.forms import ModelForm
from Board.models import *
from django.views import generic

# models.py 에 정의를 이용해 장고가 form 을 제작해줌
# form은 view에서 생성할 수 있다
class Form(ModelForm):
    class Meta:
        model = Article
        fields = ('name', 'title', 'contents', 'email')

