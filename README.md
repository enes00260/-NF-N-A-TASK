# INFINIA - Yapay Zeka Görsel Oluşturucu

INFINIA, metin veya ses girişini kullanarak yapay zeka ile görsel oluşturabilen modern bir web uygulamasıdır. **Dreamshaper-8** (Lykon/dreamshaper-8) modelini kullanarak hem gerçekçi hem de fütüristik/konsept sanat tarzında yüksek kaliteli görseller üretir.

## 🌟 Özellikler

- 🎨 Metin tabanlı görsel oluşturma
- 🎤 Sesli komut desteği
- 🔊 Görsel açıklamalarını sesli dinleme
- 🌙 Modern koyu tema arayüzü
- 🖼️ Yüksek kaliteli, gerçekçi ve fütüristik görsel çıktısı
- 🌐 Web tabanlı kullanıcı dostu arayüz
- ⚙️ Gelişmiş görsel ayarları
- 💾 Görsel indirme özelliği
- 🎲 Seed kontrolü ile görsel tekrarlama
- ❌ Negative prompt desteği

## 🚀 Model Bilgileri

- **Kullanılan Model:** Lykon/dreamshaper-8
- **Model Özellikleri:**
  - Fütüristik ve konsept sanat için özel olarak optimize edilmiş model
  - Gerçekçi detaylar, sinematik ışıklandırma ve vizyoner görsel çıktısı
  - Hem gerçekçi hem de sanatsal/fütüristik görsellerde üstün başarı 
  - Cyberpunk, sci-fi ve gelecek konseptlerinde olağanüstü sonuçlar
  - 512x512 ve üzeri çözünürlük desteği
  - CPU ve GPU desteği

**Not:** Model ilk kurulumda Hugging Face üzerinden indirilecektir. Model boyutu 4GB civarında olduğundan indirme işlemi internet hızınıza bağlı olarak 5-15 dakika sürebilir.

## 💡 Kullanımda En Verimli Sonuçlar İçin İpuçları

- **Fütüristik ve Yenilikçi Görseller İçin:**
  - Promptlarınıza şu anahtar kelimeler otomatik olarak eklenir: `futuristic, sci-fi, concept art, cyberpunk, advanced technology, next generation, visionary, 2050, high detail, cinematic lighting, ultra modern, innovation, future world`
  - Daha da spesifik sonuçlar için promptunuzu detaylandırın:
    - Örnek: `2040 yılında bir şehir manzarası, uçan arabalar, hologram reklamlar, ultra modern binalar, neon ışıklar, cyberpunk atmosfer`
    - Örnek: `Geleceğin robot doktoru, insanlarla iletişim kuruyor, yüksek teknoloji hastane ortamı, steril ve parlak`
    - Örnek: `Mars'ta koloni yaşamı, uzay giysili insanlar, kırmızı toprak, ileri teknoloji habitatlar`
- **Gerçekçi Portreler ve İnsanlar İçin:**
  - Promptunuza "photorealistic, lifelike, detailed facial features" gibi ifadeler ekleyin (otomatik eklenir).
  - Örnek: `Geleceğin insanı, cyberpunk tarzı, neon ışıklar, gerçekçi yüz, advanced technology`
- **Konsept Sanat ve Tasarım:**
  - "concept art, visionary, innovation, ultra modern" gibi anahtar kelimelerle hayal gücünüzü zorlayın.
  - Örnek: `Future city concept art, flying cars, green energy, smart buildings, high detail, cinematic lighting`
- **Ekstra İpuçları:**
  - Promptlarınızı İngilizce yazarsanız modelin anlama kapasitesi artar.
  - "Negative prompt" kısmına istenmeyen öğeleri ekleyerek daha temiz sonuçlar alabilirsiniz.
  - Yüksek çözünürlük ve adım sayısı daha detaylı sonuçlar verir, ancak işlem süresi uzar.

## 🎯 Detaylı Kullanım Kılavuzu

### 1. Ana Giriş Alanı
- Metin kutusu: Görsel için detaylı açıklama yazın
- Mikrofon butonu: Sesli komut verin
- Oluştur butonu: Görsel oluşturmayı başlatın

