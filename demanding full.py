import docx
with open('test.txt', 'r') as file :
  filedata = file.read()
  print (filedata)
  print (type(filedata))
  line = list(filedata.split(" "))
  print("enter value")
  a=int(input())

  new = ""
  for x in line:
      if '[' in x:
          if '.' in x:
              x = x[1:-2]
              if ',' in x:
                  if ']' in x:
                      x = x.replace("[", "")
                      x = x.replace("]", "")
                  li= x.split(',')
                  for i in range(len(li)):
                      b=int(li[i])
                      if b>a:
                              b=b+1
                      li[i]=b
                         
                  li=str(li).replace(" ","")
                  new +=  li+'.' + " "

              elif "–" in x or "-" in x:
                  if ']' in x:
                                        x = x.replace("[", "")
                                        x = x.replace("]", "")
                                        x = x.replace("–", "-")
                                        x = x.replace("â€“", "-")
                  li= x.split("-")
                  for i in range(len(li)):
                      b=int(li[i])
                      if b>a:
                                b=b+1
                                
                      li[i]=b
                  li=str(li).replace(" ","")
                  li=str(li).replace(",","-")
                  new +=  li + "." + " "                    
                    
                                        
              else:
                  b=int(x)
                  if b>a:
                      b=b+1
                  new += '['+str(b)+']'+ "." + " "  


          elif '.' not in x and x[-1] != ',':
                    x = x[1:-1]

                    if ',' in x:
                              if ']' in x:
                                        x = x.replace("[", "")
                                        x = x.replace("]", "")
                              li= x.split(',')
                              for i in range(len(li)):
                                  b=int(li[i])
                                  if b>a:
                                      b=b+1
                                  li[i]=b
                              li=str(li).replace(" ","")
                              new +=  li + " "
                                         



                              
                    elif "–" in x or "-" in x:
                        if ']' in x:
                                        x = x.replace("[", "")
                                        x = x.replace("]", "")
                                        x = x.replace("–", "-")
                                        x = x.replace("â€“", "-")
                        li= x.split("-")
                        for i in range(len(li)):
                            b=int(li[i])
                            if b>a:
                                b=b+1
                                
                            li[i]=b
                        li=str(li).replace(" ","")
                        li=str(li).replace(",","-")
                        new +=  li + " "                    
                    
                                        
                    else:
                        b=int(x)
                        if b>a:
                            b=b+1
                        new += '['+str(b)+']'+ " "

                                        

          elif '.' not in x and x[-1] == ',':
                    x = x[1:-2]

                    if ',' in x:
                              if ']' in x:
                                        x = x.replace("[", "")
                                        x = x.replace("]", "")
                              li= x.split(',')
                              for i in range(len(li)):
                                  b=int(li[i])
                                  if b>a:
                                      b=b+1
                                  li[i]=b
                              li=str(li).replace(" ","")
                              new +=  li+',' + " "

                  

                    elif "–" in x or "-" in x:
                        if ']' in x:
                                        x = x.replace("[", "")
                                        x = x.replace("]", "")
                                        x = x.replace("–", "-")
                                        x = x.replace("â€“", "-")
                        li= x.split("-")
                        for i in range(len(li)):
                            b=int(li[i])
                            if b>a:
                                b=b+1
                                
                            li[i]=b
                        li=str(li).replace(" ","")
                        li=str(li).replace(",","-")
                        new +=  li+',' + " "


                    else:
                        b=int(x)
                        if b>a:
                            b=b+1
                        new += '['+str(b)+']'+','+ " "
                                                                           
                  
                                        
                              


              

      else:
          new += x+" "



# Replace the target string
#filedata = filedata.replace('gold', 'silver')

# Write the file out again
with open('test-output.txt', 'w') as file:
    file.write(new)

  #file.write(filedata)



            

