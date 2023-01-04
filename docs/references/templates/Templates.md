# Templates

Templates contain the basic HTML outline of a page. Here, you organise how data is presented when a page is rendered.
Templates do not strictly have to be used for one page. You may create a template that can be reused for many pages.

## Template variables
To declare template variables to be replaced by their corresponding prop, insert the prop name enclosed by opening and closing curly braces.

Eg. ```{title}```

## Template logic
Some inline logic statements are supported by the Crest Template Engine. These allow for the manipulation of iterable data,
conditional evaluations and other general operations. A full list of all statements will be available here once the engine has
been completed. All statements should be enclosed by ```{%``` and ```%}``` and separate the function output from the header with 
```->```.

Eg. ```{% map i from items -> <p>{i}</p> %}```

Given the ```items``` prop passed as the list ```[0, 1, 1, 2, 3, 5, 8]```, the example above will generate the following content:

```html
<p>0</p>
<p>1</p>
<p>1</p>
<p>2</p>
<p>3</p>
<p>5</p>
<p>8</p>
```
__WARNING: Never permit users to upload or modify internal templates__