# Mask olan segmentation verilerinden yolo modelleri için eğitim verilerinin hazırlanması
- segmentation maskları kullanrak detection datası hazırlama
- find_bbox fonksiyonu ile masklardan bounding box sınır koordinatları alınır.
- convert fonksiyonu ile koordinatları yolo koordinatlarına(0 - 1) çevrilir.
- reverse_convert ile yolo koordinatları normal koordinatlarına çevrilir.
