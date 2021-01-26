from testapp.models import Employee
from rest_framework.serializers import ModelSerializer

class Employeeserializer(ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
#create,update such type of things default implimantation is already there because we are using viewsets
