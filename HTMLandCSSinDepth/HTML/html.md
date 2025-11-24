# HTML and CSS in Depth

Course: https://www.coursera.org/learn/html-and-css-in-depth/lecture/6j2oH/introduction-to-the-program

Additional resources: 

```<Input>``` html tag:
https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input

Form validation examples: 
https://www.the-art-of-web.com/html/html5-form-validation/

Client-side validation:
https://www.sitepoint.com/client-side-form-validation-html5/

Input type: Radio buttons:
https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio

HTML Form Submission - seding form data:
https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Sending_and_retrieving_form_data

## Module1: HTML in Depth (1-60)

**After completing this module you should be able to:**

- Use common semantic and meta tags to improve the accessibility, readability and SEO of a web page.
- Create commonly-used web page layouts and components.   
- Create and test a form with client-side validation.   
- Recognize server-side connections and the languages used to carry out requests and responses.  
- Post form data to a server. 
- Create a video and audio player that can rate the media played.
<br><br>

Few keywords HTML and CSS:
- HTML and CSS documentation: managed by W3C
- HTML is a markup language used to create webpages. 
- CSS is a stylesheet language used to describe the look and layouts of a document written in HTML. 
- You can change a web page's appearance with CSS without editing its HTML.   
- Reusability
- Maintainability
- Separating HTML and CSS makes a website much easier to manage and update
- CSS allows for efficient, centralized styling. You define a style once, and it applies to all the relevant elements, saving a huge amount of time and effort

### HTML 
- HTML stands for **HyperTest Markup Language**
- HyperTest is text which contains links to other text
- Markup refers to tags and elements used within a document 

- HTML elements with their opening and closing tags in angle brackets make up an HTML document
- HTML is the structure of the webpage, you can display images, data as tables, or forms
- HTML can assist in ensuring web accessability to people with disabilities to understand websites

- **DOM: Document Object Model**
Users need to be able to interact with elements on a web page. This means that HTML ducument must be represented in a way that JS code can query and update it. And that's the function of the DOM. It's a model of the objects in the HTML file. Web developer interact with the DOM through JS to update content, set up events, and animate HTML elements. 

### CSS - Cascading Style Sheet 
- CSS tells the web browser how to display HTML elements on screen
- you use CSS to
        - style elements within an HTML document
        - create a layout for web pgae using the box model
        - arrange page elements using normal document flow


### Semantic tags and why we need them 
Semantic tags describe the meaning of a web page and they help search engines and accessibility software like screen readers to understand the contents of a page.

- headings (h1-h6): 
- ol and ul (ordered and unordered list)

- Basic HTML page structure
```
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <header>
            <nav>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </header>
        <main>
            <article>
                <h2>My summer holiday</h2>
                <p>This summer I visited my grandparents.</p>
            </article>
        </main>
        <footer></footer>
    </body>
</html>
```
- For a typical HTML page, the structure can be semantically described using the 'header', 'main', and 'footer'
    - **header**: contains the company logo and navigation links.<br>
        The ```<nav>``` element usually in the ```<header>``` element. <br>
        Main navigation is ordered in unordered list ```<ul>```

    - **main**: articles and sections, it contains the main content of a web page 
        - ```<article>``` element indicates content which represents a complete or self-contained composition in a document page or application, that is independently distributable. (forum post, newspaper article, blog post, user comment, interactive widget). <br>
        ```<article>``` element contains a heading and paragraph (h2, p)
        
        - ```<section>``` element is semantically define individual sections of the article. It is important to note that sections should contain heading elements to semantically describe sections. The section element doesn't require the article element.


    - **footer**: contact information, social media links
        - this might contain additional navigation links or other content 

Semantic tags cheat sheet: check 'semanticHtmlElements_cheatsheet.md' file 

### Metadata 
- you will learn how search engines analyze web pages and how meta tags help provide information for search engines
- A major part of launching a website called SEO: Search Engine Optimization 
- This process involves making improvements to a website's content, semantics and delivery to improve its ranking in search results. 
- When a search engine visits your website, it analyzes the html document and media content. If it finds a link to another html document, it follows the link to that document, and continues following links until it is finished analyzing the entire website. Based on the results of the analysis and the content on your website, the search engine will rank the website for various search terms. There are many best practices you can follow to influence how search engines analyze and rank your website.

