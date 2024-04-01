# Evolving File Creator

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


## Teknik farklılıklar


### **app-v2.py:** ile **app.py:** Arasındaki Teknik Farklar

Her iki script de belirli bir dizinde dosyalar oluşturmayı ve manipüle etmeyi amaçlamaktadır. Ancak, bu iki script arasında bazı teknik farklar bulunmaktadır. İşte bu farkların bir özetidir:

1. Dosya Boyutu Artırma Yöntemi:
  - **app-v2.py:** Dosya işlemleri için ikilik modu ("ab+") kullanır ve dosya boyutunu artırmak için null baytları (b"\0") yazar.
  - **app.py:** Dosya işlemleri için metin modu ("a") kullanır ve dosya boyutunu artırmak için null baytları ("\0") yazar.
2. Dosya Kopyalama Yöntemi:
- **app-v2.py:** Kaynak ve hedef dosyaları manuel olarak açar, kaynaktan okur ve hedefe yazar.
- **app.py:** Dosya kopyalama için shutil.copy yöntemini kullanır.
3. Hata İşleme:
- **app-v2.py:** Dosya kopyalama sırasında FileNotFoundError için try-except bloğu kullanır.
- **app.py:** Aynı şekilde try-except bloğu kullanır ancak doğrudan shutil.copy kullanarak dosya bulunamama hatalarını işler.
4. Kütüphane Kullanımı:
- **app-v2.py:** Dosya işlemleri için standart open fonksiyonunu kullanır.
- **app.py:** Dosya kopyalama gibi işlemler için shutil kütüphanesini kullanır, bu da dosya ile ilgili işlemleri basitleştirebilir ve geliştirebilir.
5. Dosya Açma Modu:
- **app-v2.py:** Manuel olarak dosya kopyalarken "rb" (ikilik okuma) ve "wb" (ikilik yazma) modlarını kullanır.
- **app.py:** Dosya içeriğini metin olarak ele alarak yazma işlemi için metin modunu ("a") kullanır.
6. Dosya Oluşturma:
- **app-v2.py:** Dosyaları "x" moduyla (özel oluşturma) oluşturur, potansiyel olarak bir FileExistsError hatası alabilir.
- **app.py:** Aynı şekilde dosya oluşturmak için "x" modunu kullanır, FileExistsError'ı benzer bir şekilde ele alır.
7. Dosya Yolu Oluşturma:
- Her iki script de dosya yollarını daha iyi çapraz platform uyumluluğu için os.path.join kullanarak oluşturur.
8. Günlükleme:
- Her iki script de işleme döngüleri hakkında bilgi çıktısı vermek için logging modülünü kullanır.
9. Bekleme Süresi:
- Her iki script de işleme döngüleri arasında 1 saniyelik bir bekleme süresi ekler.
10. Dosya Boyutu Artırma Yöntemi (app-v2.py):
- **app-v2.py:**"ab+" modunu kullanır ve null baytlarını dosya boyutunu artırmak için yazmadan önce sona konumlandırır.
11. Dosya Boyutu Artırma Yöntemi (app.py):
- **app.py:** "a" modunu kullanır ve dosyaya boyut eklemek için null baytlarını ekler.

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
