# Introduction to Front-End Developement

## Module 1 - Get Started With Web Developement

### Front-end vs. back-end vs. full-stack developer

- Front-end developers: build the user-facing parts of a website that users see and interact with, focusing on design, layout, and responsiveness using languages like HTML, CSS, and JavaScript.

- Back-end developers build and maintain the server-side "behind the scenes" infrastructure, which includes databases, servers, and application logic, using languages like Python, Java, or Node.js to ensure everything functions correctly and securely. 

- Full-stack developers are confident in both areas. 

### How the internet works

**Network switch**: it connects multiple devices and allows them to communicate with each other. 
The network switch can connect to other network switches, and now two networks can connect. These network switches then connect to more network switches until you have something called interconnected network (internet). 

**Computers connect to each other to form networks and these networks connect to each other to form the Internet.**

### What is a webserver and how does it work

A server is computer that runs applications and services, ranging from websites to instant messaging. <br>
Servers are stored in data centers all over the world. 
Webserver is a specific type of server. 

Webserver has many functions, like:
    - perform email management
    - can handle thousands of requests from clients per second
    - can function as website storage and administration
    - can handle security

### Webpage vs. website, web browser

- **Webpage** is a coded document that is rendered by the browser and displays images, textx, videos and other content in the web browser
- **Website** is a collection of webpaes that link together

You type your favorite browser, a copy of the webpage is sent from the web server to your browser, each line of code is processed in a sequential order from first to last.
As each line is interpreted, the browser creates the building blocks, which is the visual representation you see on the screen. 
This creation process is known as **page rendering**. (The web page is rendered by the web browser to display what the user sees on the screen) 
The response from the web server must be a complete web page in order to fulfill the request.

- **web browser**: is a software application that you use to browse the World Wide Web. It works by sending a request to a web server and then recieves a response containing the content that is to be displayed on the screen of your device. You put the address of the website that you want to visit in the address bar. 

- **URL**: Uniform Resource Locator . The URL contains the: 
    - **Protocol** (http)
    - **domain name** (name of the website - www.wikipedia.com)
    - **file path** (/index.html)

- When you make a request using the URL, the web browser sends a request across a network and connects to another computer on the internet, called a web server. 
The web server is a special type of computer that allows other computers to make requests for data. 
So the browser and web server communicate using a protocol, the HTTP HyperText Transfer Protocol. 
The web server responds by sending a webpage back to the browser
Once the web browser recieves the content, it displays it on the screen of your device. <br>
    --> **request - response cycle** 


### Web hosting

- Websites and files are stored on web servers located in data centers. But what if you want to create your own website?
- **Web hosting**: is a service where you place your website and files on the hosting companies web server. You are renting the space for stable and secure storage 

Types of web hosting: 
    - **shared hosting**: cheapest, you pay for a location on a web server containing many web hosting accounts with shared hosting, this means that you also share the service processing power, memory and bandwith with other websites that might slow your performance.  This option is best for small website with small number of visitors. 
    - **virtual private hosting (VPS)**: is a virtual server with dedicated CPU, memory and bandwith resources. It will be running on a hardware server with other VPS instances but as the resources are fixed per VPS instance, your website is unlikely to be impacted by the performance of other VPS instances. 
    - **dedicated hosting**: is a hardware server that is dedicated to you only. All hardware, CPU, memory and bandwidth resources are yours. More expensive. 
    - **Cloud hosting**: started to be popular in the last decade. With Cloud hosting your website is running in Cloud environment, which spans across multiple physical and virtual servers. If one of the server fails, your website will run on a different server and stay online. Main advantage is that you can use as many resources as you need without hardware limitations, and you pay based on resource use. 

### Internet Protocol - IP
- Data sent across the Internet through Internet Protocol addresses (IP addresses). 
- When you send data between computers across the Internet, the computers are the destinations that request and recieve the data, and the networks are the routs that the data travels across. 
What makes that possible is the Internet Protocol (IP Version 4 and 6 ). <br>
Every computer on a network is assigned an IP address. (IP version 4 the IP address contains 4 octets separated by dots, e.c. 192.0.2.235)

- When you send data across a network, you send the data as a series of messages called IP packets or datagrams. 
- **IP packets** contain a **header** and a **payload**, which is the data. (**IP Header and IP Data**). 
    - **IP Header**: include the **destination** IP address and **source** IP address
    - **IP Data**: payload of the packet 

- The delivery can go wrong,  IP Packets: 
    - can arrive out of order
    - become damaged or corrupted during transit 
    - can be lost 
