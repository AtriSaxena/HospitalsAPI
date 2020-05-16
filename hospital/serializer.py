from rest_framework import serializers

from . models import Hospitals

class HospitalsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Hospitals
        fields= ('id','state','city','name','category','medicine','address','website','specilization')