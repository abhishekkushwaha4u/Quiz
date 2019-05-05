from rest_framework import serializers
from .models import multiple_choice

class multiple_choiceSerializer(serializers.ModelSerializer):
    class Meta():
        model = multiple_choice
        fields = "__all__"
        #general way to include all fields
        #fields = ('question_number','question','answer','a','b','c','d')
        # or use fields="__all__"