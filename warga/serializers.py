# warga/serializers.py

from rest_framework import serializers
from .models import Warga, Pengaduan

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        # Field yang akan ditampilkan di API
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon']

class PengaduanSerializer(serializers.ModelSerializer):
    # Menampilkan nama pelapor
    pelapor_nama = serializers.CharField(source='pelapor.nama_lengkap', read_only=True)
    
    class Meta:
        model = Pengaduan
        fields = '__all__'