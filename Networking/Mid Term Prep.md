
# MID TERM PREP

## Basics
Networking Topologies

Layered Architecture

datagram network, IP addresses, and routing algorithms and protocols.

Network edge- devices involved (hosts clients and servers )
Network core- Routing data efficiently across the network ( interconnected routers, network of network)

Throughput-amt data transferred per second ( bps)
Latency- Delay in data transmission
Packet loss- lost packet in data transmission

## Protocols
Protocol - Protocols define the format, order of messages sent and receivedamong network entities, and actions takenon msg transmission, receipt
TCP- Transmission control protocol
UDP - User Datagram Protocol



Bandwith - max capcity , ideal condition, 
Throughput- actual data transfer rate , network condition, 

## FDM

FDM- frequency division multiplexing 
is a technique used to send multiple signals over the same communication channel by giving each signal a different frequency.

Analogy : large apartment with multiple family, in one telephone wire 

## NIBBLE 

1 byte = 8 bits
1 nibble = 4 bits 
Hexademical A which is 1010 is stored in 1 nibble 


Physical link - coaxial cable, fiber optic cable, WIFI, 

message is broken down to packets of length L bits
R- Transmission rate 
packet transmission delay = L/R = bits/bits/sec 


## Store and forward 

receive all the package , check for errors, and proceed
latency due to checking, however integrity !
used in critical application 

## Checksum 

a common error-checking technique

checksum is often used to check for errors in data packets. It ensures that the data is correct before being forwarded.

## Packet queuing and loss

arrival rate to link exceeds the transmission rate of link for a period of time     
- packet will be queued
- packets can be dropped if memory in router fills up 

## Two key network-core function 

Forwarding and Routing 
local action, global action 

## TDM vs FDM

TDM for digital , FDM for Radio 
Interference diff.
TDM inefficient with idle time 

## Circuit vs packet switching 

dedicated communciation path, like telephone , guranteed bandwith and quality , inefficient use of resource , not scalable 

breaks down in chunks called pakcets , each may take different route,flexible, scalable requires error checking and reassembly at the derstination 

Analogy : Restaruarant vs Mcdonals

## ISP - internet 

## Content provider network 

## traceroute

provides delay measurement from source to router along end-end internet path destination. 

## DDoS

Distributed Denial of Service 

Bogus traffic, attackers send request from compromised hosts to target.

## Packet Sniffing

reading the packets passing by the links 

Wireshark 

## IP Spoofing

send pakcets with false source address 

## Internet protocol stack - Layers

- Application 
    Network applications IMAP,HTTP,SMTP
- Transport 
    Process to Process data transfer 
- Network
    Routing of datagrams from source to destination 
- Link
    data transfer between neighboring network elements
- Physical 
    bits on the wire 

Summary: What Happens at Each Step?

DataUnit	        Layer	            Example (Sending an Email)

Message	            Application Layer	Full email in Gmail
Segment	            Transport Layer	    Chunks of email data with TCP headers (sequence number)
Datagram/Packet	    Network Layer	    Email data with sender/receiver IP addresses (encapsulation)
Frame	            Data Link Layer	    Packet with MAC addresses for routing
Bits	            Physical Layer	    Electrical or wireless signals

## CIA Triad

Confidentiality - no trespasess reading , (reading), Securing from Packet sniffing, by encrytion.
Integrity - No tampering on the packages, (writing) ,Securing from IP spoofing, By VPN.
Availability - Timely manner ,(Denying) Securing from DDoS, By CDN.

## TCP vs UDP

Reliable,checksum,slower due to ack, retransmission of lost packets
vs
faster,data loss tolerant , lightweight, realtime application, no retransmission 

Latency,elasticity,efficiency 


## Elasticity

Can Tolerate some data loss, UDP has elasticity


![alt text][Comparison Table]


[Comparison Table]: https://file%2B.vscode-resource.vscode-cdn.net/var/folders/k2/4ym6nvq14tl_bnrkhhxz2gk40000gn/T/TemporaryItems/NSIRD_screencaptureui_RYOPrr/Screenshot%202025-03-02%20at%201.24.23%E2%80%AFPM.png?version%3D1740943470468


## HTTP Request Type 

Belongs to the application layer.

Persistent - One Connection = Multiple Requests
TCP is connection , whereas HTTP is Requests

Non Persistent - One Request = One Connection

🚀 Quick Comparison: Persistent vs. Non-Persistent
Feature     	Non-Persistent	                         Persistent
Connection	    New TCP connection for each request 	 One TCP connection for multiple requests
Speed	        Slower (high latency)	                 Faster (low latency)
Overhead	    High (many connections)	                 Low (fewer connections)
Usage	        Older HTTP (1.0), simple websites	     Modern HTTP (1.1, 2), dynamic websites


## Pieplining

Optimisation technique for persistent

multiple HTTP requests to be sent over the same TCP connection without waiting for the corresponding responses 

Disadv: 
Head of line blocking -> where a delay in processing an earlier request can delay all subsequent responses, even if those requests are ready

Chapter - 2

## Flow Control 

Flow control in TCP is a mechanism that prevents the sender from overwhelming the receiver with too much data at once.

How ? Sliding window protocol