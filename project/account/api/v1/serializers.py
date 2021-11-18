from rest_framework import serializers
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email','profile_image','mobile', 'username', 'password', 'password2')

    def save(self, **kwargs):
        user = User(email=self.validated_data.get('email'),
                    username=self.validated_data.get('username'),
                    mobile=self.validated_data.get('mobile'))
        if self.validated_data.get('password') != self.validated_data.get('password2'):
            raise serializers.ValidationError({
                'password': "Password doesn't match"})
        user.set_password(self.validated_data.get('password'))
        user.save()
        return user
