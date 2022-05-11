from os import stat
from django.http import HttpRequest
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


from matplotlib.pyplot import pause
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from openpyxl import Workbook
import itertools



# Create your views here.
def index(request):
   return render(request, 'index.html')
   # return HttpResponse("Hello, world. You're at the poll index.")


def waste_file(request):
    return render(request,'waste.html')



def login_user(request):
    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']

        user= authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('web')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')
    else:
        return render(request, '/')
   # return HttpResponse("cccccccccccccccccccccccccccccccc.")
   

def web(request):
   return render(request, 'web.html')




def pagelogout(request):
    
        logout(request)
        return redirect('/')





def scrapzoom(request):
    
    driver=webdriver.Edge(executable_path="C:\\Users\\Deepanshu.Rai\\Desktop\\New folder\\driver\\msedgedriver.exe")
    driver.maximize_window()
    driver.get("https://www.zoomcar.com/")
    driver.implicitly_wait(10)

    print("hello world")


    def zoomScrapp(state,city,sd,ed):
        driver.find_element(By.CLASS_NAME,"country_list__wrapper--multiselect").click()
        driver.find_element(By.XPATH,"//span[text()='India']").click()
        driver.find_element(By.CLASS_NAME,"city_list__wrapper--multiselect").click()
        driver.find_element(By.XPATH,"//span[text()='"+state+"']").click()
        driver.find_element(By.CLASS_NAME,"city-lightbox__confirm-button").click()
        driver.find_element(By.CLASS_NAME,"field-wrap").click()
        driver.fullscreen_window()
        for i in range(len(city)):
            driver.find_element(By.XPATH,"//input[contains(@class,'input-text')]").send_keys(city[i])
            pause(0.2)
        driver.find_element(By.XPATH,"//*[@class='location-search-results']/div[1]").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@class='button-primary confirm-loc-btn']").click()
        
        driver.find_element(By.XPATH,"//*[@class='ride-time']/a").click()
        driver.find_element(By.XPATH,"//span[text()="+sd+"]").click()
        driver.find_element(By.XPATH,"//*[@class='container']/div[4]/div/div[2]").click()
        driver.find_element(By.XPATH,"//span[text()="+ed+"]").click()
        
        driver.find_element(By.XPATH,"//*[@class='container']/div[4]/div/div[2]").click()
        driver.find_element(By.CLASS_NAME,"button-primary").click()
        time.sleep(5)

    if request.GET:
        StateName=request.GET['StateName']
        CityName=request.GET['CityName']
        StartDate=request.GET['StartDate']
        x=int(StartDate[3:5])
        EndDate=request.GET['EndDate']
        y=int(EndDate[3:5])
        data=zoomScrapp(StateName,CityName,str(x),str(y))
    
    def zoom():
        mycar=[]
        myloc=[]
        myprice=[]
        mydetail=[]
        mysno=[]


        carnam=driver.find_elements(By.XPATH,"//h3")
        for cn in carnam:
            mycar.append(cn.text)
        for sn in range(1,len(carnam)+1):
            mysno.append(sn)

        carloc=driver.find_elements(By.XPATH,"//*[contains(@class,'car-location ellipsis')]")
        for cl in carloc:
            myloc.append(cl.text)


        carp=driver.find_elements(By.XPATH,"//*[contains(@class,'price-bar d-f ai-c ta-c')]")
        for cp in carp:
            myprice.append(cp.text)

        ftrans=[]
        ffuel=[]
        fcapacity=[]
        cardet=driver.find_elements(By.XPATH,"//*[@class='seater']")
        for cd in cardet:
            #print(cd.text.replace("\n", "").split("."))
            mydetail.append(cd.text.replace("\n", "").split("."))
        flat_ls = list(itertools.chain(*mydetail))
        ftrans=flat_ls[::3]
        ffuel=flat_ls[1::3]
        fcapacity=flat_ls[2::3]

        
        finallist=zip(mysno,mycar,ftrans,ffuel,fcapacity,myloc,myprice)
        return (finallist)


    output=zoom()
    wb=Workbook()
    sh1=wb.active
    sh1['A1'] = 'SNO.'
    sh1['B1'] = 'Car_Name'
    sh1['C1'] = 'Transmission'
    sh1['D1'] = 'Fuel'
    sh1['E1'] = 'Capacity'
    sh1['F1'] = 'Location'
    sh1['G1'] = 'Price'

    for x in list(output):
        sh1.append(x)

    wb.save("zoomcar_data.xlsx")

    pause(100)
    driver.quit()



















