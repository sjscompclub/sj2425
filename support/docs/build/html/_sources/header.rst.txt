====================
Creating Page Header
====================

Introduction
------------


In this section, we will create a header for our webpage and, in the process,
perform/learn the following:

* Understand the general structure of the provided HTML file.
* Change the content of the *<title>* tag and understand its purpose.
* Lean about HTML *comments* (notes for humans, coders, not for computers).
* Review at least three Unix commands---namely, *ls*, *pwd* and *cd*---to
  understand the file structure and relative file locations.
* Understand the purpose of *favicon.ico*, and its location.
* Change the content of *<h1>* tag.
* Understand *CSS* (Cascading Style Sheet) and carry out some basic styling on
  *<h1>* element.
* Learn to search, choose and apply the chosen Google font on *<h1>* element.

.. * Understand *<a>* tag and its *href*  attribute.

.. note::

    In this section, we will ignore:

    * every element except *<title>* and *favicon.ico* in the *<head>* section; and 
    * all *<script>* tags at the bottom of the *<body>* tag.

The content of the initial HTML file
------------------------------------

The provided HTML file---named after your first name, followed by .html
extension---has the following content:

.. code-block:: html
    :caption: *HTML Code: student-name.html*
    :linenos:
    :emphasize-lines: 6,7,8,14,22

    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>St. Joseph's Computer Club</title>
        <link rel="icon" type="image/x-icon" 
        href="../assets/images/favicon.ico">
        <link href="../assets/css/bootstrap.min.css" rel="stylesheet">
        <link href="css/mystyle.css" rel="stylesheet">
    </head>
    <body>
        <div class="container">
            <h1>Page header</h1>
            <p>
                This is my test paragraph...
            </p>
            <a href="../index.html">
                Click to go back to the front page...
            </a>
        </div>
    <!-- In this section, we will not learn about these (script) tags. -->
    <script src="../assets/js/bootstrap.bundle.min.js"></script>
    <script src="../assets/js/anime.min.js"></script>
    <script src="js/myjs.js"></script>
    </body>
    </html>


Changing the content of *<title>* tag
-------------------------------------


On line 6, change the content of *<title>* tag from *St. Joseph's Computer
Club* to *Abc's Page* (replace *Abc* with your name).  

The *<title>* element should be similar to the following:

.. code-block:: HTML

    <title>Abc's Page</title>

In the above, replace Abc with your name---such as Conor,  Emmet, Harry, etc.---as appropriate. 

Comments in HTML files
----------------------

In HTML, any texts between *'<!--'* and *'-->'* are called comments. These
comments are for humans (coders) as notes, so computers ignore them.

In the above, on line 22, I declare the text  'In this section, we will not
learn about these (script) tags.'  as my comment for you (not for computers);
hence,  this text will not be displayed on the browser (when users access this
page).

To understand the HTML comment, perform the following:

* On line 14, surround *'<h1>Abc's page</h1>'* with *'<!--'* and *'-->'* (type *'<!--'*
  before *'<h1>'* and *'-->'* after *'</h>'*.  Your line should look like the
  following:

.. code-block::
    :linenos:
    :emphasize-lines: 1

    <!-- <h1>Abc's Page</h1> -->

* Please save the file and open it on your browser (Firefox). [if you have done
  it correctly, the browser will not display your *<h1>* tag content.]

* Now, remove the above added *'<!--'* and *'-->'* characters from the <h1>
  element, save the file and open it on your browser to test. 


Reviewing Unix Commands
-----------------------

ls, pwd, cd


