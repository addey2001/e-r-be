from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Listing
from .serializers import ListingSerializer
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
class ElevateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

#path: /listings
#Index route 
#Method: get 
    def get(self, request):
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)
        print(serializer.data)
        return Response(serializer.data)


#create route 
#Method: Post 
    def post(self, request):
        serializer = ListingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user )
        return Response(serializer.validated_data)


#path: /listings/<int:pk>/
class ElevateDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_Listing(self, pk):
        try:
            return Listing.objects.get(pk=pk)
        except Listing.DoesNotExist as e:
            print(e)
            raise NotFound('Listing not found')
    
#show route 
    def get(self, request, pk):
        listing = self.get_Listing(pk)
        serializer = ListingSerializer(listing)
        return Response (serializer.data)

    #UPDATE route 
    def put(self, request, pk):
        listing = self.get_Listing(pk)
        serializer = ListingSerializer(listing, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.validated_data)


        #DELETE route 
    def delete(self, request, pk):
        listing = self.get_Listing(pk)
        listing.delete()

        return Response (status=204)


#path: /api/listings/:pk/favorites
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


# /listings/<int:pk>/favorite
class ListingFavoriteView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        try:
            listing = Listing.objects.get(pk=pk)
        except Listing.DoesNotExist:
            raise NotFound("Listing not found")

        listing.favorites.add(request.user)
        return Response({"message": "Added to favorites"})

    def delete(self, request, pk):
        try:
            listing = Listing.objects.get(pk=pk)
        except Listing.DoesNotExist:
            raise NotFound("Listing not found")

        listing.favorites.remove(request.user)
        return Response({"message": "Removed from favorites"})