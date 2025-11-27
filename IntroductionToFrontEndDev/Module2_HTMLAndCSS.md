# Introduction to Front-End Developement

Source: https://www.coursera.org/learn/introduction-to-front-end-development/lecture/bvbzK/what-is-hyper-text-markup-language

## Module 2 - Introduction to HTML and CSS

### HTML basics:

- **HyperText Markup Language**:
    - **Hypertext**: is text which contains links to other text
    - **Markup** refers to tags and elements used within a document 
- .html suffix - file extension 
- HTML is a text file with a specific structure that consists of elements and tags 
- when you visit a website the first page that is returned to the browser is often called index.html
```
<p></p>         opening and closing tags
<img>           self-closing tag   
< left angle bracket, > right angle bracket, / forward slash 
```

- current version og HTML: HTML5
- HTML specification: rules and structures for elements and tags and it is mantained by **W3C** (World Wide Web Consortium)

#### HTML documents
- index.html file
- ```<!DOCTYPE html>``` : doctype declaration, it tells the browser that this is a html document 
- ```<html></html>``` element: html root element 
- inside the 'html' tag, I add **head** and **body**, the 2 main elements
```
<!DOCTYPE>
<html>
    <head>
        <title>Little Lemon</title>
    </head>
    <body>
        <h1>Our Menu</h1>
        <h2>Falafel</h2>
        <p>Chickpea, herbs and spices.</p>
        <h2>Pasta Salad</h2>
        <p>Lettuce, vegetables and mozzarella. </p>
    </body>
</html>
```
- **head**: contains meta tags, nothing inside the head element is displayed in the web browser
- **title**: you always add this to the head element, this is what displayed in the web browser tab.
- meta tags in the head elements can specify the description of the web page or keywords for search engines

#### HTML tags
- **Headings**: allow to display titles and subtitles
```
<h1></h1>
<h2></h2>...
<h6></h6>
```
- **Paragraph**:contains text content. Note that putting content on a new line is ignored by the web browser 
```
<p>
    This paragraph
    contains a lot of lines
    but they are ignored.
</p>
```

- **Line break**: 
```
<p>
   This paragraph<br>
   contains a lot of lines<br>
   and they are displayed.
</p>
```

- **Strong and bold**: same appearance, but strong indicates that text has importance. <br>
Only the ```<strong>``` tag provides semantic meaning (importance). The ```<b>``` tag simply bolds text visually, without semantic significance.
```
<strong>This is important and displayed bold</strong>
<b>This is displayed bold</b>
```
- **Emphasis and italics**: same visual effect, but 'em' tags stress the text 
```
<p>Wake up <em>now</em>!</p>
<p>The term <i>HTML</i> stands for HyperText Markup Language.</p>
```
- **Lists**: unordered and ordered lists
```
<ul>
    <li></li>
    <li></li>
</ul>
-----------------
<ol>
    <li></li>
    <li></li>
</ol>
```
- **Div**: tag defines a content division in a HTML document. It acts as a generic container and has no effect on the content unless it is styled by CSS
```
<div>
   <p>This is a paragraph inside a div</p>
</div>
```
- Comments: 
```
<!-- This is a comment and not displayed on the web page --> 
```
#### Linking documents
- **Websites** consist of **multiple webpages** linked together. 
- To link pages together you use the anchor tag. 
- Anchor tags create hyperlinks 

#### Images 
```
<img src="img/falafel.jpeg" width="240" height="135" alt="Falafel">
```
-**```alt```** attribute: alternative text, it is not displayed on the site. <br> Adding alt descriptions is not required to add an image on your website but it is certainly best practice. This is helpful when the image becomes unavailable, for instance, if the image file is accidentally deleted. But, most importantly, it improves the accessibility of your website to those who are differently abled. Screen readers and other accessibility tools use the Alt attribute to provide information to their users.     

