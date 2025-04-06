# PDF Çevirici - İngilizce'den Türkçe'ye

Bu proje, bir PDF dosyasındaki metinleri **İngilizce'den Türkçe'ye** çevirmek için geliştirilmiş basit bir GUI (Grafiksel Kullanıcı Arayüzü) uygulamasıdır. PDF dosyasının içeriği, sayfa sayfa ve parça parça çevrilir, çevirilen metin her sayfa için birleştirilir ve kullanıcıya sunulur.

## Özellikler

- PDF dosyasındaki metni okur ve **İngilizce'den Türkçe'ye** çevirir.
- Her sayfayı **parçalara ayırarak** çevirir ve **sayfa başına birleştirir**.
- Kullanıcı dostu **Tkinter** arayüzü ile basit ve hızlı bir kullanım sağlar.
- **İlerleme çubuğu** ile çeviri sürecini takip etme imkânı.
- Kullanıcı, çevrilen metni anında görüp kopyalayabilir.

## Gereksinimler

Bu projeyi çalıştırabilmek için aşağıdaki araçları ve kütüphaneleri kurmanız gerekmektedir:

- **Python 3.x** (Yazılım Python 3.x ile uyumlu olarak geliştirilmiştir)
- **Tkinter** (GUI için kullanılan kütüphane)
- **deep-translator** (Google Translate API kullanılarak çeviri yapılır)
- **poppler-utils** (PDF dosyalarını metne dönüştürmek için `pdftotext` komutu)

Kurulum için terminale şu komutları yazabilirsiniz:

```bash
# poppler-utils paketini yükle
sudo apt install poppler-utils

# Python kütüphanelerini yükle
pip install deep-translator
```

## Lisans
**GPL-3.0 Lisansı** altında bir proje yayınlamak istiyorsanız, GitHub deposunda ayrıca bir **LICENSE** dosyası oluşturup oraya **GPL-3.0** lisansını eklemeyi unutmayın.

<br>

> Bu program Yapay Zeka ile hazırlanmıştır. Normalde programlarımı Yapay Zeka ile hazırlamam. Bir seferilik ¯\_(ツ)_/¯
