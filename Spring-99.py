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

                        Deep3=160

                        i=1

                    if namez=="e":
                        i=2
                        Deep3=160
                 
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
                    Size_of_file1=""

                    Translate_info_Decimal=""
                    Number_of_the_file1=0

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
                        if i==2:
                                   import zstd
                                   data=zstd.decompress(data)
                        
      
                        s=str(data)

                        lenf1=len(data)
                        lenf7=len(data)
                        if lenf7>(2**32)-1:
                        	 raise SystemExit
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
                                    	Equal_info_between_of_the_cirlce_of_the_file="1"+Equal_info_between_of_the_cirlce_of_the_file
                                    	SpinS=1

                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)	

                                    if Circle_times2>=(2**48)-1:
                                            compress_or_not_compress=2
                                            
                                    Number_of_the_file = int(Equal_info_between_of_the_cirlce_of_the_file, 2)

                                    Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    
                                    Number_of_the_file=Number_of_the_file-(2**(lenf6-1)-1)
                                    
                                            
                                                   
                                    Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                    Equal_info_between_of_the_cirlce_of_the_file_18=Equal_info_between_of_the_cirlce_of_the_file_17
                                    
                                                        
                                    add_bits19=""
                                    Block=lenf6-1
                                    H=1
                                    C=1 
                                    if C==1:    
                                        count_bits=(Block)-lenf
                                        z=0
                                        if count_bits!=0:
                                            if count_bits!=Block-1:
                                                    while z<count_bits:
                                                            if z==0:
                                                                add_bits19="1"+add_bits19
                                                            if z>=1:
                                                                add_bits19="1"+add_bits19
                                                                
                                                                
                                                            
                                                            z=z+1
                                                            H=1
                                                            
                                                                   
                                    Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_18+add_bits19
                                 
                                    #print(add_bits19)
                                    
                                    lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    #print(lenfS)
                                    if lenfS==(lenf7*8)-90:
                                        Deep3=lenfS
                                    
                                    if H==1 and z>2:
                                        compress_or_not_compress=2
                                        
                                    if H==1 and z==2:
                                    
                                         Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_18+"10"
                                         lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    if H==1 and z==0:
                                         Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_18+"00"
                                         lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                       
                                    if compress_or_not_compress==1:
                                    		nameas=name+".bin"
                                    
                                    if Number_of_the_file<0:
                                                        compress_or_not_compress=2
                                                    
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
                                            
                                            Equal_info_between_of_the_cirlce_of_the_file_17=add_bits7+Equal_info_between_of_the_cirlce_of_the_file_29+add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                            

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
                                    			import zstd
                                    			width_bits3=zstd.compress(width_bits3)
                                    			f2.write(width_bits3)
                                    	
                                    		x2 = time()
                                    		x3=x2-x
                                    		xs=float(x3)
                                    		return print(x3)
                                    		
                                if i==2:

                                        
                            
                                    lenf5=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                    

                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                    Equal_info_between_of_the_cirlce_of_the_file_check=Equal_info_between_of_the_cirlce_of_the_file_2
                                 
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
                                    #print(Number_of_the_file1)
                                    

                                    Equal_info_between_of_the_cirlce_of_the_file=bin(Number_of_the_file1)[2:]
                 
                                    if   Circle_times2==0 and SpinS==0:
                                    	Equal_info_between_of_the_cirlce_of_the_file="1"+Equal_info_between_of_the_cirlce_of_the_file
                                    	SpinS=1

                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)	

                                    if Circle_times2>=(2**48)-1:
                                            compress_or_not_compress=2
                                            
                                    Number_of_the_file = int(Equal_info_between_of_the_cirlce_of_the_file, 2)

                                    Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    
                                    Number_of_the_file=Number_of_the_file-(2**(lenf6-1)-1)
                                    
                                            
                                                   
                                    Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                    Equal_info_between_of_the_cirlce_of_the_file_18=Equal_info_between_of_the_cirlce_of_the_file_17
                                    
                                                        
                                    add_bits19=""
                                    Block=lenf6-1
                                    H=1
                                    C=1 
                                    if C==1:    
                                        count_bits=(Block)-lenf
                                        z=0
                                        if count_bits!=0:
                                            if count_bits!=Block-1:
                                                    while z<count_bits:
                                                            if z==0:
                                                                add_bits19="1"+add_bits19
                                                            if z>=1:
                                                                add_bits19="1"+add_bits19
                                                                
                                                                
                                                            
                                                            z=z+1
                                                            H=1
                                                            
                                                                   
                                    Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_18+add_bits19
                                 
                                    #print(add_bits19)
                                    
                                    lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    #print(lenfS)
                                    if lenfS==(lenf7*8)-90:
                                        Deep3=lenfS
                                    
                                    if H==1 and z>2:
                                        compress_or_not_compress=2
                                        
                                    if H==1 and z==2:
                                    
                                         Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_18+"10"
                                         lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    if H==1 and z==0:
                                         Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_18+"00"
                                         lenfS=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                       
                                    if compress_or_not_compress==1:
                                    		nameas=name+".bin"
                                    
                                    if Number_of_the_file<0:
                                                        compress_or_not_compress=2
                                                    
                                    if compress_or_not_compress==2 and Circle_times2==0:
                                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[1:]
                                    
                                   
                                    Circle_times2=Circle_times2+1
                          
                                    Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file_17
                                    

                                    
                                    if compress_or_not_compress==2:
                                            
                                            Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file

                                    Number_of_the_file1=Number_of_the_file1+1

                                   
                                    
                                    if  compress_or_not_compress==2:
                                        Circle_times3=Circle_times2
                                        
                                        if compress_or_not_compress==2:
                                        	Circle_times3=Circle_times2-1
                                        	
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
                                            
                                            Equal_info_between_of_the_cirlce_of_the_file_17=add_bits7+Equal_info_between_of_the_cirlce_of_the_file_29+add_bits+Equal_info_between_of_the_cirlce_of_the_file_17

                                            Number_of_the_file=Number_of_the_file+1
                                            Circle_times2=0

                                            if Equal_info_between_of_the_cirlce_of_the_file_17[1:]==Equal_info_between_of_the_cirlce_of_the_file_check:
                                                    compress_or_not_compress=3

                                            if  compress_or_not_compress==3:

                                                        Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file1
                                                        
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
                                                        
                                                        
                                                
                                                        x2 = time()
                                                        x3=x2-x
                                                        xs=float(x3)
                                                        return print(x3)
           
d=compression()

xw1=d.cryptograpy_compression4()
print(xw1)
