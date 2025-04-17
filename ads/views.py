from rest_framework import viewsets, filters, permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Ad, ExchangeProposal
from .serializers import AdSerializer, ExchangeProposalSerializer
from .permissions import IsOwnerOrReadOnly, IsReceiverForStatusChange


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all().order_by('-created_at')
    serializer_class = AdSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter
    ]
    search_fields = ['title', 'description']
    filterset_fields = ['category', 'condition']
    ordering_fields = ['created_at', 'category', 'condition']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExchangeProposalViewSet(viewsets.ModelViewSet):
    queryset = ExchangeProposal.objects.all().order_by('-created_at')
    serializer_class = ExchangeProposalSerializer
    permission_classes = [permissions.IsAuthenticated, IsReceiverForStatusChange]
    pagination_class = StandardResultsSetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter
    ]
    filterset_fields = ['ad_sender', 'ad_receiver', 'status']
    ordering_fields = ['created_at', 'status']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save()