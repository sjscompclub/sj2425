===================
Basic Unix Commands
===================

In this section, to better understand the file structure of our source code, we will use/review some basic Unix commands.

.. image:: ../../../../assets/images/filestructurediagram01.webp
  :width: 1400
  :alt: Unix FileSystem & Project File Structure Diagram


The *ls* command
----------------

The **ls** command (*list command*) :  We use this command to list/display a folder's content (files and folders).

The *cd* command
----------------

The **cd** or **chdir** command  (*change directory command*) : We use this command to change our working/present directory.  In other words, we use this command to move around our file/folder structure.

The *pwd* command
-----------------
The **pwd** command (*print working, or present, directory command*): We use this command to display the current folder's path (or name).

Please run the following commands:

.. code-block:: sh

    :~$ cd
    # This statement should bring you to the root of your home directory
    :~$ pwd
    /home/user
    # /home/user is your root of your home directory
    :~$ ls
    Desktop  Documents  Downloads  Music  Pictures  Public  
    snap  Templates  Videos
    # This lists the content of your home directory.
    :~$ cd Documents
    # It takes you to the Documents folder of your home directory
    :~$ pwd
    /home/user/Documents
    # pwd shows you are now at /home/user/Documents folder
    :~$ ls
    # Now, it lists the content of your Documents folder
    :~$ cd sj2425.git
    # Now, it takes you to sj2425.git folder of your Documents folder
    :~$ ls
    # Now, list all contents of sj2425.git folder
    :~$ cd assets
    # Now, it takes you to the assets folder of sj2425.git 
    :~$ cd css
    # Now, it takes you to the css folder of assets folder.
    :~$ pwd
    /home/user/Documents/sj2425.git/assets/css
    # Now, it shows the location where you are.
    :~$ cd ../
    # Now, it takes you back to assets folder (parent of css folder)
    :~$ cd css
    # Now, go back again to css folder of assets folder.
    :~$ cd ../js
    # It takes back to assets and then to js folder of assets.


`Back to front page`_ 

.. _Back to front page: https://sjscompclub.github.io/sj2425/

