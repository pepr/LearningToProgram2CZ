"""Auxiliary script to check the HTML-files structure.

The script is using the HTML tidy utility (http://tidy.sourceforge.net/)
and the tidy.cfg configuration file. See also tidy.txt for the help
that can be obtained by calling 'tidy -h >tidy.txt'.

$Id: tidycheck.py,v 1.3 2004/08/27 10:32:48 prikryl Exp $
""" 

import glob, os, sys

# Get the list of the HTML files (*.htm, *.html) from the working directory.
files = glob.glob('./*.htm') + glob.glob('./*.html')

# Check the files and report the warnings and errors. The report goes to
# screen and to the tidy.log file.
log = file('tidy.log', 'w')
for fname in files:
    fin = file(fname)
    
    (cin, cout) = os.popen2('tidy.exe -config tidy.cfg >tidy.bak 2>tidy.err')
    cin.write(fin.read())
    
    fin.close()
    cin.close()
    cout.close()
    
    f = file('tidy.err')
    lines = filter(lambda line: 
                      (line.find('Error:') != -1) or 
                      (line.find('Warning:') != -1), 
                   f.readlines())
    f.close()
    os.remove('tidy.bak')
    os.remove('tidy.err')


    if lines:
        msg = 'tidy ' + fname + ':\n  ' + '  '.join(lines) + '\n'
        sys.stderr.write(msg + '\a')
        log.write(msg)
                                    
log.close()
