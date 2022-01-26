import datetime
import pickle
def getDate():
    now=datetime.datetime.now
    return str(now().date())
def display_all_books(b):
    print('\n\nBooks available in library')
    print('--------------------------')
    c=1
    for i in b:
        if i[2]>0:
            print(str(c)+')',i[0], '~By',i[1],'(',i[2],')')
            c+=1
    if len(a)==0:
        print('No books available')
    
def add_new_book(d):
    print('\n\nNew Book')
    print('--------')
    e=input('Enter Book Name:- ')
    f=input('Enter Authours name:- ')
    try:
        g=int(input('Enter The Count Of The Book:- '))
        h=int(input('Enter The Cost For Borrowing:-'))
        i=[e,f,g,h]
        d.append(i)
    except:
        print('Enter a valit number!')
    print('The book has been added\n\n')
    return d
def delete_book(j):
    print('\n\nDelete Book')
    print('-----------')
    k=input('Enter The Name Of The Book To Be Deleted:-')
    k=k.lower()
    flag=0
    for l in j:
        if l[0].lower()==k:
            flag=1
            found=j.index(l)
            break
    if flag==0:
        print('Book Not Found')
    else:
        j.pop(found)
        print("The Book Has Been Deleted.")
    
    return j
def borrow_book(b,u):
    print('\n\nBooks available in library')
    print('--------------------------')
    n=[]
    c=0
    for i in b:
        if i[2]>0:
            c+=1
            print(str(c)+')',i[0], '~By',i[1])
            n.append(c)
            
    if len(a)==0:
        print('No books available')
    else:
        try:
            m=int(input('Enter Your Choice:- '))
            if m in n:
                o=input('Enter The Name Of Borrower:- ')
                p=int(input('Enter The Phone Number Of Borrower:- '))
                r=0
                for q in b:
                    if q[2]>0:
                        r+=1
                        if r==m:
                            book=q
                            index=b.index(q)
                            break
                s=book[0]
                t=0
                da=getDate()
                borrow=[o,p,s,t,da]
                u.append(borrow)
                b[index][2]-=1
        except:
            print('Enter Proper Values')
    
    return b,u
def return_book(v,w):
    x=input('Enter The Returners Name:- ')
    x=x.lower()
    list1=[]
    for i in w:
        yy=i[0].lower()
        if x==yy and i[3]==0:
            zz=w.index(i)
            list1.append(zz)
    if len(list1)>0:
        print('Name Of Borrower:',x.title())
        print('------------------------------------------------')
        c=1
        for i in list1:
            print((c),')',w[i][2],';  Taken on:',w[i][4])
            c+=1
        try:
            y=int(input('Enter your choice:- '))
            c=1
            for i in list1:
                if c==y:
                    title=w[i][2]
                    w[i][3]=1
                    for i in v:
                        if i[0].lower()==title.lower():
                            i[2]+=1
                            cost=i[3]
                    break
                c+=1    
        except:
            print('Enter A Valid Choice!')
        while True:
            z=input('Was the return after dew? (y/n):- ')
            if z.lower()=='y'or z.lower()=='yes':
                try:
                    aa=int(input('How many days was it late?:- '))
                    cost*=aa
                    break
                except:
                    print('Enter a valid input')
            elif z.lower()=='n'or z.lower()=='no':
                break
            else:
                print('Enter a proper choice')
        print('Please pay the borrowing fee : Rs',cost,'at the counter')
    else:
        print('No data found or all books has been returned')
    return v,w
def show_borrowers(ab):
    flag=0
    if len(ab)>0:
        print('Borrow date, Borrower Name, Phone Number, Book Name')
        print('---------------------------------------------------')
        for i in ab:
            if i[3]==0:
                c=0
                e=str(i[4])+' , '
                while c<3:
                    d=i[c]
                    d=str(d)
                    while len(d)<13:
                        d+=' '
                    if c<2:d+=', '
                    e+=d
                    c+=1
                print(e)
                flag=1
    if flag==0:
        print('No Borrowers')


def main_menu():
    print('--------------------------------------')
    print('       Library Management System')
    print('--------------------------------------')
    print('1. Display All Books In Library')
    print('2. Add New Book')
    print('3. Delete A Book')
    print('4. Borrow A Book')
    print('5. Return A book')
    print('6. Show All Borrowers')
    print('9. Exit')
    
def db_creation():
    f1=open('books.dat','wb')
    books=[]
    pickle.dump(books,f1)
    f1.close()
    f3=open('borrower.dat','wb')
    borrower=[]
    pickle.dump(borrower,f3)
    f3.close()
def db_load():
    f2=open('books.dat','rb')
    a=pickle.load(f2)
    f2.close()
    f4=open('borrower.dat','rb')
    b=pickle.load(f4)
    f4.close()
    return a,b
def db_save(a,b):
    f5=open('books.dat','wb')
    pickle.dump(a,f5)
    f5.close()
    f6=open('borrower.dat','wb')
    pickle.dump(b,f6)
    f6.close()
books=[]
borrower=[]
while True:
    print('\nStartup\n')
    b=input("Is this the first time running this program?(Y/N):- ")
    if b=='y'or b=='Y':
        db_creation()
        break
    elif b=='n'or b=='N':
        books, borrower=db_load()
        break
    else:
        print('Enter a valid input')
    print('\n\n\n')
while True:
    main_menu()
    a=input('Enter your choice:- ')
    if a=='1':
        display_all_books(books)
    elif a=='2':
        books=add_new_book(books)
    elif a=='3':
        books=delete_book(books)
    elif a=='4':
        books,borrower=borrow_book(books, borrower)
    elif a=='5':
        books,borrower=return_book(books, borrower)
    elif a=='6':
        show_borrowers(borrower)
    elif a=='9':
        break
    else:
        print('Enter a valid choice')
    print('\n\n')
    db_save(books, borrower)
print('Thank you for using the system.')