from exam.models import MultipleChoice, ShortAns, ImageAns
from rest_framework.serializers import ModelSerializer
# class UserSerializer(ModelSerializer):
#     class Meta:
#         model=User
#         # fields='__all__'
#         fields=('username','first_name','last_name','email','password1', 'password2')
class MultipleChoiceSerializer(ModelSerializer):
    class Meta:
        model=MultipleChoice
        fields='__all__'

class ShortAnsSerializer(ModelSerializer):
    class Meta:
        model=ShortAns
        fields='__all__'

class ImageAnsSerializer(ModelSerializer):
    class Meta:
        model=ImageAns
        fields='__all__'
