points = 0
import webbrowser as wb
import pyautogui as pg
import time as t

show = input("What is my favorite TV show?")
if show == "the office":
    print("YES! its the best")
    wb.open ("https://www.google.com/search?q=dwight&rlz=1C1GCEA_enUS812US812&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjIko_im5_eAhXNMd8KHdrlAT0Q_AUIDigB&biw=681&bih=647#imgrc=WZE3oV19zhH8XM:")
    points += 4
elif show == "the british office":
    print ("We can't be friends anymore!")
    wb.open ("https://www.google.com/search?q=what+is+that+gif&rlz=1C1GCEA_enUS812US812&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjpu5m5oZ_eAhWRdd8KHUhYA9UQ_AUIDigB&biw=681&bih=599#imgdii=tU5CW3w7KfWj2M:&imgrc=I1ENUC8glWSVRM:")
elif show == "gossip girl":
    print ("LOVE THAT")
    wb.open ("https://www.google.com/search?q=oh+ya+gif&rlz=1C1GCEA_enUS812US812&source=lnms&tbm=isch&sa=X&ved=0ahUKEwijitf1oZ_eAhXqQ98KHZaHAV8Q_AUIDigB&biw=681&bih=647#imgrc=aAQ1dmF2RLl5vM:")
elif show == "idk":
    print ("you should know")
    wb.open ("https://www.google.com/search?q=what+is+that+gifidk&rlz=1C1GCEA_enUS812US812&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjpu5m5oZ_eAhWRdd8KHUhYA9UQ_AUIDigB&biw=681&bih=599#imgrc=hbaUi4hwN0avCM:")
elif show == "friends":
    print ("ehh")
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS812US812&biw=681&bih=647&tbm=isch&sa=1&ei=nX7QW5m4OIvM_Aa0ib2QAg&q=friends&oq=friends&gs_l=img.3..0i67l2j0l3j0i67l5.1944.2784..2939...0.0..0.157.501.6j1......0....1..gws-wiz-img.z9rkxiS1728#imgdii=FqjC-pSjYKkhWM:&imgrc=k3FTP2rDhmct6M:")
elif show == "hannah monatana":
    print ("uhhh...")
    wb.open ("https://www.google.com/search?q=hannah+montana&rlz=1C1GCEA_enUS812US812&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjRn9CVop_eAhUEVt8KHS2WDKsQ_AUIDygC&biw=681&bih=647#imgrc=YuKwp7YnrirLSM:")
else:
    print ("nope it the office")
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS812US812&biw=681&bih=647&tbm=isch&sa=1&ei=GnjQW_eJK6u9gge9hbAg&q=nope&oq=nope&gs_l=img.3..0l10.73971.74442..76193...0.0..0.53.188.4......0....1..gws-wiz-img.......0i67.NUSFY212Wlg#imgrc=IIce7H_A1PuUUM:")
t.sleep(3)
dance = input ("What is my favorite kind of dance?")
if dance == "Ballet":
    print ("Duh")
    wb.open ("https://www.google.com/search?biw=681&bih=647&tbm=isch&sa=1&ei=fXjQW_G5HNG5ggfN16K4CQ&q=yes+gif&oq=yes+gif&gs_l=img.3..0l10.4436.5485..5607...0.0..0.102.471.6j1......0....1..gws-wiz-img.......0i67.olf-hAdt9q0#imgrc=pb_HtCfV5kGinM:")
    points += 3
elif dance == "pointe":
    print ("ballet but thats kinda the same!")
    wb.open ("https://www.google.com/search?q=ballet&rlz=1C1GCEA_enUS812US812&source=lnms&tbm=isch&sa=X&ved=0ahUKEwimssOonJ_eAhUBhOAKHaZVC7YQ_AUIECgD&biw=681&bih=647#imgrc=ZvQpQ7zqXs2skM:")
    points += 1
elif dance == "jazz":
    print ("havent done that in a while")
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS812US812&biw=681&bih=647&tbm=isch&sa=1&ei=GH_QW7KxLePn_QaatoVo&q=jazz+dance+shoes&oq=jazz+dance+shoes&gs_l=img.3..0l5j0i5i30l5.8905.9611..9724...0.0..0.503.1412.2j1j1j1j0j1......0....1..gws-wiz-img.......0i67.bXRqAs_V0ns#imgrc=iw-q7E4CJB9K_M:")
elif dance == "modern":
    print ("nope")
    wb.open ("https://www.google.com/search?q=modern+dance&rlz=1C1GCEA_enUS812US812&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiz9oDQop_eAhXEnuAKHcPDBuYQ_AUIDygC&biw=681&bih=647#imgrc=kCGIrfvRwPMirM:")
