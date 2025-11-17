# HTML and CSS in Depth

Course: https://www.coursera.org/learn/html-and-css-in-depth/lecture/6j2oH/introduction-to-the-program

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











