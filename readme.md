# Part One: Solidify Terminology

1. What is HTTP?
> HyperText Tranfer Protocol. A set of rules designed to transfer information beteween networked devices.

2. What is a URL?
> Uniform Resource Locator. A unique identifier used to locate resources on the internet.

3. What is DNS?
> Domain Name System. Translates domain names such as google.com into ip addresses.

4. What is a query string?
> A part of the url that assigns values to parameters to be passed into web app or back-end database.

5. What are two HTTP verbs and how are they different?
> GET is used to request data and POST is used to send data.

6. What is an HTTP request?
> A ping to ask for access to a resource.

7. What is an HTTP response?
> Data sent in response to a request.

8. What is an HTTP header?
> Additional information or parameters given about the request or response.

Example:
> `whatismyheader.com`
> GET / HTTP/1.1 Host: whatismyheader.com Connection: keep-alive Upgrade-Insecure-Requests: 1 
> User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 
> Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 
> Accept-Encoding: gzip, deflate Accept-Language: en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7 (requested from: 74.96.64.198:58804)

9.  What are the processes that happen when you type "http://somesite.com/some/page.html" into a browser?

> The base domain is translated by the DNS into an ip address.
> Then the browser makes a request to the ip address.
> The server sends a response.
> The browser constructs the website, with any further requests/responses made accordingly.

# Part Two: Practice Tools

1. Using curl, make a GET request to the icanhazdadjoke.com API to find all jokes involving the word "pirate".
> `curl -G "https://icanhazdadjoke.com/search?term=pirate"`

2. Use dig to find what the IP address is for icanhazdadjoke.com
> `dig icanhazdadjoke.com +short`
> You can also accomplish this with ping, traceroute.

3. Make a simple web page and serve it using python3 -m http.server
> [main.py file](https://github.com/Euntastic/web-works/part-two/main.py)

# Part Three: Explore Dev Tools

Build a very simple HTML form that uses the GET method (it can use the same page URL for the action) when the form is submitted.

Add a field or two to the form and, after submitting it, explore in Chrome Developer tools how you can view the request and response headers.

Edit the page to change the form type to POST, refresh in the browser and re-submit. Do you still see the field in the query string? Explore in Chrome how you can view the request and response headers, as well as the form data.

# Part Four: Explore the URL API

At times, it’s useful for your JavaScript to look at the URL of the browser window and change how the script works depending on parts of that (particularly the query string).

[Read about the URL API](https://developer.mozilla.org/en-US/docs/Web/API/URL)

Try some of the code examples in the Chrome Console so that you can get comfortable with the basic methods and properties for instances of the URL class.