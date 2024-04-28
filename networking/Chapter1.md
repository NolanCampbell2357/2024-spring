# Chapter 1

Protocol: 
- Control sending and receiving messages. Ex: TCP, HTTP, Skype
- Define format, order of messages send and received, actions taken on transmit and receipt.

Network edge:
  
  Host/end system:
  - Clients and servers, usually in data centers
  
  Access network:
  - wired and wireless communication links
  - Cable based: Hybrid fiber coax (HFC), Digital Subscriber Line (DSL), Ethernet
  - Wireless: Wireless local area networks (WLANs), Wide-area cellular access networks, Wi-Fi

Network core:
- Interconnected routers
- network of networks
  
  Packet switches:
  - Hosts break application-layer messages into packets, forward packets from one router to the next across links
  
    Router (Layer 3):
    - Forwards and routes received packet to next link
    - Forwarding: local action: move arriving packets from router's input link to appropriate router output link
    - Routing: global action: determine source-destination paths taken by packets
  
  Packet switching with store-and-forward:
  - Entire packet must be received before transmitted to next link
  
  Circuit switching:
  - End-End resources allocated to, reserved for "call" between source and destination. 
    - Basically, a transmission sequence gets dedicated resources
  - Frequency-Division Multiplexing (FDM): Call allocated to its own band, can transmit at max rate of that band
  - Time Division Multiplexing (TDM): Time divided into slots, each call allocated periodic slots, can transmit max rate of band during time slot
  - Packet switching allows more users to use network

Internet Structure:

  ISPs, IXP, peering, CDNs:
  - ISPs: Internet Service Providers, provide access to internet service
  - IXP:Internet Exchange Point, connects global ISPs
  - Content Delivery/Provider Network: Big company runs their own network to bring content closer to users (AWS CloudFront)

Delay:

  Transmission delay: Transmission delay seconds = L bits / R bps

  Propagation delay: Propagation delay seconds = d length of physical link / s speed m/sec

  Processing delay:

  Queuing delay: 
  - Time waiting at output link for transmission, depends on congestion level of router
  - Traffic intensity/utilization vs average queuing delay: Higher traffic = higher queuing delay

  End-to-End delay: Time from source to destination

Packet loss:
- Queue (buffer) in preceding link has finite capacity
- When buffer is full, incoming packet is dropped

Throughput and Bottleneck Link:
- Rate at which bits are being sent from sender to receiver
- Slowest link is a bottleneck, and is the average e2e throughput

Protocol Layers:
- Ip Stack: application, transport, network, link, physical
- Source builds packet top to bottom, destinations re-build bottom to top

Functionality, protocols of each layer:
- Application: Supporting network applications (IMAP, HTTP)
- Transport: process-process data transfer (TCP, UDP)
- Network: Routing of datagrams from source to destination (IP)
- Link: Data transfer between neighboring network elements (Ethernet, WiFi)
- Physical: Bits on the wire

Encapsulation:
- Wrapping one thing in another