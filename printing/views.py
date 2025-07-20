from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Document, PrintJob
from .serializers import DocumentSerializer, PrintJobSerializer, PrintJobCreateSerializer
from accounts.models import User

class DocumentUploadView(generics.CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        file = self.request.FILES.get('file')
        if file:
            serializer.save(
                user=self.request.user,
                original_filename=file.name,
                file_type=file.content_type
            )

class DocumentListView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Document.objects.filter(user=self.request.user)

class PrintJobCreateView(generics.CreateAPIView):
    queryset = PrintJob.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PrintJobCreateSerializer
        return PrintJobSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PrintJobListView(generics.ListAPIView):
    serializer_class = PrintJobSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return PrintJob.objects.filter(user=self.request.user).order_by('-created_at')

class PrintJobDetailView(generics.RetrieveAPIView):
    serializer_class = PrintJobSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return PrintJob.objects.filter(user=self.request.user)