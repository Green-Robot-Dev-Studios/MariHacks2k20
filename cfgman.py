triads = False
bass = False
threshold = 12
cutoff = 5


#note cutoff in main, threshold, enable bass & triads

def load_config():
  cfg = open("config.cfg", "r")
  lines = cfg.readlines()
  for l in lines:
    k = l.split()
    if(k[0] == "hasTriads"):
      triads = bool(k[1])
    elif(k[0] == "useBass"):
      bass = bool(k[1])
    elif(k[0] == "threshold"):
      threshold = int(k[1])
    elif(k[0] == "cutoff"):
      cutoff = int(k[1])


