# Semantic HTML cheat sheet

There are hundreds of semantic tags available to help describe the meaning of your HTML documents. <br>
Below is a cheat sheet with some of the most common ones you’ll use in this course and in your development career.

## Sectioning tags
Use the following tags to organize your HTML document into structured sections. 

```<header>```<br>
The header of a content section or the web page. The web page header often contains the website branding or logo.

```<nav>```<br>
The navigation links of a section or the web page.

```<footer>```<br>
The footer of a content section or the web page. On a web page, it often contains secondary links, the copyright notice, privacy policy and cookie policy links.

```<main>```<br>
Specifies the main content of a section or the web page.

```<aside>```<br>
A secondary set of content that is not required to understand the main content.

```<article>```<br>
An independent, self-contained block of content such as a blog post or product.

```<section>```<br>
A standalone section of the document that is often used within the body and article elements.

```<details>```<br>
A collapsed section of content that can be expanded if the user wishes to view it.

```<summary>```<br>
Specifies the summary or caption of a ```<details>``` element.

```<h1>``` - ```<h6>```<br>
Headings on the web page. ```<h1>``` indicates the most important heading whereas ```<h6>``` indicates the least important. 

## Content tags

```<blockquote>```<br>
Used to describe a quotation.

```<dd>```<br>
Used to define a description for the preceding ```<dt>``` element.

```<dl>```<br>
Used to define a description list.

```<dt>```<br>
Used to describe terms inside```<dl>``` elements.

```<figcaption>```<br>
Defines a caption for a photo image.

```<figure>``` <br>
Applies markup to a photo image.

```<hr>```<br>
Adds a horizontal line to the parent element.

```<li>```<br>
Used to define an item within a list.

```<menu>```<br>
A semantic alternative to ```<ul>``` tag.

```<ol>```<br>
Defines an ordered list.

```<p>```<br>
Defines a paragraph.

```<pre>```<br>
Used to represent preformatted text. Typically rendered in the web browser using a monospace font.

```<ul>```<br>
Unordered list

## Inline tags

```<a>```<br>
An anchor link to another HTML document.

```<abbr>```<br>
Specifies that the containing text is an abbreviation or acronym.

```<b>```<br>
Bolds the containing text. When used to indicate importance use ```<strong>``` instead.

```<br>```<br>
A line break. Moves the subsequent text to a new line.

```<cite>```
Defines the title of creative work (for example a book, poem, song, movie, painting or sculpture). 
The text in the ```<cite>``` element is usually rendered in italics.

```<code>```<br>
Indicates that the containing text is a block of computer code.

```<data>```<br>
Indicates machine-readable data.

```<em>```<br>
Emphasizes the containing text.

```<i>```<br>
The containing text is displayed in italics. Used to indicate idiomatic text or technical terms.

```<mark>```<br>
The containing text should be marked or highlighted.

```<q>```<br>
The containing text is a short quotation.

```<s>```<br>
Displays the containing text with a strikethrough or line through it.

```<samp>```<br>
The containing text represents a sample.

```<small>```<br>
Used to represent small text, such as copyright and legal text.

```<span>```<br>
A generic element for grouping content for CSS styling.

```<strong>```<br>
Displays the containing text in bold. Used to indicate importance.

```<sub>```<br>
The containing text is subscript text, displayed with a lowered baseline.

```<sup>```<br>
The containing text is superscript text, displayed with a raised baseline.

```<time>```<br>
A semantic tag used to display both dates and times.

```<u>```<br>
Displays the containing text with a solid underline.

```<var>```<br>
The containing text is a variable in a mathematical expression.

## Embedded content and media tags

```<audio>```<br>
Used to embed audio in web pages.

```<canvas>```<br>
Used to render 2D and 3D graphics on web pages.

```<embed>```<br>
Used as a containing element for external content provided by an external application such as a media player or plug-in application. 

```<iframe>```<br>
Used to embed a nested web page. 

```<img>```<br>
Embeds an image on a web page.

```<object>```<br>
Similar to ```<embed>``` but the content is provided by a web browser plug-in.

```<picture>```<br>
An element that contains one ```<img>``` element and one or more ```<source>``` elements to offer alternative images for different displays/devices.

```<video>```<br>
Embeds a video on a web page.

```<source>```<br>
Specifies media resources for ```<picture>```, ```<audio>``` and ```<video>``` elements.

```<svg>```<br>
Used to define Scalable Vector Graphics within a web page.

## Table tags

```<table>```<br>
Defines a table element to display table data within a web page.

```<thead>```<br>
Represents the header content of a table. Typically contains one ```<tr>``` element.

```<tbody>```<br>
Represents the main content of a table. Contains one or more ```<tr>``` elements.

```<tfoot>```<br>
Represents the footer content of a table. Typically contains one ```<tr>``` element.

```<tr>```<br>
Represents a row in a table. Contains one or more ```<td>``` elements when used within ```<tbody>``` or ```<tfoot>```. When used within ```<thead>```, contains one or more ```<th>``` elements.

```<td>```<br>
Represents a cell in a table. Contains the text content of the cell.

```<th>```<br>
Defines a header cell of a table. Contains the text content of the header.

```<caption>```<br>
Defines the caption of a table element.

```<colgroup>```<br>
Defines a semantic group of one or more columns in a table for formatting.

```<col>```<br>
Defines a semantic column in a table.