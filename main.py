from csv import writer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("-----------------------------------------------------------")
print(" STUDENT MANAGEMENT SYSTEM")  #MADE BY HEEBA
print("-----------------------------------------------------------")
while True:
    mainmenu='''1. View Students Detail
    \n2. Submit/Delete student detail
    \n3. Analysis
		(i).   Top record
    \n 		(ii).  Bottom Records
    \n 		(iii). To print particular column
    \n 		(iv).  To print multiple columns
    \n 		(v).   To display complete statistics of the dataframe
    \n 		(vi).  To display complete information about dataframe
    \n 		(vii). To display the unique values of the columns
    \n 		(viii).To apply and display the data group by with count function
    \n		(ix).  To apply and display the data using group by with more functions
    \n 		(x).   To applying aggregate function
    \n4. Visualization
    
    \n5. Exit'''
    print(mainmenu)
    ch=int(input("Enter your choice"))
    if ch==1:
        print('''1. View student Schedule
        \n2. Press enter to go back''')
        chone=int(input("Enter your choice"))
        if chone==1:
            df=pd.read_csv("C:\\Users\\mpc\\Desktop\\student.csv")
            print(df)
            print("File Reterived Sucessfully!!!!")
        elif chone==2:
            pass
    elif ch==2:
        print('''\n1. Insert\n
        2. Enter to go back''')
        mcf=int(input("Enter your choice"))
        df=pd.read_csv("C:\\Users\\mpc\\Desktop\\student.csv")
        if mcf==1:
            col=df.columns
            print(col)
            print(df.head(1))
            j=0
            ninsert=[]
            for i in col:
                print("Enter ", col[j], " value")
                nval=input()
                ninsert.append(nval)
                j=j+1
                print(ninsert)
            with open("C:\\Users\\mpc\\Desktop\\student.csv","a") as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(ninsert)
                f_object.close()
            print("New row inserted")
    elif ch==3:											
        print("View Analysis of student")
        df=pd.read_csv("C:\\Users\\mpc\\Desktop\\student.csv")
        menu=''' 1. Top record
    \n 2. Bottom Records
    \n 3. To print particular column
    \n 4. To print multiple columns
    \n 5. To display complete statitics of the dataframe
    \n 6. To display complte information about dataframe
    \n 7. To display the unique values of the columns
    \n 8. To apply and display the data group by with count function
    \n 9. To apply and display the data using group by with more functions
    \n 10.To appying aggregate function
    \n Press enter to go back'''
        print(menu)
        ch3=int(input("Enter your choice"))
        if ch3==1:
            n=int(input("Enter the number of top rows you want to view"))
            print("Top ", n," records from the dataframe")
            print(df.head(n))
        elif ch3==2:
            n=int(input("Enter the number of records you want to view"))
            print("Bottom", n," records from the dataframe")
            print(df.tail(n))
        elif ch3==3:
            print("Name of the Columns\n", df.columns)
            co=input("Enter Column Name to be displayed")
            print(df[co])
        elif ch3==4:
            print("Name of the Columns\n", df.columns)
            co=eval(input("Enter Column Name in the square brackets as a list "))
            print(df[co])
        elif ch3==5:
            print("Complete Statistics")
            print(df.describe())
        elif ch3==6:
            print("Information about DataFrame")
            print(df.info());
        elif ch3==7:
            print("Displaying unique values of any column")
            print("Name of the Columns\n" ,df.columns)
            co=input("Enter Column Name to be displayed1")
            print("Distinct values of column ",co," are")
            print(df[co].unique(),sep='\n')
        elif ch3==8:
            print("Name of the Columns\n" ,df.columns)
            co=eval(input("Enter Column Name in the square brackets as a list "))
            print(df[co])
            col=input("Enter the column name to be displayed")
            print("Grouped Column ",col)
            dfgroup=df[co].groupby(col).count()
            print(dfgroup)
        elif ch3==9:
            print("Name of the Columns\n" ,df.columns)
            co=eval(input("Enter Column Name in the square brackets as a list "))
            print(df[co])
            col=input("Enter the column name to be displayed")
            print("Grouped columns ",col, "max", 'min','count','sum')
            dfgroup=df[co].groupby(col).agg(['max','min','count','sum'])
            print(dfgroup)
                                        
        elif ch3==10:
            print("Name of the Columns\n" ,df.columns)
            co=eval(input("Enter Column Name in the square brackets as a list "))
            print("print maximum Value of the column")
            print(df[co].max())
           
        else:
            print("invalid choice")
    elif ch==4:						#MADE BY HAMZA
        print("Data visualisation of pandas Data frame")
        menu='''1. To Display histogram of numeric column"
        \n 2. To Display Line chart
        \n 3. To Dislpay Bar graph '''
        print(menu)
        ch4=int(input("Enter Your Choice"))
        df=pd.read_csv("C:\\Users\\mpc\\Desktop\\student.csv")
        if ch4==1:
            df['Percentage'].hist(edgecolor='red',facecolor='orange')
            plt.show()
        if ch4==2:
            plt.plot(df['Percentage'])
            plt.show()
        if ch4==3:
            print("Name of the Columns\n" ,df.columns)
            co=eval(input("Enter Column Name in the square brackets as a list "))

            col=input("Enter the column name to be displayed")
            print("Grouped Column ",col)
            dfgroup=df[co].groupby(col).count()
            print(dfgroup)
            dfgroup.plot(kind='bar',title= 'Report of Graph')
            plt.show()
    con=input("Do you wish to continue")
    if con=='n':
        break
