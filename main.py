# kun_raqami = int(input("Hafta kunining raqamini kiriting (1 dan 7 gacha): "))


# if kun_raqami == 1:
#     print("Dushanba")
# elif kun_raqami == 2:
#     print("Seshanba")
# elif kun_raqami == 3:
#     print("Chorshanba")
# elif kun_raqami == 4:
#     print("Payshanba")
# elif kun_raqami == 5:
#     print("Juma")
# elif kun_raqami == 6:
#     print("Shanba")
# elif kun_raqami == 7:
#     print("Yakshanba")
# else:
#     print("Bunday hafta kuni yo'q")


oy_vaqti = str(input('Oyni kiriting: '))


if oy_vaqti == "iyun":
    print("Hozir yozgi ta'til")
elif oy_vaqti == "iyul":
    print("Hozir yozgi ta'til")
elif oy_vaqti == "avgust":
    print("Hozir yozgi tatil")
elif oy_vaqti == "sentabr":
    print("Hozir o'qish vaqti")
elif oy_vaqti == "oktabr":
    print("Hozir o'qish vaqti")
elif oy_vaqti == "noyabr":
    print("Hozir o'qish vaqti")
elif oy_vaqti == "dekabr":
    print("Hozir o'qish vaqti")
elif oy_vaqti == "yanvar":
    print("Hozir o'qish vaqti")
elif oy_vaqti == "fevral":
    print("Hozir o'qish vaqti")
elif oy_vaqti == "mart":
    print("Hozir o'qish vaqti")
elif oy_vaqti == "aprel":
    print("Hozir o'qish vaqti")
elif oy_vaqti == "may":
    print("Hozir o'qish vaqti")
else:
    print("Bunday oy yo'q")


svetofor = str(input('Rangni kiriting: '))

if svetofor == "Qizil":
    print("To'xtang")
elif svetofor == "Sariq":
  print("Tayyorlaning")
elif svetofor == "Yashil":
  print("Yurishingiz mumkin")
    

harf = input("Harfni kiriting: ")

if harf.isupper():
    print("Bosh harf")
elif harf.islower():
    print("Kichik harf")
else:
    print("Kiritilgan belgini aniqlashning iloji yo'q")




