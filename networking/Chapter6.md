# Chapter 6

Link layer services:
- Framing, link access: Encapsulate datagram into frame, adding header, trailer
  - Channel access if shared medium
  - MAC address identify source, dest
- reliable delivery between adjacent nodes
- flow control
- error detection
- error correction
- half-duplex and full duplex

Switched local area networks:

  MAC address: Unique identifier assigned to physical device
  
  ARP, ARP table:
  - Address Resolution Protocol
  - Determine MAC address from IP address
  - [IP addr, MAC addr, TTL]
  
  Addressing, routing to another subnet :
  - Datagram is sent with dest IP of host, MAC dest of router
  - MAC dest changes as packet traverses through routers
  
  Link layer switch:
    - Store, forward ethernet frames
    
    Self-learning:
    - Learn which host can be reached through which interfaces by 
    
    Forwarding table:
    - Filled in as packets pass through switch
    - [MAC addr, interface, TTL]