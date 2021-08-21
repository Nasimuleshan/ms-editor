import docx
with open('test.txt', 'r') as file :
  filedata = file.read()
  print (filedata)
  print (type(filedata))
  li = list(filedata.split(" "))
  print('enter value')
  a=int(input())

  new = ""
  for x in li:
      if '[' in x:
          if '.' in x or ',' in x:
                    x = x.replace(".", "")
                    x = x.replace(",", "")
                    x = x[1:-1]
                    x=int(x)
                    if int(x)>a:
                              x=int(x)+1
                    new += '['+str(x)+']'+'.'
          else:
                    print(x)
                    x = x[1:-1]
                    if int(x)>a:
                              x=int(x)+1
                    new += '['+ str(x)+']'+' '

      else:
                new += x+' '


          
        
print(new)

# Replace the target string
filedata = filedata.replace('gold', 'silver')

# Write the file out again
with open('test.txt', 'w') as file:
  file.write(filedata)



            

