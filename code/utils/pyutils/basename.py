import sys
import os

version=(1,1)

def useage(cmd):
	sys.stdout.write("Useage: %s PATHNAME [SUFFIX}\n" % (cmd))
	sys.stdout.write("Or: %s OPTION\n" % (cmd))
	sys.stdout.write("Print NAME with any leading directory components removed.\n")
	sys.stdout.write("If specified, also remove a trailing SUFFIX.\n\n")
	sys.stdout.write("  --help display this help and exit\n")
	sys.stdout.write("  --version output version info and exit\n")
	sys.stdout.write("Examples:\n")  
	sys.stdout.write("  %s /usr/bin/sort Output \"sort\".\n" % (cmd,))
	sys.stdout.write("  %s include/stdio.h .h Output \"stdio\".\n" % (cmd))

def xbasename(path,suffix=None):
	if(path==""):
		return ''
        elif path.rstrip('/')=='' 
		s=os.stat("/")

def main():
	useage("basename")

 

if __name__ =="__main__":
	main()