#### HTML tables
```
<table>
    <tr>
        <th>Dish</th>
        <th>Price</th>
    </tr>
    <tr>
        <td>Falafel</td>
        <td>$10.00</td>
    </tr>
    <tr>
        <td>Pasta Salad</td>
        <td>$12.00</td>
    </tr>
</table>
```

#### HTML Forms
- when a user enters data on a website, an HTML form submits an HTTP request containing the data to the server
- check practice.html

- ```<form></form>``` tag: you define forms with the 'form' html tags
- ```action``` attribute: it specifies the URL or path that the form should submit the request to. 
When the action attribute is not specified, it submits the request to the same path as the current web page
 - ```method``` attribute:it specify which HTTP method to use for the HTTP request
 There are 2 methods to submit the form data: GET, POST 
    - GET HTTP method: retrieves information from the server
    - POST HTTP method: sends data to the server

#### DOM (Document Object Model)
- When your web browser recieves an HTML page, it constructs a DOM to represent it
- DOM is a simply tree structure model of the objects in your HTML file 
- the DOM has a series of objects, each representing a sigle HTML element 
- at the root of the DOM is the 'html' object and it contains the 'head' and 'body' object
- the head object contains the title object, and the title object contains its text object 
- the body object contains 2 div objects, first div has the h1 object which contains the text object, etc... 

- So, all the elements in the HTML file are represented as objects in the Document Object Model.
- You can use JavaScript to access and modify the DOM to make your webpage dynamic. 
- For each element you can access the HTML attributes and content, this means you can update the existing content that is displayed in the web browser 
- **The DOM allows you to update and delete existing elements on the web page.**

#### Web accessability
- As a developer, you need to build an application/website what is available for everyone, even for people with disabilities 
- WAI: Web Accessibility Initiative: it aims to allow people with disabilities to understand, navigate and interact with websites. 
WAI developed specifications and supporting resources for accessibility.
People living with disabilities often use assistive technologies to aid them in browsing the web. 
Screen reader software can read the content of websites and everything that is happening.
Speech recognition software can turn spoken words into computer commands or dictate inputting text 
- ARIA: Accessible Rich Internet Application: is an aim of WAI 

How to help as a developer?
    - from the beginning of the project, think of accessibility 
    - use the correct html structure and appropriate elements
    - use semantic elements that screen reader software and other accessibility softwares can understand and interpret 


### CSS Basics

#### Styling
- CSS tells the web browser how to display html elements on screen
```
p {
    color: blue; 
}

Selector {
    property: value;
}
```
- Declaration block: everything inside the curly brackets 
- add CSS file to the html file head section, to link them together
```
<link rel="stylesheet" href="style.css">
```

- **CSS precedence**: the browser will use the most precise selector for an html element. CSS has a set of hierarchy rules which dictate which rule will apply to an element. In this example, the **ID rule takes precedence over the html type selector rule**. 

#### Selectors 
1. **Element Selectors**: selects HTML elements based on the element type.<br>
    For example, if you use p as the selector, the rule will apply to all p elements on the webpage.

2. **ID Selectors**: uses the id attribute of an HTML element. Since the id is unique within a webpage, it allows to select a specific element for styling.<br> 
    ID selector are prefixed with a # character. <br>
    HTML:

    ```
    <span id="latest">New!</span>
    ```

    CSS:

    ```
    #latest { 
        background-color: purple; 
    }
    ```

3. **Class selectors**: elements can also be selected based on the class attribute applied to them. <br>
    The CSS rule has been applied to all elements with the specified class name. <br>
    The class selector is prefixed with a . character. <br>
    In the following example, the CSS rule applies to both elements as they have the navigation CSS class applied to them: <br>

    HTML:
    ```
    <a class="navigation">Go Back</a>
    <p class="navigation">Go Forward</p>
    ```
    CSS:
    ```
    .navigation { 
        margin: 2px;
    }
    ```

4. **Element with Class Selector**:
    First we select the HTML element, then selecting the CSS class or ID.
    The example below selects all p elements that have the CSS class introduction applied to them.
    
    HTML:
    ```
    <p class="introduction"></p>
    ```
    CSS:
    ```
    p.introduction { 
        margin: 2px;
    }
    ```
