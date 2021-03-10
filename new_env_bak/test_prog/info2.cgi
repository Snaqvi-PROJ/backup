#!/home/saif/Documents/new_env/bin/python

data = {
  "branch": {
    "corinci": {
      "env": "INTEG12",
      "server": "yval0657"
    },
    "main": {
      "env": "INTEG22_E",
      "server": "yval0347"
    },
    "react": {
      "env": "TEST22_E",
      "server": "yval0s57"
    },
  },
  "logfile": "/jjas/asd/asd/asd"
}

for branchname in data['branch']:
  envname = data['branch'][branchname]['env']
  servername = data['branch'][branchname]['server']
  print 'sshscript fetchfiles '+servername
  print 'sshscript last3 '+servername
  print 'sshscript latestok '+servername
  print '====================='

