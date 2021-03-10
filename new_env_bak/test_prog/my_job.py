#!/home/saif/Documents/new_env/bin/python
import pprint

"""
data_base = {
  "1001" :
    {
      "patchname" : "Patch206_NC",
      "env" : "INTEG12_E",
      "target" : "INTER"
    },

  "1002" :
    {
      "patchname" : "PatchVCOPLMPSA-62333",
      "env" : "TEST_E",
      "target" : "ALL"
    }
}

"""
def create_job(patchname, env, target):
  data_base_up = {
    "1003" :
      {
        "patchname" : patchname,
        "env" : env,
        "target" : target
      }
  }

  data.update(data_base_up)
  return data


#print create_job('pp1', 'ee1', 'tt1')


import json, sys
data_base_file = "/home/saif/Documents/new_env/temp/data_base.json"

with open(data_base_file) as json_file:
  data = json.load(json_file)


create_job(sys.argv[1], sys.argv[2], sys.argv[3])
print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))


