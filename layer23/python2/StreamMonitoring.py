#!/usr/bin/python

import os, sys, time, getopt

lib_path = os.path.abspath('testutils')
sys.path.append(lib_path)

from testutils.TestUtilsL23 import XenaScriptTools

def helptext():
   print "Usage: %s [options] IPaddr p1 p2 ..." % (sys.argv[0])
   print 
   print "Setup a default stream on apecified ports, run for 5 seconds"
   print "print stats"
   print 
   print "Options"
   print " -d   enable debug of script commands"
   print 
   sys.exit(1)
   
def main(argv):
   c_debug = 0

   portlist = []

   try:
      opts, args = getopt.getopt(sys.argv[1:], "dh")
   except getopt.GetoptError:
      helptext()
      return

   for opt, arg in opts:
      if opt == '-h':
         helptext()
         return
      elif opt in ("-d"):
         c_debug = 1

   if len(args) <= 1:
      helptext()

   ip_address = args[0]
   
   ports = args[1:]

   xm    = XenaScriptTools(ip_address)

   if c_debug:
      xm.debugOn()
   xm.haltOn()

   xm.Comment("Logon")
   xm.LogonSetOwner("xena", "python")   

   for i in range(30):
      for port in ports:
         txres = xm.Send(port + " PT_TOTAL ?")
         rxres = xm.Send(port + " PR_TOTAL ?")
         print "%s, %s" % (txres, rxres)
      time.sleep(1)

   xm.Comment("Done")


if __name__ == '__main__':
    sys.exit(main(sys.argv))