#note cutoff in main, threshold, enable bass & triads

def load_config():

  cfg = open("config.cfg", "r")
  lines = cfg.readlines()
  for l in lines:
    k = l.split()
    if(k[0] == "hasTriads"):
      global triads
      triads = bool(k[1])
    elif(k[0] == "useBass"):
      global bass
      bass = bool(k[1])
    elif(k[0] == "threshold"):
      global threshold
      threshold = int(k[1])
    elif(k[0] == "cutoff"):
      global cutoff
      cutoff = int(k[1])
