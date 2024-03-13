import requests
from bs4 import BeautifulSoup as bs
import concurrent.futures
import base64

class proxyLists:
    """
    get free proxy list from different sources.

    return proxy list
    """

    def __init__(self):
        self.headers = {
            "accept": "*/*",
            "accept-language": 'en-US,en;q=0.9',
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }



    def get_free_proxy(self):
        proxies_list=[]
        url_lists=["https://www.sslproxies.org/","https://free-proxy-list.net","https://www.us-proxy.org/","https://free-proxy-list.net/uk-proxy.html","https://free-proxy-list.net/anonymous-proxy.html"]
        for url in url_lists:
            try:
                response = requests.get(url,headers=self.headers,timeout=(10,10))

                table_html = bs(response.text, 'html.parser').find('div',attrs={'class':'table-responsive fpl-list'})
                table = table_html.find('table')
                tbody=table.find('tbody')
                table_row=tbody.find_all('tr')
                for row in table_row:
                    columns = row.find_all('td')
                    proxy=f"{columns[0].text.strip()}:{columns[1].text.strip()}"
                    if proxy not in proxies_list:
                        proxies_list.append(proxy)
            except:
                pass
        
        return proxies_list
                    
        
    def get_freeproxie_world(self):
        page=1
        proxies_list=[]
        while page<=11:
            try:
                url= f'https://www.freeproxy.world/?type=http&anonymity=4&country=&speed=&port=&page={page}'
                response = requests.get(url,headers=self.headers,timeout=(10,10))
                table = bs(response.content, 'html.parser').find('table',attrs={'class':'layui-table'})
                tbody=table.find('tbody')
                try:
                    table_row=tbody.find_all('tr')
                    if len(table_row)==0:
                        break
                except:
                    break
                for row_1 in table_row:
                    columns_1 = row_1.find_all('td')
                    if len(columns_1)>=8:
                        proxy=f"{columns_1[0].text.strip()}:{columns_1[1].text.strip()}"
                        proxies_list.append(proxy)
                page+=1
            except:
                pass

        return proxies_list


    def get_proxyscrape(self):
        proxies_list=[]
        try:
            url="https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&country=all&anonymity=elite&timeout=10000&proxy_format=ipport&format=json"

            response=requests.get(url,headers=self.headers,timeout=(10,10))

            proxies_json_data=response.json()['proxies']

            for proxie in proxies_json_data:
                if proxie['alive']:
                    proxies_list.append(f"{proxie['proxy']}")

        except:
            pass

        return proxies_list


    def get_proxy_list(self):
        proxies_list=[]
        try:
            url="https://www.proxy-list.download/api/v2/get?l=en&t=http"

            response=requests.get(url,headers=self.headers,timeout=(10,10))

            proxies_json_data=response.json()['LISTA']

            for proxie in proxies_json_data:
                proxies_list.append(f"{proxie['IP']}:{proxie['PORT']}")
        
        except:
            pass

        return proxies_list


    def get_anonymouse_cz_proxy(self):
        proxies_list=[]
        try:
            url="https://anonymouse.cz/proxy-list/"

            response=requests.get(url,headers=self.headers,timeout=(10,10))

            table_row=bs(response.content, 'html.parser').find('table').find_all('tr')[1:]

            for row in table_row:
                columns = row.find_all('td')
                proxy=f"{columns[0].text.strip()}:{columns[1].text.strip()}"
                proxies_list.append(proxy)
        
        except:
            pass

        return proxies_list


    def get_iproyal_proxy(self):
        proxies_list=[]
        page=1
        while page<=5:
            try:
                url=f"https://iproyal.com/free-proxy-list/?page={page}&entries=100"
                response = requests.get(url,headers=self.headers,timeout=(10,10))
                div_tag_lists=bs(response.content, 'html.parser').find('div',attrs={'class':'overflow-auto astro-lmapxigl'}).find_all('div',recursive=False)[1:]
                if len(div_tag_lists)==0:
                    break
                for div_tag in div_tag_lists:
                    child_div_tags=div_tag.find_all('div')
                    ip=child_div_tags[0].text.strip()
                    port=child_div_tags[1].text.strip() 
                    proxies_list.append(f"{ip}:{port}")
            except:
                pass
            page+=1
        
        return proxies_list


    def get_hidemy_proxy(self):
        proxies_list=[]
        try:
            url="https://hidemy.io/en/proxy-list/"
            response=requests.get(url,headers=self.headers,timeout=(10,10))
            tr_tag_lists=bs(response.content, 'html.parser').find('table').find('tbody').find_all('tr')
            for tr_tag in tr_tag_lists:
                td_tags=tr_tag.find_all('td')
                proxy=f"{td_tags[0].text.strip()}:{td_tags[1].text.strip()}"
                proxies_list.append(proxy)
        except:
            pass
        return proxies_list


    def get_proxydb_proxy(self):
        offset_num=0
        proxy_lists=[]
        while offset_num<200:
            payload_data={
                "protocol": "http",
                "protocol": "https",
                "offset": offset_num
            }
            url="https://proxydb.net/list"

            proxydb_headers={
                "accept":"application/json",
                "accept-encoding":"gzip, deflate, br, zstd",
                "accept-language":"en-US,en;q=0.9",
                "content-type":"application/x-www-form-urlencoded;charset=UTF-8",
                "host":"proxydb.net",
                "origin":"https://proxydb.net",
                "referer":"https://proxydb.net/?protocol=http&protocol=https",
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            }
            try:
                response=requests.post(url,json=payload_data,headers=proxydb_headers,timeout=(10,10))
                json_data_lists=response.json()
                for data in json_data_lists:
                    types=data['type']
                    if types=="http" or types=="https":
                        proxy=f"{data['ip']}:{data['port']}"
                        proxy_lists.append(proxy)
            except:
                pass
            offset_num+=15


    def get_advanced_proxy(self):
        proxy_lists=[]
        try:
            url="https://advanced.name/freeproxy?type=http"
            response=requests.get(url,headers=self.headers,timeout=(10,10))
            tr_tag_lists=bs(response.content, 'html.parser').find('table',attrs={"id":"table_proxies"}).find('tbody').find_all('tr')
            for tr_tag in tr_tag_lists:
                td_tags=tr_tag.find_all('td')
                ip_string=td_tags[1]["data-ip"]
                port_string=td_tags[2]["data-port"]
                ip=base64.b64decode(ip_string).decode('utf-8')
                port=base64.b64decode(port_string).decode('utf-8')
                proxy=f"{ip}:{port}"
                proxy_lists.append(proxy)
        except:
            pass
        return proxy_lists


    def get_freeproxylist_cc_proxy(self):
        proxy_lists=[]
        page=1
        while page<=5:
            url=f"https://freeproxylist.cc/servers/{page}.html"
            try:
                response=requests.get(url,headers=self.headers,timeout=(10,10))
                tr_tag_lists=bs(response.content, 'html.parser').find('table',attrs={"id":"proxylisttable"}).find('tbody').find_all('tr')
                for tr_tag in tr_tag_lists:
                    td_tags=tr_tag.find_all('td')
                    proxy=f"{td_tags[0].text.strip()}:{td_tags[1].text.strip()}"
                    proxy_lists.append(proxy)
            except:
                pass
            page+=1
        
        return proxy_lists
        

    def get_proxysitelist_proxy(self):
        proxy_lists=[]
        try:
            url="https://proxysitelist.net/"
            response = requests.get(url,headers=self.headers,timeout=(10,10))

            li_tag_lists=bs(response.content, 'html.parser').find_all('tr')[1:]
            for li_tag in li_tag_lists:
                td_tags=li_tag.find_all('td')
                proxy=f"{td_tags[0].text.strip()}:{td_tags[1].text.strip()}"
                proxy_lists.append(proxy)
        except:
            pass

        return proxy_lists



    # collect all sources free proxy 
    def get_free_proxy_lists(self):
        proxy_lists = []
        function_list = [self.get_free_proxy, self.get_freeproxie_world, self.get_proxyscrape, self.get_proxy_list,self.get_anonymouse_cz_proxy,self.get_iproyal_proxy,self.get_hidemy_proxy,self.get_proxydb_proxy,self.get_advanced_proxy,self.get_freeproxylist_cc_proxy,self.get_proxysitelist_proxy]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit tasks to the thread pool
            futures = [executor.submit(func) for func in function_list]

            # Wait for all threads to complete and collect results
            for future in concurrent.futures.as_completed(futures):
                try:
                    proxy_list = future.result()
                    if proxy_list is not None:
                        proxy_lists.extend(proxy_list)
                except:
                    pass

        return proxy_lists


