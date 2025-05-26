# # Alarm Sistemi - Bulanık Mantık Tabanlı Uyanma Yardımcısı

Bu proje, kullanıcının uyku kalitesi, uyanma süresi, çevresel gürültü seviyesi, gün ve iş miktarına göre bulanık mantık (fuzzy logic) kullanarak alarm şiddeti ve müzik türü öneren bir alarm sistemi arayüzü sunar.

![A resmi](https://github.com/SametURAL/ProSleep/raw/main/a.png)


## Özellikler

- **Kullanıcı Girdileri:**  
  - Uyku süresi (saat)  
  - Uyanma süresi (dakika)  
  - Gürültü seviyesi (0-100)  
  - Gün seçimi (Hafta içi, Cumartesi, Pazar)  
  - İş miktarı (0-100)  

- **Çıktılar:**  
  - Alarm şiddeti (Düşük, Orta, Yüksek)  
  - Müzik türü (Rahatlatıcı, Orta, Enerjik)  
  - Grafiksel gösterim (matplotlib ile)  
  - Alarm ve müzik türüne göre açıklamalar

---

## Kurulum ve Çalıştırma

1. Python 3.x yüklü olmalıdır.  
2. Gerekli kütüphaneleri yükleyin:  
   ```bash

    pip install numpy matplotlib scikit-fuzzy 
  ---- hata alırsanız aşağıdaki proje ortamdaki tüm kütüphaneleri indirebilirsiniz.
```bash

    pip install -r requirements.txt


   conda env create -f requirements.yml
   conda activate fuzzy_env
```

```bash
git clone https://github.com/SametURAL/ProSleep.git
```

- Proje klasörüne geç
python
```bash
cd ProSleep
```


- Programı çalıştır
```bash
python
python gui.py
```

