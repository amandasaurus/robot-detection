# robot_detection

robot_detection is a python module to detect if a given HTTP User Agent is a web crawler. It uses the list of registered robots from http://www.robotstxt.org: (Robots Database)[http://www.robotstxt.org/db.html)

## Usage

There is only one, function, ``is_robot`` that takes a string (unicode or not) and returns True iff that string matches a known robot in the robotstxt.org robot database

### Example

    >>> import robot_detection
    >>> robot_detection.is_robot(user_agent_string)

## Updating

You can download a new version of the Robot Database from [this link](http://www.robotstxt.org/dbexport.html).

Download the database dump, and run the file ``robot_detection.py`` with the file as first argument.

    $ wget http://www.robotstxt.org/db/all.txt
    $ python robot_detection.py all.txt

If the database has changed, it'll print out the new version of ``robot_useragents`` variable that you need to put into the source code.

## Tests

Some simple unittests are included. Running the ``tests.py`` file will run the tests.
