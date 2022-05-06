from time import time
import os
import binascii
import math
import os.path

lenf=0
name=""
add_bits=""
Make_togher=""

namez = input("c,  compress or e, extract? ")

#@Author Jurijus Pacalovas
class compression:
       
        def cryptograpy_compression4(self):
                
                self.name = "Written: Jurijus pacalovas"

                if namez!="c" and namez!="e":
                        print("The wrong letter")
                        raise SystemExit
                if namez=="c" or namez=="e":        
                    if namez=="c":
                        Deep3=8

                        i=1

                    if namez=="e":
                        i=2
                 
                    Number_add_plus_one=""
                    Prime_Not=""
                    Times_6=""
                    Corrupted=0
                      
                    name = input("What is name of file? ")

                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                            
                    
                    namem=""
                    namema="?"
        
                    nameas=name
                    nac=len(nameas)
                    
                    compress_or_not_compress=1
                    Circle_times3=0

                    if i==2:
                        if nameas[nac-4:nac]==".bin":
                   
                        	nameas=name[:nac-4]
                        	nac=len(nameas)
                        	
                        	C=1

                        elif nameas[nac-4:nac]!=".bin":
                                print("Sorry, this is not binary file!")
                                raise SystemExit
                   
                    if i==1:
                        
                        nameas=name+".bin"
                    
                    	
                    nac=len(nameas)
                    
                   
                    s=""

                    Equal_info_between_of_the_cirlce_of_the_file=""
                    Equal_info_between_of_the_cirlce_of_the_file_2=""

                    Prime_Not=""
                    Times_6=""

                    Translate_info_Decimal=""

                    D=0

                    x=0
                    x1=0
                    x2=0
                    n=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
      
                        s=str(data)

                        lenf1=len(data)
                        lenf7=len(data)
                        if lenf7>(2**32)-1 or lenf7==0:
                            raise SystemExit
                        
                        END_working=0
                        Circle_times2=0
                                   
                        Equal_info_between_of_the_cirlce_of_the_file_23=""
 
                        sda18=""
                        Equal_info_between_of_the_cirlce_of_the_file_29=""
                        
                        SpinS=0
                        while END_working<10:
                       
                            Circle_times3=Circle_times3+1
                            D=1
                            if D==1:
                                if Circle_times3==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    

                                    if Circle_times3==1:
                                        Equal_info_between_of_the_cirlce_of_the_file_2=sda
                            
                                    n = int(Equal_info_between_of_the_cirlce_of_the_file_2, 2)
                                
                                    width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                    width_bits=(width_bits/8)*2
                                    width_bits=str(width_bits)
                                    width_bits="%0"+width_bits+"x"
                             
                                    width_bits3=binascii.unhexlify(width_bits % n)                                    
                                    width_bits2=len(width_bits3)
                                    
                                    data=width_bits3
                                  
                                    lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            sda="0"+sda
                                            z=z+1

                                    Equal_info_between_of_the_cirlce_of_the_file_2=sda

                                    lenf3=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                lenf2=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                #print(lenf2)
                                

                                #########################################################################################################################################################
                                
                                
                                if i==1:

                                    lenf5=len(Equal_info_between_of_the_cirlce_of_the_file_2)

                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                 
                                    lenf5=len(Equal_info_between_of_the_cirlce_of_the_file)
                                    
                                    
                                    #Extract
                            
                                    s=""

                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                    
                                    Number_add_plus_one=""
                                    Prime_Not=""
                                    Times_6=""
                                  
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                   
                                    g=0

                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2

                                    
                                    if   Circle_times2==0 and SpinS==0:
                                    	Equal_info_between_of_the_cirlce_of_the_file="1"+Equal_info_between_of_the_cirlce_of_the_file
                                    	SpinS=1

                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)                      
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                                
                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                    
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                
                                    add_bits=""

                                    Times_6=""

                                    #Compression

                                    sda10=""
                                    Translate_info_Decimal=""
                                    
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                 
                                    

                                    if Circle_times2>=(2**8)-2:
                                            compress_or_not_compress=2

                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                            
                                    
                                    Find_center_info=Equal_info_between_of_the_cirlce_of_the_file

                                    block=0
                                    Find_Save=1
                                    
                                    
                                    block2=0
                                    Find_center_top=""
                                    

                                    Find_center_info=Equal_info_between_of_the_cirlce_of_the_file
                                    

                                    Put_center_info=0
                                    
                                                 
                                    block=0
                                    while block<lenf6:
                                                        

                                                        Put_center_info_2=Put_center_info+24
                                                        Put_center_info_3=Put_center_info

                                                        Find_center_info1=Find_center_info[Put_center_info_2:Put_center_info_2+6]
                                                        Find_center_info4=Find_center_info[Put_center_info_2:Put_center_info_2+5]
                                                        Find_center_info3=Find_center_info[Put_center_info_3:Put_center_info_3+5]
                                                        Find_center_info5=Find_center_info[Put_center_info_5:Put_center_info_5+6]

                                                        #0-6,6-12,12-18,18-24,24-30;30*6=180;5*6=30
                                                        
                                                        if Find_center_info4=="00101" and Find_center_info3!="111111" and Find_center_info1!="000000":
                                                            
                                                            
                                                            
                                                            Find_center_info=Find_center_info[:Put_center_info_2]+Find_center_info[Put_center_info_2+5:]
                                                            Find_center_top=Find_center_top+"011111"
                                                            Center_top_two_blocks=1
                                                            
                                                            
                                                        elif Find_center_info4!="00101" and Find_center_info3=="11111" and Find_center_info1!="000000":     
                                                        
                                                            
                                                            
                                                            Find_center_info=Find_center_info[:Put_center_info_3]+Find_center_info[Put_center_info_3+5:]
                                                            Find_center_top=Find_center_top+"000000"
                                                            Center_top_two_blocks=1
                   
                                                            
                                                        elif Find_center_info4!="00101" and Find_center_info3!="11111" and Find_center_info1=="000000":
                                                        

                                                            
                                                          
                                                            Find_center_info=Find_center_info[:Put_center_info_2]+Find_center_info[Put_center_info_2+6:]
                                                            Find_center_top=Find_center_top+"000101"
                                                            Center_top_two_blocks=1
                                                            
                                                            
                                                        
                                                        elif Find_center_info4=="00101" and Find_center_info3=="11111":
                                                                compress_or_not_compress=2

                                                                Find_center_info=Find_center_info[:Put_center_info_2]+Find_center_info[Put_center_info_2+5:]
                                                                Find_center_info=Find_center_info[:Put_center_info_3]+Find_center_info[Put_center_info_3+5:]
                                                                Find_center_top=Find_center_top+"1000101"
                                                                
                                                        elif Find_center_info4=="00101" and Find_center_info1=="00000":
                                                                compress_or_not_compress=2

                                                                Find_center_info=Find_center_info[:Put_center_info_2]+Find_center_info[Put_center_info_2+5:]
                                                                Find_center_info=Find_center_info[:Put_center_info_3]+Find_center_info[Put_center_info_2+5:]
                                                                Find_center_top=Find_center_top+"1100101"
                                                                   
                                                        else:
                                                            
                                                            
                                                                
                                                            
                                                            Find_center_info=Find_center_info[:Put_center_info_5]+Find_center_info[Put_center_info_5+6:]
                                                            Find_center_top=Find_center_top+Find_center_info5
                                                            
                                                            
                                                             
                                                        Put_center_info=Put_center_info+(6*30)
                                                        block=Put_center_info
                                                        
                                                 
                                    
                                     
                                    center_top=len(Find_center_top)
                                          
                                    long_top_comperession=bin(center_top)[2:]
                                    lenf=len(long_top_comperession)

                                    add_bits7=""
                                    count_bits=32-lenf%32
                                    z=0
                                    if count_bits!=0:
                                        if count_bits!=32:
                                                while z<count_bits:
                                                    add_bits7="0"+add_bits7
                                                    z=z+1

                                    center_top1=len(Find_center_top1)
                                          
                                     
                                          
                                    Equal_info_between_of_the_cirlce_of_the_file_17=add_bits7+long_top_comperession+Find_center_top+Find_center_info
                                    lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    #print(lenfS)
                                    
                                    if lenf6<=lenfS:
                                        Deep3=lenfS
                                    
                                    if compress_or_not_compress==2 and Circle_times2==0:
                                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[1:]
                                    
                                   
                                    Circle_times2=Circle_times2+1
                          
                                    Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file_17
                                    

                                    
                                    if compress_or_not_compress==2:
                                            
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file
                                   
                                    
                                    if   lenfS<=Deep3 or compress_or_not_compress==2:
                                        Circle_times3=Circle_times2
                                        
                                        if compress_or_not_compress==2:
                                        	Circle_times3=Circle_times2-1

                                    

                                    
                                   
                                    Circle_times2=Circle_times2+1
                                    
                                    if   lenfS<=Deep3 or compress_or_not_compress==2:
                                    	   
                                            Times_comperession=bin(Circle_times3)[2:]
                                            lenf=len(Times_comperession)

                                            add_bits7=""
                                            count_bits=8-lenf%8
                                            z=0
                                            if count_bits!=0:
                                                if count_bits!=8:
                                                        while z<count_bits:
                                                         	add_bits7="0"+add_bits7
                                                         	z=z+1    
                                    

                                    if   lenfS<=Deep3 or compress_or_not_compress==2:
                                                Equal_info_between_of_the_cirlce_of_the_file_17="1"+Equal_info_between_of_the_cirlce_of_the_file_17
                                                lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                add_bits=""
                                                count_bits=8-lenf%8
                                                if count_bits==8:
                                                	count_bits=0
                                                count_bits2=count_bits
                                                z=0
                                                if count_bits!=0:
                                                        if count_bits!=8:
                                                                while z<count_bits:
                                                                        add_bits="0"+add_bits
                                                                        z=z+1

                                   

                                    if   lenfS<=Deep3 or compress_or_not_compress==2:
                                            lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)                                           
                                            Equal_info_between_of_the_cirlce_of_the_file_17=add_bits7+Times_comperession+add_bits+Equal_info_between_of_the_cirlce_of_the_file_17

                                    if   lenfS<=Deep3 or compress_or_not_compress==2:
                                                
                                    		L=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    		n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)
                                    		width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    		width_bits=(width_bits//8)*2
                                    		width_bits=str(width_bits)
                                    		width_bits="%0"+width_bits+"x"
                                    		width_bits3=binascii.unhexlify(width_bits % n)
                                    		width_bits2=len(width_bits3)
                                    		add_bitszzza=""
                                    		add_bitszs=""
                                    		Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                    		
                                    		with open(nameas, "wb") as f2:
                                    			f2.write(width_bits3)
                                    	
                                    		x2 = time()
                                    		x3=x2-x
                                    		xs=float(x3)
                                    		return print(x3)
                                    		
                                if i==2:

                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                              
                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                    
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)

                                    add_bits=""

                                    Times_6=""

                                    #Extract

                                    sda10=""
                                    Translate_info_Decimal=""
                                  
                                    Number_add_plus_one=""
                                    Prime_Not=""
                                    Times_6=""
                                
                                    Number_of_the_file=0
                                    Prime_Not=0
                                 
                                    if C==1 and Circle_times2==0:
                                        Times_6=Equal_info_between_of_the_cirlce_of_the_file[0:8]
                                        T = int(Times_6, 2)
                                        Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[8:]

                                        if Equal_info_between_of_the_cirlce_of_the_file[0:1]=="1":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[1:]
                                        
                                        elif Equal_info_between_of_the_cirlce_of_the_file[0:2]=="01":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[2:]
                                                
                                        elif Equal_info_between_of_the_cirlce_of_the_file[0:3]=="001":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[3:]


                                        elif Equal_info_between_of_the_cirlce_of_the_file[0:4]=="0001":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[4:]

                                        elif Equal_info_between_of_the_cirlce_of_the_file[0:5]=="00001":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[5:]

                                        elif Equal_info_between_of_the_cirlce_of_the_file[0:6]=="000001":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[6:]
                                        elif Equal_info_between_of_the_cirlce_of_the_file[0:7]=="0000001":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[7:]
    
                                        elif Equal_info_between_of_the_cirlce_of_the_file[0:8]=="00000001":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[8:]
                                        
                                        elif Equal_info_between_of_the_cirlce_of_the_file[0:9]=="000000001":
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[9:]
    
                                        if C==1 and T!=0:
                                            
                                                    Top_center=Equal_info_between_of_the_cirlce_of_the_file[0:32]
                                                    Top = int(Times_6, 2)
                                                    Top_center=Top_center[32:]
                                                    Top_center2=Top_center[:Top]
                                                    Equal_info_between_of_the_cirlce_of_the_file=Top_center2
                                                    
                                                    Equal_info_between_of_the_cirlce_of_the_file1=Top_center[Top:]
                                                    
                                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file
                                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)

                                                    Find_center_info=Equal_info_between_of_the_cirlce_of_the_file

                                                    Put_center_info=0
                                                 
                                                    block=0
                                                    while block!=Top:
                                                        Find_center_info1=Find_center_info[block:block+6]
                                                        Find_center_info3=Find_center_info[block:block+6]
                                                        
                                                        Find_center_info2=Find_center_info[block:block+6]
                                                        Find_center_info4=Find_center_info[block:block+7]

                                                        #0-6,6-12,12-18,18-24,24-30;30*6=180;5*6=30
                                                        
                                                        if Find_center_info1=="011111":
                                                            
                                                            Put_center_info_2=Put_center_info+24
                                                            
                                                            Equal_info_between_of_the_cirlce_of_the_file1=Equal_info_between_of_the_cirlce_of_the_file1[:Put_center_info_2]+"00101"+Equal_info_between_of_the_cirlce_of_the_file1[Put_center_info_2:]
                                                            Put_center_info=Put_center_info+((6*30)-6)
                                                            
                                                            block=block+6
                                                            
                                                        elif Find_center_info1=="000000":
                                                            
                                                            Put_center_info_2=Put_center_info
                                                            Equal_info_between_of_the_cirlce_of_the_file1=Equal_info_between_of_the_cirlce_of_the_file1[:Put_center_info_2]+"11111"+Equal_info_between_of_the_cirlce_of_the_file1[Put_center_info_2:]
                                                            Put_center_info=Put_center_info+((6*30)-6)
                   
                                                            block=block+6
                                                
                                                        elif Find_center_info2=="000101":

                                                            Put_center_info_2=Put_center_info+24
                                                          
                                                            Equal_info_between_of_the_cirlce_of_the_file1=Equal_info_between_of_the_cirlce_of_the_file1[:Put_center_info_2]+"000000"+Equal_info_between_of_the_cirlce_of_the_file1[Put_center_info_2:]
                                                            
                                                            Put_center_info=Put_center_info+((6*30)-6)
                                                            
                                                        
                                                            block=block+6

                                                        elif Find_center_info4=="1000101":

                                                                Put_center_info_2=Put_center_info+24-5
                                                            
                                                                Equal_info_between_of_the_cirlce_of_the_file1=Equal_info_between_of_the_cirlce_of_the_file1[:Put_center_info_2]+"00101"+Equal_info_between_of_the_cirlce_of_the_file1[Put_center_info_2:]
                                                                Put_center_info_2=Put_center_info
                                                                Equal_info_between_of_the_cirlce_of_the_file1=Equal_info_between_of_the_cirlce_of_the_file1[:Put_center_info_2]+"11111"+Equal_info_between_of_the_cirlce_of_the_file1[Put_center_info_2:]
                                                                Put_center_info=Put_center_info+((6*30)-7)
                                                                block=block+7
                                                        elif Find_center_info4=="1100101":

                                                                Put_center_info_2=Put_center_info+24-6
                                                            
                                                                Equal_info_between_of_the_cirlce_of_the_file1=Equal_info_between_of_the_cirlce_of_the_file1[:Put_center_info_2]+"00101"+Equal_info_between_of_the_cirlce_of_the_file1[Put_center_info_2:]
                                                                Put_center_info_2=Put_center_info
                                                                Equal_info_between_of_the_cirlce_of_the_file1=Equal_info_between_of_the_cirlce_of_the_file1[:Put_center_info_2]+"000000"+Equal_info_between_of_the_cirlce_of_the_file1[Put_center_info_2:]
                                                                Put_center_info=Put_center_info+((6*30)-7)
                                                            
                                                                block=block+7                                                                                                                           
                                                            
                                                        else:
                                                            Put_center_info_2=Put_center_info
                                                            Equal_info_between_of_the_cirlce_of_the_file1=Equal_info_between_of_the_cirlce_of_the_file1[:Put_center_info_2]+Find_center_info1+Equal_info_between_of_the_cirlce_of_the_file1[Put_center_info_2:]
                                                            Put_center_info=Put_center_info+((6*30)-6)
                                                            
                                                            block=block+6
                                                             
                                                    
                                                        
                                                 
                                                    Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file1
                                                    lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                    
                                                     
                                                
                                       
                                    Times_6=Number_add_plus_one
                                    Number_add_plus_one=""
                                      
                                    #####################################################################################################################################################
                                   
                                    Prime_Not=""
                                    
                                    
                                    
                                     
                                    Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file_17
                                   

                                    if i==2:
                                        Make_togher=""
                                        Make_togher=Times_6
                                        Number_add_plus_one=""
                                        add_bits=""
                                        if C==1 and T!=0:
                                                Circle_times2=Circle_times2+1

                                        lenf9=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                        #print(Circle_times2)
                                        
                                        
                                        if  Circle_times2==T:
                                        	   
                                            if C==1 and T==0:
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file
                                            	lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	add_bits=""
                                            	count_bits=8-lenf%8
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=8:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                        
                                            if C==1 and T!=0:
 
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_17[1:]
                                            	lenf14=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	#print(lenf14)
                                            	
                                            		
                                            	
                                            	lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	add_bits=""
                                            	count_bits=8-lenf%8
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=8:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17

                                            L=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                         
                                            n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)
                                            width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            width_bits=(width_bits//8)*2
                                            width_bits=str(width_bits)
                                            width_bits="%0"+width_bits+"x"
                                            width_bits3=binascii.unhexlify(width_bits % n)
                                            width_bits2=len(width_bits3)

                                            add_bitszzza=""
                                            add_bitszs=""
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                             
                                            with open(nameas, "wb") as f2:
                                            
                                              
                                            	f2.write(width_bits3)
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            return print(x3)
   
d=compression()

xw1=d.cryptograpy_compression4()
print(xw1)
