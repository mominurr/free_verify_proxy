from .proxy_verify import proxyVerify
from .proxy import ProxyScraper
import concurrent.futures

class VerifyProxyLists:
    """
    This class retrieves proxies from various sources, verifies if they are working, and returns a list of functional proxies.

    ### Workflow:

    1. **Collect Proxies**: Proxies are collected from different websites.
    2. **Filter Proxies**: The collected proxy list can be filtered based on various criteria such as country, protocol, anonymity level, and more.
    3. **Verify Proxies**: Each proxy in the filtered list is verified to check if it is working. The verification happens in parallel using multiple threads for faster results.
    4. **Return Working Proxies**: The method returns a list of proxies that are confirmed to be working after the verification process.

    ### Usage:

    #### Default Case (No Filters Applied):

    If you don't need to apply any filters and want to retrieve and verify proxies from all countries, protocols, and anonymity levels, simply call the method without any arguments:

    ```python
    from free_verify_proxy import VerifyProxyLists

    # Instantiate the VerifyProxyLists class
    verify_proxy_lists = VerifyProxyLists()

    # Retrieve the verified proxy list with no filters (includes all proxies)
    verified_proxies = verify_proxy_lists.get_verifyProxyLists()

    # Print the list of verified proxies
    print(verified_proxies)

    # Example Output:
    [
        {'proxy': '3.127.121.101:80', 'countryCode': 'DE', 'protocol': 'http', 'anonymityLevel': 'elite'}, 
        {'proxy': '13.36.104.85:80', 'countryCode': 'FR', 'protocol': 'http', 'anonymityLevel': 'elite'},
        ...
        {'proxy': '15.236.106.236:3128', 'countryCode': 'FR', 'protocol': 'https', 'anonymityLevel': 'high anonymous'}
    ]
    ```

    #### Custom Case (With Filters Applied):

    You can also customize the filters to narrow down the list of proxies. Below is an example of how to filter proxies by country code, protocol, anonymity level, and more:

    ```python
    from free_verify_proxy import VerifyProxyLists

    # Instantiate the VerifyProxyLists class
    verify_proxy_lists = VerifyProxyLists()

    # Retrieve the verified proxy list based on specific filters (optional)
    verified_proxies = verify_proxy_lists.get_verifyProxyLists(
        countryCodes=["US", "FR"],           # Filter proxies by country codes (e.g., "US", "FR")
        protocols=["http", "https"],         # Filter proxies by protocol (e.g., "http", "https")
        anonymityLevels=["elite"],           # Filter proxies by anonymity level (e.g., "elite")
        excludedCountries=["CN"],            # Exclude proxies from specific countries (e.g., "CN")
        number_of_threads=150,               # Use 150 threads for parallel verification
        timeout=(5, 5)                       # Set connection and read timeout to 5 seconds
    )

    # Print the list of verified proxies
    print(verified_proxies)

    # Example Output:
    [
        {'proxy': '3.127.121.101:80', 'countryCode': 'DE', 'protocol': 'http', 'anonymityLevel': 'elite'}, 
        {'proxy': '13.36.104.85:80', 'countryCode': 'FR', 'protocol': 'http', 'anonymityLevel': 'elite'},
        ...
        {'proxy': '15.236.106.236:3128', 'countryCode': 'FR', 'protocol': 'https', 'anonymityLevel': 'high anonymous'}
    ]
    ```
    """

    def __init__(self):
        self.checker = proxyVerify()

    def get_verifyProxyLists(
        self,
        countryCodes=["all"],
        protocols=["all"],
        anonymityLevels=["all"],
        excludedCountries=[],
        number_of_threads=100,
        timeout=(5, 5)
    ):
        """
        Retrieves and verifies a list of proxies based on specified filters.

        Args:
            countryCodes (list, optional): 
                - A list of country codes (ISO 3166-1 alpha-2 format) to filter proxies by location. 
                - Example: ["US", "IE", "FR"]
                - Default: ["all"] (Includes proxies from all countries).
            
            excludedCountries (list, optional):
                - A list of country codes to exclude from the proxy list.
                - Example: ["US", "CN"]
                - Default: [] (No exclusion).

            protocols (list, optional): 
                - A list of protocols to filter proxies by supported protocol type.
                - Supported values: ["http", "https"]
                - Example: ["http"]
                - Default: ["all"] (Includes all protocol types).

            anonymityLevels (list, optional): 
                - A list of anonymity levels to filter proxies by their anonymity.
                - Supported values: ["transparent", "anonymous", "high", "elite"]
                - Example: ["elite", "anonymous"]
                - Default: ["all"] (Includes all anonymity levels).

            number_of_threads (int, optional): 
                - Number of threads to use for parallel proxy verification.
                - Default: 100.

            timeout (tuple, optional): 
                - A timeout (connect, read) in seconds for proxy verification.
                - Example: (5, 5) means a 5-second timeout for connection and read.
                - Default: (5, 5).
        """

        # Get proxy list from ProxyScraper
        proxy_lists = ProxyScraper().getProxys()

        # Ensure countryCodes is set to ["all"] if it's empty
        if len(countryCodes) == 0:
            countryCodes = ["all"]

        # Filter proxies based on excluded countries
        if excludedCountries:
            excludedCountries = [country.upper() for country in excludedCountries]
            proxy_lists = [proxy for proxy in proxy_lists if proxy['countryCode'] not in excludedCountries]

        # Filter proxies based on countryCodes
        if "all" not in countryCodes:
            countryCodes = [country.upper() for country in countryCodes]
            proxy_lists = [proxy for proxy in proxy_lists if proxy['countryCode'] in countryCodes]

        # Filter proxies based on protocols
        if "all" not in protocols:
            protocols = [protocol.lower() for protocol in protocols]
            proxy_lists = [proxy for proxy in proxy_lists if proxy['protocol'] in protocols]

        # Filter proxies based on anonymityLevels
        if "all" not in anonymityLevels:
            anonymityLevels = [anonymity.lower() for anonymity in anonymityLevels]
            proxy_lists = [proxy for proxy in proxy_lists if proxy['anonymityLevel'] in anonymityLevels]

        # If there are no proxies after filtering, return an empty list
        if len(proxy_lists) == 0:
            return []

        # Initialize list for verified proxies
        verified_proxies = []

        # Start concurrent verification using ThreadPoolExecutor
        with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_threads) as executor:
            # Start the load operations and mark each future with its proxy dict
            future_to_proxy = {executor.submit(self.checker.verify_proxy, proxy_dict, timeout): proxy_dict for proxy_dict in proxy_lists}
            for future in concurrent.futures.as_completed(future_to_proxy):
                proxy_data = future_to_proxy[future]
                try:
                    flag = future.result()
                    if flag:
                        verified_proxies.append(proxy_data)
                except:
                    pass

        return verified_proxies

