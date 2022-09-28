import webbrowser, sys
from ftplib import FTP # Socket-based FTP tools
from getpass import getpass # Hidden password input
if sys.version[0] == '2': input = raw_input # 2.X compatibility
nonpassive = False # Force active mode FTP for server?
filename = input('File?') # File to be downloaded
dirname = input('Dir? ') or '.' # Remote directory to fetch from
sitename = input('Site?') # FTP site to contact
user = input('User?') # Use () for anonymous
if not user:
    userinfo = ()
else:
    from getpass import getpass # Hidden password input
    userinfo = (user, getpass('Pswd?'))
print('Connecting...')
connection = FTP(sitename) # Connect to FTP site
connection.login(*userinfo) # Default is anonymous login
connection.cwd(dirname) # Xfer 1k at a time to localfile
if nonpassive: # Force active FTP if server requires
    connection.set_pasv(False)
print('Downloading...')
localfile = open(filename, 'wb') # Local file to store download
connection.retrbinary('RETR ' + filename, localfile.write, 1024)
connection.quit()
localfile.close()
print('Playing...')
webbrowser.open(filename)
