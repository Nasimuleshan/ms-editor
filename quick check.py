import docx
from docx import Document

import docx2txt

my_text = docx2txt.process("test-output.docx")

document = Document()


print (type(my_text))
line = list(my_text.split(" "))
print("enter value")
a=int(input())

new = ""
for x in line:
      if '[' in x :
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


          elif '.' not in x and x[-1] != ',' and x[-1] != ';'and x[-1] != ':':
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



          elif '.' not in x and x[-1] == ':':
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
                              new +=  li+':' + " "

                  

                    elif "–" in x or "-" in x:
                              if ']' in x:
                                        x = x.replace("[", "")
                                        x = x.replace("]", "")
                              x = x.replace("–", "-")                                              
                              li= x.split("-")
                              for i in range(len(li)):
                                        b=int(li[i])
                                        if b>a:
                                                  b=b+1
                                                  
                                        li[i]=b
                              li=str(li).replace(" ","")
                              li=str(li).replace(",","-")
                              new +=  li+':' + " "


                    else:
                        b=int(x)
                        if b>a:
                            b=b+1
                        new += '['+str(b)+']'+':'+ " "
          
          elif '.' not in x and x[-1] == ';':
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
                              new +=  li+';' + " "

                  
 
                elif "–" in x or "-" in x:
                              if ']' in x:
                                        x = x.replace("[", "")
                                        x = x.replace("]", "")
                              x = x.replace("–", "-")
                              li= x.split("-")
                              for i in range(len(li)):
                                        b=int(li[i])
                                        if b>a:
                                                  b=b+1
                                                  
                                        li[i]=b
                              li=str(li).replace(" ","")
                              li=str(li).replace(",","-")
                              new +=  li+';' + " "


                else:
                        b=int(x)
                        if b>a:
                            b=b+1
                        new += '['+str(b)+']'+';'+ " "                                                                 
                  
                                        
                              


              

      else:
          new += x+" "


document.add_paragraph(new)
document.save('test-output.docx')



            

