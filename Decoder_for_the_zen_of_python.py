s= 'Tkmu Pvyboi sc k widrsmkv mrkbkmdob mbokdon yx dro czeb yp k wywoxd dy rovz myfob kx sxceppsmsoxdvi zvkxxon rkmu. ' \
   'Ro rkc loox boqscdobon pyb mvkccoc kd WSD dgsmo lopybo, led rkc bozybdonvi xofob zkccon k mvkcc. Sd rkc loox dro dbknsdsyx yp ' \
   'dro bocsnoxdc yp Okcd Mkwzec dy lomywo Tkmu Pvyboi pyb k pog xsqrdc okmr iokb dy onemkdo sxmywsxq cdenoxdc sx dro gkic, wokxc, ' \
   'kxn odrsmc yp rkmusxq.'
import string

for i in range(14):
    l = ''
    for j in s:
        if j in string.punctuation or j==' ':
            l+=j
        elif ord(j.lower()) in range(97,97+i):
            l+=chr(ord(j)+i)
        elif ord(j.lower()) in range(97+i , ord('z')+1 ):
            l+=chr(ord(j)-i)

    print(l)

