from curl_cffi import requests
from bs4 import BeautifulSoup as bs
import concurrent.futures
import base64,random
import country_converter as coco

class ProxyScraper:
    """
    get free proxy list from different sources.

    return proxy list
    """
    def __init__(self):
        self.BrowserNames = [
                "chrome",
                "chrome99",
                "chrome100",
                "chrome101",
                "chrome104",
                "chrome107",
                "chrome110",
                "chrome116",
                "chrome119",
                "chrome120",
                "chrome123",
                "chrome124",
                "chrome131",
                "chrome133a",
                "edge99",
                "edge101",
                "safari",
                "safari15_3",
                "safari15_5",
                "safari17_0",
                "safari18_0",
                "firefox133",
                "firefox135"
            ]

    def get_free_proxy(self):
        proxies_list=[]
        url_lists=["https://www.sslproxies.org/","https://free-proxy-list.net","https://www.us-proxy.org/","https://free-proxy-list.net/uk-proxy.html","https://free-proxy-list.net/anonymous-proxy.html"]
        for url in url_lists:
            try:
                response = requests.get(url,impersonate=random.choice(self.BrowserNames),timeout=(10,10))

                table_html = bs(response.text, 'html.parser').find('div',attrs={'class':'table-responsive fpl-list'})
                table = table_html.find('table')
                tbody=table.find('tbody')
                table_row=tbody.find_all('tr')
                for row in table_row:
                    try:
                        columns = row.find_all('td')
                        if len(columns) < 7:
                            continue  # Skip malformed rows

                        proxy = f"{columns[0].text}:{columns[1].text}"
                        protocol_bool = columns[6].text.strip().lower()
                        if protocol_bool.lower() == "no":
                            protocol = "http"
                        else:
                            protocol = "https"
                        proxy_data = {
                            "proxy": proxy.strip(),
                            "countryCode": columns[2].text.strip().upper(),
                            "protocol":protocol,
                            "anonymityLevel": columns[4].text.strip().lower()
                        }

                        if proxy_data not in proxies_list:
                            proxies_list.append(proxy_data)
                    except:
                        pass
            except:
                pass
        
        return proxies_list
                    
        
    def get_freeproxie_world(self):
        page=1
        proxies_list=[]
        # for http and high anonymity level proxy
        while page<=5:
            try:
                url= f'https://www.freeproxy.world/?type=http&anonymity=4&country=&speed=&port=&page={page}'
                response = requests.get(url,impersonate=random.choice(self.BrowserNames),timeout=(10,10))
                table = bs(response.content, 'html.parser').find('table',attrs={'class':'layui-table'})
                tbody=table.find('tbody')
                try:
                    table_row=tbody.find_all('tr')
                    if len(table_row)==0:
                        break
                except:
                    break
                for row in table_row:
                    try:
                        columns = row.find_all('td')
                        if len(columns) < 7:
                            continue  # Skip malformed rows

                        proxy = f"{columns[0].text.strip()}:{columns[1].text.strip()}"
                        countryCode = coco.convert(names=columns[2].text.strip(), to='ISO2')
                        proxy_data = {
                            "proxy": proxy.strip(),
                            "countryCode": countryCode.upper(),
                            "protocol": columns[5].text.strip().lower(),
                            "anonymityLevel": columns[6].text.strip().lower()
                        }

                        if proxy_data not in proxies_list:
                            proxies_list.append(proxy_data)
                    except:
                        pass
                        
            except:
                pass
            page+=1
        
        # for https and high anonymity level proxy
        page=1
        while page<=5:
            try:
                url= f'https://www.freeproxy.world/?type=https&anonymity=4&country=&speed=&port=&page={page}'
                response = requests.get(url,impersonate=random.choice(self.BrowserNames),timeout=(10,10))
                table = bs(response.content, 'html.parser').find('table',attrs={'class':'layui-table'})
                tbody=table.find('tbody')
                try:
                    table_row=tbody.find_all('tr')
                    if len(table_row)==0:
                        break
                except:
                    break
                for row in table_row:
                    try:
                        columns = row.find_all('td')
                        if len(columns) < 7:
                            continue  # Skip malformed rows

                        proxy = f"{columns[0].text.strip()}:{columns[1].text.strip()}"
                        countryCode = coco.convert(names=columns[2].text.strip(), to='ISO2')
                        proxy_data = {
                            "proxy": proxy.strip(),
                            "countryCode": countryCode.upper(),
                            "protocol": columns[5].text.strip().lower(),
                            "anonymityLevel": columns[6].text.strip().lower()
                        }

                        if proxy_data not in proxies_list:
                            proxies_list.append(proxy_data)
                    except:
                        pass
            except:
                pass
            page+=1
        return proxies_list


    def get_proxyscrape(self):
        proxies_list=[]
        try:
            url="https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&country=all&anonymity=elite&timeout=10000&proxy_format=ipport&format=json"

            response=requests.get(url,impersonate=random.choice(self.BrowserNames),timeout=(10,10))

            proxies_json_data=response.json()['proxies']

            for proxie_data in proxies_json_data:
                if proxie_data['alive']:
                    proxies_list.append({"proxy":proxie_data["proxy"],"countryCode":proxie_data["ip_data"]["countryCode"].upper(),"protocol":proxie_data["protocol"].lower(),"anonymityLevel":proxie_data["anonymity"].lower()})

        except:
            pass

        return proxies_list


    def get_proxy_list(self):
        proxies_list=[]
        try:
            url="https://www.proxy-list.download/api/v2/get?l=en&t=http"

            response=requests.get(url,impersonate=random.choice(self.BrowserNames),timeout=(10,10))

            proxies_json_data=response.json()['LISTA']

            for proxie_data in proxies_json_data:
                proxy=f"{proxie_data['IP']}:{proxie_data['PORT']}"
                proxies_list.append({"proxy":proxy,"countryCode":proxie_data["ISO"].upper(),"protocol":"http","anonymityLevel":proxie_data["ANON"].lower()})
        except:
            pass

        try:
            url="https://www.proxy-list.download/api/v2/get?l=en&t=https"

            response=requests.get(url,impersonate=random.choice(self.BrowserNames),timeout=(10,10))

            proxies_json_data=response.json()['LISTA']

            for proxie_data in proxies_json_data:
                proxy=f"{proxie_data['IP']}:{proxie_data['PORT']}"
                proxies_list.append({"proxy":proxy,"countryCode":proxie_data["ISO"].upper(),"protocol":"https","anonymityLevel":proxie_data["ANON"].lower()})
        except:
            pass


        return proxies_list


    def get_geonode_proxy(self):
        proxies_list=[]
        try:
            url="https://proxylist.geonode.com/api/proxy-list?protocols=http%2Chttps&limit=500&page=1&sort_by=lastChecked&sort_type=desc"

            response=requests.get(url,impersonate=random.choice(self.BrowserNames),timeout=(10,10))

            proxies_json_data=response.json()['data']

            for proxie_data in proxies_json_data:
                proxy=f"{proxie_data['ip']}:{proxie_data['port']}"
                proxies_list.append({"proxy":proxy,"countryCode":proxie_data["country"].upper(),"protocol":proxie_data["protocols"][0].lower(),"anonymityLevel":proxie_data["anonymityLevel"].lower()})
        except:
            pass

        return proxies_list


    def get_iproyal_proxy(self):
        proxies_list=[]
        page=1
        while page<=5:
            try:
                url=f"https://iproyal.com/free-proxy-list/?page={page}&entries=100"
                response = requests.get(url,impersonate=random.choice(self.BrowserNames),timeout=(10,10))
                div_tag_lists=bs(response.content, 'html.parser').find('div',attrs={'class':'shadow-s'}).find_all('div',recursive=False)[1:]
                if len(div_tag_lists)==0:
                    break
                for div_tag in div_tag_lists:
                    try:
                        child_div_tags=div_tag.find_all('div')
                        proxy=f"{child_div_tags[0].text.strip()}:{child_div_tags[1].text.strip()}"
                        protocol = child_div_tags[2].text.strip()
                        countryCode=coco.convert(names=child_div_tags[3].text.strip(), to='ISO2')
                        if "http" in protocol.lower() or "https" in protocol.lower():
                            proxies_list.append({"proxy":proxy,"countryCode":countryCode.upper(),"protocol":protocol.lower(),"anonymityLevel":"unknown"})
                    except:
                        pass
            except:
                pass
            page+=1
        
        return proxies_list


    # def get_hidemy_proxy(self):
    #     proxies_list=[]
    #     for i in range(0,640,64):
    #         url = f"https://hidemy.io/en/proxy-list/?type=hs&anon=34&start={i}#list"
    #         try:
    #             response=requests.get(url,impersonate=random.choice(self.BrowserNames),timeout=(10,10))
    #             print(response.status_code)
    #             tr_tag_lists=bs(response.content, 'html.parser').find('table').find('tbody').find_all('tr')
    #             for tr_tag in tr_tag_lists:
    #                 try:
    #                     td_tags=tr_tag.find_all('td')
    #                     proxy=f"{td_tags[0].text.strip()}:{td_tags[1].text.strip()}"
    #                     protocol = td_tags[4].text.strip()
    #                     countryCode=coco.convert(names=td_tags[2].text.strip(), to='ISO2')
    #                     anonymityLevel = td_tags[5].text.strip()
    #                     proxies_list.append({"proxy":proxy,"countryCode":countryCode,"protocol":protocol,"anonymityLevel":anonymityLevel})
    #                 except:
    #                     pass
    #         except:
    #             pass
    #     return proxies_list


    def get_proxydb_proxy(self):
        offset_num=0
        proxy_lists=[]
        while offset_num<=200:
            payload_data={"protocols":["http","https"],"anonlvls":[],"offset":offset_num}
            url="https://proxydb.net/list"

            proxydb_headers={
                "accept":"*/*",
                "accept-encoding":"gzip, deflate, br, zstd",
                "accept-language":"en-US,en;q=0.9",
                "content-type":"application/x-www-form-urlencoded;charset=UTF-8",
                "host":"proxydb.net",
                "origin":"https://proxydb.net",
                "referer":"https://proxydb.net/?protocol=http&protocol=https",
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
            }
            try:
                response=requests.post(url,json=payload_data,headers=proxydb_headers,timeout=(10,10))
                json_data_lists=response.json()["proxies"]
                for data in json_data_lists:
                    types=data['type']
                    if types=="http" or types=="https":
                        proxy=f"{data['ip']}:{data['port']}"
                        anonymityLevel = data["anonlvl"]
                        if data["anonlvl"] == 4:
                            anonymityLevel = "high anonymous"
                        if data["anonlvl"] == 3:
                            anonymityLevel = "distorting"
                        if data["anonlvl"] == 2:
                            anonymityLevel = "anonymous"
                        if data["anonlvl"] == 1:
                            anonymityLevel = "transparent"
                        proxy_lists.append({"proxy":proxy,"countryCode":data["ccode"].upper(),"protocol":types,"anonymityLevel":anonymityLevel})
            except:
                pass
            offset_num+=30

        return proxy_lists





    def get_advanced_proxy(self):
        proxy_lists=[]
        try:
            url="https://advanced.name/freeproxy?type=http"
            response=requests.get(url,impersonate=random.choice(self.BrowserNames),timeout=(10,10))
            tr_tag_lists=bs(response.content, 'html.parser').find('table',attrs={"id":"table_proxies"}).find('tbody').find_all('tr')
            for tr_tag in tr_tag_lists:
                td_tags=tr_tag.find_all('td')
                ip_string=td_tags[1]["data-ip"]
                port_string=td_tags[2]["data-port"]
                ip=base64.b64decode(ip_string).decode('utf-8')
                port=base64.b64decode(port_string).decode('utf-8')
                proxy=f"{ip}:{port}"
                protocol = td_tags[3].find_all("a")[0].text.strip()
                countryCode=td_tags[4].text.strip()
                anonymityLevel = td_tags[3].find_all("a")[-1].text.strip()
                if protocol.lower() == "http" or protocol.lower() == "https":
                    proxy_lists.append({"proxy":proxy,"countryCode":countryCode.upper(),"protocol":protocol.lower(),"anonymityLevel":anonymityLevel.lower()})
        except:
            pass
        return proxy_lists


    def get_freeproxylist_cc_proxy(self):
        proxy_lists=[]
        page=1
        while page<=5:
            url=f"https://freeproxylist.cc/servers/{page}.html"
            try:
                response=requests.get(url,impersonate=random.choice(self.BrowserNames),timeout=(10,10))
                tr_tag_lists=bs(response.content, 'html.parser').find('table',attrs={"id":"proxylisttable"}).find('tbody').find_all('tr')
                for tr_tag in tr_tag_lists:
                    try:
                        td_tags=tr_tag.find_all('td')
                        proxy=f"{td_tags[0].text.strip()}:{td_tags[1].text.strip()}"
                        protocol_bool = td_tags[5].text.strip()
                        countryCode=td_tags[2].text.strip()
                        anonymityLevel = td_tags[4].text.strip()
                        if protocol_bool.lower() == "no":
                            protocol = "http"
                        else:
                            protocol = "https"
                        proxy_lists.append({"proxy":proxy,"countryCode":countryCode.upper(),"protocol":protocol,"anonymityLevel":anonymityLevel.lower()})
                    except:
                        pass
            except:
                pass
            page+=1
        
        return proxy_lists
        

    def get_proxysitelist_proxy(self):
        proxy_lists=[]
        try:
            url="https://proxysitelist.net/"
            response = requests.get(url,impersonate=random.choice(self.BrowserNames),timeout=(10,10))

            li_tag_lists=bs(response.content, 'html.parser').find_all('tr')[1:]
            for li_tag in li_tag_lists:
                try:
                    td_tags=li_tag.find_all('td')
                    proxy=f"{td_tags[0].text.strip()}:{td_tags[1].text.strip()}"
                    protocol = td_tags[2].text.strip()
                    countryCode=td_tags[3].text.strip()
                    anonymityLevel = td_tags[4].text.strip()
                    proxy_lists.append({"proxy":proxy,"countryCode":countryCode.upper(),"protocol":protocol,"anonymityLevel":anonymityLevel.lower()})
                except:
                    pass
        except:
            pass

        return proxy_lists



    # collect all sources free proxy 
    def getProxys(self):
        proxy_lists = []
        function_list = [self.get_free_proxy, self.get_freeproxie_world, self.get_proxyscrape, self.get_proxy_list,self.get_iproyal_proxy,self.get_proxydb_proxy,self.get_advanced_proxy,self.get_freeproxylist_cc_proxy,self.get_proxysitelist_proxy]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit tasks to the thread pool
            futures = [executor.submit(func) for func in function_list]

            # Wait for all threads to complete and collect results
            for future in concurrent.futures.as_completed(futures):
                try:
                    proxy_list = future.result()
                    if proxy_list is not None and len(proxy_list)!=0:
                        proxy_lists.extend(proxy_list)
                except:
                    pass
        unique_proxies = []
        seen = set()

        for proxy in proxy_lists:
            proxy_tuple = tuple(proxy.items())  # Convert dict to tuple
            if proxy_tuple not in seen:
                seen.add(proxy_tuple)
                unique_proxies.append(proxy)

        return unique_proxies



# if __name__=="__main__":
#     proxy_instance = ProxyScraper()  # Create an instance
#     unique_proxies = proxy_instance.getProxys()  # Call the method

#     print("Unique proxies:", len(unique_proxies))

#     print(unique_proxies[:3])


