import pygame

# --- EKRAN AYARLARI ---

GENISLIK = 1280
YUKSEKLIK = 720
FPS = 60

# Tam Ekran Modu ve Otomatik Ölçeklendirme Flag'leri
# pygame.SCALED: Görüntüyü bozmadan her monitöre sığdırır.
# pygame.FULLSCREEN: Oyunu tam ekranda başlatır.
EKRAN_FLAGLARI = pygame.FULLSCREEN | pygame.SCALED

# --- GÖRSEL AYARLAR ---
# Karakterlerin ekran boyutuna göre ölçeklendirilme oranı
KARAKTER_BOYUT_CARPANI = 3

# --- RENK PALETİ ---
# RGB formatında renk tanımlamaları
SIYAH = (0, 0, 0)
BEYAZ = (255, 255, 255)
ALTIN = (255, 215, 0)
GRI = (50, 50, 50)
