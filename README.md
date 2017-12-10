# Kur Tahmin Etme Oyunu 

Oyunun amacı seçilen gün aralığındaki kur değerlerinden yola çıkarak, bir sonraki günün kur değerini yapay zekadan daha doğru tahmin etmeye çalışmaktır.

Oyun tek kişi tarafından bilgisayara karşı oynanmaktadır. 

Proje indirildikten sonra, bulunduğu klasöre gidilerek 'python3 guessing_game.py' komutu ile oyun çalıştırılır. Internet uygulamasıdır, python3 ve flask kullanılarak sınırlı sürede geliştirilmiştir.  

1. Ekran

İlk ekranda 2 girdi alanı bulunmaktadır. Bu girdi alanlarına 1 ile 1000 arasında tam sayı değerler yazılmalıdır. 
Oyunda yaklaşık ardışık 1000 günlük kur değerleri kullanılmaktadır. 
İstenilen bir aralık seçilerek değerler görüntülenebilir ve son günün bir sonraki günü için kur tahmini yapılır. 
Örneğin: Yukarıdaki girdi alanına 50, aşağıdaki girdi alanına 250 diyelim.
Bu örnek 50. günden 250. güne kadar olan kur değerlerini grafik olarak bize gösterir. Grafik kapatıldıktan sonra değerlerin sıralı halini 2. ekranda görebiliriz. 

2. Ekran

Seçilen aralıktaki kur değerlerini gösterir.
Sayfanın en alt kısmındaki girdi alanı oyuncunun tahminidir, tahmin tam sayı veya ondalık sayı olarak yazılabilir. (Örneğin: 250 veya 250.12 yazılabilir)
Tahmin sayfadaki son değerden bir sonraki gün için yapılır. 
Yapay zeka tahmin etme algoritmasında, oyuncu tarafından 1. ekranda seçilen aralıktaki değerler kullanılarak model oluşturulmuş ve sonraki gün için tahminleme yapılmıştır. 

3. Ekran

Oyuncunun tahmini, yapay zekanın tahmini ve gerçek sonuç sırasıyla görülebilir.
Oyuncunun tahmininin gerçek değere yakın olması durumda kazandınız, aksi durumda kaybettiniz ifadeleri görülür.

# Oluşabilecek Problemler

Seçilen gün aralığı minimum 10 gün olmalıdır, aksi takdirde tahminleme algoritması hata verecektir.
Input check yapılmamıştır, beklenen değerler dışında input denemeyiniz. 






