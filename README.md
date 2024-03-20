# free_verify_proxy

free_verify_proxy is a Python library that collects free proxy from different sources and verifies whether the proxy is working or not. It checks the functionality of given proxies by making requests to various proxy detection servers. This library is useful for anyone who needs to ensure the reliability of proxies for their applications.


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
- [Anonymouse](https://anonymouse.cz/proxy-list/)
- [IP Royal](https://iproyal.com/free-proxy-list)
- [HideMy](https://hidemy.io/en/proxy-list/)
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



# Installation

You can install free_verify_proxy via pip:

```
pip install free_verify_proxy
```

or

```
pip install git+https://github.com/mominurr/free_verify_proxy.git
```

When installing free_verify_proxy using pip, the necessary dependencies (requests and beautifulsoup4) will be automatically installed along with the package. You don't need to separately install these dependencies.


# Usage

```
from free_verify_proxy import VerifyProxyLists

verify_proxy_lists = VerifyProxyLists().get_verifyProxyLists(number_of_threads=100, timeout=(5,5))

print(verify_proxy_lists)

['85.62.218.250:3128','45.144.65.8:4444','103.153.154.6:80',.........................,'38.156.233.78:999']

```

# Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or create a pull request on GitHub.

# License

This project is licensed under the MIT License - see the LICENSE file for details.