- Meta tags define metadata about a web page (Metadata is data about the web page)
- Meta tags are added inside the ```<head>``` element of the html document, and nothing inside the head element is displayed in the web browser
- Meta element has 2 attributes: name and content 
```
<meta name="name of the metadata" content="value of the metadata">

<meta name="author" content="Anett Keszler">
<meta name="description" content="Anett's first web page">
<meta name="keywords" content="holidays, free, summer, vacation">       / previously used to provide search keywords for search engines, but this led to a manipulation of search engines
```
- It is recommended not to include 'keywords' metadata in your webpage, it's overused. 
```
<meta name="robots" content="index, follow">                            / it tells search engines if and how they should analyze your web page
```
    - index: tells the bot to analyze the page 
    - follow: tells the bot to also visit all links on the web page
    - noindex: tells the bot not to analyze the page
    - nofollow: tells the bot not to also visit all links on the web page

    - but some bots will ignore this value, so it's best not to rely on that

```
<meta name="viewport" content="width=device-width, initial scale=1.0">  / it's important when designing responsive web pages
```
    - viewport data to help web browsers display websites at the appropriate scale on the device being used.     
    - viewport metadat is important for user experience and for SEO, because many search engines include websites mobile experience as a part of there ranking algorithms


### Bare bones layout

In VSC, we have the follofing folder structure:
    - index.html file
    - js folder --> script.js file
    - css folder --> styles.css

Index.html: You need to add the CSS file to the css folder, the JavaScript file to the jsfolder, a link element to reference the CSS file and a script element to reference the JS file.

#### Layout design 
- Top navbar layout
- Carousel layout: Product-focused websites often use a large carousel on their homepage to highlight their featured products, discounts and offers.
- Blog layout: The blog layout is used to feature multiple content items of differing importance. It is often seen on news websites where new articles will appear on the page each day based on current events.
- Dashboard layout: Dashboard layouts are often used in enterprise software for managing various web applications. They typically feature a sidebar for navigation with the main content area containing forms for configuration or reporting data such as graphs and tables. 

### UX with meta tags
- meta tags help web pages create previews of other web pages
- Traditional SEO meta tags are oriented towards search results, not direct links
- Open Graph Protocol (OGP, estabilished by Facebook in 2010):
    - to improve the user experience, they found a way to display information about a website before a user clicks on the link 
    - OGP is a set of metadata rules for describing websites
    - Open Graph Protocol is a set of metadata rules that allows web pages to describe themselves to social networks. 
    - **Social media platforms use these meta tags to create a preview of the shared web page.**  
    - The aim is to improve user expreience
    - the OGP must always include these four properties on a webpage:
    ```
    <meta property="og:title" content="My first web page">              / this is the text that will appear in the preview
    <meta property="og:type" content="website">                         / website, video, music, article...
    <meta property="og:url" content="https://example.com">
    <meta property="og:image" content="https://example.com/me.jpg">

    <meta property="og:description" content="...">
    <meta property="og:locale" content="en_US">
    <meta property="og:site_name" content="Little Lemon">
    ```

- Effective social media cards help to inform Internet users about your website and drive traffic towards it. The extra time a developer spends adding social media tags is worth the effort! 

### Forms and form validation
- **Form validation is a process that ensures the data entered by the user in a form is valid and conforms to rules defined by the developer** 
    - **Client-side validation**: checks errors as soon as they are typed into the form, checks if a form has been filled out correctly. If error, an error message will alert the user of the invalid data <br>
     Client-side validation checks for errors as soon as they are typed into the form. The web browser does this by validating the submitted data against the specified input type. The web browser will show an error message if the wrong type of input has been submitted.
    - **Server-side validation**: checkes for error after the data has been submitted to the web server. It is more secure, because it prevents malicious users from tampering with your website's code and submitting invalid data to your server. When the form data is recieved by the web server, the backend will validate the data before processing it. 
        - checking the data against database 
        - validating data against business requirements

- Most websites use both, client- and server-side validation to provide immediate feedback to users, but also to protect against malicious data submission to ensure data integrity 

### Input types

