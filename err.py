##def foo(s):
##    n = int(s)
###    print '>>> n = %d' % n
##    assert n != 0, 'n is zero!'
##    return 10 / n
##
##def main():
##    foo('0')
##
##main()

##import logging
##logging.basicConfig(level=logging.INFO)
##
##s = '0'
##n = int(s)
##logging.info('n = %d' % n)
##print 10/n

# pdb
##s = '0'
##n = int(s)
##print 10 / n 


import pdb

s = '0'
n = int(s)
pdb.set_trace()
print 10 / n 
