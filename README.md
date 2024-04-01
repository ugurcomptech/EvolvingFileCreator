# Gizli Dosya Oluşturucu

Bu script, çalıştığı bilgisayar üzerinde, scriptin içinde belirtilen dosya yollarına `.txt` uzantılı dosyalar oluşturur. Dosyaların boyutu başlangıçta 0 KB olup saniyede 500 MB artmaktadır. Arttırılacak olan boyut ne kadar fazla olursa, işlem o kadar uzun sürebilir.



## Güncelleme : 01.04.2024

Yazmış olduğum yeni script win32api ve win32con modülleri aracılığıyla Windows işletim sistemi özelliklerini kullanır. Dosyaları oluşturduktan sonra win32api.SetFileAttributes() fonksiyonu kullanılarak her dosyanın gizli bayrağı ayarlanır (win32con.FILE_ATTRIBUTE_HIDDEN). Böylece dosyalar normal dosya listelemelerinde görünmez olur, ancak hala işletim sistemi tarafından erişilebilirler.

Terminalden girip kontrol ettiğimiz zamanda oluşan dosyalar gözükmemektedir. 

![image](https://github.com/ugurcomptech/EvolvingFileCreator-V2/assets/133202238/63b9bbfc-775b-445c-86b9-d292eeded4be)


Aşağıdaki komutu powershell terminaline yazarak  gizli dosyaların boyutunu görebilirsiniz.

```powershell
Get-ChildItem -Recurse -Force | Measure-Object -Property Length -Sum
```

![image](https://github.com/ugurcomptech/EvolvingFileCreator-V2/assets/133202238/82fc7c43-3359-47df-b488-9cb69c568e4a)

Aşağıdaki komutu powershell terminaline yazarak gizli dosyaları direkt olarak görebilirsiniz.

```powershell
Get-ChildItem -Recurse -Force | Sort-Object Length -Descending | Format-Table FullName, Length -AutoSize
```

![image](https://github.com/ugurcomptech/EvolvingFileCreator-V2/assets/133202238/bd654c64-2fe5-4313-bf3a-b00abea66d1f)



## Güncelleme : 25.11.2023

Yazmış olduğum yeni scripti deneme testlerine tabi tuttum. Eski scripte nazaran dosya boyutunu arttırma işlemini daha hızlı gerçekleştirdi. İki dakikalık test süresinde, app.py scripti 1 dosya üzerinden yaklaşık 5 GB'lık bir dosya oluşturabildi. Diğer scriptim olan app-v2.py ise aynı süre içinde 1 dosya üzerinden yaklaşık 9 GB'lık bir dosya alanı kapladı. Teknik detaylara geçmeden önce belirtmeliyim ki, neredeyse 2 katı bir hızla bu işlemi gerçekleştiriyor. Bu, daha yüksek performansın sağlandığını gösteriyor. Ancak, ne kadar etkileyici olursa olsun, bu tür işlemleri yasal sınırlar içinde ve dikkatlice kullanmayı unutmayınız.



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
