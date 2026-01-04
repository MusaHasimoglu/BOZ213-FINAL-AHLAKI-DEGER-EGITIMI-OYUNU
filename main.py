import pygame
import sys
import os
from settings import *
from player import Player
# Her bir bölüm modüler bir yapıda ayrı dosyalardan içe aktarılır
from bolum1 import Level1
from bolum2 import Level2
from bolum3 import Level3
from bolum4 import Level4
from bolum5 import Level5
from bolum6 import Level6
from bolum7 import Level7
from bolum8 import Level8
from bolum9 import Level9
from bolum10 import Level10
from menu import Menu 

class Game:
    def __init__(self):
        """Oyunun temel bileşenlerini ve sistemlerini başlatan yapıcı metod."""
        pygame.init()
        
        # --- SES SİSTEMİ BAŞLATMA ---
        pygame.mixer.init()
        
        # --- EKRAN AYARLARI ---
        # settings.py dosyasındaki EKRAN_FLAGLARI (Tam Ekran + Ölçekleme) eklendi
        self.pencere = pygame.display.set_mode((GENISLIK, YUKSEKLIK), EKRAN_FLAGLARI)
        pygame.display.set_caption("Ahlaki Değer Eğitimi") # Oyun ismi güncellendi
        
        # Oyunun her bilgisayarda aynı hızda çalışması için saat objesi oluşturulur
        self.clock = pygame.time.Clock()

        # Menü sistemi başlatılır ve varsayılan durum "MENU" olarak atanır
        self.menu = Menu(self.pencere)
        self.durum = "MENU" 

        # Oyuncu (Player) nesnesi tekil bir grup içinde yönetilir
        self.player = Player((100, 595)) 
        self.player_group = pygame.sprite.GroupSingle(self.player)

        # Bölüm kontrol değişkenleri
        self.current_level_id = 1 
        self.level = None

        # --- MÜZİĞİ BAŞLAT ---
        self.arka_plan_muzigi_cal()

    def arka_plan_muzigi_cal(self):
        """Atmosferi desteklemek için arka plan müziğini sonsuz döngüde başlatır."""
        muzik_yolu = "assets/Sounds/Menu Theme.wav"
        
        if os.path.exists(muzik_yolu):
            try:
                pygame.mixer.music.load(muzik_yolu)
                pygame.mixer.music.set_volume(0.15)
                pygame.mixer.music.play(loops=-1)
            except Exception as e:
                print(f"Müzik çalma hatası: {e}")
        else:
            print(f"Uyarı: {muzik_yolu} dosyası bulunamadı.")

    def setup_level(self):
        """Seçili bölüm ID'sine göre ilgili sınıfı örnekler ve oyuncu konumunu ayarlar."""
        if self.current_level_id == 1:
            self.level = Level1(self.pencere, self.player, self.player_group)
        elif self.current_level_id == 2:
            self.player.rect.centerx = 150 
            self.level = Level2(self.pencere, self.player, self.player_group)
        elif self.current_level_id == 3:
            self.player.rect.x = 100
            self.player.rect.y = 620
            self.level = Level3(self.pencere, self.player, self.player_group)
        elif self.current_level_id == 4:
            self.player.rect.x = 50 
            self.player.rect.y = 640 
            self.level = Level4(self.pencere, self.player, self.player_group)
        elif self.current_level_id == 5: 
            self.player.rect.x = 50    
            self.player.rect.y = 550  
            self.level = Level5(self.pencere, self.player, self.player_group)
        elif self.current_level_id == 6: 
            self.player.rect.x = 50    
            self.player.rect.y = 450  
            self.level = Level6(self.pencere, self.player, self.player_group)
        elif self.current_level_id == 7: 
            self.player.rect.x = 50    
            self.player.rect.y = 450  
            self.level = Level7(self.pencere, self.player, self.player_group)
        elif self.current_level_id == 8: 
            self.player.rect.x = 50    
            self.player.rect.y = 450  
            self.level = Level8(self.pencere, self.player, self.player_group)
        elif self.current_level_id == 9: 
            self.player.rect.x = 50    
            self.player.rect.y = 450  
            self.level = Level9(self.pencere, self.player, self.player_group)
        elif self.current_level_id == 10: 
            self.player.rect.x = 50    
            self.player.rect.y = 450  
            self.level = Level10(self.pencere, self.player, self.player_group)

    def run(self):
        """Oyunun ana döngüsü; olayları yönetir, ekranı günceller ve durumu kontrol eder."""
        while True:
            if self.durum == "MENU":
                self.durum = self.menu.run()
                if self.durum == "OYUN":
                    self.setup_level()
            
            elif self.durum == "OYUN":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    # --- F11 İLE TAM EKRAN GEÇİŞİ ---
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_F11:
                            pygame.display.toggle_fullscreen()

                # Her karede ekran temizlenir
                self.pencere.fill(SIYAH) 

                if self.level:
                    new_level_id = self.level.run()

                    # Bölüm geçiş kontrolü
                    if new_level_id != self.current_level_id:
                        self.current_level_id = new_level_id
                        self.setup_level()

            # Grafiklerin ekrana yansıtılması
            pygame.display.update()
            
            # FPS 60'a sabitlenir
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