To solve these problems, the payload contains other protocols, too. 
    - Transmission Control Protocol (TCP) - can solve all three above mentioned issues (out of order, damaged, lost), but delivery is delayed a bit 
    - User Datagram Protocol (UDP) - can solve the corrupt packet issue, but packets still can arrive out of order or not arrive at all 

The payload part of IP packets supports multiple protocols to make sure that information arrives as expected. Two of these are Transmission Control Protocol (TCP) and User Datagram Protocol (UDP). TCP is used to send data that must arrive correctly and in order.

### HTTP 
- HTTP is a core operational protocol of the world wide web. It is what enables your web browser to communicate with the web server that hosts a website.
HTTP works to transfer web resources such as HTML files, and is the foundation of any data exchanges on the web
-**HTTP: HyperText Transfer Protocol**. It is a protocol used for transferring web resources such as HTML documents, images, files and other files.
- **HTTP is a request-response based protocol.**
- A web browser (client) sends an HTTP request to a server and the web server sends the HTTP response back to the browser

- **HTTP Request** consists of:
    - method (GET / POST / PUT / DELETE ) 
        - GET: retrieve information from the server
        - POST: send data to the server 
        - PUT: update 
        - DELETE: removes the resource
    - path (/): is the representation of where the resource is stored on the web server 
    - version (1.1 and 2.0 is most used)
    - headers: additional information about the client making the request 
     

**HTTP Response**: similar format than the request, but it will optionally contain the body, which is the message body, such as the HTML document, the image file, etc.. + the HTTP Status Code. 

- HTTP Status Codes: range is from 100 to 599 
    - There are 5 groups of status codes: they are grouped by the first digit of the error number 
        - Informational: 100-199
            - 100: Continue, the web client should continue to request or ignore the response if the request is already finished 
        - Successful: 200-299
            - 200 OK, successful response from the web server
        - Redirection: 300-399
            - Redirection responses indicate to the web client that the requested resource has been moved to a different path 
            - 301: Moved permanently 
            - 302: Found
        - Client Error: 400-499
            - indicates that the requests contained bad synthax or content and cannot be processed by the web server. 
            - 400: client submitted bad sata to the web server 
            - 401: user must log into an account before the request can be processed 
            - 403: the request was valid but the web server is refusing to process it (indicates that the user has not sufficient permission to execute an action in a web application)
            - 404: the request resource was not found on the web server
        - Server Error: 500-599
            - indicates that the failure occured on the web server while trying to process the request 
            - 500: internal server error 
            - 502: Bad Gateway
            - 503: Service Unavailable

- **HTTPS** : Secure HTTP - lock icon besides the URL, it uses encryption. It works in the same way as HTTP, the requests and responses have the same content. But before the content is sent, it is encrypted. Only the other computer can turn the secret code back into its original content. 

#### HTTP Request Examples:
- Every HTTP request begins with the **HTTP Request line**.
- This consists of the **HTTP method**, **the requested resource** and the **HTTP protocol version**. 
```
GET /home.html HTTP/1.1 
```
**HTTP Request Headers**: After the request line, the HTTP headers are followed by a line break.
A header is a case-insensitive name followed by a: and then followed by a value.
Common headers are:
```
Host: example.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0
Accept: */*
Accept-Language: en
Content-type: text/json
```

**HTTP Request Body**: 
HTTP requests can optionally include a request body. A request body is often included when using the HTTP POST and PUT methods to transmit data.
```
POST /users HTTP/1.1
Host: example.com

{
 "key1":"value1",
 "key2":"value2",
 "array1":["value3","value4"]
}
```

#### HTTP Response examples: 
When the web server is finished processing the HTTP request, it will send back an HTTP response.<br>
The first line of the response is the status line. This line shows the client if the request was successful or if an error occurred.<br>
```
HTTP/1.1 200 OK 
```
The line begins with the HTTP protocol version, followed by the status code and a reason phrase. The reason phrase is a textual representation of the status code.

**HTTP Response Headers**: 
Following the status line, there are optional HTTP response headers followed by a line break.<br>
Similar to the request headers, there are many possible HTTP headers that can be included in the HTTP response.

**HTTP Response Body**:
Following the HTTP response headers is the HTTP response body. This is the main content of the HTTP response.

This can contain images, video, HTML documents and other media types.
```
HTTP/1.1 200 OK                         / --> Status Line 
Date: Fri, 11 Feb 2022 15:00:00 GMT+2   / --> Response Header 
Server: Apache/2.2.14 (Linux)
Content-Length: 84
Content-Type: text/html

<html>                                  / --> Response Body
  <head><title>Test</title></head>
  <body>Test HTML page.</body>
</html>
```