5. Descendant Selectors: are useful if you need to select HTML elements that are contained within another selector.
    HTML:
    ```
    <div id="blog">
        <h1>Latest News</h1>
    <div>
    ...
    ```
    CSS:
    ```
    #blog h1 {
        color: blue;
    }
    ```
    The CSS rule will select all h1 elements that are contained within the element with the ID blog.<br>
    The structure of a descendant selector is a CSS selector, followed by a single space character, followed by another CSS selector.
    
6. Child Selectors: 
   Child selectors are more specific than descendant selectors. They only select elements that are immediate descendants (children) of a selector (the parent).

HTML:
```
<div id="blog">
  <h1>Latest News</h1>
  <div>
    <h1>Today's Weather</h1>
    <p>The weather will be sunny</p>
  </div>
  <p>Subscribe for more news</p>
</div>
```
If you wanted to style the h1 element containing the text Latest News, you can use the following child selector:
CSS:
```
#blog > h1 {
  color: blue;
}
```
Note, that this will not go beyond a single depth level. Therefore, the CSS rule will not be applied to the h1 element containing the text Today's Weather.

6. :hover pseudoclass: the hover pseudo-class allows you to style an element when the mouse cursor hovers over the element.<br>
The simplest example of this is changing the color of a hyperlink when it is hovered over. To do this, you add the :hover pseudo-class to the end of the selector. In the following example, adding :hover  to the a element will change the color of the hyperlink to orange when it is hovered over.
```
a:hover {
  color: orange;
}
```

#### Text and color in CSS:

**COLORS**: 
From CSS Version 3, there are five main ways to reference a color: 
- **By RGB value**: <br>
RGB is a color model that adds the colors red (R), green (G) and blue (B) together to create colors. This is based on how the human eye sees colors.<br>
Each value is defined as a number between 0 and 255, representing the intensity of that color.<br>
For example, the color **red** would have the RGB value of **255,0,0** since the intensity of the red color would be 100% while blue and green would be 0%.<br>
The color **black** then would be **0,0,0** and the color **white 255,255,255**.
```
p { 
  color: rgb(255, 0, 0); 
}
```
- **By RGBA value**: <br>
RGBA is an extension of RGB that add an alpha (A) channel. The alpha channel represents the opacity, or transparency, of the color.
```
p { 
  color: rgba(255, 0, 0, 0.8); 
}
```
- **By HSL value**: <br>
HSL is a newer color model defined as **Hue (H), Saturation (S) and Lightness (L)**. The aim of the model is to simplify mental visualization of the color that the value represents.<br>
Think of a rainbow that has been turned into a full circle. This represents the **Hue**. The Hue value is the degree value on this circle, from 0 degrees to 360 degrees. 0 is red, 120 is green and 240 is blue.<br>
**Saturation** is the distance from the center of the circle to its edge. The saturation value is represented by a percentage from 0% to 100% where 0% is the center of the circle and 100% is its edge.<br>
**Lightness** is the third element of this color model. Think of it as turning the circle into a 3D cylinder where the bottom of the cylinder is more black(100%) and toward the top is more white(0%).
```
p { 
  color: hsl(0, 100%, 50%);
}
```
- **By hex value**: 
Hexadecimal has 16 digits. This is counted as 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
Colors specified using hexadecimal are prefixed with a # symbol followed by the RGB value in hexadecimal format.
For example, the color red which is RGB 255,0,0 would be written as hexadecimal #FF0000.

- **By predefined color names**: 
black, white, red, blue, green, yellow, ....

**TEXT**: 
**Text color**: <br>
```
p { 
  color: red;
}
```
**Text font and size**: <br>
It is recommended to include several fonts when using the font-family property. These are specified in a fallback order, meaning that if the first font is not available, it will check for the second font.
```
p { 
  font-family: "Courier New", monospace;
  font-size: 12px;
}
```
**Text Transformation**: 
It is useful if you want to ensure the correct capitalization of the text content. 
```
p { 
  text-transform: uppercase;
}
```
The most commonly used values for the text-transform property are:  **uppercase**,  **lowercase**,  **capitalize**  and **none**.

