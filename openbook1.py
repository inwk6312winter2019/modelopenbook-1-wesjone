fin = open('running-config.cfg')
def list_ifname_ip():
  s = 'nameif'
  d = {}
  s2 = 'ip address'
  for line in fin:
    if s in line:
      d[line]=ip_add()
  print(d)
def ip_add():
  s2 = 'ip address'
  for line in fin:
    if s2 in line:
      return line
list_ifname_ip()

