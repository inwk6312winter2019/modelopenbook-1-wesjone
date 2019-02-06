
def replace_head(s1,s2,s3,net1,net2,net3,f1,f2):
  for line in f1:
    if s1 in line:
      newline = line.replace(s1,s3)
      f2.write(newline)
    elif s2 in line:
      newline = line.replace(s2,s3)
      f2.write(newline)
    else:
      f2.write(line)
if __name__ =='__main__':
  s1 = '192'
  s2 = '172'
  s3 = '10'
  net1 = '255.255.0.0'
  net2 = '255.255.255.0'
  net3 = '255.0.0.0'
  fread = open('running-config.cfg','r')
  fwrite = open('newconfig.cfg','w')
  replace_head(s1,s2,s3,net1,net2,net3,fread,fwrite)

