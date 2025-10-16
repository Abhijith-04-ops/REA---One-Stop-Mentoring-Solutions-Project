import datetime

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from keras import Sequential

from REA_app.models import *


# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Dropout, Flatten
# from tensorflow.keras.layers import Conv2D
# from tensorflow.keras.optimizers import Adam
# from tensorflow.keras.layers import MaxPooling2D
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# import nltk
# nltk.download('omw-1.4')

# import nltk
# nltk.download('punkt')
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
# import requests
# Create your views here.

def loginn(request):
    return render(request,'index.html')


def login_POST(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    qry=login.objects.filter(username=username,password=password)
    if qry.exists():
        if qry[0].usertype=="admin":
            request.session['lid']=qry[0].id
            return HttpResponse("<script>alert('Login success');window.location='/admin_home'</script>")
        elif qry[0].usertype=="mentor":
            request.session['lid']=qry[0].id
            return HttpResponse("<script>alert('Login success');window.location='/mentor_home'</script>")
        else:
            return HttpResponse("<script>alert('Invalid Username and Password!!');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('User not found');window.location='/'</script>")


import matplotlib
matplotlib.use('agg')  # Use the Agg backend (non-interactive)
import matplotlib.pyplot as plt

# import matplotlib.pyplot as plt
import numpy as np

def plot_diary_graph(emo_list, score_list):

    x = np.array(emo_list)
    y = np.array(score_list)
    # myexplode = [0.2, 0, 0, 0]

    plt.barh(x,y)
    plt.yticks(rotation = 45)
    d=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    plt.savefig(r"C:\Users\Abhi\PycharmProjects\REA\REA_app\static\graphs\\" + d +"diary.png")
    path="/static/graphs/" + d + "diary.png"
    plt.close()
    return path

def plot_image_graph(emo_list, score_list):
    x = np.array(emo_list)
    y = np.array(score_list)
    # myexplode = [0.2, 0, 0, 0]

    plt.barh(x,y)
    plt.yticks(rotation = 45)
    d=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    plt.savefig(r"C:\Users\Abhi\PycharmProjects\REA\REA_app\static\graphs\\" + d +"image.png")
    path="/static/graphs/" + d + "image.png"
    plt.close()
    return path



def logout(request):
    request.session['lid'] = ''
    return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")


def app_reviews(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        qry=app_review.objects.all()
        return render(request,'admin_module/app review.html',{"data":qry})

def approved_mentor(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        qry=mentor.objects.filter(LOGIN__usertype="mentor")
        return render(request,'admin_module/approved mentor.html',{"data":qry})

def change_password(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        return render(request,'admin_module/change password.html')

def change_password_POST(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        current_password=request.POST['textfield']
        new_password=request.POST['textfield2']
        re_enter_password=request.POST['textfield3']
        qry=login.objects.filter(password=current_password,id=request.session['lid'])
        if qry.exists():
            if new_password==re_enter_password:
                login.objects.filter(id=request.session['lid'], password=current_password).update(password=re_enter_password)
                return HttpResponse("<script>alert('Password Changed Successfully!!');window.location='/admin_home'</script>")
            else:
                return HttpResponse("<script>alert('Password Mismatch. Please Try Again');window.location='/change_password'</script>")
        else:
            return HttpResponse("<script>alert('Current Password Is Incorrect.Try Again');window.location='/change_password'</script>")


def view_complaint(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        qry=complaint.objects.all()
        return render(request,'admin_module/complaint.html',{"data":qry})

def mentor_approval(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        qry=mentor.objects.filter(LOGIN__usertype="pending")
        return render(request,'admin_module/mentor approval.html',{"data":qry})

def rejected_mentor(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        qry = mentor.objects.filter(LOGIN__usertype="reject")
        return render(request,'admin_module/rejected mentor.html',{"data":qry})

def approve_mentor(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        login.objects.filter(id=id).update(usertype="mentor")
        return redirect('/mentor_approval')

def reject_mentor(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        login.objects.filter(id=id).update(usertype="reject")
        return redirect('/mentor_approval')

def send_reply(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        return render(request,'admin_module/send reply.html',{"id":id})

def send_reply_POST(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        textarea=request.POST['textarea']
        qry=complaint.objects.filter(id=id).update(reply=textarea,Rdate=datetime.datetime.now().strftime("%Y-%m-%d"))
        return HttpResponse("<script>alert('Replied Successfully!!');window.location='/view_complaint'</script>")

def view_mentor_review(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        qry=mentor_review.objects.all()
        return render(request,'admin_module/view mentor review.html',{"data":qry})

def admin_home(request):
        return render(request,'admin_module/admin_index.html')

# ===================================================================================================================================================
#                                                 MENTOR MODULE
# ========================================================================================================================================================

def mentor_home(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        return  render(request,'mentor_module/mentor_index.html')

def add_motivational_content(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        return render(request,'mentor_module/add_motivational_content.html')
def add_motivational_content_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        print(request.session["lid"])
        title1=request.POST['textfield']
        content1=request.POST['textarea']
        dat=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        obj=motivation()
        obj.content=content1
        obj.title=title1
        obj.date=dat
        obj.MENTOR=mentor.objects.get(LOGIN=request.session["lid"])
        obj.save()
        return HttpResponse("<script>alert('Content Added SuccessFully!!');window.location='/mentor_home'</script>")

def add_tips(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        return render(request,'mentor_module/add_tips.html')

def add_tips_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        tips1=request.POST['textarea']
        dat=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        obj=tips()
        obj.tip=tips1
        obj.date=dat
        obj.MENTOR=mentor.objects.get(LOGIN=request.session["lid"])
        obj.save()
        return HttpResponse("<script>alert('Tips Added SuccessFully!!');window.location='/mentor_home'</script>")

def change_mentor_password(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        return render(request,'mentor_module/change_mentor_password.html')

def change_mentor_password_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        currentpassword=request.POST['textfield']
        newpassword=request.POST['textfield2']
        reenterpassword=request.POST['textfield3']
        qry =login.objects.filter(password=currentpassword, usertype="mentor")
        if qry.exists():
            if newpassword==reenterpassword:
                login.objects.filter(usertype="mentor").update(password=reenterpassword)
                return HttpResponse(
                    "<script>alert('Password Changed Successfully!!');window.location='/mentor_home'</script>")
            else:
                return HttpResponse(
                    "<script>alert('Password Mismatch. Please Try Again');window.location='/change_mentor_password'</script>")
        else:
            return HttpResponse("<script>alert('Current Password Is Incorrect.Try Again');window.location='/change_mentor_password'</script>")


def edit_motivational_content(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        qry=motivation.objects.get(id=id)
        return render(request,'mentor_module/edit_motivational_content.html',{"data":qry,"id":id})

def edit_motivational_content_post(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        title=request.POST['textfield']
        content=request.POST['textarea']
        motivation.objects.filter(id=id).update(title=title,content=content)
        return HttpResponse("<script>alert('Editted Successfully!!!');window.location='/view_motivational_content'</script>")

def mentor_register(request):
    return render(request,'mentor_module/mentor_register.html')

def mentor_register_post(request):
        photo=request.FILES['fileField']
        date=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs=FileSystemStorage()
        fs.save(r"C:\Users\Abhi\PycharmProjects\REA\REA_app\static\mentor_photo\\"+date+'.jpg',photo)
        path="/static/mentor_photo/"+date+'.jpg'
        name=request.POST['textfield']
        gender=request.POST['RadioGroup1']
        phone=request.POST['textfield2']
        email=request.POST['textfield3']
        password=request.POST['textfield4']
        obj=login()
        obj.username=email
        obj.password=password
        obj.usertype='pending'
        obj.save()
        obj1=mentor()
        obj1.photo=path
        obj1.name=name
        obj1.email=email
        obj1.phone=phone
        obj1.gender=gender
        obj1.LOGIN=obj
        obj1.save()
        return HttpResponse("<script>alert('Registration Success');window.location='/'</script>")

def view_approved_request(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        user2 = requests.objects.filter(MENTOR__LOGIN=request.session["lid"], status="approve")
        return render(request,'mentor_module/view_approved_request.html',{"data":user2})

def view_motivational_content(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        qry = motivation.objects.filter(MENTOR__LOGIN=request.session['lid'])
        return render(request,'mentor_module/view_motivational_content.html',{"data":qry})

def view_motivational_content_delete(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        motivation.objects.filter(id=id).delete()
        return HttpResponse("<script>alert('Deleted Successfully!!');window.location='/view_motivational_content'</script>")

def view_motivational_content_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        return HttpResponse("ok")

def view_profile_edit_profile(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        print(request.session["lid"])
        data=mentor.objects.get(LOGIN=request.session["lid"])
        return render(request,'mentor_module/view_profile_edit_profile.html',{"data":data})

def view_profile_edit_profile_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        try:
            photo=request.FILES['fileField']
            date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            fs = FileSystemStorage()
            fs.save(r"C:\Users\Abhi\PycharmProjects\REA\REA_app\static\mentor_photo\\" + date + '.jpg', photo)
            path = "/static/mentor_photo/" + date + '.jpg'
            nam=request.POST['textfield']
            gendr=request.POST['RadioGroup1']
            phon=request.POST['textfield2']
            # emal=request.POST['textfield3']
            mentor.objects.filter(LOGIN=request.session["lid"]).update(photo=path, name=nam,gender=gendr,phone=phon)
            return HttpResponse(
                "<script>alert('Profile Updated Successfully!!');window.location='/view_profile_edit_profile'</script>")
        except Exception as e:
            nam = request.POST['textfield']
            gendr = request.POST['RadioGroup1']
            phon = request.POST['textfield2']
            # emal = request.POST['textfield3']
            mentor.objects.filter(LOGIN=request.session["lid"]).update(name=nam, gender=gendr, phone=phon)
            return HttpResponse("<script>alert('Profile Updated Successfully!!');window.location='/view_profile_edit_profile'</script>")

def view_request_approve_reject(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        user1=requests.objects.filter(MENTOR__LOGIN=request.session["lid"],status="pending")
        return render(request,'mentor_module/view_request_approve_reject.html',{"data":user1})


def request_approve(request, id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        requests.objects.filter(id=id).update(status="approve")
        return HttpResponse("<script>alert('Approved');window.location='/view_request_approve_reject'</script>")

def request_reject(request, id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        requests.objects.filter(id=id).update(status="reject")
        return HttpResponse("<script>alert('Rejected!!');window.location='/view_request_approve_reject'</script>")

def view_review(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        qry=mentor_review.objects.filter(MENTOR__LOGIN=request.session['lid'])
        return render(request,'mentor_module/view_review.html',{'data':qry})

def view_tips(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        qry=tips.objects.filter(MENTOR__LOGIN=request.session['lid'])
        return render(request,'mentor_module/view_tips.html',{"data":qry})

def view_tips_delete(request,id):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        tips.objects.filter(id=id).delete()
        return HttpResponse("<script>alert('Deleted Successfully!!');window.location='/view_tips'</script>")

def view_emotion_graph(request, id):
    res=diary.objects.filter(USER_id=id)
    text_dict={'anger':0, 'anticipation':0, 'disgust':0, 'fear':0, 'joy':0, 'sadness':0, 'surprise':0, 'trust':0}
    for i in res:
        text_dict[i.emotion]+=1
    print(text_dict)
    emo_list=[]
    score_list=[]
    for i in text_dict:
        emo_list.append(i)
        score_list.append(text_dict[i])
    path=plot_diary_graph(emo_list, score_list)
    cont_list=[]
    for i in range(0, len(emo_list)):
        cont_list.append([emo_list[i], score_list[i]])
    return render(request, "mentor_module/view_emotion_graph.html",{'path': path,'cont_list': cont_list})

#-------------------------------------IMAGE EMOTION---------------------------------------------
def view_image_emotion_graph(request,id):
    res2 = emotions.objects.filter(USER_id=id)
    text_dict2 = {"Angry":0 , "Disgusted":0 , "Fearful":0 , "Happy":0 , "Neutral":0 , "Sad":0 , "Surprised":0}
    for i in res2:
        text_dict2[i.emotion] += 1
    print(text_dict2)
    emo_list1 = []
    score_list1 = []
    for i in text_dict2:
        emo_list1.append(i)
        score_list1.append(text_dict2[i])
    path2 = plot_image_graph(emo_list1, score_list1)
    cont_list2 = []
    for i in range(0, len(emo_list1)):
        cont_list2.append([emo_list1[i], score_list1[i]])
    return render(request, "mentor_module/view_image_emotion_graph.html", {'path2':path2,'cont_list2':cont_list2})




# ===========mentor chat
def chatt(request,u):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        # request.session['head']="CHAT"
        request.session['uid'] = u
        return render(request,'mentor_module/mentor_user_chat.html',{'u':u})


def chatsnd(request,u):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Please Login!!');window.location='/'</script>")
    else:
        d=datetime.datetime.now().strftime("%Y-%m-%d")
        # t=datetime.datetime.now().strftime("%H:%M:%S")
        c = request.session['lid']
        b=request.POST['n']
        print(b)
        print(u,"userrrrrrrrrr")
        m=request.POST['m']
        cc = mentor.objects.get(LOGIN__id=c)
        uu = user.objects.get(id=request.session['uid'])
        obj=chat()
        obj.date=d
        obj.type='mentor'
        obj.MENTOR=cc
        obj.USER=uu
        obj.message=m
        obj.save()
        print(obj)
        v = {}
        if int(obj) > 0:
            v["status"] = "ok"
        else:
            v["status"] = "error"
        r = JsonResponse.encode(v)
        return r
    # else:
    #     return redirect('/')

def chatrply(request):
    # if request.session['log']=="lo":
        c = request.session['lid']
        cc=mentor.objects.get(LOGIN__id=c)
        uu=user.objects.get(id=request.session['uid'])
        res = chat.objects.filter(MENTOR=cc,USER=uu)
        print(res)
        v = []
        if len(res) > 0:
            print(len(res))
            for i in res:
                v.append({
                    'type':i.type,
                    'chat':i.message,
                    'nam':i.USER.name,
                    'upic':i.USER.photo,
                    'dtime':i.date,
                    'tname':i.MENTOR.name,
                })
            # print(v)
            return JsonResponse({"status": "ok", "data": v, "id": cc.id})
        else:
            return JsonResponse({"status": "error"})

#============================================================================================================================
#                                            ANDROID APP
#============================================================================================================================

def and_login(request):
    val=request.POST["usr"]
    pd=request.POST["pwd"]
    res=login.objects.filter(username=val,password=pd,usertype="user")
    if res.exists():
        return JsonResponse({"status":"OK","lid":res[0].id})

    else:
        return JsonResponse({"status":"error"})

def and_guest_login(request):

    res = mentor.objects.all()
    li = []
    for i in res:
        m = ''
        tx = ''
        mot=motivation.objects.filter(MENTOR=i.id)
        if mot.exists():
            m = mot[0].content
        mw=mentor_review.objects.filter(MENTOR=i.id)
        tp=tips.objects.filter(MENTOR=i.id)
        if tp.exists():
            tx = tp[0].tip
        a = 0
        if mw.exists():
            t = 0

            for j in mw:
                t= t + int(float(j.rating))
            a = t / int(len(mw))
        li.append({'id':i.id,'img':i.photo,'name':i.name,'tips':tx,'content':m,'rating':a})
    return JsonResponse({"status": "ok", 'data': li})

def and_Registration(request):
    name=request.POST["na"]
    pic=request.FILES["pic"]
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs = FileSystemStorage()
    fs.save(r"C:\Users\Abhi\PycharmProjects\REA\REA_app\static\user\\" + date + '.jpg', pic)
    path = "/static/user/" + date + '.jpg'
    email=request.POST["em"]
    phone=request.POST["phon"]
    pswd=request.POST["pwd"]
    gndr=request.POST["gdr"]
    log=login()
    log.username=email
    log.password=pswd
    log.usertype="user"
    log.save()
    usr=user()
    usr.LOGIN = log
    usr.photo=pic
    usr.username=email
    usr.email=email
    usr.name=name
    usr.gender=gndr
    usr.phone=phone
    usr.save()
    return JsonResponse({"status":"ok"})


def and_view_mentor(request):
    men=mentor.objects.filter(LOGIN__usertype="mentor")
    li = []
    for i in men:
        li.append({'id': i.id, 'name': i.name, 'gender': i.gender,'phone': i.phone,'email': i.email,'img': i.photo})
    print(li)
    return JsonResponse({"status": "ok", 'data': li})

def and_sent_mentor_request(request):
    lid = request.POST["lid"]
    mid = request.POST["mid"]
    if requests.objects.filter(USER__LOGIN=lid, MENTOR=mid).exists():
        return JsonResponse({"status":"exist"})
    else:
        obj= requests()
        obj.status='pending'
        obj.date=datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
        obj.USER= user.objects.get(LOGIN=lid)
        obj.MENTOR=mentor.objects.get(id=mid)
        obj.save()
        return JsonResponse({"status":"ok"})

def and_our_mentor(request):
    lid=request.POST["lid"]
    res=requests.objects.filter(USER__LOGIN=lid, status='approve')
    li=[]
    for i in res:
        li.append({"id": i.MENTOR.id, "name": i.MENTOR.name, "gender": i.MENTOR.gender,"phone" : i.MENTOR.phone,"email" : i.MENTOR.email, "img" : i.MENTOR.photo})
    print(li)
    return JsonResponse({"status": "ok", 'data': li})

def and_view_motivation_content(request):
    lid=request.POST["lid"]
    mid=request.POST["mid"]
    mot=motivation.objects.filter(MENTOR=mid)
    li=[]
    for i in mot:
        li.append({"date": i.date, "mentor":i.MENTOR.name,"title":i.title,"content":i.content})
    print(li)
    return JsonResponse({"status": "ok", 'data': li})

def and_view_tips(request):
    lid=request.POST["lid"]
    mid=request.POST["mid"]
    ti=tips.objects.filter(MENTOR=mid)
    li=[]
    for i in ti:
        li.append({"date": i.date,"mentor":i.MENTOR.name,"tips":i.tip})
    print(li)
    return JsonResponse({"status": "ok", 'data': li})

def and_view_mentor_review(request):
    mid = request.POST["mid"]
    re = mentor_review.objects.filter(MENTOR=mid)
    li=[]
    for i in re:
        li.append({"id":i.id,"img":i.USER.photo, "name":i.USER.name, "date":i.date, "rating":i.rating, "review":i.review})
    print(li)
    return JsonResponse({"status": "ok", 'data': li})

def and_send_mentor_review(request):
    mid = request.POST["mid"]
    lid= request.POST["lid"]
    review = request.POST["rvw"]
    rating = request.POST["rtn"]
    obj = mentor_review()
    obj.review = review
    obj.rating = rating
    obj.date = datetime.datetime.now().strftime("%d/%m/%Y")
    obj.USER = user.objects.get(LOGIN=lid)
    obj.MENTOR_id = mid
    obj.save()
    return JsonResponse({"status": "ok"})

def and_send_app_review(request):
    lid = request.POST["lid"]
    revw = request.POST["rvw"]
    ratin = request.POST["rtn"]
    obj = app_review()
    obj.review = revw
    obj.rating = ratin
    obj.date = datetime.datetime.now().strftime("%d/%m/%Y")
    obj.USER = user.objects.get(LOGIN=lid)
    obj.save()
    return JsonResponse({"status":"ok"})

def and_Change_Password(request):
    lid = request.POST["lid"]
    print(lid)
    curpsd = request.POST["crp"]
    newpsd = request.POST["nwp"]
    obj = login.objects.filter(id = lid,password=curpsd)
    if obj.exists():
        login.objects.filter(id=lid, password=curpsd).update(password=newpsd)
        return  JsonResponse({"status":"ok"})
    else:
        return JsonResponse({"status":"none"})


def and_view_profile(request):
    lid = request.POST["lid"]
    obj = user.objects.get(LOGIN=lid)
    dt = {'name': obj.name, 'email': obj.email, 'phone': obj.phone, 'gender': obj.gender, 'pic': obj.photo}
    return JsonResponse({"status":"ok","data":dt})

def and_update_profile(request):
    try:
        name = request.POST["na"]
        lid = request.POST["lid"]
        pic = request.FILES["pic"]
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs = FileSystemStorage()
        fs.save(r"C:\Users\Abhi\PycharmProjects\REA\REA_app\static\user\\" + date + '.jpg', pic)
        path = "/static/user/" + date + '.jpg'
        email = request.POST["em"]
        phone = request.POST["phon"]
        gndr = request.POST["gdr"]
        user.objects.filter(LOGIN=lid).update(
            name=name,
            email=email,
            phone=phone,
            gender=gndr,
            photo=path,
        )

        return JsonResponse({"status":"ok"})
    except Exception as e:

        name = request.POST["na"]
        lid = request.POST["lid"]
        email = request.POST["em"]
        phone = request.POST["phon"]
        gndr = request.POST["gdr"]
        user.objects.filter(LOGIN=lid).update(
            name=name,
            email=email,
            phone=phone,
            gender=gndr,
        )
        return JsonResponse({"status": "ok"})


def and_send_complaint(request):
    lid = request.POST["lid"]
    cmp = request.POST["comp"]
    obj = complaint()
    obj.complaint=cmp
    obj.Cdate = datetime.datetime.now().strftime("%d/%m/%Y-%H/%M/%S")
    obj.USER = user.objects.get(LOGIN=lid)
    obj.reply="pending"
    obj.save()
    return JsonResponse({"status": "ok"})

def and_view_complaint_reply(request):
    lid = request.POST["lid"]
    c = complaint.objects.filter(USER__LOGIN=lid)
    li = []
    for i in c:
        li.append({"id": i.id, "cdate": i.Cdate, "complaint": i.complaint, "rdate": i.Rdate,"reply":i.reply})
        print(li)
    return JsonResponse({"status": "ok", 'data': li})


def and_delete_complaint(request):
    cid = request.POST["cid"]
    complaint.objects.get(id=cid).delete()
    return JsonResponse({"status": "ok"})

def and_view_request_status(request):
    lid = request.POST["lid"];
    res = requests.objects.filter(USER=user.objects.get(LOGIN__id=lid))
    li = []
    for i in res:
        li.append({"id": i.id, "img": i.MENTOR.photo, "name": i.MENTOR.name, "email": i.MENTOR.email, "phone": i.MENTOR.phone,"gender":i.MENTOR.gender,"status":i.status})
    print(li)
    return JsonResponse({"status": "ok", 'data': li})

def and_custom_delete_request(request):
    id = request.POST["comp"]
    requests.objects.filter(id=id).delete()
    return JsonResponse({"status": "ok"})

#-------------------------------------------------------------------------------
def add_chat(request):
    lid = request.POST['lid']
    toid = request.POST['toid']
    print("toid",toid)
    message = request.POST['message']
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    t=datetime.datetime.now().strftime("%H:%m:%d")
    expid = mentor.objects.get(id=toid)
    print("ex",expid)
    uid = user.objects.get(LOGIN=lid)
    obj=chat()
    obj.date=d
    obj.type='user'
    obj.MENTOR_id=expid.id
    obj.USER=uid
    obj.message=message
    obj.save()
    return JsonResponse({'status':"Inserted"})



def view_chat(request):
    lid = request.POST['lid']
    toid = request.POST['toid']
    lastid = request.POST['lastid']
    print("View Chat....",lid,toid,lastid)
    res=chat.objects.filter(USER=user.objects.get(LOGIN=lid))
    res=chat.objects.filter(Q(USER=user.objects.get(LOGIN=lid),MENTOR=toid),Q(id__gt=lastid))
    # print(res[0].message)
    ar=[]
    for i in res:
        ar.append({
            "id":i.id,
            "date":i.date,
            "userid":i.USER.id,
            "sid":i.type,
            "chat":i.message,
        })
    print(ar,"arrrrrrrrrrr")
    return JsonResponse({'status':"ok",'data':ar})

def and_add_diary_content(request):
    diry = request.POST['diary']
    lid = request.POST['lid']

    # ####    emotion calculation code1
    # import text2emotion as te
    # emo=te.get_emotion(diry)
    # print(emo)

    ####    emotion calculation code2
    from LeXmo import LeXmo
    emo = LeXmo.LeXmo(diry)
    emo.pop('text', None)
    print(emo)
    try:
        emo.pop("negative")
        emo.pop("positive")
    except Exception as e:
        print("Exception found : ", e)
    print(emo)

    emo_list=[]
    score_list=[]
    for i in emo:
        emo_list.append(i)
        score_list.append(round(float(emo[i]), 5))

    # create emotion list and scorelist
    print(emo_list)
    print(score_list)

    #  find max value in score
    max_val=max(score_list)
    print("Max ", max_val)

    #get index from scorelist
    idx=score_list.index(max_val)
    print("Idx ", idx)

    #   get emotion with max val
    max_emo=emo_list[idx]
    print("Emotion  ", max_emo)


    d = datetime.datetime.now().strftime("%d-%m-%Y")
    t = datetime.datetime.now().strftime("%H:%M:%S")
    obj = diary()
    obj.USER = user.objects.get(LOGIN=lid)
    obj.date=d
    obj.time=t
    obj.content=diry
    obj.emotion=max_emo
    obj.save()




    return JsonResponse({"status": "ok"})

def and_view_diary_content(request):
    lid = request.POST['id']
    content = diary.objects.filter(USER=user.objects.get(LOGIN=lid))
    li = []
    for i in content:
        li.append({"id":i.id, "date": i.date, "time": i.time, "content": i.content,})
    print(li)
    return JsonResponse({"status": "ok", 'data': li})

def and_delete_content(request):
    did = request.POST["id"]
    diary.objects.get(id=did).delete()
    return JsonResponse({"status": "ok"})

# def insertmood(request):
#     lid = request.POST["lid"]
#     pic = request.FILES["pic"]
#     d=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#     filepath=r"C:\Users\Abhi\PycharmProjects\REA\REA_app\static\emotions\\"+d+".jpg"
#     fs=FileSystemStorage()
#     fs.save(filepath, pic)
#     emotion=predict(filepath)
#     print(emotion,"===============================")
#     obj=emotions()
#     obj.date=datetime.datetime.now().strftime("%Y-%m-%d")
#     obj.photo="/static/emotions/"+d+".jpg"
#     obj.emotion=emotion
#     obj.USER=user.objects.get(LOGIN_id=lid)
#     obj.save()
#     return JsonResponse({'status':'ok', 'name':emotion})





import cv2
def predict(filepath):
    model = Sequential()
    model.load_weights(r'C:\Users\Abhi\PycharmProjects\REA\model.h5')
    cv2.ocl.setUseOpenCL(False)
    # dictionary mapping class labels with corresponding emotions
    emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

    # start the webcam feed
    frame = cv2.imread(filepath)

    # To find haar cascade to draw bounding box around face
    facecasc = cv2.CascadeClassifier(r'C:\Users\Abhi\PycharmProjects\REA\haarcascade_frontalface_default.xml')
    # while True:
        # Capture frame
    # ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facecasc.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y - 50), (x + w, y + h + 10), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
        prediction = model.predict(cropped_img)
        maxindex = int(np.argmax(prediction))
        return emotion_dict[maxindex]










def insertmood(request):
    lid=request.POST['lid']

    ###     TEXT EMOTION
    diry = request.POST['diary']

    # ####    emotion calculation code1s
    # import text2emotion as te
    # emo=te.get_emotion(diry)
    # print(emo)

    ####    emotion calculation code2
    from LeXmo import LeXmo
    emo = LeXmo.LeXmo(diry)
    emo.pop('text', None)
    print(emo)
    try:
        emo.pop("negative")
        emo.pop("positive")
    except Exception as e:
        print("Exception found : ", e)
    print(emo)

    emo_list = []
    score_list = []
    for i in emo:
        emo_list.append(i)
        score_list.append(round(float(emo[i]), 5))

    # create emotion list and scorelist
    print(emo_list)
    print(score_list)

    #  find max value in score
    max_val = max(score_list)
    print("Max ", max_val)

    # get index from scorelist
    idx = score_list.index(max_val)
    print("Idx ", idx)

    #   get emotion with max val
    max_emo = emo_list[idx]
    print("Emotion  ", max_emo)

    d = datetime.datetime.now().strftime("%d-%m-%Y")
    t = datetime.datetime.now().strftime("%H:%M:%S")
    obj = diary()
    obj.USER = user.objects.get(LOGIN=lid)
    obj.date = d
    obj.time = t
    obj.content = diry
    obj.emotion = max_emo
    obj.save()

    ##      IMAGE EMOTION
    pic=request.FILES['pic']
    d=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs=FileSystemStorage()
    filepath = r"C:\Users\Abhi\PycharmProjects\REA\REA_app\static\emotions\\" + d + ".jpg"
    # fs.save(r"C:\Users\Abhi\PycharmProjects\REA\REA_app\static\emotions\\"+'a.jpg',pic)
    fs.save(filepath, pic)
    path="/static/emotions/"+d+'.jpg'

    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Dropout, Flatten
    from tensorflow.keras.layers import Conv2D
    from tensorflow.keras.optimizers import Adam
    from tensorflow.keras.layers import MaxPooling2D
    from tensorflow.keras.preprocessing.image import ImageDataGenerator
    import os
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

    import cv2
    ####emotion finding
    import requests

    import cv2
    model = Sequential()

    model.add(
        Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(7, activation='softmax'))

    model.load_weights(r'C:\Users\Abhi\PycharmProjects\REA\model.h5')

    # prevents openCL usage and unnecessary logging messages
    cv2.ocl.setUseOpenCL(False)

    # dictionary which assigns each label an emotion (alphabetical order)
    emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral",
                    5: "Sad",
                    6: "Surprised"}

    frame = cv2.imread(filepath)
    # frame = cv2.imread(r"C:\Users\Abhi\PycharmProjects\REA\REA_app\static\emotions\\" + 'a.jpg')

    facecasc = cv2.CascadeClassifier(
        r'C:\Users\Abhi\PycharmProjects\REA\haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facecasc.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    import numpy as np
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y - 50), (x + w, y + h + 10), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
        prediction = model.predict(cropped_img)
        maxindex = int(np.argmax(prediction))
        print(emotion_dict[maxindex])
        res_emo = emotion_dict[maxindex]
        obj = emotions()
        obj.date=datetime.datetime.now().strftime("%Y-%m-%d")
        obj.photo=path
        obj.emotion=res_emo
        obj.USER=user.objects.get(LOGIN_id=lid)
        obj.save()
        return JsonResponse({'status':"suggestion", 'name':str(res_emo)})
    return JsonResponse({'status':'not found'})

def video_call(request,id):
    return render(request, 'mentor_module/index.html')

def new_video_call(request):
    return render(request,'mentor_module/new_index.html')







