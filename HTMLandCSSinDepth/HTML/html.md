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














