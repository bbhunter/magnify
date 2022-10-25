import sys
import time
import getopt
import requests

argumentList = sys.argv[1:]
rate = -1
outputResult = []

def loadFile(file):
  try:
    with open(file) as f:
      lines = [line.rstrip('\n') for line in f]
      return lines
  except:
    print("Error: the file "+ file + " does not exist.")

def convertResult(result):
  return str(result) + '\n'

def writeFile(file):
  try:
    f = open(file,"w")
    f.writelines(list(map(convertResult, outputResult)))
    f.close()
    print("Results saved: " + file)
  except:
    print("Error: unable to save results in "+ file)
    
def helpMenu():
  print("""
  Usage: magnify [-u] <url> [-f] <file> [-o] <filename>
  -h: Help
  -u --url: URL
  -f --file: Input file containing URLs
  -r --rate: Rate limit in seconds
  -o --output: Output file name/path
  """)

def curlUrl(url):
  keywords = loadFile('keywords.txt')
  result = [url]
  r = requests.get(url)
  result.append(r.status_code)
  for word in keywords:
    if word in str(r.content):
      result.append(word)
  return result

def multipleCurl(urls):
  for url in urls:
    result = curlUrl(url)
    print(result)
    outputResult.append(result)
    if(rate != -1):
        time.sleep(rate)
    
try:
  opts, args = getopt.getopt(argumentList,"f:h:r:u:o:",["file=", "rate=", "url=","output="])

  for opt, arg in reversed(opts):
    if opt == '-h':
      helpMenu()
      sys.exit()
    elif opt in ("-u","--url"):
      print(curlUrl(arg))
    elif opt in ("-f","--file"):
      urls = loadFile(arg)
      multipleCurl(urls)
    elif opt in ("-o", "--output"):
      writeFile(arg)
    elif opt in ("-r", "--rate"):
      rate = int(arg)

except getopt.GetoptError:
  helpMenu()
  sys.exit(2)


