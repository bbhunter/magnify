import sys
import getopt
import requests

argumentList = sys.argv[1:]

outputfile = ''

def loadFile(file):
  with open(file) as f:
    lines = [line.rstrip('\n') for line in f]
    return lines

def handleResult(results):
  for result in results:
    print(result)

def helpMenu():
  print("""
  Usage: magnify [-u] <url> [-f] <file> [-o] <filename>
  -h: Help
  -u --url: URL
  -f --file: Input file containing URLs 
  -o --output: Output filename
  """)

def curlUrl(url):
  keywords = loadFile('keywords.txt')
  results = [url]
  r = requests.get(url)
  results.append(r.status_code)
  for word in keywords:
    if word in str(r.content):
      results.append(word)
  return results

def multipleCurl(urls):
  for url in urls:
    print(curlUrl(url))

try:
  opts, args = getopt.getopt(argumentList,"f:h:u:o:",["file=", "url=","output="])

  for opt, arg in opts:
    if opt == '-h':
      helpMenu()
      sys.exit()
    elif opt in ("-u","--url"):
      print(curlUrl(arg))
    elif opt in ("-f","--file"):
      urls = loadFile(arg)
      multipleCurl(urls)
    elif opt in ("-o", "--output"):
      print(arg)
      outputfile = arg
except getopt.GetoptError:
  helpMenu()
  sys.exit(2)