Check inputTypes_cheatsheet.md file

### Creating a form 

Check signup.html file 

### Client-side validation
- as a developer you can use HTML and CSS to guide the users to enter the correct data on forms
```
<label for="firstName">First name:</label><br>
<input type="text" id="firstName" name="firstName" required minlength="3" maxlength="12">
```

- required
- minlength
- maxlength
- min and max attributes: Determine the minimum and maximum values allowed for an input field. They are usually applied to numerical text inputs, range inputs or dates. 
- multiple: Indicates that the user can enter more than one value in a single input field. This attribute can only be used for email and file input types
- pattern: Defines a particular pattern that an input field value has to fulfill to be considered valid. This attribute expects a regular expression to specify the pattern. It works with text, date, search, URL, tel, email and password input types. For example, you can restrict phone numbers to be only from the UK
```
<input type="tel" id="phone" name="phone" pattern=”^(?:0|\+?44)(?:\d\s?){9,10}$” > 
```

- a built-in function of the browser will generate warning message displayed on the screen, that the input you typed is invalid
- a much better user experience and a management of web server resources, if we apply client-side validation 

### Radio button 

- ideal for example to an online table booking form in a restaurant
- it allows us to setup groups of limited options, and only one option by groups can be selected

- for the example, check booking.html file


### Form submission

- what happens when you click on the order button 
- the web browser communicates with the web server using a HTTP request-response cycle
- the web browser send requests to the web server and the web server sends back a response  
- there are two ways a form can send data to the web server: **HTTP get method** or **HTTP post method** 

```
<form method="get"></form>
<form method="post"></form>
```

- **1. Using 'GET' method to send data to the server**: <br>
when the 'Login' button is clicked, the form data is sent as part of the request URL. <br>
This means that the user data is appended to the end of the URL in the web browser navigation bar. The web server recieves the HTTP GET request, and extracts the form data from the URL. <br>
While this is an easy way to submit data, it has 3 key problems: 
    - length of the URL is limited to 2000 characters (if you have a large form, some data may be lost)
    - length of the URL is limited on the server side 
    - security: personal information is sent through URL, anyone can see it when opening browse history

- **2. Using 'POST' method to send data to the server: <br>**
- The form data is inserted into the content of the HTTP request.
When the submit button is pressed, it will send an HTTP post request with the data contained in the body of the request
It is more secure, but still it can be read by a third party listening to the HTTP request.

To secure the request completely, HTTPS is used to encrypt the data, so that only the sender and reciever can understand the data.
Once the web server recieves the request, it processes it and sends back an HTTP response 

#### Address location 
```
<form action="/login"> 
</form> 
```
The action attribute specifies to which web address the form must be sent. This is address is location of server-side code that will process the request.
It is important to note that action can be a full URL address such as https://meta.com, an absolute path such as /login, or a relative path such as login. 

The absolute path, which starts with a forward slash, will use the base address of the current website, such as https://meta.com and combine it with the absolute path. For example, if /login is the absolute path, the form will be submitted to https://meta.com/login. If the address is https://meta.com/company-info/ and /login is the absolute path, the submission address will still be https://meta.com/login.

Similarly, a relative path will combine the current web address with a relative path. For example, if the web browser is currently on the web page https://meta.com/company-info/, and the relative path is set to login, the form will be submitted to https://meta.com/company-info/login. 

```
<form method="get"> 
</form> 

<form method="post"> 
</form> 

```
The form will default to the HTTP GET method when the method attribute is not provided. 

As you may already know, when the form is submitted using the HTTP GET method, the data in the form's fields are encoded in the URL. And when the form is submitted using the HTTP POST method, the data is sent as part of the HTTP request body. 

When the web server receives the request, it processes the data and sends back an HTTP response. The response indicates the result of the submission, which can be successful or fail due to invalid or incorrect data. 


### Video and Audio
```
<video width="320" height=""240" controls muted>
    <source src="dance.mp4" type="video/mp4">
    <source src=dance.ogg type="video/ogg">
</video>
```

```
<audio loop controls>
    <source src="music.ogg" type="audio/ogg">
    <source src="music.mp3" type="audio/mpeg">
</audio>
```

