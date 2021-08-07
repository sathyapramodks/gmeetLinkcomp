from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import datetime
import pytz

# Create your views here.
def redirection(request):
    dictClassLink = {
    'CNC': 'http://meet.google.com/xsd-nxuy-bdu',
    'MM': 'https://meet.google.com/dwu-finb-pms',
    'AHP': 'https://meet.google.com/nnb-dhtz-zft',
    'PPCE': 'https://meet.google.com/aff-nicy-drf',
    'PDS': 'https://meet.google.com/dkw-qotg-qut',
    'TWM': 'https://meet.google.com/grp-biqj-aru',
    'MEL': 'https://meet.google.com/wsr-yesp-pmc',
    'MTL': 'https://meet.google.com/fsc-jvsi-mcc',
    'ADDI': 'https://meet.google.com/yjp-odij-yec',
    'DOME': 'https://meet.google.com/nud-nqdv-zfk'
    }
    sampleurl = 'https://www.youtube.com/'

    dt = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
    timeNow = dt.time()
    print(timeNow)
    """ return HttpResponse('hello') """
    #PERIOD 1- 08:30AM TO 09:30AM
    if (timeNow > datetime.time(8,25,0, )) and (timeNow < datetime.time(8,40,0, )):
        print('block 1')
        if dt.isoweekday() == 1:
            return HttpResponse('No class')
        elif dt.isoweekday() == 2:
            return HttpResponse('No class')
        elif dt.isoweekday() == 3:
            print('PDS LINK {} ADDi link {}' .format(dictClassLink['PDS'], dictClassLink['ADDI']))
            return render(request, 'index.html')
        elif dt.isoweekday() == 4:
            return HttpResponse('No class')
        elif dt.isoweekday() == 5:
            return HttpResponse('No class')
        elif dt.isoweekday() == 6:
            return HttpResponse('No class')
        else:
            return HttpResponse('No class')

    #PERIOD 2- 09:45AM TO 10:45AM
    elif (timeNow > datetime.time(9,40,0, )) and (timeNow < datetime.time(9,55,0, )):
        print('block 2')
        if dt.isoweekday() == 1:
            return redirect(dictClassLink['MM'])
        elif dt.isoweekday() == 2:
            return redirect(dictClassLink['MM'])
        elif dt.isoweekday() == 3:
            return redirect(dictClassLink['DOME'])
        elif dt.isoweekday() == 4:
            return redirect(dictClassLink['CNC'])
        elif dt.isoweekday() == 5:
            return redirect(dictClassLink['PPCE'])
        elif dt.isoweekday() == 6:
            return redirect(dictClassLink['TWM'])
        else:
            return HttpResponse('no class now bro')

    #PERIOD 3- 11:00AM TO 12:00PM
    elif (timeNow > datetime.time(10,55,0, )) and (timeNow < datetime.time(11,10,0, )):
        print('block 3')
        if dt.isoweekday() == 1:
            return redirect(dictClassLink['CNC'])
        elif dt.isoweekday() == 2:
            return redirect(dictClassLink['PPCE'])
        elif dt.isoweekday() == 3:
            return redirect(dictClassLink['CNC'])
        elif dt.isoweekday() == 4:
            print('PDS LINK {} ADDi link {}' .format(dictClassLink['PDS'], dictClassLink['ADDI']))
        elif dt.isoweekday() == 5:
            print('PDS LINK {} ADDi link {}' .format(dictClassLink['PDS'], dictClassLink['ADDI']))
        elif dt.isoweekday() == 6:
            return redirect(dictClassLink['AHP'])
        else:
            return HttpResponse('no class now bro')

    #PERIOD 4- 1:45 TO 2:45
    elif (timeNow > datetime.time(13,40,0, )) and (timeNow < datetime.time(13,55,0, )):
        print('block 4')
        if dt.isoweekday() == 1:
            return redirect(dictClassLink['PPCE'])
        elif dt.isoweekday() == 2:
            return redirect(dictClassLink['MTL'])
        elif dt.isoweekday() == 3:
            return redirect(dictClassLink['MEL'])
        elif dt.isoweekday() == 4:
            return redirect(dictClassLink['DOME'])
        elif dt.isoweekday() == 5:
            return redirect(dictClassLink['AHP'])
        elif dt.isoweekday() == 6:
            print(dictClassLink['DOME'])
            return redirect(dictClassLink['DOME'])
        else:
            return HttpResponse('no class now bro')

    #PERIOD 5- 03:00PM TO 04:00PM
    elif (timeNow > datetime.time(14,55,0, )) and (timeNow < datetime.time(15,10,0, )):
        print('block 5')
        if dt.isoweekday() == 1:
            print(dictClassLink['AHP'])
        elif dt.isoweekday() == 2:
            print(dictClassLink['MTL'])
        elif dt.isoweekday() == 3:
            print(dictClassLink['MEL'])
        elif dt.isoweekday() == 4:
            print(dictClassLink['DOME'])
        elif dt.isoweekday() == 5:
            print(dictClassLink['MM'])
        elif dt.isoweekday() == 6:
            return HttpResponse('no class now bro')
        else:
            return HttpResponse('no class today bro')       
    
    else:
        print('lastelse')
        #return render(request, 'templates/index.html')
        return HttpResponse('<h1> no class link available currently </h1>') 
        #return render(request, 'index.html') 

def PDSjoin(request):
    return redirect('https://meet.google.com/dkw-qotg-qut') 

def ADDIjoin(request):
    
    return redirect('https://meet.google.com/yjp-odij-yec') 