### Other Internet Protocols:
Hypertext Transfer Protocols (HTTP) are used on top of Transmission Control Protocol (TCP) to transfer webpages and other content from websites.

**Domain Name System Protocol (DNS)**
Your computer needs a way to know with which IP address to communicate when you visit a website in your web browser, for example, meta.com. The Domain Name System Protocol, commonly known as DNS, provides this function. Your computer then checks with the DNS server associated with the domain name and then returns the correct IP address.

**File Transfer Protocol (FTP)**
When running your websites and web applications on the Internet, you'll need a way to transfer the files from your local computer to the server they'll run on. The standard protocol used for this is the File Transfer Protocol or FTP. FTP allows you to list, send, receive and delete files on a server. Your server must run an FTP Server and you will need an FTP Client on your local machine. You'll learn more about these in a later course.

**Secure Shell Protocol (SSH)**
When you start working with servers, you'll also need a way to log in and interact with the computer remotely. The most common method of doing this is using the Secure Shell Protocol, commonly referred to as SSH. Using an SSH client allows you to connect to an SSH server running on a server to perform commands on the remote computer.
All data sent over SSH is encrypted. This means that third parties cannot understand the data transmitted. Only the sending and receiving computers can understand the data.

**Secure File Transfer Protocol (SFTP)**
The data is transmitted insecurely when using the File Transfer Protocol. This means that third parties may understand the data that you are sending. This is not right if you transmit company files such as software and databases. To solve this, the SSH File Transfer Protocol, alternatively called the Secure File Transfer Protocol, can be used to transfer files over the SSH protocol. This ensures that the data is transmitted securely. Most FTP clients also support the SFTP protocol.


### Webpage, website, web application
- **Webpage**: is one single page that consists of HTML, CSS and JS. It displays images, text, videos and other content in the web browser.  

- **Website**: is a collection of web pages that linked together under one domain name. 

- **Web application**: more interactive than a website (vs. website is informative, and displayes the same content for everyone, it's not personalized). Example: online food ordering application, social media platform --> you have to sign in, and the content displayed is personalized based on your user account and location. Dynamically updated content. 

### Developer Tools
- To open developer tools: Command + option + J OR Right click --> Inspect 

- Elements: shows the HTML structure of the web page and the CSS properties
- Console: this tab outputs JS logs and errors from the web application 
- Sources tab shows all content resolved for the current page
- Network: you can inspect the timeline and details of HTTP requests and responses of the webpage
- Performance: shows what the web browser is doing over time
- Memory: displays the parts of your code that are consuming the most resources

### Frameworks and Libraries: 
- these are open-source or proprietary 

**Libraries**: 
    -are reusable pieces of code that can be used by your application. <br>
    - they provide a specific functionality. For exmample: email validation libraries when you build an e commerce application or web shop. No need to build your own validation process, there are libraries available. <br>
    - it saves time for you as a developer.

**Frameworks**: 
    - provide a structure to build with, and where the developers add their own code that the framework interacts with
    - Express, Django, ASP.NET, Rails, Spring
    - For example: by the e commerce application a framework would handle recieving HTTP requests. The developer would implement code that processes the request and returns a response from which the framework would send a response over HTTP. 

Most frameworks use many libraries.

### APIs and services: 

**API (Application Programming Interface)**: is a set of functions and procedures for creating applications that access the features or data of an operating system, application or other service.
Browser API, REST API, Sensor-Based API

APIs are the bridge between different components or systems (gateway or middleware)
**Examples**: 
1. **Browser or Web API**: it is built into the browser itself. They extend the funcionality of the browser by adding new services and are designed to simplify complex funcions and provide easy syntax for building advanced features. 
DOM API: turns the html ducument into tree of nodes that are represented as JS objects 
2. **REST API**: it is a web server that provides data for web and mobile applications.
REST (Representational State Transfer) is a set of principles that help build highly efficient APIs. One of the main responsibilities of REST API is sending and recieving data to and from a centralized database. 
These APIs use endpoints to specify how different resources can be accessed 
The endpoint is built into the URL when accessing the API. Once the endpoint is hit, the API performs whatever service side processing is needed to build the response. 
3. **Sensor-Based API**: these are actual physical senses that are interconnected with each other. The sensors can communicate through API and track and respond to physical data. For example, smart lights, node bots

### IDE: Integrated Developement Environment 
- IDE is a software for building applications 
Benefits: 
- syntax highlighting help to read the language keywords, it warns for errors
- autocomplete of syntaxes 