- HTML ```<video>``` and ```<audio>``` tags are used to embedding media on a webpage 
- both tags support different file types that can be played in the web browser 
    - video: .mp4, .webm, .ogg
    - audio: .mp3, .wav, .ogg

- the file types are supported by most web browsers. In case the file type is not supported, the video tag allows for multiple sources to be specified. The browser will search through the sources and use the first one that is supported. 
 
- ```controls``` attribute: it enables player controls, such as a pause and volume button 
- ```loop``` attribute: automatically starts playing the music when its ended
- ```muted``` attribute: when the user opens the browser, the video is muted by default. 


### Images

```
<img src="photo.png">
<img src="photo.png" width="640" height="480"> 
```

- ```<img>``` element used to add images to the web page
- ```src``` attribute specifies the source/address of the image
- ```width``` and ```height``` attributes: specify the size of the image. You can set the image to a larger or smaller size and the web browser will automatically scale the image. One useful feature of rendering images in the web browser is that the web browser can automatically keep the correct ratio of width to height.

But what happens if the photo doesn’t load? Perhaps the file was accidentally deleted, or you mistyped the file name. Luckily, the web browser has a way to display some text when the image fails to load. This is done using the alt attribute.

```
<img src="photo.png" width="320" alt="My Profile Photo"> 
```

It is important to ensure that screen reader accessibility software can interpret images displayed in the web browser. To support this, the ```<img>``` tag is combined with the ```<figure>``` and ```<figcaption>``` tags to provide a description of the image.

```
<figure> 
   <img src="photo.png" width="320" alt="My Profile Photo"> 
   <figcaption>A photo of myself on a beach in 2015</figcaption> 
</figure>
```
- supported file types for images: 
    - .APNG – Animated Portable Network Graphics 
    - .AVIF – AV1 Image Format 
    - .GIF – Graphics Interchange Format 
    - .JPEG / .JPG – Joint Photographic Expert Group image format 
    - .PNG – Portable Network Graphics 
    - .SVG – Scalable Vector Graphics 
    - .WEBP – Web Picture Format

### iFrame
- iFrame is a HTML element that allows you to embedd content from another website into a webpage 
```
<iframe src="" width="" height=""></iframe>
```

- iframe is often used to display adverts, embed content from another website (social media post, map)
- ```src``` attribute: contains the content that is embedded, value of the attribute is the URL of the content 

- it is not secure, you can inject malicious code 
- ```allow``` attribute: limitst which browser features the iframe can access 
- ```sandbox``` attribute: limits the behaviour within the iframe (preventing files from being downloaded, preventing pop-up windows). When sandbox attribute is used with an empty value, all sandbox restrictions will apply to the iframe.

```
<iframe src="https://www.example.com" allow="camera 'none'; microphone 'none';" sandbox=""></iframe>
```
    - allow: it disables camera and microphone
    - sandbox="": all sandbox restrictions will apply to the iframe
    - sandbox="allow-downloads"

- ```allow``` attribute: It specifies what features or permissions are available to the frame
    - allow="fullscreen” the fullscreen mode can be activated 
    - allow=“geolocation” lets you access the user’s location 
    - ```<iframe src="https://example.com/…" allow="camera; microphone"> </iframe>```

- ```referrerpolicy``` attribute: A referrer is the HTTP header that lets the page know who is loading it. This attribute indicates which referrer information to send when loading the frame resource.
    - ```no-referrer```:  The referrer header will not be sent. 
    - ```origin```: The referrer will be limited to the origin of the referring page 
    - ```strict-origin```: The origin of the document is sent as the referrer only when using the same protocol security level (HTTPS to HTTPS) 


- ```sandbox``` attribute: To enforce greater security, a sandbox applies extra restrictions to the content in the iframe. To lift particular restrictions, an attribute value (permission token) is used
    - ```allow-downloads```: Allows the user to download an item 
    - ```allow-forms```: Allows the user to submit forms 
    - ```allow-modals```: The resource can open modal windows 
    - ```allow-orientation-lock```: Lets the resource lock the screen orientation 
    - ```allow-popups```: Allows popups to open 
    - ```allow-presentation```: Allows a presentation session to start 
    - ```allow-scripts```: Lets the resource run scripts without creating popup windows 