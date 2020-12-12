import re
import requests



class color:
    BLACK     = lambda s: '\033[30m' + str(s) + '\033[0m'
    RED       = lambda s: '\033[31m' + str(s) + '\033[0m'
    GREEN     = lambda s: '\033[32m' + str(s) + '\033[0m'
    YELLOW    = lambda s: '\033[33m' + str(s) + '\033[0m'
    BLUE      = lambda s: '\033[34m' + str(s) + '\033[0m'
    MAGENTA   = lambda s: '\033[35m' + str(s) + '\033[0m'
    CYAN      = lambda s: '\033[36m' + str(s) + '\033[0m'
    WHITE     = lambda s: '\033[37m' + str(s) + '\033[0m'
    UNDERLINE = lambda s: '\033[4m'  + str(s) + '\033[0m'


x = requests.get('https://api.tjournal.ru/v1.9/timeline/mainpage').json()['result']
x = sorted(x, key=lambda post: post['commentsCount'], reverse=True)

for post in x:
    if post['url'].startswith('https://tjournal.ru/animals'):
        continue
    # print('-' * 80)
    # print(color.GREEN(f"{post['commentsCount']:>3} {post['title']}"), '\n', '    ' + post['url'], sep='')
    
    try:
        url = re.match(r'https://tjournal.ru/[a-z]+/[0-9]+', post['url']).group()
    except:
        url = 'ERROR' + post['url']

    if post['title']:
        print(color.GREEN(f"{post['commentsCount']:>3} {post['title']}"), '    ' + url, sep='')

#html = requests.get('https://tjournal.ru/new').text
#pattern = re.compile('(?<=<h2 class="content-header__title l-island-a">).*?(?=</h2>)', re.DOTALL)
#for title in re.findall(pattern, html):
#    print(title.strip())


