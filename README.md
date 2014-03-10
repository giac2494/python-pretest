
# Language exercises

Put each solution in a separate python module named `excerciseN.py` where `N` is the number of the excercise.

    mkdir language_excercises
    cd language_excercises
    touch excercise1.py
    touch excercise2.py
    # ... and so on ...

1. n = [1, 3, 5] Please add the code to print out the second element in the list.


2. Write a function find_longest_word() that takes a list of words and returns the length of the longest one. Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n

3. Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n (where n is the number of lines in the file).

4. Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards from English into Swedish. Write a function translate() that takes a list of English words and returns a list of Swedish words.

5. Give the yourself a nickname:
Declare three variables, consisting of your first name, your last name, and a nickname. Write a program that prints out your first name, then your nickname in parenthesis, and then your last name. Example output: George (Woody) Washington

6. Add two variables together:
Declare three variables (x, y, and z) as integers. Assign a value of 9 to x, assign a value of 7 to y, and then make z equal to the sum of those two variables. Print out the contents of the z variable.

7. Implement python client that downloads the resources from the http://ialpython.apiary.io/people endpoint and transforms the entities into name: email dictionaries and prints them.

# Django Excercises

## Instructions

this goes in a `django_excercises` folder under `/vagrant/python-pretest`

    mkdir /vagrant/python-pretest/django_excercises
    cd /vagrant/python-pretest/django_excercises
    touch zoo_client.py
    # ... and so on ....

## Features

Implement a django server and a python command line client to manage a zoo.

Components:

 - django project named `zoo_pro`
 - django app named `zoo`
 - python command line client named `zoo_client.py`

The zoo app exposes a web service for the command line client to store animals into a database.

### Store animal

The zookeper uses the command line client to add an animal to the database.

    $ python zoo_client.py store "Zebra"
    OK

The command line client prints `OK` if the operation went correctly.

The zookeeper can add more animals:

    $ python zoo_client.py store "Zebra"
    OK
    $ python zoo_client.py store "Hyppo"
    OK
    $ python zoo_client.py store "Hyppo"
    OK
    $ python zoo_client.py store "Python"
    OK


### Fetch all animals

The zookeper uses the command line client to list all the animals who live in the zoo

    $ python zoo_client.py list
    OK listing all animals:
    Zebra
    Python
    Hyppo
    Hyppo

The client first displays an informative line and then prints out all the animals one per line.


### Query animal count (optional)

The zookeper uses the command line client to know how many animals live in the zoo

    $ python zoo_client.py count "Zebra"
    1
    $ python zoo_client.py count "Hyppo"
    2



# Submission

Push all the excercises to your github repo and make `mpaolini` a contributor:

 - login into github and create a new repo named `ial-python-pretest`
 - go to repo settings (bottom right), then collaborators (left column), write `mpaolini` and click "Add collaborator"
 - `git init`
 - `git add .`
 - `git commit -m test finished`
 - `git remote add origin https://github.com/<username>/ial-python-pretest.git` 
 - `git push -u origin master`
