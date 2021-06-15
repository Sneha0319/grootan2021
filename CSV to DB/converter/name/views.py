from django.shortcuts import render
import csv
from django.db import connection

def encode(a):
    ans=""
    for i in a:
        m=ord(i)+3 #encoding key 3
        ans+=chr(m)
    return ans

def index(request):
    if(request.method=="POST"):
        name = request.POST["filename"]
        saver = request.POST["saver"]
        print(name)
        lis=[]
        with open(name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            ans=[]
            for row in csv_reader:
                if line_count == 0:
                    ans.append(row)
                    line_count += 1
                else:
                    ans.append(row)
                    line_count += 1
        
        query="CREATE TABLE IF NOT EXISTS "+saver +" ("
        j=0
        flag=-1
        for i in ans[0]:
            if(i=="password"):
                flag=j
            query+=i+" varchar(200),"
            j+=1
        query=query[:-1]
        query+=");"
        print(query)
        curosr=connection.cursor()
        curosr.execute(query)
        query="INSERT INTO "+saver+ " VALUES("
        for i in range(1,len(ans)):
            sub=query[::]
            m=0
            for j in ans[i]:
                if(m==flag):
                    j=encode(j)
                sub+="'"+j+"',"
                m+=1
            sub=sub[:-1]
            sub+=");"
            print(sub)
            curosr.execute(sub)
    return render(request,"index.html")
