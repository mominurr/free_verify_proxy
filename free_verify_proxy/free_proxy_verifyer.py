import requests
import random

class proxyVerify:
    """
    ProxyVerify class to verify if a proxy is working or not.
    Returns True if the proxy is working, else False.

    # Example usage:
    checker = proxyVerify()
    proxy_address = "37.187.17.89:3128"
    result = checker.verify_proxy(proxy=proxy_address)
    print(result)

    """
    
    def __init__(self):
        self.proxy_judges = [
            'http://proxyjudge.us/',
            'http://mojeip.net.pl/asdfa/azenv.php',
            "https://ifconfig.me/ip",
            "https://ipinfo.io/ip",
            "https://checkip.amazonaws.com",
            "https://api.ipify.org/",
            "https://httpbin.org/ip",
            "https://www.icanhazip.com/",
            "https://jsonip.com/",
            "https://api.seeip.org/jsonip",
            "https://ip.smartproxy.com/json",
        ]
        self.url=None


    def verify_proxy(self,proxy,timeout=(5,5)):
        """
        Verify if the proxy is working or not.
        Args:
            proxy (str): Proxy address in the format "ip:port" (e.g., "37.187.17.89:3128").
            timeout (tuple, optional): Timeout for the request. Defaults to (5, 5).
        Returns:
            bool: True if the proxy is working, else False.
        """
        self.url = random.choice(self.proxy_judges)
        proxies = {
            'http': f'http://{proxy}',
            'https': f'https://{proxy}'
        }
        try:
            response = requests.get(self.url, proxies=proxies, timeout=timeout)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False
        

