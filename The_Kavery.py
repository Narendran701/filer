import requests

from bs4 import BeautifulSoup as bss

class college:
        def kavery(self):
                base_url = 'http://kavery.org.in/placement11-12.aspx'

                head = {'User-Agent':'Mozilla/5.0 (Linux; <Android Version>'}

                req = requests.get(url=base_url, headers=head)

                soup = bss(req.content, 'lxml')

                lokt = soup.find('table')

                t_row = lokt.find_all('tr')

                lst = []

                for tm in t_row:
                        td = tm.find_all('td')
                        row = [tp.get_text() for tp in td if tp.get_text()]
                        lst.append(row)
                st = 0
                l = ['s.No','Name','Placed']
                print(l)
                while st <=27: 
                        print(lst[st])
                        st += 1

obj = college()
obj.kavery()
		
