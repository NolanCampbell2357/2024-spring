# Chapter 2

Network application architecture:

  Client-server, Peer-to-peer:
  - Client-server:
    - Server: Always-on host, permanent IP address, in data centers for scaling
    - Client: contact, communicate with server, may be intermittently connected, Dynamic IP address, not communicate with each other
    - HTTP, FTP
  - Peer-to-peer:
    - No always on server
    - Peer requests service from other peers, self scalable
    - P2P file sharing

Client and server processes:
- Client process: Process that initiates communication
- Server Process: process that waits to be contacted
- Use IP address : socket to communicate between client-server

Transport services:
  - Data integrity/reliable data transfer: file transfer, web transactions. 
  - Throughput: Some apps need minimum amount, others elastic
  - Timing: Some apps require little delay (video games)

Web and HTTP:
  HTTP Object: 
  - Usually a file like a HTML, of JS file
  
  Non-persistent and persistent connections, performance:
  - Non-persistent
    1. TCP connection opened
    2. At most one object sent over TCP
    3. TCP connection closed
  - Persistent HTTP
    1. TCP connection opened
    2. Multiple objects send over single TCP connection
    3. TCP connection closed
  
  RTT:
  - RTT: Time for a small packet to travel from client to server and back
  - HTTP response time per object on non-persistent conenection:
    - One RTT to initiate TCP connection
    - One RTT for HTTP request and first few bytes of HTTP response to return
    - 2 per HTTP object, overhead for each TCP connection
  - Persistent HTTP
    - One RTT for all objects
  
  HTTP request/response messages:
        {
          method: "string"
          URL: "string"
          version: "string"
          headers: [header field: "value", ...]
          body: 
        }

  HTTP methods and status codes:
  - Methods
    - POST: POST form content to server
    - GET: Send data to server
    - HEAD: Request headers
    - PUT: Upload new file to server
  - Status codes:
    - 200 OK: Request succeeded
    - 301 Moved Permanently
    - 400 Bad Request
    - 404 Not Found
    - 505 HTTP version not supported

  HTTP headers:

  Cookies:
  - Little piece of data stored on client to maintain state

  Web caching (proxy):
  - Satisfy client request without involving origin server
  - Store objects in cache for faster retrieve
  
  Conditional GET:
  - Goal: Don't send object if cache has up-to-date version
  - Cache: specify date of cached copy in HTTP request: If-modified-since: <date>
  - Server: response contains no object if cached copy is up-to-date
    - Returns 304 Not Modified
  
  HTTP/2:
  - Key goal: Decreased delay in multi-object HTTP requests
  - Multiple, pipelined GETS over single TCP connection
  
  HTTP/3: 
  - Adds security, per object error- and congestion- control over UDP

DNS:
- Domain Name System: Distributed database implements in hierarchy of many name servers
  
  Different DNS servers, Recursive queries:
  - Root name servers: Official, contact-of-last-resort by name servers that can not resolve name
  - Top-level Domain Server (TLD): Responsible for .com, .org, country domains
  - Authoritative DNS Servers: Organization's own DNS server(s), providing authoritative hostname to IP mappings for organization
  - Local DNS name servers: Does not strictly belong in hierarchy, each ISP has one, first place host request goes
  
  DNS records (4 types):
    - Structure: (name, value, type, TTL)
    - type=A
      - `name` is hostname
      - `value` is ip address
    - Type=CNAME
      - `name` is alias name for some canonical name
      - Ex: www.ibm.com is really servereast2.bakup.ibm.com
      - `value` is canonical name
    - Type=NS
      - `name` is domain (foo.com)
      - `value` is hostname of authoritative name server for this domain
    - Type=MX
      - `value` is name of mailserver associated with `name`

  DNS query/response messages:
      {
        identification: 16 bit # for quury, reply uses same #
        flags: [query or reply, recursion desired, recursion available, reply is authoritative]
        questions: name, type fields for query
        answers: RRs in response to query
        authority: records for authoritative servers
      }

Wireshark:
  HTTP and DNS trace: Look at HWs

Socket and socket programming:
  UDP socket: no "connection" between client and server. Client sends and hopes it gets there
  TCP socket: Client and server communicate, ensure no missed packet