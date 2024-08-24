# 🎬 Film Öneri Sistemi

Bu Streamlit uygulaması, kullanıcıların favori film türlerine ve en sevdikleri filmlere göre kişisel film önerileri almasını sağlar. OpenAI'nin GPT-4 modelini kullanarak, kullanıcıların girdiği bilgilere dayanarak 5 film önerisi sunar.

## 🚀 Başlarken

Bu uygulamayı yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### Gereksinimler

- Python 3.7 veya üzeri
- `streamlit` ve `openai` kütüphaneleri

### Kurulum

1. **Depoyu klonlayın veya indirin:**

    ```bash
    git clone https://github.com/kullaniciadi/film-oneri-sistemi.git
    cd film-oneri-sistemi
    ```

2. **Gerekli Python kütüphanelerini yükleyin:**

    ```bash
    pip install streamlit openai
    ```

3. **OpenAI API anahtarınızı alın:**

   OpenAI API anahtarınızı almak için [OpenAI](https://platform.openai.com/signup) web sitesine gidin ve kaydolun veya oturum açın.

4. **API anahtarınızı koda ekleyin:**

   `app.py` dosyasındaki `YOUR_OPENAI_API_KEY` kısmını kendi OpenAI API anahtarınız ile değiştirin:

    ```python
    openai.api_key = "YOUR_OPENAI_API_KEY"
    ```

### Uygulamayı Çalıştırma

Terminal veya komut satırından aşağıdaki komutu çalıştırarak Streamlit uygulamasını başlatın:

    
  ```bash  
   streamlit run app.py
  ```


# 📋 Kullanım

- Sevdiğiniz Film Türlerini Girin: Kullanıcı, sevdiği film türlerini virgülle ayırarak girmelidir (örneğin: Aksiyon, Komedi, Drama).

- En Sevdiğiniz 3 Filmi Girin: Kullanıcı, en sevdiği 3 filmi virgülle ayırarak girmelidir (örneğin: Inception, The Godfather, The Dark Knight).

- Öneri Al Butonuna Tıklayın: Tüm gerekli bilgiler girildikten sonra, "Öneri Al" butonuna tıklayarak kişisel film önerilerinizi alabilirsiniz.

# 🔧 Özelleştirme

Bu uygulama, OpenAI GPT-4 modelini kullanarak film önerileri sunmaktadır. İhtiyaçlarınıza göre OpenAI prompt'unu veya diğer uygulama mantığını özelleştirebilirsiniz.

# 🤝 Katkıda Bulunun

Katkıda bulunmak isterseniz, lütfen bir fork oluşturun, bir özellik dalı açın ve pull request gönderin!

# Fork oluşturun.

* Yeni bir dal (branch) oluşturun: git checkout -b feature/ÖzellikAdı

* Değişikliklerinizi commit edin: git commit -m 'Özellik ekle: ÖzellikAdı'

* Dalınıza push edin: git push origin feature/ÖzellikAdı
* 
Bir pull request açın.



# 📧 İletişim
Herhangi bir soru için lütfen nuray527@gmail.com adresinden iletişime geçin.


