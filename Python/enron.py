import re
import argparse
import sys
  
class Server:
  '''
  This class opens and reads a given file based on the variable 'path' which acts
  as the path to the file. It then splits the contents of the file using the delimeter 
  'End Email' into a list where each email is an element of the list. 
  Iterating through the emails list and using ReGex each attribute was grabbed from the text and assigned to a list as a string.
  emails[0] will print the whole first email,
  message_id[0] will print the first message_id matching that first email, and so on.
   
  '''
  
  def __init__(self, path):
    self.path = path
    with open(path, "r", encoding="utf-8") as f:
      file_contents = f.read()
      self.emails = file_contents.split("End Email", 10000)
      self.message_id = []
      self.date = []
      self.subject = []
      self.sender = []
      self.receiver = []
      self.body = []
      for email in self.emails:
          try:
              self.message_id.append(str(re.search('(?<=ID:)(.*)', email).groups()[0][2:-1]))
              self.date.append(str(re.search('(?<=Date: )(.*)', email).groups()[0]))
              self.subject.append(str(re.search('(?<=Subject: )(.*)', email).groups()[0]))
              self.sender.append(str(re.search('(?<=From: )(.*)', email).groups()[0]))
              self.receiver.append(str(re.search('(?<=To: )(.*)', email).groups()[0]))
              pattern = 'X-FileName: '
              for match in re.finditer(pattern, email):
                  end = match.end()
                  self.body.append(str(email[end:]))
          except:
              continue

    f.close()
      
  

class Email:
  '''
  The Email class assigns all the previously made attributes to their parameters. 
  '''
  def __init__(self, message_id, date, subject, sender, receiver, body):
    self.message_id = message_id
    self.date = date
    self.subject = subject
    self.sender = sender
    self.receiver = receiver
    self.body = body
    
    
def main(path):
  '''
  Creates an instance of server that then outputs the length of the list of emails.
  '''
  server = Server(path)
  return len(server.emails)
  
  
def parse_args(args_list):
  '''
  An argument parser that requires the path to the textfile and makes it a string.
  '''
  parser = argparse.ArgumentParser()
  parser.add_argument("path", type=str)
  return parser

if __name__ == "__main__": 
  arg = parse_args(sys.argv[1:])
  main(arg)