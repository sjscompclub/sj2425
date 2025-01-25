.. |br| raw:: html

     <br>
============================
Changing Page Header Content
============================

In the provided HTML file, line number 13 will be the focus of this lesson.

.. code-block:: HTML
    :linenos:
    :emphasize-lines: 13


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

On line 13, please change 
|br| ``<h1> Page header</h1>`` 
|br| to 
|br| ``<h1 id="page_header">Welcome to Abc's Page </h1>``,
|br| replacing ``Abc`` with your first name.


.. note::

    Since we only have one ‘Page header’ for our page, we have given it an id
    of page_header (in other words, this h1 tag has an id attribute with the
    value of page_header).

    In the next lesson, we will use this id to style our page header.


`Back to front page`_ 

.. _Back to front page: https://sjscompclub.github.io/sj2425/





