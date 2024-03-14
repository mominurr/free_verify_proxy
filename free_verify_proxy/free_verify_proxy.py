from .free_proxy_verifyer import proxyVerify
from .proxy import proxyLists
import concurrent.futures

class VerifyProxyLists:
    """
    get verify proxy list. proxy collected from different websites. 

    after collecting proxy list, verify if the proxy is working or not. 

    after verification, return the working proxy list.

    usage:

        from free_verify_proxy import VerifyProxyLists

        verify_proxy_lists = VerifyProxyLists().get_verifyProxyLists()

        print(verify_proxy_lists)

        ['85.62.218.250:3128','45.144.65.8:4444','103.153.154.6:80',.........................,'38.156.233.78:999']

    """
    def __init__(self):
        self.checker = proxyVerify()

    def verifyer(self, proxy_list, timeout):
        verified_list = []
        for proxy in proxy_list:
            try:
                if self.checker.verify_proxy(proxy=proxy, timeout=timeout):
                    verified_list.append(proxy)
            except:
                pass
        return verified_list


    def get_verifyProxyLists(self, number_of_threads=100, timeout=(5, 5)):
        """
        Args:
            number_of_threads (int, optional): Number of threads to use for verification. Defaults to 100.

            timeout (tuple, optional): Timeout for proxy verification. Defaults to (5,5).
            
        """
        proxy_lists = proxyLists().get_free_proxy_lists()
        verified_proxies = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_threads+1) as executor:
            futures = []
            chunk_size = len(proxy_lists) // number_of_threads
            for i in range(0, len(proxy_lists), chunk_size):
                chunk = proxy_lists[i:i + chunk_size]
                future = executor.submit(self.verifyer, chunk, timeout)
                futures.append(future)

            for future in concurrent.futures.as_completed(futures):
                try:
                    verified_proxies.extend(future.result())
                except:
                    pass

        return verified_proxies