### 2. Görsel Ayarları

#### 📐 Boyut Ayarları
- Genişlik: 256px - 1024px arası (64px adımlarla)
- Yükseklik: 256px - 1024px arası (64px adımlarla)
- Önerilen: 512x512 (hız/kalite dengesi için)

#### 🎚️ Kalite Ayarları
- **Adım Sayısı (Steps):** 20-150 arası
  - 20-30: Hızlı oluşturma, düşük detay
  - 40-60: Dengeli oluşturma
  - 70+: Yüksek detay, yavaş oluşturma

- **Guidance Scale:** 1-20 arası
  - 1-5: Yaratıcı ama dağınık sonuçlar
  - 6-8: İdeal denge (önerilen: 7.5)
  - 9+: Açıklamaya daha sadık sonuçlar

#### 🎲 Seed Kontrolü
- Özel seed numarası girilebilir
- -1 değeri rastgele seed kullanır
- Rastgele seed butonu ile yeni değer üretilebilir
- Aynı görseli tekrar oluşturmak için seed'i not alın

#### ❌ Negative Prompt
- İstenmeyen özellikleri belirtin
- Varsayılan değer: "blurry, bad quality, worst quality, text, watermark"
- Özelleştirilebilir (örn: deformed, ugly, cartoon, anime)

### 3. Sonuç Görüntüleme
- Oluşturulan görsel büyük kartta gösterilir
- Görsel altında kullanılan ayarlar listelenir
- Dinle butonu: Açıklamayı sesli dinleyin
- İndir butonu: Görseli PNG formatında kaydedin

### 4. Optimizasyon İpuçları

#### 🚀 Hızlı Denemeler İçin
```
Boyut: 512x512
Adım Sayısı: 30-40
Guidance Scale: 7.5
```

#### 💎 Yüksek Kalite İçin
```
Boyut: 768x768 veya üzeri
Adım Sayısı: 50+
Guidance Scale: 7-8
Detaylı prompt ve negative prompt
```

## 🚀 Kurulum

### Model Bilgileri

