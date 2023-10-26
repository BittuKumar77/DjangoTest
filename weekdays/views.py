from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# def monday(request):
#     return HttpResponse("<h1>sadest Day</h1>")

# def tuesday(request):
#     return HttpResponse("<h2>No Work</h2>")

# def wednesday(request):
#     return HttpResponse("<h2>Longest day of week</h2>")

# def daily_msg(request,day):
#     if day == '1':
#         m='Sadest Day of the week'
#     elif day == '2':
#         m="No work of the day" 
#     elif day == '3':
#         m="Longest of th day" 
#     elif day == '4':
#         m="Its long day" 
#     elif day == '5':
#         m="Waiting for weekned" 
#     elif day == '6':
#         m="Happiest of the week" 
#     elif day == '7':
#         m="<h1>Thinking about Monday</h1>"
#     else:
#         m='Invalid Day'
#     return HttpResponse(m)


d={
    'sunday':'saddest ',
    'monday':'saddest Day in the week',
    'tuesday':'No work for day',
    'wednesday':'lazy day',
    'thursday':None,
    'friday':'Big day',
    'saturday':'Sad day',
}

def week_list(request):
    day = list(d)
#     l='''<ul>
#             <li><a href="sunday">Sunday</li>
#             <li><a href="monday">Monday</li>
#             <li><a href="tuesday">Tuesday</li>
#             <li><a href="wednesday">Wednesday</li>
#             <li><a href="thursday">Thursday</li>
#             <li><a href="friday">Friday</li>
#             <li><a href="saturday">Saturday</li>
#         </ul>
# '''
#     return HttpResponse(l)

    #    res =''''''
    #    for i in d:
    #         res+=f'<li><a href ="{i}">{i}</a></li>'
    #    l=f'<ul>{res}</ul>'
    #    return HttpResponse(l)
    return render(request,'weekdays/home.html',{'col':day})

def display(request,day):
    #a= int(input('amt: '))
    m=d[day.lower()]
    return render(request,'weekdays/index.html',{'msg':m,'day':day})
    

def display_num(request,num):
    l=list(d)
    day =l[num-1]
    # m=d[day]
    # return redirect('week:home',day=day)

    p= reverse('week:home',args=[day])
    return HttpResponseRedirect(p)

def hello(request):
    return render(request,'weekdays/home.html')

# def index(request):
#     return render(request,'weekdays/index.html')




