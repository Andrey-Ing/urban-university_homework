import re

1. Создайте функцию extract_image_links(html_text), которая принимает HTML-текст и извлекает ссылки на изображения.
2. Используйте регулярные выражения для поиска URL-адресов картинок с расширениями .jpg, .jpeg, .png или .gif.
3. Верните список всех найденных ссылок на изображения.

sample_html = "<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> <img src='https://example.com/image3.gif'>"

image_links = extract_image_links(sample_html)
if image_links:
  for image_link in image_links:
    print(image_link)
else:
  print("Нет ссылок с картинками в HTML тексте.")

Вывод на консоль:
https://example.com/image1.jpg
http://example.com/image2.png
https://example.com/image3.gif

Примечания:
Вам могут понадобится следующие спец. символы: / ? [] | +
Учтите что 'http' это подстрока строки 'https'.



def extract_image_links(html_text):
    pass

<img src="https://example.com/photo/low.jpg">



pattern = r'<img\s+src\s*=\s*[\'"]\s*https?://\S+[.]'


    for m in re.finditer(r'\d\d\.\d\d\.\d{4}', r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'):
        print('Дата', m[0], 'начинается с позиции', m.start())
        # -> Дата 19.01.2018 начинается с позиции 20
    # -> Дата 01.09.2017 начинается с позиции 45















