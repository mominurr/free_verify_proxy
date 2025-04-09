# Free Verify Proxy

`free_verify_proxy` is a Python library that collects free proxies from various sources and verifies whether they are functional. It checks the reliability of proxies by making requests to multiple proxy detection servers. This library is useful for developers, researchers, and web scrapers who need working proxies for their applications.

## Features

- Scrapes free proxies from multiple public proxy lists.

- Supports filtering proxies based on country, protocol, and anonymity level.

- Multi-threaded proxy verification for high performance.

- Uses multiple proxy judge URLs for accurate testing.

- Returns a verified list of working proxies.


# Proxy Sources

## Public Proxy Lists (HTTP/HTTPS)

- [SSL Proxies](https://www.sslproxies.org/)
- [Free Proxy List](https://free-proxy-list.net)
- [US Proxy](https://www.us-proxy.org/)
- [UK Proxy](https://free-proxy-list.net/uk-proxy.html)
- [Anonymous Proxy](https://free-proxy-list.net/anonymous-proxy.html)
- [FreeProxy World](https://www.freeproxy.world)
- [ProxyScrape](https://proxyscrape.com/free-proxy-list)
- [Proxy List Download](https://www.proxy-list.download/)
- [Geonode Proxy](https://geonode.com/free-proxy-list)
- [IP Royal](https://iproyal.com/free-proxy-list)
- [ProxyDB](https://proxydb.net/list)
- [Advanced Name](https://advanced.name/freeproxy?type=http)
- [Free Proxy List CC](https://freeproxylist.cc/servers)
- [Proxy Site List](https://proxysitelist.net/)



# Proxy Judges/Checkers

## HTTP/HTTPS

- [ProxyJudge](http://proxyjudge.us/)
- [MojeIP](http://mojeip.net.pl/asdfa/azenv.php)
- [ifconfig.me](https://ifconfig.me/ip)
- [ipinfo.io](https://ipinfo.io/ip)
- [checkip.amazonaws.com](https://checkip.amazonaws.com)
- [ipify.org](https://api.ipify.org/)
- [httpbin.org](https://httpbin.org/ip)
- [icanhazip.com](https://www.icanhazip.com/)
- [jsonip.com](https://jsonip.com/)
- [SeeIP](https://api.seeip.org/jsonip)
- [SmartProxy](https://ip.smartproxy.com/json)
- [ip-api.com](https://ip-api.com/)
- [ip.nf](https://ip.nf/me.json)


**Note:** The library uses many more proxy judges for better accuracy, ensuring reliable proxy verification.

# Installation

You can install free_verify_proxy via pip:

```
pip install free-verify-proxy
```

or

```
pip install git+https://github.com/mominurr/free_verify_proxy.git
```

When installing free_verify_proxy using pip, the necessary dependencies (requests, curl_cffi, country_converter and beautifulsoup4) will be automatically installed along with the package. You don't need to separately install these dependencies.


# Usage:

## Parameters

- **`countryCodes`** (*list, optional*):  
  A list of country codes (ISO 3166-1 alpha-2 format) to filter proxies by location.  
  **Example:** `["US", "IE", "FR"]`  
  **Default:** `["all"]` (Includes proxies from all countries).

- **`excludedCountries`** (*list, optional*):  
  A list of country codes to exclude from the proxy list.  
  **Example:** `["US", "CN"]`  
  **Default:** `[]` (No exclusion).

- **`protocols`** (*list, optional*):  
  A list of protocols to filter proxies by supported protocol type.  
  **Supported values:** `["http", "https"]`  
  **Example:** `["http"]`  
  **Default:** `["all"]` (Includes all protocol types).

- **`anonymityLevels`** (*list, optional*):  
  A list of anonymity levels to filter proxies by their anonymity.  
  **Supported values:** `["transparent", "anonymous", "high", "elite"]`  
  **Example:** `["elite", "anonymous"]`  
  **Default:** `["all"]` (Includes all anonymity levels).

- **`number_of_threads`** (*int, optional*):  
  Number of threads to use for parallel proxy verification.  
  **Default:** `100`.

- **`timeout`** (*tuple, optional*):  
  A timeout (connect, read) in seconds for proxy verification.  
  **Example:** `(5, 5)` (5-second timeout for connection and read).  
  **Default:** `(5, 5)`.


## Default Case (No Filters Applied):

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

## Custom Case (With Filters Applied):

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
  {'proxy': '13.54.47.197:80', 'countryCode': 'AU', 'protocol': 'https', 'anonymityLevel': 'elite'}
]
```


# Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or create a pull request on GitHub.

# License

This project is licensed under the MIT License - see the LICENSE file for details.