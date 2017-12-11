# Kur Tahmin Etme Oyunu 

Oyunun amacı seçilen gün aralığındaki kur değerlerinden yola çıkarak, bir sonraki günün kur değerini yapay zekadan daha doğru tahmin etmeye çalışmaktır.

Oyun tek kişi tarafından bilgisayara karşı oynanmaktadır. 

Proje indirildikten sonra, bulunduğu klasöre gidilerek 'python3 guessing_game.py' komutu ile oyun çalıştırılır. Internet uygulamasıdır, python3 ve flask kullanılarak sınırlı sürede geliştirilmiştir.  


## 1. Ekran


<img width="280" alt="screen shot 2017-12-11 at 12 56 18 am" src="https://user-images.githubusercontent.com/10326364/33826096-e6d8ca66-de74-11e7-9610-bb549eac93cf.png">

İlk ekranda 2 girdi alanı bulunmaktadır. Bu girdi alanlarına 1 ile 1000 arasında tam sayı değerler yazılmalıdır. 
Oyunda yaklaşık ardışık 1000 günlük kur değerleri kullanılmaktadır. 
İstenilen bir aralık seçilerek değerler görüntülenebilir ve son günün bir sonraki günü için kur tahmini yapılır. 
Örneğin: Yukarıdaki girdi alanına 50, aşağıdaki girdi alanına 250 diyelim.
Bu örnek 50. günden 250. güne kadar olan kur değerlerini grafik olarak bize gösterir. Grafik kapatıldıktan sonra değerlerin sıralı halini 2. ekranda görebiliriz. 


<img width="963" alt="screen shot 2017-12-11 at 12 56 28 am" src="https://user-images.githubusercontent.com/10326364/33826209-41be1ee0-de75-11e7-9a73-b4c3c8428ca1.png">


## 2. Ekran

Seçilen aralıktaki kur değerlerini gösterir.
Sayfanın en alt kısmındaki girdi alanı oyuncunun tahminidir, tahmin tam sayı veya ondalık sayı olarak yazılabilir. (Örneğin: 250 veya 250.12 yazılabilir)
Tahmin sayfadaki son değerden bir sonraki gün için yapılır. 
Yapay zeka tahmin etme algoritmasında, oyuncu tarafından 1. ekranda seçilen aralıktaki değerler kullanılarak model oluşturulmuş ve sonraki gün için tahminleme yapılmıştır. 

<img width="227" alt="screen shot 2017-12-11 at 12 57 04 am" src="https://user-images.githubusercontent.com/10326364/33826218-4896cbc2-de75-11e7-92cd-16f307bab707.png">

## 3. Ekran

Oyuncunun tahmini, yapay zekanın tahmini ve gerçek sonuç sırasıyla görülebilir.
Oyuncunun tahmininin gerçek değere yakın olması durumda kazandınız, aksi durumda kaybettiniz ifadeleri görülür.


<img width="286" alt="screen shot 2017-12-11 at 12 57 21 am" src="https://user-images.githubusercontent.com/10326364/33826222-4aaa93bc-de75-11e7-9053-9a2633a3d32e.png">

## Requirements

pandas==0.19.2
numpy==1.11.3
Flask==0.12
statsmodels==0.8.0
matplotlib==1.5.3
scikit_learn==0.19.1

## Oluşabilecek Problemler

Seçilen gün aralığı minimum 10 gün olmalıdır, aksi takdirde tahminleme algoritması hata verecektir.
Input check yapılmamıştır, beklenen değerler dışında input denemeyiniz. 









