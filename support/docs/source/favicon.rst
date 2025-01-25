=============================================
Changing the File's  Favourite Icon (FavIcon)
=============================================

A favicon---short for "favourite icon"---is displayed on a browser's tab,
bookmark bar, history and in search results. 


In the provided HTML file, line number 7 will be the focus of this lesson.

.. code-block:: HTML
    :linenos:
    :emphasize-lines: 7


    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>St. Joseph's Computer Club</title>
        <link rel="icon" type="image/x-icon" href="../assets/images/favicon.ico">
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



A link element defines a relationship between the current document (the one we
are editing now)  and an external resource,  such as an image, video, codes,
etc., file.  In the above link tag has the following attributes and their
values:

#. Attribute **rel** (relationship) has the value of  **icon**.

#. Attribute  ``type``  (file type of the linked file) has the value of ``image/x-icon``.

#. Attribute **href** (hyperlink reference) has the value of  **../assets/images/favicon.ico** , where:  
  
    #. **favicon.ico**  is the name of the icon (image) file, and
   
    #. **../assets/images/** is path to the icon file from this html file.



`Back to front page`_ 

.. _Back to front page: https://sjscompclub.github.io/sj2425/

