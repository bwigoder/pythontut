#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def file_to_string(filename):
  filecontents = open(filename).read(100000)
  return filecontents

def extract_year(fileoutput):
  match = re.search(r'Popularity in (\d+)', fileoutput)
  if match:
    file_year = match.group(1)
    return file_year
  else:
    print 'Could not parse year'
    return ''

def extract_names_and_rank_numbers(fileoutput):
  allmatches = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td>',fileoutput)
  listofmatches = []
  if allmatches:
    for match in allmatches:
      #add all matches to a list, with the name, followed by the rank
      listofmatches.append(match[1]+' '+match[0])
    # Sort the matches in alphabetical order
    listofmatches.sort()
  return listofmatches

def extract_info(filename,summary):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # First, lets convert the file contents to a string
  fileoutput = file_to_string(filename)
  
  # Now, let's get the year
  year = extract_year(fileoutput)

  # Now, let's get the names and rank numbers
  listofnames = extract_names_and_rank_numbers(fileoutput)

# Now build the return output
  if summary:
    output = year + '\n'
    if listofnames:
        for item in listofnames:
          output += item + '\n'
  else:
    output = '['
    output += '\'' + year + '\''
    if listofnames:
      for item in listofnames:
        output += ',\'' + item + '\''
    output += ']'

  return output

def write_summary_to_file(filename,summarytext):
  summary_filename = filename + '.summary'
  file_object = open(summary_filename,'w')
  file_object.write(summarytext)
  file_object.close()
  return

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
  if summary:
    summarytext = extract_info(args[0],True)
    write_summary_to_file(args[0],summarytext)
  else:
    print extract_info(args[0],False)
  
if __name__ == '__main__':
  main()
