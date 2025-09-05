from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.common import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


# Create your views here.
class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(pk=serializer.data['id'])
        refresh = RefreshToken.for_user(user)
        return Response({'Access': str(refresh.access_token)}, 201)