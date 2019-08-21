# Project 1: Computing Environment, and SQL

Over the course of the semester, you will work with a variety of software packages, including PostgreSQL, Apache Spark, Python Django, and others. Installing those packages and getting started can often be a hassle, because of software dependencies. You have three choices.

* Install the different software packages on your own machine (most of these packages should have tutorials to install them on different OSs). If you have a Linux box or a Mac, this should be possible; it may be more difficult with Windows. In any case, although we will try our best, we would likely not be able to help you with any problems.
* (**Preferred Option**) **Use Vagrant with Virtual Box** as discussed below. If you have a reasonably modern machine (within last 3-4 years), VirtualBox should generally work fine.

---

### Git & Github

Git is one of the most widely used version control management systems today, and invaluable when working in a team. GitHub is a web-based hosting service built around git --
it supports hosting git repositories, user management, etc. There are other similar services, e.g., bitbucket.

We will use GitHub to distribute the assignments, and other class materials. Our use of git/github for the class will be minimal; however, we encourage you to use it for
collaboration for your class project, or for other classes. 

#### Cloning the Class Repository
We will be using the department `gitlab` for downloading project materials,
and Elms for uploading.  Clone `Project1` by installing `git`, and then: 

`git clone https://gitlab.cs.umd.edu/keleher/424-f19/project1.git`

*NOTE*: If you are having trouble installing `git`, you can just download the files instead (as a zipfile), although updating may become tedious. 

### Vagrant + Virtual Box

