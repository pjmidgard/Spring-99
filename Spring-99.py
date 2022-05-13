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

                        
                        Deep=1        
                        Deep7=float("1.3331001")
                                
                        Deep3=8
                        print(Deep7)
                        
                        count_bits2=0
                        Self=0
                        Cut=0
                        i=1

                    if namez=="e":

                        Deep=1        
                        Deep7=float("1.3331001")
                                
                        Deep3=8
                        print(Deep7)
                        
                        count_bits2=0
                        Self=0
                        Cut=0
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

                        elif nameas[nac-7:nac]==".bin":
                                nameas=name[:nac-7]
                                nac=len(nameas)
                                C=2
                                
                   
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
                        if lenf7==0:
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
                                if i==1:
                                    if lenf7>=(2**40)-1:
                                        raise SystemExit

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


                                    
                 
                                    if   Circle_times2==0 and SpinS==0:
                                        Check_info=Equal_info_between_of_the_cirlce_of_the_file
                                        Equal_info_between_of_the_cirlce_of_the_file="1"+Equal_info_between_of_the_cirlce_of_the_file+Equal_info_between_of_the_cirlce_of_the_file+Equal_info_between_of_the_cirlce_of_the_file
                                        SpinS=1
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                    if Circle_times2>=(2**48)-3:
                                            compress_or_not_compress=2
                                            
                                    Number_of_the_file = int(Equal_info_between_of_the_cirlce_of_the_file, 2)

                                    Number_of_the_file1=Number_of_the_file*Number_of_the_file

                                    Number_of_the_file2=str(Number_of_the_file1)

                                    Number_of_the_file3=len(Number_of_the_file2)
                                    #print(Number_of_the_file3)

                                    Number_of_the_file4=int(Number_of_the_file3//Deep7)
                                
                                    #print(Number_of_the_file4)

                                    Number_of_the_file5=Number_of_the_file2[Number_of_the_file4:]+Number_of_the_file2[:Number_of_the_file3-Number_of_the_file4]
                                    Number_of_the_file7=len(Number_of_the_file5)
                                    #print(Number_of_the_file7)

                                    Number_of_the_file6=int(Number_of_the_file5)
                                    
                                    
                                    
                                    
                                    Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file6)[2:]
                                    
                                            #print(len(Equal_info_between_of_the_cirlce_of_the_file_17))
                              
                                    
                                    lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    #print(lenfS)

                                    if lenfS>=lenf6:
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


                                    if   lenfS<=Deep3 or compress_or_not_compress==2:
                                    	   
                                            Equal_info_between_of_the_cirlce_of_the_file0=bin(lenf7)[2:]
                                            lenf=len(Equal_info_between_of_the_cirlce_of_the_file0)

                                            add_bits8=""
                                            count_bits=48-lenf%48
                                            z=0
                                            if count_bits!=0:
                                                if count_bits!=48:
                                                        while z<count_bits:
                                                         	add_bits8="0"+add_bits8
                                                         	z=z+1
                                                
                                    if   lenfS<=Deep3 or compress_or_not_compress==2:
                                    	   
                                            Equal_info_between_of_the_cirlce_of_the_file_29=bin(Circle_times3)[2:]
                                            lenf=len(Equal_info_between_of_the_cirlce_of_the_file_29)

                                            add_bits7=""
                                            count_bits=48-lenf%48
                                            z=0
                                            if count_bits!=0:
                                                if count_bits!=48:
                                                        while z<count_bits:
                                                         	add_bits7="0"+add_bits7
                                                         	z=z+1
                                            		

                                    if   lenfS<=Deep3 or compress_or_not_compress==2:

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
                                    	   


                                            Equal_info_between_of_the_cirlce_of_the_file1=bin(count_bits2)[2:]
                                            lenf=len(Equal_info_between_of_the_cirlce_of_the_file1)

                                            add_bits9=""
                                            count_bits=8-lenf%8
                                            z=0
                                            if count_bits!=0:
                                                if count_bits!=8:
                                                        while z<count_bits:
                                                         	add_bits9="0"+add_bits9
                                                         	z=z+1       

                                    if   lenfS<=Deep3 or compress_or_not_compress==2:
                                            lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)                                           
                                            Equal_info_between_of_the_cirlce_of_the_file_17=add_bits9+Equal_info_between_of_the_cirlce_of_the_file1+add_bits8+Equal_info_between_of_the_cirlce_of_the_file0+add_bits7+Equal_info_between_of_the_cirlce_of_the_file_29+add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                    if   lenfS<=Deep3 or compress_or_not_compress==2:
                                            Equal_info_between_of_the_cirlce_of_the_file_19=Equal_info_between_of_the_cirlce_of_the_file_17

                                    if   lenfS<=Deep3 or compress_or_not_compress==2:

                                                                    

                                                                    Circle_times2=0
                                                                    C=1
                                                              
                                                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_17
                                                                    
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
                                                                 
                                                                    if C==1:
                                                                        if   Circle_times2==0 and Self==0:
                                                                                
                                                                                
                                                                                Translate_info_Decimal=Equal_info_between_of_the_cirlce_of_the_file[0:8]
                                                                                Translate_info_Decimal_2 = int(Translate_info_Decimal, 2)
                                                                                if Translate_info_Decimal_2>7:
                                                                                        Corrupted=1
                                                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[8:]
                                                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)

                                                                                sda10=Equal_info_between_of_the_cirlce_of_the_file[0:48]
                                                                                File_size = int(sda10, 2)
                                                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[48:]
                                                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                                                
                                                                                
                                                                                Times_6=Equal_info_between_of_the_cirlce_of_the_file[0:48]
                                                                                T = int(Times_6, 2)
                                                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[48:]
                                                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                                                Check_file=Equal_info_between_of_the_cirlce_of_the_file[Translate_info_Decimal_2:]
                                                                                lert=len(Check_file)
                                                                                File_size=File_size*8
                                                                                #print(File_size)
                                                                                
                                                                                
                                                                                Self=1
                                                                        if   Circle_times2==0:
                                                                                SpinS=0
                                                                                Equal_info_between_of_the_cirlce_of_the_file1=bin(count_bits2)[2: ]
                                                                                lenf=len(Equal_info_between_of_the_cirlce_of_the_file1)
                                                                                

                                                                                add_bits9=""
                                                                                count_bits=File_size-lenf%File_size
                                                                                z=0
                                                                                if count_bits!=0:
                                                                                        if count_bits!=File_size:
                                                                                                while z<count_bits:
                                                                                                        add_bits9="0"+add_bits9
                                                                                                        z=z+1



                                                                                Equal_info_between_of_the_cirlce_of_the_file_17=""
                                                                                
                                                                                Equal_info_between_of_the_cirlce_of_the_file=add_bits9+Equal_info_between_of_the_cirlce_of_the_file1
                                                                                Equal_info_between_of_the_cirlce_of_the_file3=add_bits9+Equal_info_between_of_the_cirlce_of_the_file1
                                                                                
                                                                                
                                                                                #print(count_bits2)
                                                 
                                                                                if   Circle_times2==0 and SpinS==0:
                                                                                        Equal_info_between_of_the_cirlce_of_the_file="1"+Equal_info_between_of_the_cirlce_of_the_file+Equal_info_between_of_the_cirlce_of_the_file+Equal_info_between_of_the_cirlce_of_the_file
                                                                                        SpinS=1
                                                                                
                                                                        if   Circle_times2>0:
                                                                                Translate_info_Decimal_2=0
                                                                                
                                                                        
                                                                                
                                    
                                                                        if C==1 and T!=0:
                                                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file
                                                                                
                                                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                                                #print(lenf6)

                                                                                


                                                                            
                                                                                if Circle_times2>=(2**48)-3:
                                                                                        compress_or_not_compress=2
                                                                                            
                                                                                Number_of_the_file = int(Equal_info_between_of_the_cirlce_of_the_file, 2)

                                                                                Number_of_the_file1=Number_of_the_file*Number_of_the_file

                                                                                Number_of_the_file2=str(Number_of_the_file1)

                                                                                Number_of_the_file3=len(Number_of_the_file2)
                                                                                #print(Number_of_the_file3)

                                                                                Number_of_the_file4=int(Number_of_the_file3//Deep7)
                                                                                
                                                                                #print(Number_of_the_file4)

                                                                                Number_of_the_file5=Number_of_the_file2[Number_of_the_file4:]+Number_of_the_file2[:Number_of_the_file3-Number_of_the_file4]
                                                                                Number_of_the_file7=len(Number_of_the_file5)
                                                                                #print(Number_of_the_file7)

                                                                                Number_of_the_file6=int(Number_of_the_file5)
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file6)[2:]
                                                                                    
                                                                                #print(len(Equal_info_between_of_the_cirlce_of_the_file_17))
                                                                              
                                                                                    
                                                                                lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                                                #print(lenfS)

                                                                               
                                                                               
                                                                                
                                                                    Times_6=Number_add_plus_one
                                                                    Number_add_plus_one=""
                                                                      
                                                                    #####################################################################################################################################################
                                                                   
                                                                    Prime_Not=""
                                                                    
                                                                    
                                                                    
                                                                     
                                                                    Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file_17
                                                                   

                                                                    if i==1:
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
                                                                                count_bits=File_size-lenf%File_size
                                                                                z=0
                                                                                if count_bits!=0:
                                                                                        if count_bits!=File_size:
                                                                                            while z<count_bits:
                                                                                                add_bits="0"+add_bits
                                                                                                z=z+1
                                                                                Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                                                        
                                                                            if C==1 and T!=0:
                                                                                    
                                                                                Circle_times2=0
                                                                                
                                                                                File_Minus_Size=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                                                Equal_info_between_of_the_cirlce_of_the_file_18=Equal_info_between_of_the_cirlce_of_the_file_17
                                                                                
                                   
                                                                                lenfg=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                                                #print(Equal_info_between_of_the_cirlce_of_the_file_18)
                                                                                #print(Check_file)
                                                                            
                                                                               
                                                                                #print(File_Minus_Size)
                                                                                
                                                                                    
                                                                                count_bits2=count_bits2+1

                                                   
                                                        
                                    if   lenfS<=Deep3 or compress_or_not_compress==2 and Check_file==Equal_info_between_of_the_cirlce_of_the_file_18:
                                                        Long_Cut=len(Equal_info_between_of_the_cirlce_of_the_file3)
                                                        #print(File_size)
                                                        #print(Long_Cut)
                                                        Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file3[Long_Cut-File_size:]
                                                        Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file3
                                                        lenf14=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                        Cut=1
                                                        #print(Check_file)
                                                        #print(lenf14)
                                                   
                                                        
                                                                
                                                    	
                                    if   lenfS<=Deep3 or compress_or_not_compress==2 and Check_info==Equal_info_between_of_the_cirlce_of_the_file3:
                                            
                                                
                                    		
                                    		Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_19
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

                                    if   lenfS<=Deep3 or compress_or_not_compress==2 and Check_info!=Equal_info_between_of_the_cirlce_of_the_file3:
                                                Equal_info_between_of_the_cirlce_of_the_file_17=Check_info
                                    if   lenfS<=Deep3 or compress_or_not_compress==2 and Check_info!=Equal_info_between_of_the_cirlce_of_the_file3:             
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

                                    		nameas=nameas+".b2"
                                    		
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

                                    if C==2:
                                                
                                            	
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file
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
                                            
                                 
                                    if C==1:
                                        if   Circle_times2==0 and Self==0:
                                                
                                                
                                                Translate_info_Decimal=Equal_info_between_of_the_cirlce_of_the_file[0:8]
                                                Translate_info_Decimal_2 = int(Translate_info_Decimal, 2)
                                                if Translate_info_Decimal_2>7:
                                                        Corrupted=1
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[8:]
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)

                                                sda10=Equal_info_between_of_the_cirlce_of_the_file[0:48]
                                                File_size = int(sda10, 2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[48:]
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                
                                                
                                                Times_6=Equal_info_between_of_the_cirlce_of_the_file[0:48]
                                                T = int(Times_6, 2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[48:]
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                Check_file=Equal_info_between_of_the_cirlce_of_the_file[Translate_info_Decimal_2:]
                                                lert=len(Check_file)
                                                File_size=File_size*8
                                                #print(File_size)
                                                
                                                
                                                Self=1
                                        if   Circle_times2==0:
                                                SpinS=0
                                                Equal_info_between_of_the_cirlce_of_the_file1=bin(count_bits2)[2: ]
                                                lenf=len(Equal_info_between_of_the_cirlce_of_the_file1)
                                                

                                                add_bits9=""
                                                count_bits=File_size-lenf%File_size
                                                z=0
                                                if count_bits!=0:
                                                        if count_bits!=File_size:
                                                                while z<count_bits:
                                                                        add_bits9="0"+add_bits9
                                                                        z=z+1



                                                Equal_info_between_of_the_cirlce_of_the_file_17=""
                                                
                                                Equal_info_between_of_the_cirlce_of_the_file=add_bits9+Equal_info_between_of_the_cirlce_of_the_file1
                                                Equal_info_between_of_the_cirlce_of_the_file3=add_bits9+Equal_info_between_of_the_cirlce_of_the_file1
                                                
                                                
                                                #print(count_bits2)
                 
                                                if   Circle_times2==0 and SpinS==0:
                                                        Equal_info_between_of_the_cirlce_of_the_file="1"+Equal_info_between_of_the_cirlce_of_the_file+Equal_info_between_of_the_cirlce_of_the_file+Equal_info_between_of_the_cirlce_of_the_file
                                                        SpinS=1
                                                
                                        if   Circle_times2>0:
                                        	Translate_info_Decimal_2=0
                                        	
                                        
                                        	
    
                                        if C==1 and T!=0:
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file
                                                
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                #print(lenf6)

                                                


                                            
                                                if Circle_times2>=(2**48)-3:
                                                        compress_or_not_compress=2
                                                            
                                                Number_of_the_file = int(Equal_info_between_of_the_cirlce_of_the_file, 2)

                                                Number_of_the_file1=Number_of_the_file*Number_of_the_file

                                                Number_of_the_file2=str(Number_of_the_file1)

                                                Number_of_the_file3=len(Number_of_the_file2)
                                                #print(Number_of_the_file3)

                                                Number_of_the_file4=int(Number_of_the_file3//Deep7)
                                                
                                                #print(Number_of_the_file4)

                                                Number_of_the_file5=Number_of_the_file2[Number_of_the_file4:]+Number_of_the_file2[:Number_of_the_file3-Number_of_the_file4]
                                                Number_of_the_file7=len(Number_of_the_file5)
                                                #print(Number_of_the_file7)

                                                Number_of_the_file6=int(Number_of_the_file5)
                                                    
                                                    
                                                    
                                                    
                                                Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file6)[2:]
                                                    
                                                #print(len(Equal_info_between_of_the_cirlce_of_the_file_17))
                                              
                                                    
                                                lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                #print(lenfS)

                                               
                                               
                                                
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
                                            	count_bits=File_size-lenf%File_size
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=File_size:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                        
                                            if C==1 and T!=0:
                                                    
                                                Circle_times2=0
                                                
                                                File_Minus_Size=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                Equal_info_between_of_the_cirlce_of_the_file_18=Equal_info_between_of_the_cirlce_of_the_file_17
                                                
   
                                                lenfg=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                #print(Equal_info_between_of_the_cirlce_of_the_file_18)
                                                #print(Check_file)
                                            
                                               
                                                #print(File_Minus_Size)
                                                
                                                    
                                                count_bits2=count_bits2+1

                                            if C==1 and T!=0 and Check_file==Equal_info_between_of_the_cirlce_of_the_file_18:
                                            	
                                      	
                                                Long_Cut=len(Equal_info_between_of_the_cirlce_of_the_file3)
                                                #print(File_size)
                                                #print(Long_Cut)
                                                Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file3[Long_Cut-File_size:]
                                                Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file3
                                                lenf14=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                Cut=1
                                            	#print(Check_file)
                                            	#print(lenf14)
                                           
                                            	
                                            		
                                            if C==1 and T!=0 and Check_file==Equal_info_between_of_the_cirlce_of_the_file_18 and Cut==1:	
                                            	lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	add_bits=""
                                            	count_bits=File_size-lenf%File_size
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=File_size:
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
