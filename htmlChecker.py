#  File: htmlChecker.py
#  Description: Check whether an HTML file has the correct set of tags
#  Student's Name: Amy Fang
#  Student's UT EID: af27947
#  Course Name: CS 313E 
#  Unique Number: 86940
#
#  Date Created: 06/28/17
#  Date Last Modified: 06/29/17

# Stack class
class Stack:
   def __init__(self):
      self.items = []

   def isEmpty (self):
      return self.items == []

   def push (self, item):
      self.items.append(item)

   def pop (self):
      return self.items.pop()

   def peek (self):
      return self.items[-1]

   def size (self):
      return len(self.items)

   def __str__(self):
      if self.items == []:
         return "[]"
      
      result = "["
      for item in self.items:
         result += str(item) + ", "
      result = result[:-2]
      result += "]"         
      return result

##################################################

# Returns a tag and a boolean flag
def getTag(datafile):

   # flag is True if in tag, False if not in a tag
   flag = False

   # stores the tag
   tag = ""

   # While the loop hasn't completed a tag
   while True:

      # the character to be analyzed, always the first character of the datafile
      ch = datafile[0]

      # start tag
      if ch == '<':
         datafile.remove(ch)
         flag = True
         continue

      # end tag
      if ch == '>' or (ch == ' ' and flag):
         datafile.remove(ch)

         # if tag is empty, then don't return an empty tag
         if tag == '':
            continue

         # if tag is not empty, then we finish the tag and break out of the loop
         flag = False
         break

      # if flag is true, then we're inside a tag
      if flag:
         datafile.remove(ch)
         tag += ch

      # if flag is false, then we're outside a tag
      else:
         datafile.remove(ch)

   # if datafile is empty, return tag and false to end processing of datafile
   if len(datafile) == 0:
      return tag, False

   # if datafile is not empty, return tag and true to keep processing datafile
   else:
      return tag, True

# prints a list without commas and quotation marks
def printList(lst):
   result = "["
   for item in lst:
      result += item + ", "
   result = result[:-2]
   result += "]"
   return result
    
def main():
   
   # open file
   infile = open("htmlfile.txt", "r")

   # initialize list
   tagList = []

   # creates a single list with all the characters
   datafile = list(infile.read())
   flag = True

   # appends the tags
   while flag:

      # returns the tag and a flag (true if loop should continue, false if done processing)
      tag, flag = getTag(datafile)
      tagList.append(tag)

      if len(datafile) <= 1:
         break

   # close file
   infile.close()

   # display tagList
   print("tagList =", printList(tagList))
   print()
   
   # initialize validtags, exceptions, and stack
   VALIDTAGS = []
   EXCEPTIONS = ["meta", "br", "hr"]
   stack = Stack()
   
   # iterate through the list of tags
   for tag in tagList:

      # if tag is not in validtags
      if tag not in VALIDTAGS:
         VALIDTAGS.append(tag)
         print("New tag", tag, "found and added to list of valid tags")

      # if tag is a start tag
      if tag[0] != "/":

         # if tag is an exception, do not put on stack
         if tag in EXCEPTIONS:
            print("Tag", tag, "does not need to match: stack is still", stack)
            continue

         # add tag
         stack.push(tag)
         print("Tag", tag, "pushed: stack is now", stack)

      # if tag is an end tag
      else:
         lastTag = stack.peek()

         # if end tag is a match, remove start tag from stack
         if tag[1:] == lastTag:
            stack.pop()
            print("Tag", tag, "matches top of stack: stack is now", stack)
            
         # if end tag is NOT a match
         else:
            print("Error: tag is", tag, "but top of stack is", lastTag)
            break

   print()

   # if stack is empty, then all tags have been matched
   if stack.size() == 0:
      print("Processing complete. No mismatches found.")

   # if stack is not empty, then some tags haven't been matched
   else:
      print("Processing complete. Unmatched tags remain on stack:", stack)

   print()
   VALIDTAGS.sort()   # sort into alphabetical order
   EXCEPTIONS.sort()
   print("VALIDTAGS =", printList(VALIDTAGS))        
   print("EXCEPTIONS =", printList(EXCEPTIONS)) 

main()
