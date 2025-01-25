.. _open-source-on-vscode:
=========================================
Opening the Source Code folder on VS Code
=========================================

Creating a new branch:

.. code-block:: console

    :~$ cd 
    :~$ cd Documents
    :~$ cd sj2425.git
    :~$ git branch
    :~$ git branch -c YOUR-FIRST-NAME-X
    :~$ git branch
    :~$ git checkout YOUR-FIRST-NAME-X

.. Attention::

    In the above, please replase **YOUR-FIRST-NAME-X** with your first name +
    one digit number for **X**. 

To open your website source folder on Visual Studio Code (VS Code), please run
the following statements (without ' *:~$* '):

.. code-block:: bash
    :linenos:

    :~$ cd 
    :~$ cd Documents/sj2425.git/YOUR-FIRST-NAME
    :~$ code .

.. Attention::

    In line 2 above, please replace **YOUR-FIRST-NAME** with your first name (all lower case). 



Work on your file (add/edit/update your file)...

Now, update the remote server:

.. code-block:: console

    :~$ cd
    :~$ cd Documents
    :~$ cd sj2425.git
    :~$ git status
    :~$ git add .
    :~$ git status
    :~$ git commit -m "First day update"
    :~$ git push origin HEAD
    :~$ git remote show origin


`Back to front page`_ 

.. _Back to front page: https://sjscompclub.github.io/sj2425/

