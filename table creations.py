print("print multiplication table")
table=int(input("enter the table to print"))
for i in range(1,101):
    ans=table*i
    print(table,"*",i,"=",ans)
