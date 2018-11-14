#write a code to print all prime numbers from 1 to 150

num=1
while(num<151):
    cnt = 2
    status = 0
    while(cnt<num):
        if num%cnt == 0:
            status = 1
            break
        cnt += 1
    if status == 0:
        print(num)
    num+=1
    """else:
        print(num,"is not prime ")"""
