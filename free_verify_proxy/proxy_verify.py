import requests
import random

class proxyVerify:
    """
    ProxyVerify class to verify if a proxy is working or not.
    Returns True if the proxy is working, else False.

    Example usage:
    ---------------
    checker = ProxyVerify()

    proxy_dict = {"proxy": "37.187.17.89:3128", "countryCode": "FR", "protocol": "http", "anonymityLevel": "elite"}

    result = checker.verify_proxy(proxy_dict)
    
    print(result)
    """
    
    def __init__(self):
        self.proxy_judges = [
            "http://proxyjudge.us/",
            "http://mojeip.net.pl/asdfa/azenv.php",
            "https://ifconfig.me/ip",
            "https://ipinfo.io/ip",
            "https://checkip.amazonaws.com",
            "https://api.ipify.org/",
            "https://httpbin.org/ip",
            "https://www.icanhazip.com/",
            "https://jsonip.com/",
            "https://api.seeip.org/jsonip",
            "https://ip.smartproxy.com/json",
            "https://ip-api.com/",
            "https://ip.nf/me.json",
            "https://wtfismyip.com/text",
            "https://myexternalip.com/raw",
            "https://ipwho.is/",
            "https://api.myip.com/",
            "https://ipinfo.io/json",
            "https://www.trackip.net/ip",
            "https://icanhazip.com",
            "https://ident.me",
            "https://api64.ipify.org",
            "https://freeipapi.com/api/json",
            "https://showip.net/",
            "https://www.myip.com/",
            "https://check-host.net/ip",
            "https://www.iplocation.net/find-ip-address",
            "https://api.db-ip.com/v2/free/self",
            "https://www.ip2location.com/",
            "https://www.whatsmyip.org/",
            "https://check.torproject.org/",
            "https://api.trackip.net/",
            "https://ipx.ac/ip",
            "https://api.my-ip.io/ip",
            "https://ip.tyk.nu/",
            "https://api.bigdatacloud.net/data/client-ip",
            "https://proxycheck.io/v2/",
            "https://www.infosniper.net/",
            "https://get.geojs.io/v1/ip",
            "https://ipapi.co/ip/",
            "https://www.canyouseeme.org/"
        ]

        self.url=None


    def verify_proxy(self, proxy_dict, timeout=(5, 5)):
        """
        Verifies if the proxy is working or not.

        Args:
            proxy_dict (dict or str): 
                - If a dictionary, it must contain the proxy address under the key 'proxy' (e.g., {"proxy": "37.187.17.89:3128"}).
                - If a string, it should be the proxy address in the format "ip:port" (e.g., "37.187.17.89:3128").
            timeout (tuple, optional): 
                - Timeout for the request. Defaults to (5, 5), where the first value is the connection timeout and the second is the read timeout.

        Returns:
            bool: 
                - True if the proxy is working (status code 200), else False.
        """
        # If a string is provided instead of a dictionary, convert it into the expected format
        if isinstance(proxy_dict, str):
            proxy_dict = {"proxy": proxy_dict}

        # Choose a random proxy judge URL
        self.url = random.choice(self.proxy_judges)

        # Prepare the proxy dictionary for the request
        proxies = {
            'http': f'http://{proxy_dict["proxy"]}',
            'https': f'https://{proxy_dict["proxy"]}'
        }

        try:
            # Make a request to the chosen judge URL
            response = requests.get(self.url, proxies=proxies, timeout=timeout)
            # If the response status code is 200, the proxy is working
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            # If any exception occurs, the proxy is not working
            return False
        