[Virtual Box](https://www.virtualbox.org/) is a virtualization software package (similar to VMWare or Parallels), which allows you to construct and run virtual machines on your computer. [Vagrant](https://www.vagrantup.com/) enables users to create and configure lightweight, reproducible, and portable development environments using VirtualBox. We will provide `VagrantFiles` for different assignments, that will help you start the VMs with the requisite packages installed.

- In order to use this option, you have to first install Vagrant and VirtualBox on your machine (called `Host` henceforth). See the instructions on the two websites above to do that.
- Vagrant makes things **super-easy**. We will provide you with appropriate setup files -- all you need to do is `vagrant up` to start the virtual machine.
- More specifically: in the git sub-directory `project1`, run `vagrant up`. This will start the virtual machine in the background. You may be prompted to run `vagrant box update`. Do so.
- By default, vagrant only provides **ssh** access into the virtual machine (called `Guest VM` henceforth), using `vagrant ssh`. This will work as if you are doing `ssh` into a remote machine.
- The Guest VM will have access to the files in the current directory *on the host machine* (i.e., the files in the `project1` directory and its subdirectories). These are mounted in the guest VM at `/vagrant`. It would be best if you only make edits to that directory -- since those edits will survive a `vagrant destroy`. In fact, you can continue using your favorite text editor (in the host machine) to edit files, and only use the VM for running specific programs (like `postgres`, `psql`, or `ipython notebook` below).
- If the Guest VM has a program (e.g., a Web Server) running and listening on a specific port (e.g., 80), you can access those ports from the host machine by adding them to the `VagrantFile`. The provided VagrantFile has two such mappings: for port 8888, used by iPython (mapped to port 8888 on the host machine), and for port 80, used by a Web server (mapped to port 8080 on the host machine).
- If you just exit the `ssh` the VM continues running in the background.
- Some other vagrant commands that you would need to be familiar with:
    - `vagrant destroy`: will remove all traces of the guest machine from your system. It'll stop the guest machine, power it down, and remove all of the guest hard disks. Any data stored on the VM will be deleted (except in `/vagrant/`). When you are ready to work again, just do `vagrant up`.
    - `vagrant suspend`: will save the current running state of the machine and stop it. When you do `vagrant up` again, it will restart with that state.
    - `vagrant halt`: will shutdown the machine.


---

### PostgreSQL

PostgreSQL is a full-fledged and powerful relational database system, and will be used for several assignments. 

PostgreSQL is already installed on your virtual machine. To get started, start the virtual machine using `vagrant up`. 

The current version of PostgreSQL is 9.5.19. You will find the detailed documentation at:
http://www.postgresql.org/docs/9.5/interactive/index.html. 

Following steps will get you started with creating a database and populating it with the `University` dataset provided on the book website: http://www.db-book.com

* You will be using PostgreSQL in the client-server mode. Recall that the server is a continuously running process that listens on a specific port (the actual port would differ, and you can usually choose it when starting the server). In order to connect to the server, the client will need to know the port. The client and server are often on different machines, but for you, it may be easiest if they are on the same machine (i.e., the virtual machine). 

* Using the **psql** client is the easiest -- it provides a command-line access to the database. But there are other clients too, including a GUI (although that would require starting the VM in a GUI mode, which is a bit more involved). We will assume **psql** here. If you really want to use the graphical interfaces, we recommend trying to install PostgreSQL directly on your machine.

* Important: The server should be already started on your virtual machine -- you do not need to start it. However, the following two help pages discuss how to start the
   server: [Creating a database cluster](http://www.postgresql.org/docs/current/static/creating-cluster.html) and [Starting the server](http://www.postgresql.org/docs/current/static/server-start.html)

* PostgreSQL server has a default superuser called **postgres**. You can do everything under that username, or you can create a different username for yourself. If you run a command (say `createdb`) without any options, it uses the same username that you are logged in under (i.e., `vagrant`). However, if you haven't created a PostgreSQL user with that name, the command will fail. You can either create a user (by logging in as the superuser), or run everything as a superuser (typically with the option: **-U postgres**).

* After the server has started, the first step is to **create** a database, using the **createdb** command. PostgreSQL automatically creates one database for its own purpose, called **postgres**. It is preferable you create a different database for your data. Here are more details on **createdb**: 
   http://www.postgresql.org/docs/current/static/tutorial-createdb.html

* We will create a database called **university**.
	```
	createdb university
	```
* Once the database is created, you can connect to it. There are many ways to connect to the server. The easiest is to use the commandline tool called **psql**. Start it by:
	```
	psql university
	```
	**psql** takes quite a few other options: you can specify different user, a specific port, another server etc. See documentation: http://www.postgresql.org/docs/current/static/app-psql.html

* Note: you don't need a password here because PostgreSQL uses what's called `peer authentication` by default. You would typically need a password for other types of connections to the server (e.g., through JDBC).

Now you can start using the database. 
    
   - The psql program has a number of internal commands that are not SQL commands; such commands are often client and database specific. For psql, they begin with the
   backslash character: `\`. For example, you can get help on the syntax of various PostgreSQL SQL commands by typing: `\h`.

   - `\d`: lists out the tables in the database.

   - All commands like this can be found at:  http://www.postgresql.org/docs/current/static/app-psql.html. `\?` will also list them out.

   - To populate the database using the provided university dataset, use the following: `\i DDL.sql`, followed by 
	   ```
	   \i smallRelationsInsertFile.sql
	   ``` 

   - For this to work, the two .sql files must be in the same directory as the one where you started psql. The first command creates the tables, and the
   second one inserts tuples in it. 
	
   - Create a different database ```university_large``` for the larger dataset provided (`largeRelationsInsertFile.sql`). Since the table names
   are identical, we need a separate database. You would need this for the reading homework.

---

### Python and Jupyter/IPython

We will be using Python for most of the assignments; you wouldn't typically use Python for systems development, but it works much better as an instructional tool. Python is easy to pick up, and we will also provide skeleton code for most of the assignments. 

IPython is an enhanced command shell for Python, that offers enhanced introspection, rich media, additional shell syntax, tab completion, and rich history. 

**IPython Notebook** started as a web browser-based interface to IPython, and proved especially popular with Data Scientists. A few years ago, the Notebook functionality was forked off as a separate project, called [Jupyter](http://jupyter.org/). Jupyter provides support for many other languages in addition to Python. 

* Start the VM using `vagrant up`. Python, IPython, and Jupyter are already loaded.

* To use Python, you can just do `python` (or `ipython`), and it will start up the shell.

* To use Jupyter Notebook, do `cd /vagrant` followed by: 
	```
	jupyter notebook --port=8888 --no-browser --ip=0.0.0.0
	``` 
This will start a server on the VM, listening on port 8888. We will access it from the **host** (as discussed above, the VagrantFile maps the 8888 port on the guest VM to the 8888 port on the host VM). To do that, simply start the browser, and point it to: http://127.0.0.1:8888

* You should see the Notebooks in the `project1/` directory. Click to open the "IPython Getting Started" Notebook, and follow the instruction therein.

* The second Notebook ("Basics of SQL") covers basics of SQL, by connecting to your local PostgreSQL instance. The Notebook also serves as an alternative mechanism to run queries. However, in order to use that, you must set up a password in `psql` using `\password` (set the password to be `ubuntu`).

# The Actual Assignment 
*This assignment is to be done by **yourself**.*

You should have the following present in your vagrant directory (`/vagrant` in the VM):

1. README.md: This file.
1. small.sql: The SQL script for creating the data.
1. queries.py: The file where to enter your answer; this is the file to be submitted
1. answers.py: The answers to the queries on the small dataset.
1. SQLTesting.py: File to be used for testing your submission -- see below.
1. Vagrantfile: A Vagrantfile that creates the 'flights' database and populates it using `small.sql` file.

*Our testing will be done on the different, large dataset*. 

### Schema 
The dataset contains synthetic air flight data. Specifically it contains the following tables:

1. airports: airportid, city, name, total2011, total2012
1. customers: customerid, name, birthdate, frequentflieron
1. airlines: airlineid, name, hub
1. flights: flightid, source, dest, airlineid, local_departing_time, local_arrival_time
1. flewon: flightid, customerid, flightdate

See the provided SQL file for the table definitions.

The dataset was generated synthetically: the airport ids and the cities were chosen from the biggest airports in the US, but the rest of the data is populated randomly. The data will not make sense. For example, two different flights between the same cities may have very different flight durations. The flight times between the cities may not correspond to geographical distances that you know. Some other information about the data:
- **The dates in the *large* database might be different than in the *small*.**
- Each customer may at most take one flight every day.
- The flight times were chosen between 30 minutes to 5 hours randomly.
- All flights are daily (start and end on a single day), and none are overnight. 
- For every flight from city A to city B, there is corresponding return flight from B to A.
- The "flewon" table only contains the flight date -- the flight times must be extracted from the flights table.

In many cases (especially for complex queries or queries involving 
`max` or `min`), you will find it easier to create temporary tables
using the `with` construct. This also allows you to break down the full
query and makes it easier to debug.

You don't have to use the "hints" if you don't want to; there might 
be simpler ways to solve the questions.

### Testing and submitting using SQLTesting.py
Your answers (i.e., SQL queries) should be added to the `queries.py` file. A simple query is provided for the first answer to show you how it works.
You are also provided with a Python file `SQLTesting.py` for testing your answers.

- We recommend that you use `psql` to design your queries, and then paste the queries to the `queries.py` file, and confirm it works.

- SQLTesting takes quite a few options: use `python3 SQLTesting.py -h` to see the options.

- To get started with SQLTesting, do: `python3 SQLTesting.py -v -i` -- that will run each of the queries and show you your answer and correct answer.

- If you want to test your answer to Question 1, use: `python3 SQLTesting.py -q 1`. The program compares the result of running your query against the provided answer (in the `answers.py` file).

- The `-v` flag will print out more information, including the correct and submitted answers etc.

- If you want to test your answers to all questions (this is what we will do), use: `python3 SQLTesting.py` and look at the final total score.

- `-i` flag to SQLTesting will run all the queries, one at a time (waiting for you to press Enter after each query).

- **Note that**: We will basically run this same program on your submitted `queries.py` file, but with the larger dataset; your score on the assignment will 
be score output by the program. The program tries to do partial credits (as you can see in the code). It is very unlikely that your score on the larger, hidden 
dataset will be higher than your score on the provided dataset.  

### Submission Instructions
Submit the `queries.py` file using ELMS  [here](https://umd.instructure.com/courses/1267269/assignments/4946597). **Due September 6.**
      
### Assignment Questions
See `queries.py` file.
