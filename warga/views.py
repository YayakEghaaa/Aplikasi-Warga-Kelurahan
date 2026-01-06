from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Warga
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import WargaSerializer, PengaduanSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter 
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt

class WargaListView(ListView):
    model         = Warga
    template_name = 'warga/warga_list.html' 

class WargaDetailView(DetailView):
    model         = Warga
    template_name = 'warga/warga_detail.html'
    
class PengaduanListView(ListView):
    model               = Pengaduan
    template_name       = 'Warga/pengaduan_list.html'
    context_object_name = 'daftar_pengaduan'
    
class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')
    
class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')
    
class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')
    
class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')

# class WargaListAPIView(ListAPIView):
#     queryset = Warga.objects.all()
#     serializer_class = WargaSerializer

# class WargaDetailAPIView(RetrieveAPIView):
#     queryset = Warga.objects.all()
#     serializer_class = WargaSerializer

# class PengaduanListAPIView(ListAPIView):
#     queryset = Pengaduan.objects.all()
#     serializer_class = PengaduanSerializer

# class PengaduanDetailAPIView(RetrieveAPIView):
#     queryset = Pengaduan.objects.all()
#     serializer_class = PengaduanSerializer

class WargaViewSet(viewsets.ModelViewSet):
    """
    API endpoint untuk CRUD data warga.
    PUBLIC: Bisa lihat (GET)
    AUTHENTICATED: Bisa semua (GET, POST, PUT, DELETE)
    """
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']
    permission_classes = [AllowAny]

class PengaduanViewSet(viewsets.ModelViewSet):
    """
    API endpoint untuk CRUD data pengaduan.
    HANYA ADMIN: Bisa semua
    """
    queryset = Pengaduan.objects.all().order_by('-tanggal_lapor')
    serializer_class = PengaduanSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['judul', 'deskripsi']
    ordering_fields = ['status', 'tanggal_lapor']
    # Tetap menggunakan DEFAULT_PERMISSION_CLASSES (IsAuthenticated)
    # Bisa juga diatur: permission_classes = [IsAdminUser]

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def get_auth_token(request):
    """
    Endpoint untuk mendapatkan token authentication
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response(
            {'detail': 'Username dan password harus diisi'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key
        })
    else:
        return Response(
            {'detail': 'Username atau password salah'},
            status=status.HTTP_401_UNAUTHORIZED
        )