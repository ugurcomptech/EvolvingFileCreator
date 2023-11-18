# Evolving File Creator

Bu script, çalıştığı bilgisayar üzerinde, scriptin içinde belirtilen dosya yollarına `.txt` uzantılı dosyalar oluşturur. Dosyaların boyutu başlangıçta 0 KB olup saniyede 500 MB artmaktadır. Arttırılacak olan boyut ne kadar fazla olursa, işlem o kadar uzun sürebilir.


## Bu Virüs Bulaştı: Dosyaları Nasıl Bulup Silebilirim?

- Bilgisayarı kapatıp yeniden başlatarak virüsün dosya oluşturmasını engelleyebilirsiniz (Ben bu virüs de regedite kaydetme komutu eklemedim ama saldırganlar ekleyebilir).
- Size saldıran kişi yüksek ihtimalle klasör isimlerini sistem dosyalarıyla benzer şekilde bir isim yapmıştır, onları kontrol edebilirsiniz.
- Treesize gibi programlar indirip disklerinizi taratabilirsiniz ve bilmediğiniz büyük boyuttaki dosyaları silebilirsiniz.



## Kurulum

Projeyi çalıştırmak için aşağıdaki adımları takip edebilirsiniz.

1. **Python Yükleyin:** Eğer bilgisayarınızda Python yüklü değilse, [Python'un resmi web sitesinden](https://www.python.org/downloads/) Python'u indirip yükleyebilirsiniz.

2. **Gerekli Kütüphaneleri Yükleyin:** Projeyi çalıştırmak için aşağıdaki komutu terminal veya komut istemcisinde çalıştırabilirsiniz:

    ```bash
    pip install -r requirements.txt
    ```

3. **Projeyi Çalıştırın:** Aşağıdaki komutla projeyi başlatabilirsiniz:

    ```bash
    python app.py
    ```

## Klasör Yapısı

- **Program1:**
    - ArtanBoyutluDosya_1.txt
    - ArtanBoyutluDosya_2.txt
    - ...
- **Program2:**
    - ArtanBoyutluDosya_1.txt
    - ArtanBoyutluDosya_2.txt
    - ...


Her klasör, içindeki dosyaların artan boyutlu sürümlerini ve ardışık kopyalarını içerir.

## Ayarlar

Proje ayarları `app.py` dosyasının içinde yapılmaktadır. Aşağıdaki değişkenleri değiştirerek projeyi özelleştirebilirsiniz:

- `folder_paths`: Dosyaların oluşturulacağı klasör yollarını içeren bir liste.
- `file_count`: Her klasörde oluşturulan dosya sayısı.
- `file_size_increase`: Her bir dosyanın artırılacak boyutu megabayt cinsinden.
- `max_loop_count`: Döngü limiti, yani dosya oluşturma ve kopyalama işleminin kaç kez tekrarlanacağı.


## Lisans

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Bu projeyi [MIT Lisansı](https://opensource.org/licenses/MIT) altında lisansladık. Lisansın tam açıklamasını burada bulabilirsiniz.
