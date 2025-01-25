.. _styling-header
======================
Styling Header Section
======================

* Pleasese open the HTML file named after your first name using VS Code.

* In the `<head>` tag, just before the closing `</head>` tag, paste the
  following CSS code:

.. code-block:: console
    
    <style>
        #header{
            width: 100%;
            height: 100vh; 
            min-height: 10rem; 
            text-align: center;
            background-color: rgba(0, 0, 0, 0.9) !important;

            background: url(images/mushrooms.jpg); 
            background-position: top; 
            background-size: 100%; 
            background-repeat: no-repeat; 
            background-attachment: scroll;  

            display: flex;
            justify-content: center;
            align-items: center;
            }

        #header-h1{
            color: white;
            font-size: 70px;
            }
        #header-p{
            color: white;
            font-size: 30px; 
            }
    </style>

* Please save the file, and then click the 'Go Live' button to view the outcome.
 
.. note::
    We will examine the details of the above codes and the id attribute of HTML tags.

`Back to front page`_ 

.. _Back to front page: https://sjscompclub.github.io/sj2425/

