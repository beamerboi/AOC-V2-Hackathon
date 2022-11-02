from rest_framework.generics import CreateAPIView, ListAPIView
from contact.models import Contact
from contact.serializers import ContactSerializer


class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ContactListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'pk'