- **Kullanılan Model:** Lykon/dreamshaper-8
- **Model Özellikleri:**
  - Fütüristik ve konsept sanat için özel olarak optimize edilmiş model
  - Gerçekçi detaylar, sinematik ışıklandırma ve vizyoner görsel çıktısı
  - Hem gerçekçi hem de sanatsal/fütüristik görsellerde üstün başarı
  - Yüksek detay, doku ve renk anlayışı
  - Prompt'a sadık, tutarlı kompozisyon oluşturma
  - 512x512 ve üzeri çözünürlük desteği (768x768 ve 1024x1024'te güçlü sonuçlar)
  - CPU ve GPU desteği (GPU önerilir)

**Önemli Not:** Model ilk kurulumda Hugging Face üzerinden indirilecektir. Model boyutu 4GB civarında olduğundan indirme işlemi internet hızınıza bağlı olarak 5-15 dakika sürebilir.

### Sistem Gereksinimleri

- **Minimum:**
  - 8GB RAM
  - 4GB disk alanı
  - CPU: Intel i5/AMD Ryzen 5 veya üzeri

- **Önerilen:**
  - 16GB RAM
  - NVIDIA GPU (4GB VRAM veya üzeri)
  - 8GB disk alanı
  - CPU: Intel i7/AMD Ryzen 7 veya üzeri

### Performans İyileştirmeleri

1. **Otomatik Cihaz Seçimi:**
   - GPU varsa otomatik GPU kullanımı
   - GPU belleği yetersizse otomatik CPU'ya geçiş
   - Bellek optimizasyonu için torch.no_grad() kullanımı

2. **Görsel Oluşturma Ayarları:**
   - Varsayılan boyut: 512x512 piksel
   - Adım sayısı: 30 (hız/kalite dengesi)
   - Guidance Scale: 7.5 (prompt uyumu)
   - Otomatik bellek yönetimi

3. **Hata Yönetimi:**
   - Gelişmiş hata yakalama
   - Otomatik kurtarma mekanizmaları
   - Detaylı hata loglaması

## 💪 Güçlü Yönler

- **Fütüristik Görsel Üretiminde Uzmanlaşma:**
  - Dreamshaper-8 modeli özellikle fütüristik, bilim kurgu ve ileri teknoloji konseptlerini üretmede ustalaşmıştır
  - Teknoloji ve fütürizmi harmanlayarak geleceğe dönük etkileyici sonuçlar verir
  - Cyberpunk, sci-fi ve gelecek şehirleri konularında ileri düzey görsel kalitesi
  - Sinematik ışıklandırma ve detay seviyesi ile profesyonel konsept sanat kalitesinde çıktılar

- **Teknolojik Detaylar:**
  - Modern teknolojik aygıtlar, robotlar ve ileri teknoloji yapılar konusunda zengin detaylar
  - Gerçekçi ve aynı zamanda vizyoner teknoloji tasarımları
  - Neon, hologram ve gelecekçi UI elementlerini başarıyla entegre edebilme

- **Model Değişikliği Esnekliği:**
  - Farklı Stable Diffusion modellerine kolayca geçiş yapabilme imkanı
  - Hugging Face modellerinin tamamı ile uyumlu yapı
  - Minimum kod değişikliği ile farklı özelliklerdeki modelleri entegre edebilme
  - Esnek mimari sayesinde zamanla gelişen yeni modellere hızlı adaptasyon

## 🔍 Zayıf Yönler

- **Tematik Dengesizlik:**
  - Model, fütüristik fotoğraflar ve konseptler yönünde daha baskın sonuçlar üretme eğilimindedir
  - Tarihi, rustik veya pastoral temalarda aynı seviyede başarı göstermeyebilir
  - Prompt'ta açıkça belirtilmediği durumlarda teknolojik ve modern öğeleri dahil etme eğilimi

- **Gerçekçi İnsan Portreleri:**
  - Gerçekçi insan portreleri oluştururken bazen ince anatomik detaylarda tutarsızlıklar gösterebilir
  - Özellikle el detayları ve mimikler konusunda hassas ayarlamalar gerekebilir

### Gereksinimler

- Python 3.11 veya üzeri // 3.11.9.64 ile çalıştırıldı
- pip (Python paket yöneticisi)
- Hugging Face API token'ı: `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` ** Bu tokeni kullanabilirsiniz

### Adım Adım Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/KULLANICI_ADINIZ/INFINIA.git
cd INFINIA
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt // 
```

3. Hugging Face token'ı zaten `app.py` dosyasında ayarlanmıştır:
```python
os.environ["HUGGING_FACE_HUB_TOKEN"] = "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"
```

## 🎯 Kullanım

1. Uygulamayı başlatın:
```bash
python app.py
```

2. Tarayıcınızda `http://127.0.0.1:5000` adresine gidin

3. Görsel oluşturmak için:
   - Metin kutusuna açıklama yazın veya
   - Mikrofon butonuna tıklayarak sesli komut verin
   - "Oluştur" butonuna tıklayın

4. Oluşturulan görseli:
   - Görüntüleyin
   - Açıklamasını dinleyin
   - İndirin

## 🛠️ Teknolojiler

- **Backend:**
  - Flask (Web framework)
  - Stable Diffusion (Görsel oluşturma modeli)
  - SpeechRecognition (Ses tanıma)
  - gTTS (Metin-to-Ses dönüşümü)

- **Frontend:**
  - HTML5
  - Tailwind CSS (Koyu tema desteği)
  - JavaScript
  - Font Awesome

## 📝 Önemli Notlar

- Uygulama ilk başlatıldığında model dosyaları indirilecektir
- Görsel oluşturma işlemi donanımınıza bağlı olarak zaman alabilir
- Ses tanıma özelliği için mikrofon erişimi gereklidir
- İnternet bağlantısı gereklidir
- Yüksek kaliteli görseller için daha fazla işlem süresi gerekir
- Seed numaralarını not alarak beğendiğiniz görselleri tekrar oluşturabilirsiniz

## 🔒 Güvenlik

- token temp mail ile alınmıştır
- Üretilen görselleri kontrol edin

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.

---