**Text decoration**: 
```
p { 
  text-decoration: underline red solid 5px;
  text-decoration-line: underline;              / underline, overline, line-through and none
  text-decoration-color: red;
  text-decoration-style: solid;                 / solid,  double,  dotted,  dashed  and  wavy
  text-decoration-thickness: 5px;
}
```

#### Box model:
Every box consits of 4 parts:
    Content: the actual content of the element, like the text or image (size: content width + content hight)
        - width, height
        - min-width, max-width
        - min-height, max-height
    Padding: extends the content (size: padding box width: content width + paddin-left + padding-right, padding box height: content height + padding top + padding bottom )
    Border: goes around the padding and content (size: border box width: padding width + border left + border right, border box height: padding height + border top + border bottom )
    Margin: extends the border area to separate the element from its neighboring elements (size: margin box width: border box width + margin left + margin right, margin box height: border box height )

#### Document flow - Block vs in-line elements
Document flow: 

**Block level elements**: <br>
will occupy the full horizontal width of its parent element and the vertical height of its content. <br>
Each block level element has a new line before and after, therefore multiple block level elements will stack on top of each other.<br>
Examples: div, form, h1<br>

**In-line elements**: only occupy the width and height of their content. <br>
They don't appear on a new line, therefore multiple inline elements can form a row of elements. <br>
Examples: p, a, img, input, label, b, i, strong, em, span

You can change a block level element to appear inline and vice versa. 
```
#id {
    display: inline;
    display: block;
}
```

#### Alignment basics: 
**Horizontal alignments of the elements:** <br>
**Align text to the center**: 
```
p {
    text-align: center;
}
```
- **left, right, center, justify** 
- The **justify** alignment spreads the text out so that every line of the text has the same width.


- To align HTML elements, you must consider the box model and document flow
**HTML Element Center Alignment**: 
To center align an element, you set a width on the element and push its margins out to fill the remaining available space of the parent element as in the following HTML structure:
```
<div class="parent">
  <div class="child">
  </div>
</div>
```
```
.parent {
  border: 4px solid red;
}
```
The child element will have a width equal to 50% of the parent element with a padding of 20 pixels. Note that padding: 20px is shorthand for setting the padding top, bottom, left and right to 20px. To visualize the space it occupies, set the border to green:
To align the element to the center, set its margin property to auto. The auto will tell the browser to calculate the margin automatically based on the space available.
The result is the child element is centered within the parent element:
```
.child {
  width: 50%;
  padding: 20px;
  border: 4px solid green;
  margin: auto;
}
```
It is important to note that this works because the div element is a block-level element.  

If you want to align an inline element like img, you will need to change it to a block-level element. Similar to the div example, you add the img to a parent element:

```
<div class="parent">
  <img src="photo.png" class="child">
</div>
```
The CSS rule then changes the img element to a block-level element and sets its margin to auto:

```
.child {
  display: block;
  width: 50%;
  margin: auto;
}
```

**HTML Element Left / Right Alignment**: 
The two most common ways to left and right align elements are to use the **float** property and the **position** property.

The **float** property sets an element's position relative to the text content within a parent element. Text will wrap around the element.
In the following example, the image will be aligned to the right of the div element. The text content will wrap around the image:
```
<div class="parent">
  <img src="photo.png" class="child"> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur eu odio eget leo auctor porta sit amet sit amet justo. Donec fermentum quam in diam volutpat, at lacinia diam placerat. Aenean quis feugiat sem. Suspendisse a dui massa. Phasellus scelerisque, mi vestibulum iaculis tristique, orci tellus gravida nisi, in pellentesque elit massa ut lorem. Sed elementum ornare nunc vel cursus. Duis sed enim in nulla efficitur convallis sed eget dolor. 
</div>
```
```
.child {
  float: right;
}
```












