This Python 2.7 script will take a csv file specified by the operator and parse it for URLs. It will take the URLs and request the status code and print to the screen any bad requests or unreachable URLs as well as what the code is. The program will also print a summary at the end of the number of successes, failures, and unreachable sites. 

Assumptions: 

- The input file will always be formatted like the tactics.csv file in this directory. 

- The program was written in Python 2.7 and will need to be run in the same environment. 

Dependencies: 

- The Requests library for Python must be installed before using this program. Installation instructions can be found at: http://docs.python-requests.org/en/master/user/install/

Instructions:

Run the program by typing the program name and the name of the cvs file to be analyzed. (On Mac OS, I had to specify the Python program to interpret the script. My command is “python2.7 tl.py testy.csv”. Yours may be different depending on which OS you’re running the program on.) 
