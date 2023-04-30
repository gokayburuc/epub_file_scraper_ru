import requests
import bs4
import urllib.parse


base_url = 'https://aldebaran.ru/author/gorkiyi_maksim/'

# urllist


def URLListMaker(base_url, limitPage):
    urllist = list()
    urllist.append(base_url)

    url_page = base_url+'pagenum-'

    for pageNo in range(2, limitPage, 1):
        new_url = url_page+str(pageNo)+'/'
        print(new_url)
        urllist.append(new_url)

    return urllist

# content collector


def PageLinks(url):
    content = requests.get(url).content
    bsobj = bs4.BeautifulSoup(content, 'lxml')

    # links and linklist
    links = bsobj.find_all('a', href=True)
    linklist = [link['href']
                for link in links if str(link).find('gorkiyi_maksim') != -1]

    rawlinklist = list()

    # download links
    for x in linklist:
        newlink = urllib.parse.urljoin(url, x) + 'download.epub'
        rawlinklist.append(newlink)

    uniques = set(rawlinklist)
    print(uniques)

    return uniques


if __name__ == "__main__":
    base_url = 'https://aldebaran.ru/author/gorkiyi_maksim/'
    PageLinks(base_url)
    pass
