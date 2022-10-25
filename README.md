# Magnify
A tool for spider multiple URLs & check for sensitive variables in code.

## Why?
It is hard to check waybackurls by copy & paste in browser. Many URL get 404. Hence, This tool helps to reduce the error links & helps to find sensitive keywords in code.

## Usage
```
Usage: magnify [-u] <url> [-f] <file> [-r] <rate> [-o] <filename>
  -h: Help
  -u --url: URL
  -f --file: Input file containing URLs
  -r --rate: Rate limit in seconds
  -o --output: Output file name/path
```

## Install
```
git clone https://github.com/heydc7/magnify.git
cd magnify/
python3 main.py -u https://google.com
```
