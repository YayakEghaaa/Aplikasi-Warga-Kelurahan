from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Warga
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import WargaSerializer, PengaduanSerializer
from rest_framework import viewsets

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
    API endpoint yang memungkinkan data warga dilihat, dibuat, diubah, atau dihapus.
    """
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer

class PengaduanViewSet(viewsets.ModelViewSet):
    """
    API endpoint yang memungkinkan data pengaduan dilihat, dibuat, diubah, atau dihapus.
    """
    queryset = Pengaduan.objects.all().order_by('-tanggal_lapor')
    serializer_class = PengaduanSerializer