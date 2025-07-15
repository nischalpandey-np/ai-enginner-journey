
---

## 🌐 Week 1 (Part 3): Network Communication Protocols & The World Wide Web

### 📌 Topics Covered:

* TCP (Transmission Control Protocol)
* UDP (User Datagram Protocol)
* HTTP (HyperText Transfer Protocol)
* The World Wide Web (WWW)

---

### 📦 1. TCP (Transmission Control Protocol)

TCP is a **connection-oriented** protocol. It ensures **reliable, ordered, and error-checked** delivery of data between devices.

#### 🔑 Key Features:

* Data is broken into **packets** and reassembled in the correct order.
* Retransmits lost packets.
* Slower but **reliable**.

#### 📦 Use Cases:

* Browsing websites (HTTP/HTTPS)
* Emails (SMTP)
* File transfers (FTP)

#### 🔄 Example:

Sending a message over TCP is like sending multiple pages of a document with a tracker — if any page goes missing, it is resent until the whole file is complete.

---

### 🚀 2. UDP (User Datagram Protocol)

UDP is a **connectionless** protocol. It sends data without checking if it was received.

#### 🔑 Key Features:

* No error-checking or reordering.
* Much **faster** than TCP.
* Suitable for real-time communication.

#### 📦 Use Cases:

* Online gaming
* Live video/audio streaming
* VoIP (Voice over IP)

#### 🔄 Example:

Sending data via UDP is like shouting in a room — you don't know if everyone heard it, but it’s quick.

---

### 🌐 3. HTTP (HyperText Transfer Protocol)

HTTP is the protocol used by web browsers to request and transfer web pages.

#### 🔑 Key Features:

* **Stateless**: Each request is independent (unless cookies or sessions are used).
* Works on **TCP** (port 80).
* Most modern websites use **HTTPS** (secure version using encryption).

#### 📦 Basic Flow:

1. You type `www.example.com`.
2. Browser sends an HTTP request to the server.
3. Server responds with an HTML page.
4. Browser renders the page for you.

---

### 🌍 4. The World Wide Web (WWW)

* The WWW is a **system of interlinked web pages** and content accessible via the Internet.
* Invented by **Tim Berners-Lee** in 1989.
* It uses **HTTP/HTTPS** to retrieve documents hosted on **web servers**.

#### 🌐 Components of WWW:

* **Web Browsers**: Tools to access web content (Chrome, Firefox, etc.)
* **Web Servers**: Computers that store and serve web pages.
* **URLs (Uniform Resource Locators)**: The addresses of resources on the web.

#### ⚙️ Summary:

* **Internet** = the infrastructure (like roads)
* **WWW** = the content (like websites, videos, etc.) riding on the infrastructure

---

### ✅ Summary Table

| Protocol/Concept | Description                                     | Use Cases                    |
| ---------------- | ----------------------------------------------- | ---------------------------- |
| TCP              | Reliable, ordered communication                 | Web browsing, file downloads |
| UDP              | Fast, unreliable communication                  | Gaming, live streaming       |
| HTTP             | Protocol for transferring web pages             | Websites, APIs               |
| WWW              | Collection of web pages and content on Internet | Everything on the web        |

---

