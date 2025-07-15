
---

## 🌐 Week 1 (Part 2): Basics of Computer Networks

### 📌 Topics Covered:

* Basics of Computer Networks
* IP Addresses
* Internet Routing Protocols

---

### 🖧 1. Basics of Computer Networks

A **computer network** is a collection of interconnected computers that share resources and communicate with each other.

#### 🔗 Types of Networks:

* **LAN (Local Area Network)**: Small area, like a home or office.
* **WAN (Wide Area Network)**: Covers large geographical areas (e.g., the internet).
* **MAN (Metropolitan Area Network)**: Covers a city or large campus.

#### 📡 Components of a Network:

* **Router**: Directs data packets to the right destination.
* **Switch**: Connects devices in a LAN and transfers data based on MAC addresses.
* **Modem**: Converts digital signals into analog (and vice versa) for internet access.

---

### 🌍 2. IP Addresses

An **IP address** is like a digital home address — it identifies a device on a network.

#### IPv4 vs IPv6:

* **IPv4**: 32-bit address (e.g., `192.168.1.1`) → About 4.3 billion unique addresses.
* **IPv6**: 128-bit address (e.g., `2001:0db8:85a3::8a2e:0370:7334`) → Solves IPv4 exhaustion problem.

#### 🧠 Fun fact:

* Every time you visit a website, your computer sends a request to the **IP address** of that site, not its name (e.g., `google.com` → `142.250.195.78` behind the scenes).

---

### 🚦 3. Internet Routing Protocols

Think of routing protocols like **Google Maps** for the internet — they find the best path to deliver data.

#### 🛰️ What is Routing?

Routing is the process of selecting a path for data to travel from one computer to another.

#### 🧭 Key Protocols:

* **IP (Internet Protocol)**: Delivers packets across networks.
* **TCP (Transmission Control Protocol)**: Ensures data arrives completely and in order.
* **UDP (User Datagram Protocol)**: Faster, but doesn't guarantee delivery.
* **BGP (Border Gateway Protocol)**: Decides how data is routed across the internet backbone.

#### ✈️ Example:

You open `example.com`.
→ Your browser looks up the IP address via **DNS**.
→ Your router sends the data packet through a series of routers, using **BGP** to find the best route.
→ Data reaches the destination server, and the website is loaded.

---

### ✅ Summary

| Concept           | Key Point                                              |
| ----------------- | ------------------------------------------------------ |
| Network           | Devices connected to share data/resources              |
| IP Address        | Unique identifier for a device on a network            |
| IPv4 vs IPv6      | 32-bit vs 128-bit addressing system                    |
| Routing Protocols | Rules for directing traffic across networks            |
| TCP vs UDP        | Reliable vs faster, lightweight transmission           |
| BGP               | Protocol for routing between different networks (ISPs) |

---

