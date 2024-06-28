# import random
# num =random.randint(-20,-1)
# print(f"The random number for this time is {num}")


import random
alpabhet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
alpa = alpabhet.upper()
# print(f'{alpa}')
num = "1,2,3,4,5,6,7,8,9,0"
charc = '!,@,#,$,%,^,&,*,(,),-,+'
combine = str(alpabhet) + str(alpa) + str(num) + str(charc)
combine_list = combine.split(",")
password1 = random.choice(combine_list)
password2 = random.choice(combine_list)
password3 = random.choice(combine_list)
password4 = random.choice(combine_list)
password5 = random.choice(combine_list)
password6 = random.choice(combine_list)
password7 = random.choice(combine_list)
password8 = random.choice(combine_list)
password9 = random.choice(combine_list)
password10 = random.choice(combine_list)
password =password1+password10+password2+password3+password4+password5+password5+password6+password7+password8+password9
print(f"your suggested password is {password}")

