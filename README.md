free_verify_proxy
===========

free_verify_proxy is a Python library that collects free proxy different source and verify whether a proxys is working or not. It checks the functionality of a given proxys by making requests to various proxy detection servers. This library is useful for anyone who needs to ensure the reliability of proxys for their applications.

Installation
------------

You can install free_proxy_verifyer via pip:

`pip install free_verify_proxy`

or

`pip install git+https://github.com/mominurr/free_verify_proxy.git`

Usage
-----

```
from free_verify_proxy import VerifyProxyLists

verify_proxy_lists = VerifyProxyLists().get_verifyProxyLists()

print(verify_proxy_lists)

['85.62.218.250:3128','45.144.65.8:4444','103.153.154.6:80',.........................,'38.156.233.78:999']

```

Contributing
------------

Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or create a pull request on GitHub.

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.