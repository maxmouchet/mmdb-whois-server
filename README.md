# mmdb-whois-server
Serve MMDB files over the WHOIS protocol.

## Usage

First download an MMDB file, for example the free [Country & ASN database](https://ipinfo.io/products/free-ip-database) from [<img src="https://ipinfo.io/static/ipinfo-small.svg" alt="IPinfo" width="12"/> IPinfo](https://ipinfo.io):

```bash
ipinfo download country-asn -f mmdb
```

Then install the dependencies and run the server:
```bash
poetry install
# Use a non-privileged port instead of 43 so that we don't need to be root.
poetry run mmdb-whois-server --port 8043 country_asn.mmdb
```

Alternatively, you can use Docker:
```bash
docker run --rm -it -p 8043:43 -v $(pwd):/data \
    ghcr.io/maxmouchet/mmdb-whois-server:main /data/country_asn.mmdb
```

Finally, query the server:
```bash
whois -h localhost -p 8043 -- 1.1.1.1
# as-domain:       cloudflare.com
# as-name:         Cloudflare, Inc.
# asn:             AS13335
# continent:       OC
# continent-name:  Oceania
# country:         AU
# country-name:    Australia
```

## Public server

An instance of this server is hosted over IPv4 and IPv6 at `whois.dscp.dev` and serves the free Country & ASN database, updated daily:

```bash
whois -h whois.dscp.dev -- 1.1.1.1
# as-domain:       cloudflare.com
# as-name:         Cloudflare, Inc.
# asn:             AS13335
# continent:       OC
# continent-name:  Oceania
# country:         AU
# country-name:    Australia
#
# % IP address data provided by https://ipinfo.io
```
