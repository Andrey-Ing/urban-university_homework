import re

sample_html = ("<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'>"
               "<img src='https://example.com/image3.gif'> <img src='https://example.com/lolo.lol'>")


def extract_image_links(html_text):
    url_list = list()

    file_extension = '(jpe?g|png|gif)'
    pattern_teg = r'<img\s+src\s*=\s*[\'"]\s*https?://\S+[.]' + file_extension + 's*[\'"]s*>'
    pattern_url = r'https?://\S+' + file_extension

    for teg in re.finditer(pattern_teg, html_text):
        teg = teg[0]
        url_list.append(re.search(pattern_url, teg)[0])

    return url_list


image_links = extract_image_links(sample_html)
if image_links:
    for image_link in image_links:
        print(image_link)
else:
    print("Нет ссылок с картинками в HTML тексте.")
