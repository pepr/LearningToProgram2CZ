import os
import time

fname = time.strftime('%Y%m%d%H%M', time.localtime())
print fname


os.system('zip %s *.bat *.htm *.html *.dif *.css *.py *.txt' % fname)