def scraprevv(request):
    driver=webdriver.Edge(executable_path="C:\\Users\\Deepanshu.Rai\\Desktop\\New folder\\driver\\msedgedriver.exe")
    driver.maximize_window()
    driver.get("https://www.revv.co.in")
    driver.implicitly_wait(10)

    print("hello world")
    def scraprevv(state,sd,ed):
        driver.find_element(By.CLASS_NAME,"locationBox").click()
        pause(1)
        driver.find_element(By.XPATH,"//div[text()='"+state+"']").click()
        driver.find_element(By.XPATH,"//*[@class='datePickerBox']").click()
        driver.find_element(By.XPATH,"//span[text()='"+sd+"']").click()
        pause(1)
        driver.find_element(By.XPATH,"//button[text()='7:30']").click()
        driver.find_element(By.XPATH,"//*[@class='dateTextFieldUnSelectedNew']").click()
        driver.find_element(By.XPATH,"//span[text()='"+ed+"']").click()
        pause(1)
        driver.find_element(By.XPATH,"//button[text()='7:30']").click()
        driver.find_element(By.XPATH,"//b[text()='Search']").click()
        pause(2)


    if request.GET:
        StateName=request.GET['StateName']
        StartDate=request.GET['StartDate']
        x=int(StartDate[3:5])
        EndDate=request.GET['EndDate']
        y=int(EndDate[3:5])
        data=scraprevv(StateName,str(x),str(y))

    def revv():
        mysno=[]
        mycar=[]
        carname = driver.find_elements(By.XPATH,"//*[@class='car-title']")
        for cn in carname:
            mycar.append(cn.text)
        for sn in range(1,len(carname)+1):
            mysno.append(sn)


        myprice1=[]
        fp240=[]
        fp528=[]
        fpunl=[]
        carp = driver.find_elements(By.XPATH,"//*[@class='priceLabel']")
        for cp in carp:
            myprice1.append(cp.text)
        fp240=myprice1[::3]
        fp528=myprice1[1::3]
        fpunl=myprice1[2::3]


        myrange=[]
        carrg = driver.find_elements(By.XPATH,"//*[@class='kmSpan']")
        for cr in carrg:
            myrange.append(cr.text)


        myconfig=[]
        ftran=[]
        fuel=[]
        capacity=[]
        config=driver.find_elements(By.XPATH,"//span[@class='car-brief']")
        for con in config:
            myconfig.append(con.text)
        ftran=myconfig[::3]
        fuel=myconfig[1::3]
        capacity=myconfig[2::3]

        driver.find_element(By.XPATH,"//*[@class='topBarFilter d-none d-md-flex']/div/div/input").click()
        pause(2)
        myprice2=[]
        fpw240=[]
        fpw528=[]
        fpwunl=[]
        carp = driver.find_elements(By.XPATH,"//*[@class='priceLabel']")
        for cp in carp:
            myprice2.append(cp.text)
        fpw240=myprice2[::3]
        fpw528=myprice2[1::3]
        fpwunl=myprice2[2::3]

        finallist1=zip(mysno,mycar,ftran,fuel,capacity,fp240,fp528,fpunl,fpw240,fpw528,fpwunl)
        return(finallist1)



    output1=revv()


    wb1=Workbook()
    sh1=wb1.active
    sh1['A1'] = 'SNO.'
    sh1['B1'] = 'Car_Name'
    sh1['C1'] = 'Transmission'
    sh1['D1'] = 'Fuel'
    sh1['E1'] = 'Capacity'
    sh1['F1'] = 'without_fuel_200+'
    sh1['G1'] = 'without_fuel_400+'
    sh1['H1'] = 'without_fuel_unlimited'
    sh1['I1'] = 'with_fuel_200+'
    sh1['J1'] = 'with_fuel_400+'
    sh1['K1'] = 'with_fuel_unlimited'

    for x in list(output1):
        sh1.append(x)

    wb1.save("revv_data.xlsx")


    pause(100)
    driver.quit()


