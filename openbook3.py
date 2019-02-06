fin = open('running-config.cfg')
def indi(s1,s2,s3):
  transit_access_in = []
  fw_management_access_in = []
  global_access = []
  for line in fin:
    if s1 in line:
      transit_access_in.append(line)
    elif s2 in line:
      fw_management_access_in.append(line)
    elif s3 in line:
      global_access.append(line)
  print(transit_access_in,fw_management_access_in,global_access)
if __name__ == '__main__':
  s1 = 'transit_access_in'
  s2 = 'fw-management_access_in'
  s3 = 'global_access'
  indi(s1,s2,s3)



