print( "First Module's Name: {}".format(__name__) )
'''
When Python runs a file, the first thing before reading any line code,
two special variables are setted. When the Python file is run directly
the __name__ = __nain__
'''
def main():
	print("This is run directly")

if __name__ == '__main__':
	main()
else:
	print("Run From Import")

'''
This allow us to execute lines of code only when not imported
'''