elif dance == "contemporary":
    print ("love that but not what I was thinking")
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS812US812&biw=681&bih=647&tbm=isch&sa=1&ei=mH_QW7SSMMrp_Qal8b7YAw&q=handstand&oq=handstand&gs_l=img.3..0l10.11529.14136..14299...0.0..1.106.976.15j1......0....1..gws-wiz-img.......0i67.q0yeQ2_ismA#imgrc=h3f8Z6s3dS6kCM:")
elif dance == "hip hop":
    print ("uh no")
    wb.open ("https://www.google.com/search?q=hip+hop&rlz=1C1GCEA_enUS812US812&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjdw8yPo5_eAhVqZN8KHeZoDCMQ_AUIECgD&biw=681&bih=647#imgrc=O__JpE1erTkTPM:")
else:
    print ("WRONG its ballet")
    wb.open ("https://www.google.com/search?q=no+gif&rlz=1C1GCEA_enUS812US812&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjdsYHRnJ_eAhVPT98KHblOCvMQ_AUIDigB&biw=681&bih=647#imgrc=OV6KUTJphxwHeM:")
t.sleep(3)   
dessert = input ("Whats my favorite dessert?")
if show == "key lime pie":
    print ("Yes good guess!")
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS812US812&biw=681&bih=647&tbm=isch&sa=1&ei=_njQW6GAOuiI_Qb7s5PoAQ&q=key+lime+pie&oq=key+lime+pie&gs_l=img.3..0j0i67l2j0l7.29551.31480..32358...0.0..1.381.1388.8j1j2j1......0....1..gws-wiz-img.gkwVGCx_D7A#imgrc=9btOq579suGWDM:")
    points += 15
elif dessert == "fro yo":
    print ("Thants good too!")
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS812US812&biw=681&bih=647&tbm=isch&sa=1&ei=_njQW6GAOuiI_Qb7s5PoAQ&q=key+lime+pie&oq=key+lime+pie&gs_l=img.3..0j0i67l2j0l7.29551.31480..32358...0.0..1.381.1388.8j1j2j1......0....1..gws-wiz-img.gkwVGCx_D7A#imgrc=9btOq579suGWDM:")
elif dessert == "Chocolate":
    print ("Thats a no")
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS812US812&biw=681&bih=647&tbm=isch&sa=1&ei=_njQW6GAOuiI_Qb7s5PoAQ&q=key+lime+pie&oq=key+lime+pie&gs_l=img.3..0j0i67l2j0l7.29551.31480..32358...0.0..1.381.1388.8j1j2j1......0....1..gws-wiz-img.gkwVGCx_D7A#imgrc=9btOq579suGWDM:")
    points -= 111
elif dessert == "idk":
    print ("key lime pie")
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS812US812&biw=681&bih=647&tbm=isch&sa=1&ei=_njQW6GAOuiI_Qb7s5PoAQ&q=key+lime+pie&oq=key+lime+pie&gs_l=img.3..0j0i67l2j0l7.29551.31480..32358...0.0..1.381.1388.8j1j2j1......0....1..gws-wiz-img.gkwVGCx_D7A#imgrc=9btOq579suGWDM:")
elif dessert == "ice cream":
    print ("not what I was thinking...")
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS812US812&biw=681&bih=647&tbm=isch&sa=1&ei=_njQW6GAOuiI_Qb7s5PoAQ&q=key+lime+pie&oq=key+lime+pie&gs_l=img.3..0j0i67l2j0l7.29551.31480..32358...0.0..1.381.1388.8j1j2j1......0....1..gws-wiz-img.gkwVGCx_D7A#imgrc=9btOq579suGWDM:")
elif dessert == "pie":
    print ("close what kind")
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS812US812&biw=681&bih=647&tbm=isch&sa=1&ei=_njQW6GAOuiI_Qb7s5PoAQ&q=key+lime+pie&oq=key+lime+pie&gs_l=img.3..0j0i67l2j0l7.29551.31480..32358...0.0..1.381.1388.8j1j2j1......0....1..gws-wiz-img.gkwVGCx_D7A#imgrc=9btOq579suGWDM:")
elif dessert == "salad":
    print ("WHAT?!?!?!")
    wb.open ("https://www.google.com/search?q=omg+no+gif&rlz=1C1GCEA_enUS812US812&source=lnms&tbm=isch&sa=X&ved=0ahUKEwid5sKHnZ_eAhUtnOAKHbzuD7AQ_AUIDigB&biw=681&bih=647#imgrc=8I06fuKxvKuV6M:")
    points -= 900
else:
    print ("close it was key lime pie")
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS812US812&biw=681&bih=647&tbm=isch&sa=1&ei=_njQW6GAOuiI_Qb7s5PoAQ&q=key+lime+pie&oq=key+lime+pie&gs_l=img.3..0j0i67l2j0l7.29551.31480..32358...0.0..1.381.1388.8j1j2j1......0....1..gws-wiz-img.gkwVGCx_D7A#imgrc=9btOq579suGWDM:")
t.sleep(3)
pet = input ("What kind of pet do I have?")
if pet == "Cat":
    print ("Yes!")
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS812US812&biw=681&bih=647&tbm=isch&sa=1&ei=6HnQW7_YAeSiggebjICYCA&q=black+and+grey+cat+together&oq=black+and+grey+cat+together&gs_l=img.3..0j0i8i30l3.5314.6535..6679...0.0..0.318.516.0j1j0j1......0....1..gws-wiz-img.......0i30j0i5i30.sUnLfCI517Y#imgrc=wW3t0Y0jdhrWhM:")
    points += 6
