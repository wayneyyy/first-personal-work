import re
import json


def getHtml(cursor):
    url = 'https://video.coral.qq.com/varticle/5991863028/comment/v2?callback=_varticle5991863028commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + str(
        cursor) + '&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1614089967203'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    response = requests.get(url, headers=headers)
    html = response.text
    return html

def parseData(data):
    content = '"content":"(.*?)"'
    allcontent = re.compile(content, re.S).findall(data)
    return (allcontent)

def getcursor(data):
    last = '"last":"(.*?)"'
    cursor = re.compile(last, re.S).findall(data)[0]
    return (cursor)


def main():
    cursor = 0
    for i in range(1, 195):
        data = getHtml(cursor)
        contents = parseData(data)
        with open('comments.json', 'a+', encoding='utf-8') as f:
            f.write(json.dumps(contents, ensure_ascii=False, indent=1))
        cursor = getcursor(data)


main()
