# Chapter 5

Routing algorithms:

  Link-State, Dijkstra’s algorithm: Not writing that
  
  Distance-Vector: 
  - from time to time, each node sends its own distance vector estimate to neighbors

Routing in Internet:
  Autonomous systems (AS):
  - Aggregate routers into regions
  - Intra-AS: routing within same AS
  - Inter-AS: Routing among AS'es

  OSPF, intra-AS routing:
  - Open Shortest Path First
  - Each router floods OSPF link-state advertisements to all other routers in AS
  - Multiple link cost possible
  - Authenticated

  BGP, inter-AS routing:
  - Border Gateway routing

    eBGP, iBGP:
    - eBGP: obtain subnet reachability information from neighboring ASes
    - iBGP: propagate reachability information to all AS-internal routers

    AS-PATH (shortest):
    
    NEXT-HOP (hot potato):
    - Choose local gateway that has least intra-domain cost. Don't worry about inter-domain cost
  
  Performance vs. Policy:

ICMP:
- Communicates network level information: error reporting, ping commands