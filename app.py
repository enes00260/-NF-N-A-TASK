"""
INFINIA - Yapay Zeka Görsel Oluşturucu
=====================================
Bu uygulama, kullanıcıların metin veya ses girişi ile yapay zeka destekli görseller oluşturmasını sağlar.
Stable Diffusion XL modeli kullanılarak yüksek kaliteli görseller üretilir.

Temel Özellikler:
- Metin tabanlı görsel oluşturma
- Sesli komut desteği
- Text-to-Speech özelliği
- Yüksek çözünürlüklü görsel çıktısı
"""

# Gerekli kütüphanelerin içe aktarılması
from flask import Flask, request, jsonify, render_template  # Web framework için temel modüller
import os  # Dosya sistemi işlemleri için
import base64  # Görsel ve ses verilerinin kodlanması için
from PIL import Image  # Görsel işleme için
import io  # Giriş/çıkış işlemleri için
import torch  # PyTorch - derin öğrenme framework'ü
from diffusers import StableDiffusionPipeline  # Stable Diffusion modeli için
import speech_recognition as sr  # Ses tanıma için
from gtts import gTTS  # Metin-to-Ses dönüşümü için
import tempfile  # Geçici dosya işlemleri için
import random  # Rastgele sayı üretimi için
import time  # Zaman işlemleri için
from deep_translator import GoogleTranslator

# Flask uygulamasının oluşturulması
app = Flask(__name__)

# Hugging Face API token'ının ayarlanması
os.environ["HUGGING_FACE_HUB_TOKEN"] = "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"

# CUDA (GPU) kullanılabilir mi kontrol et
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Kullanılan cihaz: {device}")

# Stable Diffusion modelinin yüklenmesi
model_id = "Lykon/dreamshaper-8"  # Fütüristik ve konsept sanat için güçlü model
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32,
    use_auth_token=os.environ["HUGGING_FACE_HUB_TOKEN"]
)

# Model'i seçilen cihaza taşı
pipe = pipe.to(device)

# Görsel kayıt klasörünün oluşturulması
# Üretilen görseller bu klasörde saklanacak
UPLOAD_FOLDER = 'static/generated'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def enhance_prompt(prompt):
    tr_to_en = {
        "araba": "car",
        "uzay": "space",
        "robot": "robot",
        "gelecek": "future",
        "şehir": "city",
        "insan": "person",
        "gemi": "ship",
        "dünya": "earth",
        "modern": "modern",
        "ev": "house",
        "teknoloji": "technology",
        "uçak": "airplane",
        "bilim": "science",
        "sanat": "art",
        "yapay zeka": "artificial intelligence",
        "uzay gemisi": "spaceship",
        "geleceğin": "future",
        "cyberpunk": "cyberpunk",
        "atmosfer": "atmosphere",
        "futuristik": "futuristic",
        "neon": "neon",
        "ışık": "light",
        "yüksek teknoloji": "high technology",
        "koloni": "colony",
        "mars": "mars",
        "insansı": "humanoid",
        "portre": "portrait",
        "şehir manzarası": "cityscape",
        "uçan araba": "flying car",
        "hologram": "hologram",
        "enerji": "energy",
        "bilim kurgu": "science fiction",
        "gelecek şehir": "future city",
        "ileri teknoloji": "advanced technology",
        "konsept": "concept",
        "tasarım": "design",
        "detaylı": "detailed",
        "yüksek detay": "high detail",
        "sinematik": "cinematic",
        "uzaylı": "alien",
        "yapay": "artificial",
        "akıllı": "smart",
        "gökdelen": "skyscraper",
        "otonom": "autonomous",
        "drone": "drone",
        "bilgisayar": "computer",
        "telefon": "smartphone",
        "tablet": "tablet",
        "kadın": "woman",
        "erkek": "man",
        "çocuk": "child",
        "yaşlı": "elderly",
        "doğa": "nature",
        "orman": "forest",
        "dağ": "mountain",
        "deniz": "sea",
        "okyanus": "ocean",
        "nehir": "river",
        "göl": "lake",
        "plaj": "beach",
        "ada": "island",
        "çöl": "desert",
        "gök": "sky",
        "yıldız": "star",
        "gezegen": "planet",
        "galaksi": "galaxy",
        "astronot": "astronaut",
        "uydu": "satellite",
        "meteor": "meteor",
        "köprü": "bridge",
        "yol": "road",
        "ofis": "office",
        "havalimanı": "airport",
        "istasyon": "station",
        "park": "park",
        "gemi": "ship",
        "uçak": "aircraft",
        "helikopter": "helicopter",
        "tren": "train",
        "otobüs": "bus",
        "motorsiklet": "motorcycle",
        "bisiklet": "bicycle",
        "elektrikli araç": "electric vehicle",
        "portre": "portrait",
        "yüz": "face",
        "heykel": "sculpture",
        "resim": "painting",
        "grafiti": "graffiti",
        "poster": "poster",
        "illüstrasyon": "illustration",
        "doktor": "doctor",
        "mühendis": "engineer",
        "öğretmen": "teacher",
        "bilim insanı": "scientist",
        "sanatçı": "artist",
        "programcı": "programmer",
        "lazer": "laser",
        "kristal": "crystal",
        "metal": "metallic",
        "cam": "glass",
        "karanlık": "dark",
        "renkli": "colorful",
        "parlak": "bright",
        "minimalist": "minimalistic"
    }

    style_enhancers = {
        "cyberpunk": "cyberpunk style, futuristic city",
        "retro": "vintage, retro aesthetics"
    }

    """
    Prompt'u zenginleştiren yardımcı fonksiyon
    - Türkçe promptu otomatik olarak İngilizce'ye çevirir (deep-translator ile)
    - Kalite artırıcı ve fütüristik anahtar kelimeler ekler
    """
    try:
        translated = GoogleTranslator(source='auto', target='en').translate(prompt)
    except Exception:
        translated = prompt  # Çeviri başarısız olursa orijinal promptu kullan
    future_enhancers = "futuristic, concept art, high detail"
    base_enhancers = "highly detailed, 4k, HD, sharp focus, high quality, professional lighting"
    enhanced_prompt = translated.lower()
    for tr, en in tr_to_en.items():
        if tr in enhanced_prompt:
            enhanced_prompt = enhanced_prompt.replace(tr, en)
    added_enhancers = []
    for category, enhancers in style_enhancers.items():
        if category in prompt.lower():
            added_enhancers.append(enhancers)
    all_enhancers = [base_enhancers, future_enhancers] + added_enhancers
    return f"{enhanced_prompt}, {', '.join(all_enhancers)}"


