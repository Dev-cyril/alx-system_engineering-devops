# 0x10. HTTPS SSL
``DevOps`` ``SysAdmin`` ``Security``

Concepts
* DNS
* Web stack debugging
* Bash function
* [HTTPS](https://www.instantssl.com/http-vs-https)
* [the two main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)
* [HAProxy SSL termination on Ubuntu 16.04](https://devops.ionos.com/tutorials/install-and-configure-haproxy-load-balancer-on-ubuntu-1604/)
* [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)

## Tasks
| Files | Descriptions |
|-------|--------------|
[0-world_wide_web](./0-world_wide_web) | configures domain zone so that the subdomain 'www' points to load-balancer IP and bash script also display information about subdomains
[1-haproxy_ssl_termination](./1-haproxy_ssl_termination) | configures HAproxy to handle encryted traffic, unencrypt it and pass it on to its destination.
[100-redirect_http_to_https](/100-redirect_http_to_https) | enforce HTTPS traffic so that no unecrpted traffic is possible (ie., configures HAproxy to automatically redirect HTTP traffic to HTTPS

