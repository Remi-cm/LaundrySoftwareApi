

class RegistrationAdminAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationAdminSerializer

    def post(self, request, *args, **kwargs):
       
        data_query = {
            'email': request.data['email'],
            'username': request.data['username'],
            'role': 'ADMIN',
            'phone': request.data['phone'],
            'password': request.data['password']
        }
        serializer = self.serializer_class(data=data_query)
        serializer.is_valid(raise_exception=True)
        user_instance = serializer.save()
        
        output_serializer = self.serializer_class(user_instance)
        
        return Response(output_serializer.data) 