@app.route('/')
def home():
    """Ana sayfa route'u - index.html şablonunu render eder"""
    return render_template('index.html')

@torch.no_grad()
def generate_image(prompt, negative_prompt, width, height, num_inference_steps, guidance_scale, generator):
    return pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        width=width,
        height=height,
        num_inference_steps=num_inference_steps,
        guidance_scale=guidance_scale,
        generator=generator
    ).images[0]

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        original_prompt = data.get('prompt', '')
        
        # Prompt'u zenginleştir
        enhanced_prompt = enhance_prompt(original_prompt)
        
        # Görüntü oluşturma ayarları
        width = int(data.get('width', 512))  # Varsayılan boyutu düşürdük
        height = int(data.get('height', 512))  # Varsayılan boyutu düşürdük
        num_inference_steps = int(data.get('steps', 30))  # Adım sayısını azalttık
        guidance_scale = float(data.get('guidance_scale', 7.5))  # Guidance scale'i düşürdük
        
        # İstenmeyen öğeleri engellemek için negatif prompt
        negative_prompt = "blurry, bad quality, worst quality, text, watermark, signature, out of focus, ancient, historical, ruins, buildings, temples, mosques, old architecture"
        
        # Seed yönetimi - görsel tekrarlanabilirliği için
        seed = data.get('seed', None)
        if seed is None or seed == -1:
            seed = random.randint(0, 2147483647)
        else:
            seed = int(seed)
        generator = torch.Generator(device=device).manual_seed(seed)
        
        # Görsel oluşturma
        try:
            image = generate_image(
                prompt=enhanced_prompt,
                negative_prompt=negative_prompt,
                width=width,
                height=height,
                num_inference_steps=num_inference_steps,
                guidance_scale=guidance_scale,
                generator=generator
            )
        except RuntimeError as e:
            if "out of memory" in str(e):
                print("GPU bellek hatası, CPU'ya geçiliyor...")
                pipe = pipe.to("cpu")
                generator = torch.Generator(device="cpu").manual_seed(seed)
                image = generate_image(
                    prompt=enhanced_prompt,
                    negative_prompt=negative_prompt,
                    width=width,
                    height=height,
                    num_inference_steps=num_inference_steps,
                    guidance_scale=guidance_scale,
                    generator=generator
                )
                pipe = pipe.to(device)  # İşlem bittikten sonra GPU'ya geri dön
            else:
                raise e
        # Oluşturulan görseli kaydet
        timestamp = int(time.time())
        image_filename = f"generated_{timestamp}.png"
        image_path = os.path.join(UPLOAD_FOLDER, image_filename)
        image.save(image_path)
        
        relative_path = os.path.join('static', 'generated', image_filename)
        
        return jsonify({
            'success': True,
            'image_path': relative_path,
            'description': enhanced_prompt,
            'settings': {
                'width': width,
                'height': height,
                'steps': num_inference_steps,
                'guidance_scale': guidance_scale,
                'negative_prompt': negative_prompt,
                'seed': seed
            }
        })
    except Exception as e:
        print(f"Hata detayı: {str(e)}")  # Hata loglaması ekledik
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    """
    Ses-to-Metin dönüşüm endpoint'i
    
    Bu fonksiyon:
    1. Ses dosyasını alır
    2. Google Speech Recognition ile metne çevirir
    3. Sonucu JSON formatında döndürür
    """
    try:
        audio_file = request.files['audio']
        recognizer = sr.Recognizer()
        
        # Geçici dosya oluştur ve ses dosyasını kaydet
        with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
            audio_file.save(temp_audio.name)
            with sr.AudioFile(temp_audio.name) as source:
                audio = recognizer.record(source)
                # Türkçe dil desteği ile metne çevir
                text = recognizer.recognize_google(audio, language='tr-TR')
        
        # Geçici dosyayı sil
        os.unlink(temp_audio.name)
        return jsonify({'success': True, 'text': text})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    """
    Metin-to-Ses dönüşüm endpoint'i
    
    Bu fonksiyon:
    1. Metni alır
    2. Google Text-to-Speech ile ses dosyası oluşturur
    3. Ses dosyasını base64 formatında döndürür
    """
    try:
        data = request.get_json()
        text = data.get('text', '')
        # Türkçe dil desteği ile ses oluştur
        tts = gTTS(text=text, lang='tr')
        # Geçici ses dosyası oluştur
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_audio:
            tts.save(temp_audio.name)
            # Ses dosyasını base64'e dönüştür
            with open(temp_audio.name, 'rb') as audio_file:
                audio_data = base64.b64encode(audio_file.read()).decode('utf-8')
        # Geçici dosyayı sil
        os.unlink(temp_audio.name)
        return jsonify({'success': True, 'audio': audio_data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Uygulama başlatma ayarları
if __name__ == '__main__':
    app.run(debug=True)  # Debug modu aktif, geliştirme için ideal 