elif pet == "dog":
    print ("what??")
    wb.open ("https://www.bing.com/images/search?view=detailV2&ccid=7xt4jLLK&id=C2041A048FDFDF7332CF29D556499DA88C62BBF5&thid=OIP.7xt4jLLKUGaOchfyeia5LAHaGC&mediaurl=http%3a%2f%2fwww.catster.com%2fwp-content%2fuploads%2f2015%2f06%2f201301-cat-national-dress-up-pet-day-1.jpg&exph=489&expw=600&q=cat+dressed+like+a+dog&simid=608033343050088550&selectedIndex=9&ajaxhist=0:")
elif pet == "fish":
    print ("eww")
elif pet == "cow":
    print ("love them but not as a PET!")
elif pet == "chickens":
    print ("want them")
    wb.open ("https://www.bing.com/images/search?view=detailV2&ccid=Mxf%2bJeLG&id=1F1F2F37E43AE468B6324B7ACE30A63D9F59FCC6&thid=OIP.Mxf-JeLG5k9IsPzJ1MEy5wHaHH&mediaurl=http%3a%2f%2fi0.wp.com%2flaughingsquid.com%2fwp-content%2fuploads%2f2015%2f03%2f11074704_945838625435281_9202056889222674104_n.jpg%3ffit%3d750%252C720&exph=720&expw=750&q=pink+chickens&simid=608041439073012847&selectedIndex=1&ajaxhist=0:")
elif pet == "snake":
    print ("NOOOOO")
else:
    print ("Nope I have 2 cats")
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS812US812&biw=681&bih=647&tbm=isch&sa=1&ei=6HnQW7_YAeSiggebjICYCA&q=black+and+grey+cat+together&oq=black+and+grey+cat+together&gs_l=img.3..0j0i8i30l3.5314.6535..6679...0.0..0.318.516.0j1j0j1......0....1..gws-wiz-img.......0i30j0i5i30.sUnLfCI517Y#imgrc=zYgtGEtGouIINM:")
t.sleep(3)
hair = input ("what color is my hair?")
if hair == "blue":
    print ("Yes!")
    wb.open ("https://www.google.com/search?biw=681&bih=647&tbm=isch&sa=1&ei=OnrQW66rJPKi_Qa_oJMo&q=blue&oq=blue&gs_l=img.3..0i67l2j0l2j0i67l2j0j0i67j0j0i67.13870.14531..14663...0.0..0.91.278.4......0....1..gws-wiz-img.i7pkWj7uuWo#imgrc=BfjOS7w6zxm5kM:")
    points += 3
elif hair == "pink":
    print ("It was but...")
    wb.open ("https://www.google.com/search?biw=681&bih=647&tbm=isch&sa=1&ei=SnrQW4vUCuSV_Qay-b_ABA&q=pink+and+blue&oq=pink+and+blue&gs_l=img.3..0l10.21307.22439..22761...0.0..0.463.2227.1j2j1j2j2......0....1..gws-wiz-img.......0i10j0i7i30.s4uXTypixhM#imgrc=DQLxuIG5Bxd7FM:")
    points -= 300
elif hair == "red":
    print ("nope")
elif hair == "dirty blonde":
    print ("I guess but also...")
elif hair == "blonde":
    print ("noo")
elif hair == "green":
    print ("sort of")
    wb.open ("https://www.bing.com/images/search?view=detailV2&ccid=TkqoeZ6g&id=3C41CFBCDAADEA0C3C5C235675946291418113A7&thid=OIP.TkqoeZ6gfJ8f2oqkHibvTwAAAA&mediaurl=http%3a%2f%2fwww.lovethispic.com%2fuploaded_images%2f77404-Blue-Green-Hair.jpg&exph=393&expw=371&q=green+blue+hair&simid=608053563729448934&selectedIndex=2&ajaxhist=0:")
else:
    print ("nope")
    wb.open ("https://www.google.com/search?biw=681&bih=647&tbm=isch&sa=1&ei=YXrQW-H9Hu3l_Qbzy4-ICQ&q=blue+ends+hair+&oq=blue+ends+hair+&gs_l=img.3..0j0i7i30l8j0i7i5i30.22390.28265..28531...1.0..0.277.1394.12j3j1......0....1..gws-wiz-img.......0i67j0i10i67j0i30.GkBnmdpUEoU#imgrc=4hmdeWOD3TDA0M:")
t.sleep(3)
print ("You scored: ")
print (points)
print("out of 31")
