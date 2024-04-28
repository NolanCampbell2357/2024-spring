# Chapter 3


Multiplexing/demultiplexing: UDP, TCP:
- Multiplexing at sender: Handle data from multiple sockets, add transport header
- Demultiplexing at receiver: Use header info to deliver received segments to correct socket
- How demultiplexing works: Host receives IP  datagrams, host uses IP address and port number to direct segment to socket
- Connectionless and connection oriented demultiplexing
- 

UDP segment:
      {
        source port:
        dest port:
        length: in bytes including header
        checksum: Goal to detect errors in segment
        payload
      }

Checksum:
- Compute checksum and see if it matches sent checksum

Reliable data transfer:
- rdt_send()
- use acks to ensure message is received, if not resend

TCP:
- point-to-point
- cumulative acks
- reliable, in-order stream
- bi-directional
- connection-oriented

  MSS vs. MTU:

  TCP segment:
      {
        source port:
        dest port:
        sequence number: bytes of data into bytestream
        ack number: seq # of next expected byte
        headlen:
        receive window: flow control: # bytes receiver willing to accept
        checksum:
        body:
      }

  RTT: Round-trip time

  TCP reliable data transfer:
    Fast retransmit:
    - If sender receives 3 additional ACKs for same data, resend unACKed segments with smallest seq#

  Flow control: rwnd (receive window):
  - Flow control: Receiver controls sender, so sender won't overflow receiver's buffer
  - rwnd: Field on TCP segment, advertises free buffer space

  Congestion control:
  - Too many sources sending too much data too fast
    
    AIMD (additive-increase, multiplicative-decrease):
    - Senders can increase sending rate until packet loss occurs, then decrease sending rate on loss event
    - Additive increase: Increase sending rate by 1, maximum segment size every RTT until loss detected
    - Multiplicative Decrease, sending rate in half at each loss event

    cwnd (congestion window), ssthresh (slow start threshold):
    - Increase rate exponentially, until first loss
    - initially cwnd = 1 mss
    - double cwnd every RTT
    - Switch to linear at 1/2 after first loss
    - ssthresh is set to 1/2 of cwnd before loss event
        
Connection management:
  3-way handshake:
  - Client sends SYNbit=1, SEQ=x
  - Server chooses init seq num, sends SYNbit=1, Seq=y, ACKbit=1; ACKnum=x+1
  - Client sends Ack for SynAck: ACKbit=1, ACKnum=y+1
  - Received ACK(y) indicates client is live

  Close a connection:
  - client, server each close their side of connection, send TCP segment with FIN bit = 1
  - Respond to received FIN with ACK