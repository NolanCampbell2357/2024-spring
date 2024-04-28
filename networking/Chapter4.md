# Chapter 4

Inside a router:
- input ports, switching, output ports, buffer management, scheduling
-  Input ports: Using header field values, lookup output port using forwarding table in input port memory
   -  Destination forwarding: forward based only on destination IP address
   -  Generalized forwarding: forward based on any set of header field values

Forwarding table:
- Longest prefix match: When looking for table entry for given destination address, use longest address prefix that matches destination address

IPv4:
  
  IPv4 datagram format:
      {
        ver: version number
        headlen:
        type of service:
        length: total length of datagram
        16-bit identifier: for reassembly
        flgs: for reassembly
        fragment offset: for reassembly
        timetolive: remaining max hops
        upper layer protocol: TCP, UDP
        header checksum:
        source IP:
        dest IP:
        options: timestamp, record route taken, etc.
        payload: typically a tcp segment
      }
  
  addressing:
  - subnet: Device interfaces that can physically reach each other without passing through an intervening router
  - IP address: subnet part (upper bits), host part (lower bits)
  - CIDR: Subnet portion of address of arbitrary length

  DHCP:
  - Dynamic Host Configuration Protocol
  - Goal: host dynamically obtains IP address from network server on join
  - Client: broadcast request, DHCP server: Broadcasts offer for IP
  
  NAT, NAT translation table:
  - All devices in local network share just one IPv4 address as far as outside world concerned
  - NAT table: [WAN side addr, LAN side addr]

IPv6:
  
  IPv6 datagram format:
      {
        ver
        pri: identify priority among datagrams in flow
        flow label: identify datagrams
        source address:
        dest address:
        payload:
      }
  
  Tunneling:
  - IPv6 datagram carried as payload in IPv4 datagram amon IPv4 routers