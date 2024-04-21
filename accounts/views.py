from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import * #OrderForm, AnthonyOffenseForm, AnthonyOffenseForm,  CreateUserForm
from .filters import OrderFilter


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, 'Username or Password is Incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def homePage(request):
    context = {}
    return render(request, 'accounts/homepage.html', context) 

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products' :products})
    

#anthony------------------------------------------------------------------------------------
@login_required(login_url='login')
def anthony(request):
    anthonyoffenses = AnthonyOffense.objects.all()
    anthonystudents = AnthonyStudent.objects.all()

    total_students = anthonystudents.count()
    total_offenses = anthonyoffenses.count()
    minor = anthonyoffenses.filter(category='Minor').count()
    major = anthonyoffenses.filter(category='Major').count()

    #myFilter = OrderFilter(request.GET, queryset = anthonyoffenses)
    #anthonyoffenses = myFilter.qs

    context = {'offenses' :anthonyoffenses, 'students': anthonystudents,
    'total_offenses': total_offenses, 'minor': minor, 'major': major,} #'myFilter': myFilter}

    return render(request, 'accounts/anthony.html', context)

@login_required(login_url='login')
def anthonyprofile(request, pk_test):
    anthonystudents = AnthonyStudent.objects.get(id=pk_test)

    anthonyoffenses = anthonystudents.anthonyoffense_set.all()
    offense_count = anthonyoffenses.count()

    myFilter = OrderFilter(request.GET, queryset = anthonyoffenses)
    anthonyoffenses = myFilter.qs

    context = {'students': anthonystudents, 'offenses': anthonyoffenses, "offense_count": offense_count, 'myFilter': myFilter}
    return render(request, 'accounts/anthonyprofile.html', context)    

@login_required(login_url='login')
def anthonycreateOffense(request, pk):
    
    name = AnthonyStudent.objects.get(id=pk)
    anthonyoffenses = name.anthonyoffense_set.all()
    
    anthonyform = AnthonyOffenseForm(initial={'name': name})
    
    if request.method == 'POST':
        anthonyform = AnthonyOffenseForm(request.POST)
        if anthonyform.is_valid():
            anthonyform.save()
            return redirect('anthony')

    context = {'anthonyform': anthonyform, 'students': name, 'offenses': anthonyoffenses}
    return render(request, 'accounts/anthonyoffense_form.html', context)

@login_required(login_url='login')
def anthonyupdateOffense(request, pk):

    anthonyoffense = AnthonyOffense.objects.get(id=pk)
    anthonyform = AnthonyOffenseForm(instance=anthonyoffense)
    
    if request.method == 'POST':
        anthonyform = AnthonyOffenseForm(request.POST, instance=anthonyoffense)
        if anthonyform.is_valid():
            anthonyform.save()
            return redirect('anthony')

    context = {'anthonyform': anthonyform}
    return render(request, 'accounts/anthonyoffense_form.html', context)

@login_required(login_url='login')
def anthonydeleteOffense(request, pk):
    anthonyoffense = AnthonyOffense.objects.get(id=pk)
    if request.method == "POST":
        anthonyoffense.delete()
        return redirect('anthony')
    context = {'item': anthonyoffense}
    return render(request, 'accounts/anthonydelete.html', context)


#charles------------------------------------------------------------------------------------
@login_required(login_url='login')
def charles(request):
    charlesoffenses = CharlesOffense.objects.all()
    charlesstudents = CharlesStudent.objects.all()

    total_students = charlesstudents.count()
    total_offenses = charlesoffenses.count()
    minor = charlesoffenses.filter(category='Minor').count()
    major = charlesoffenses.filter(category='Major').count()

    #myFilter = OrderFilter(request.GET, queryset = anthonyoffenses)
    #anthonyoffenses = myFilter.qs

    context = {'offenses' :charlesoffenses, 'students': charlesstudents,
    'total_offenses': total_offenses, 'minor': minor, 'major': major,} #'myFilter': myFilter}

    return render(request, 'accounts/charles.html', context)

@login_required(login_url='login')
def charlesprofile(request, pk_test):
    charlesstudents = CharlesStudent.objects.get(id=pk_test)

    charlesoffenses = charlesstudents.charlesoffense_set.all()
    offense_count = charlesoffenses.count()

    context = {'students': charlesstudents, 'offenses': charlesoffenses, "offense_count": offense_count,}
    return render(request, 'accounts/charlesprofile.html', context)

@login_required(login_url='login')
def charlescreateOffense(request, pk):
    
    name = CharlesStudent.objects.get(id=pk)
    charlesoffenses = name.charlesoffense_set.all()
    
    charlesform = CharlesOffenseForm(initial={'name': name})
    if request.method == 'POST':
        charlesform = CharlesOffenseForm(request.POST)
        if charlesform.is_valid():
            charlesform.save()
            return redirect('charles')

    context = {'charlesform': charlesform, 'students': name, 'offenses': charlesoffenses}
    return render(request, 'accounts/charlesoffense_form.html', context)

@login_required(login_url='login')
def charlesupdateOffense(request, pk):

    charlesoffense = CharlesOffense.objects.get(id=pk)
    charlesform = CharlesOffenseForm(instance=charlesoffense)
    
    if request.method == 'POST':
        charlesform = CharlesOffenseForm(request.POST, instance=charlesoffense)
        if charlesform.is_valid():
            charlesform.save()
            return redirect('charles')

    context = {'charlesform': charlesform}
    return render(request, 'accounts/charlesoffense_form.html', context)

@login_required(login_url='login')
def charlesdeleteOffense(request, pk):
    charlesoffense = CharlesOffense.objects.get(id=pk)
    if request.method == "POST":
        charlesoffense.delete()
        return redirect('charles')
    context = {'item': charlesoffense}
    return render(request, 'accounts/charlesdelete.html', context)

#berchman------------------------------------------------------------------------------------
@login_required(login_url='login')
def berchman(request):
    berchmanoffenses = BerchmanOffense.objects.all()
    berchmanstudents = BerchmanStudent.objects.all()

    total_students = berchmanstudents.count()
    total_offenses = berchmanoffenses.count()
    minor = berchmanoffenses.filter(category='Minor').count()
    major = berchmanoffenses.filter(category='Major').count()


    context = {'offenses' :berchmanoffenses, 'students': berchmanstudents,
    'total_offenses': total_offenses, 'minor': minor, 'major': major,}

    return render(request, 'accounts/berchman.html', context)

@login_required(login_url='login')
def berchmanprofile(request, pk_test):
    berchmanstudents = BerchmanStudent.objects.get(id=pk_test)

    berchmanoffenses = berchmanstudents.berchmanoffense_set.all()
    offense_count = berchmanoffenses.count()

    context = {'students': berchmanstudents, 'offenses': berchmanoffenses, "offense_count": offense_count,}
    return render(request, 'accounts/berchmanprofile.html', context)

@login_required(login_url='login')
def berchmancreateOffense(request, pk):
    
    name = BerchmanStudent.objects.get(id=pk)
    berchmanoffenses = name.berchmanoffense_set.all()
    
    berchmanform = BerchmanOffenseForm(initial={'name': name})
    if request.method == 'POST':
        berchmanform = BerchmanOffenseForm(request.POST)
        if berchmanform.is_valid():
            berchmanform.save()
            return redirect('berchman')

    context = {'berchmanform': berchmanform, 'students': name, 'offenses': berchmanoffenses}
    return render(request, 'accounts/berchmanoffense_form.html', context)

@login_required(login_url='login')
def berchmanupdateOffense(request, pk):

    berchmanoffense = BerchmanOffense.objects.get(id=pk)
    berchmanform = BerchmanOffenseForm(instance=berchmanoffense)
    
    if request.method == 'POST':
        berchmanform = BerchmanOffenseForm(request.POST, instance=berchmanoffense)
        if berchmanform.is_valid():
            berchmanform.save()
            return redirect('charles')

    context = {'berchmanform': berchmanform}
    return render(request, 'accounts/berchmanoffense_form.html', context)

@login_required(login_url='login')
def berchmandeleteOffense(request, pk):
    berchmanoffense = BerchmanOffense.objects.get(id=pk)
    if request.method == "POST":
        berchmanoffense.delete()
        return redirect('berchman')
    context = {'item': berchmanoffense}
    return render(request, 'accounts/berchmandelete.html', context)

#bosco------------------------------------------------------------------------------------
@login_required(login_url='login')
def bosco(request):
    boscooffenses = BoscoOffense.objects.all()
    boscostudents = BoscoStudent.objects.all()

    total_students = boscostudents.count()
    total_offenses = boscooffenses.count()
    minor = boscooffenses.filter(category='Minor').count()
    major = boscooffenses.filter(category='Major').count()


    context = {'offenses' :boscooffenses, 'students': boscostudents,
    'total_offenses': total_offenses, 'minor': minor, 'major': major,}

    return render(request, 'accounts/bosco.html', context)

@login_required(login_url='login')
def boscoprofile(request, pk_test):
    boscostudents = BoscoStudent.objects.get(id=pk_test)

    boscooffenses = boscostudents.boscooffense_set.all()
    offense_count = boscooffenses.count()

    context = {'students': boscostudents, 'offenses': boscooffenses, "offense_count": offense_count,}
    return render(request, 'accounts/boscoprofile.html', context)

@login_required(login_url='login')
def boscocreateOffense(request, pk):
    
    name = BoscoStudent.objects.get(id=pk)
    boscooffenses = name.boscooffense_set.all()
    
    boscoform = BoscoOffenseForm(initial={'name': name})
    if request.method == 'POST':
        boscoform = BoscoOffenseForm(request.POST)
        if boscoform.is_valid():
            boscoform.save()
            return redirect('bosco')

    context = {'boscoform': boscoform, 'students': name, 'offenses': boscooffenses}
    return render(request, 'accounts/boscooffense_form.html', context)

@login_required(login_url='login')
def boscoupdateOffense(request, pk):

    boscooffense = BoscoOffense.objects.get(id=pk)
    boscoform = BoscoOffenseForm(instance=boscooffense)
    
    if request.method == 'POST':
        boscoform = BoscoOffenseForm(request.POST, instance=boscooffense)
        if boscoform.is_valid():
            boscoform.save()
            return redirect('bosco')

    context = {'boscoform': boscoform}
    return render(request, 'accounts/boscooffense_form.html', context)

@login_required(login_url='login')
def boscodeleteOffense(request, pk):
    boscooffense = BoscoOffense.objects.get(id=pk)
    if request.method == "POST":
        boscooffense.delete()
        return redirect('bosco')
    context = {'item': boscooffense}
    return render(request, 'accounts/boscodelete.html', context)

#joseph------------------------------------------------------------------------------------
@login_required(login_url='login')
def joseph(request):
    josephoffenses = JosephOffense.objects.all()
    josephstudents = JosephStudent.objects.all()

    total_students = josephstudents.count()
    total_offenses = josephoffenses.count()
    minor = josephoffenses.filter(category='Minor').count()
    major = josephoffenses.filter(category='Major').count()


    context = {'offenses' :josephoffenses, 'students': josephstudents,
    'total_offenses': total_offenses, 'minor': minor, 'major': major,}

    return render(request, 'accounts/joseph.html', context)

@login_required(login_url='login')
def josephprofile(request, pk_test):
    josephstudents = JosephStudent.objects.get(id=pk_test)

    josephoffenses = josephstudents.josephoffense_set.all()
    offense_count = josephoffenses.count()

    context = {'students': josephstudents, 'offenses': josephoffenses, "offense_count": offense_count,}
    return render(request, 'accounts/josephprofile.html', context)

@login_required(login_url='login')
def josephcreateOffense(request, pk):
    
    name = JosephStudent.objects.get(id=pk)
    josephoffenses = name.josephoffense_set.all()
    
    josephform = JosephOffenseForm(initial={'name': name})
    if request.method == 'POST':
        josephform = JosephOffenseForm(request.POST)
        if josephform.is_valid():
            josephform.save()
            return redirect('joseph')

    context = {'josephform': josephform, 'students': name, 'offenses': josephoffenses}
    return render(request, 'accounts/josephoffense_form.html', context)

@login_required(login_url='login')
def josephupdateOffense(request, pk):

    josephoffense = JosephOffense.objects.get(id=pk)
    josephform = JosephOffenseForm(instance=josephoffense)
    
    if request.method == 'POST':
        josephform = JosephOffenseForm(request.POST, instance=josephoffense)
        if josephform.is_valid():
            josephform.save()
            return redirect('joseph')

    context = {'josephform': josephform}
    return render(request, 'accounts/josephoffense_form.html', context)

@login_required(login_url='login')
def josephdeleteOffense(request, pk):
    josephoffense = JosephOffense.objects.get(id=pk)
    if request.method == "POST":
        josephoffense.delete()
        return redirect('joseph')
    context = {'item': josephoffense}
    return render(request, 'accounts/josephdelete.html', context)

#martin------------------------------------------------------------------------------------
@login_required(login_url='login')
def martin(request):
    martinoffenses = MartinOffense.objects.all()
    martinstudents = MartinStudent.objects.all()

    total_students = martinstudents.count()
    total_offenses = martinoffenses.count()
    minor = martinoffenses.filter(category='Minor').count()
    major = martinoffenses.filter(category='Major').count()


    context = {'offenses' :martinoffenses, 'students': martinstudents,
    'total_offenses': total_offenses, 'minor': minor, 'major': major,}

    return render(request, 'accounts/martin.html', context)

@login_required(login_url='login')
def martinprofile(request, pk_test):
    martinstudents = MartinStudent.objects.get(id=pk_test)

    martinoffenses = martinstudents.martinoffense_set.all()
    offense_count = martinoffenses.count()

    context = {'students': martinstudents, 'offenses': martinoffenses, "offense_count": offense_count,}
    return render(request, 'accounts/martinprofile.html', context)

@login_required(login_url='login')
def martincreateOffense(request, pk):
    
    name = MartinStudent.objects.get(id=pk)
    martinoffenses = name.martinoffense_set.all()
    
    martinform = MartinOffenseForm(initial={'name': name})
    if request.method == 'POST':
        martinform = MartinOffenseForm(request.POST)
        if martinform.is_valid():
            martinform.save()
            return redirect('martin')

    context = {'martinform': martinform, 'students': name, 'offenses': martinoffenses}
    return render(request, 'accounts/martinoffense_form.html', context)

@login_required(login_url='login')
def martinupdateOffense(request, pk):

    martinoffense = MartinOffense.objects.get(id=pk)
    martinform =  MartinOffenseForm(instance=martinoffense)
    
    if request.method == 'POST':
        martinform = MartinOffenseForm(request.POST, instance=martinoffense)
        if martinform.is_valid():
            martinform.save()
            return redirect('martin')

    context = {'martinform': martinform}
    return render(request, 'accounts/martinoffense_form.html', context)

@login_required(login_url='login')
def martindeleteOffense(request, pk):
    martinoffense = MartinOffense.objects.get(id=pk)
    if request.method == "POST":
        martinoffense.delete()
        return redirect('martin')
    context = {'item': martinoffense}
    return render(request, 'accounts/martindelete.html', context)

#paul------------------------------------------------------------------------------------
@login_required(login_url='login')
def paul(request):
    pauloffenses = PaulOffense.objects.all()
    paulstudents = PaulStudent.objects.all()

    total_students = paulstudents.count()
    total_offenses = pauloffenses.count()
    minor = pauloffenses.filter(category='Minor').count()
    major = pauloffenses.filter(category='Major').count()


    context = {'offenses' :pauloffenses, 'students': paulstudents,
    'total_offenses': total_offenses, 'minor': minor, 'major': major,}

    return render(request, 'accounts/paul.html', context)

@login_required(login_url='login')
def paulprofile(request, pk_test):
    paulstudents = PaulStudent.objects.get(id=pk_test)

    pauloffenses = paulstudents.pauloffense_set.all()
    offense_count = pauloffenses.count()

    context = {'students': paulstudents, 'offenses': pauloffenses, "offense_count": offense_count,}
    return render(request, 'accounts/paulprofile.html', context)

@login_required(login_url='login')
def paulcreateOffense(request, pk):
    
    name = PaulStudent.objects.get(id=pk)
    pauloffenses = name.pauloffense_set.all()
    
    paulform = PaulOffenseForm(initial={'name': name})
    if request.method == 'POST':
        paulform = PaulOffenseForm(request.POST)
        if paulform.is_valid():
            paulform.save()
            return redirect('paul')

    context = {'paulform': paulform, 'students': name, 'offenses': pauloffenses}
    return render(request, 'accounts/pauloffense_form.html', context)

@login_required(login_url='login')
def paulupdateOffense(request, pk):

    pauloffense = PaulOffense.objects.get(id=pk)
    paulform =  PaulOffenseForm(instance=pauloffense)
    
    if request.method == 'POST':
        paulform = PaulOffenseForm(request.POST, instance=pauloffense)
        if paulform.is_valid():
            paulform.save()
            return redirect('paul')

    context = {'paulform': paulform}
    return render(request, 'accounts/pauloffense_form.html', context)

@login_required(login_url='login')
def pauldeleteOffense(request, pk):
    pauloffense = PaulOffense.objects.get(id=pk)
    if request.method == "POST":
        pauloffense.delete()
        return redirect('paul')
    context = {'item': pauloffense}
    return render(request, 'accounts/pauldelete.html', context)

#anne------------------------------------------------------------------------------------
@login_required(login_url='login')
def anne(request):
    anneoffenses = AnneOffense.objects.all()
    annestudents = AnneStudent.objects.all()

    total_students = annestudents.count()
    total_offenses = anneoffenses.count()
    minor = anneoffenses.filter(category='Minor').count()
    major = anneoffenses.filter(category='Major').count()


    context = {'offenses' :anneoffenses, 'students': annestudents,
    'total_offenses': total_offenses, 'minor': minor, 'major': major,}

    return render(request, 'accounts/anne.html', context)

@login_required(login_url='login')
def anneprofile(request, pk_test):
    annestudents = AnneStudent.objects.get(id=pk_test)

    anneoffenses = annestudents.anneoffense_set.all()
    offense_count = anneoffenses.count()

    context = {'students': annestudents, 'offenses': anneoffenses, "offense_count": offense_count,}
    return render(request, 'accounts/anneprofile.html', context)

@login_required(login_url='login')
def annecreateOffense(request, pk):
    
    name = AnneStudent.objects.get(id=pk)
    anneoffenses = name.anneoffense_set.all()
    
    anneform = AnneOffenseForm(initial={'name': name})
    if request.method == 'POST':
        anneform = AnneOffenseForm(request.POST)
        if anneform.is_valid():
            anneform.save()
            return redirect('anne')

    context = {'anneform': anneform, 'students': name, 'offenses': anneoffenses}
    return render(request, 'accounts/anneoffense_form.html', context)

@login_required(login_url='login')
def anneupdateOffense(request, pk):

    anneoffense = AnneOffense.objects.get(id=pk)
    anneform =  AnneOffenseForm(instance=anneoffense)
    
    if request.method == 'POST':
        anneform = AnneOffenseForm(request.POST, instance=anneoffense)
        if anneform.is_valid():
            anneform.save()
            return redirect('anne')

    context = {'anneform': anneform}
    return render(request, 'accounts/anneoffense_form.html', context)

@login_required(login_url='login')
def annedeleteOffense(request, pk):
    anneoffense = AnneOffense.objects.get(id=pk)
    if request.method == "POST":
        anneoffense.delete()
        return redirect('anne')
    context = {'item': anneoffense}
    return render(request, 'accounts/annedelete.html', context)

#faustina------------------------------------------------------------------------------------
@login_required(login_url='login')
def faustina(request):
    faustinaoffenses = FaustinaOffense.objects.all()
    faustinastudents = FaustinaStudent.objects.all()

    total_students = faustinastudents.count()
    total_offenses = faustinaoffenses.count()
    minor = faustinaoffenses.filter(category='Minor').count()
    major = faustinaoffenses.filter(category='Major').count()

    context = {'offenses' :faustinaoffenses, 'students': faustinastudents,
    'total_offenses': total_offenses, 'minor': minor, 'major': major,}

    return render(request, 'accounts/faustina.html', context)

@login_required(login_url='login')
def faustinaprofile(request, pk_test):
    faustinastudents = FaustinaStudent.objects.get(id=pk_test)

    faustinaoffenses = faustinastudents.faustinaoffense_set.all()
    offense_count = faustinaoffenses.count()

    context = {'students': faustinastudents, 'offenses': faustinaoffenses, "offense_count": offense_count,}
    return render(request, 'accounts/faustinaprofile.html', context)

@login_required(login_url='login')
def faustinacreateOffense(request, pk):
    
    name = FaustinaStudent.objects.get(id=pk)
    faustinaoffenses = name.faustinaoffense_set.all()
    
    faustinaform = FaustinaOffenseForm(initial={'name': name})
    if request.method == 'POST':
        faustinaform = FaustinaOffenseForm(request.POST)
        if faustinaform.is_valid():
            faustinaform.save()
            return redirect('faustina')

    context = {'faustinaform': faustinaform, 'students': name, 'offenses': faustinaoffenses}
    return render(request, 'accounts/faustinaoffense_form.html', context)

@login_required(login_url='login')
def faustinaupdateOffense(request, pk):

    faustinaoffense = FaustinaOffense.objects.get(id=pk)
    faustinaform =  FaustinaOffenseForm(instance=faustinaoffense)
    
    if request.method == 'POST':
        faustinaform = FaustinaOffenseForm(request.POST, instance=faustinaoffense)
        if faustinaform.is_valid():
            faustinaform.save()
            return redirect('faustina')

    context = {'faustinaform': faustinaform}
    return render(request, 'accounts/faustinaoffense_form.html', context)

@login_required(login_url='login')
def faustinadeleteOffense(request, pk):
    faustinaoffense = FaustinaOffense.objects.get(id=pk)
    if request.method == "POST":
        faustinaoffense.delete()
        return redirect('faustina')
    context = {'item': faustinaoffense}
    return render(request, 'accounts/faustinadelete.html', context)

#mary------------------------------------------------------------------------------------
@login_required(login_url='login')
def mary(request):
    maryoffenses = MaryOffense.objects.all()
    marystudents = MaryStudent.objects.all()

    total_students = marystudents.count()
    total_offenses = maryoffenses.count()
    minor = maryoffenses.filter(category='Minor').count()
    major = maryoffenses.filter(category='Major').count()

    context = {'offenses' :maryoffenses, 'students': marystudents,
    'total_offenses': total_offenses, 'minor': minor, 'major': major,}

    return render(request, 'accounts/mary.html', context)

@login_required(login_url='login')
def maryprofile(request, pk_test):
    marystudents = MaryStudent.objects.get(id=pk_test)

    maryoffenses = marystudents.maryoffense_set.all()
    offense_count = maryoffenses.count()

    context = {'students': marystudents, 'offenses': maryoffenses, "offense_count": offense_count,}
    return render(request, 'accounts/maryprofile.html', context)

@login_required(login_url='login')
def marycreateOffense(request, pk):
    
    name = MaryStudent.objects.get(id=pk)
    maryoffenses = name.maryoffense_set.all()
    
    maryform = MaryOffenseForm(initial={'name': name})
    if request.method == 'POST':
        maryform = MaryOffenseForm(request.POST)
        if maryform.is_valid():
            maryform.save()
            return redirect('mary')

    context = {'maryform': maryform, 'students': name, 'offenses': maryoffenses}
    return render(request, 'accounts/maryoffense_form.html', context)

@login_required(login_url='login')
def maryupdateOffense(request, pk):

    maryoffense = MaryOffense.objects.get(id=pk)
    maryform =  MaryOffenseForm(instance=maryoffense)
    
    if request.method == 'POST':
        maryform = MaryOffenseForm(request.POST, instance=maryoffense)
        if maryform.is_valid():
            maryform.save()
            return redirect('mary')

    context = {'maryform': maryform}
    return render(request, 'accounts/maryoffense_form.html', context)

@login_required(login_url='login')
def marydeleteOffense(request, pk):
    maryoffense = MaryOffense.objects.get(id=pk)
    if request.method == "POST":
        maryoffense.delete()
        return redirect('mary')
    context = {'item': maryoffense}
    return render(request, 'accounts/marydelete.html', context)

#rita------------------------------------------------------------------------------------
@login_required(login_url='login')
def rita(request):
    ritaoffenses = RitaOffense.objects.all()
    ritastudents = RitaStudent.objects.all()

    total_students = ritastudents.count()
    total_offenses = ritaoffenses.count()
    minor = ritaoffenses.filter(category='Minor').count()
    major = ritaoffenses.filter(category='Major').count()

    context = {'offenses' :ritaoffenses, 'students': ritastudents,
    'total_offenses': total_offenses, 'minor': minor, 'major': major,}

    return render(request, 'accounts/rita.html', context)

@login_required(login_url='login')
def ritaprofile(request, pk_test):
    ritastudents = RitaStudent.objects.get(id=pk_test)

    ritaoffenses = ritastudents.ritaoffense_set.all()
    offense_count = ritaoffenses.count()

    context = {'students': ritastudents, 'offenses': ritaoffenses, "offense_count": offense_count,}
    return render(request, 'accounts/ritaprofile.html', context)

@login_required(login_url='login')
def ritacreateOffense(request, pk):
    
    name = RitaStudent.objects.get(id=pk)
    ritaoffenses = name.ritaoffense_set.all()
    
    ritaform = RitaOffenseForm(initial={'name': name})
    if request.method == 'POST':
        ritaform = RitaOffenseForm(request.POST)
        if ritaform.is_valid():
            ritaform.save()
            return redirect('rita')

    context = {'ritaform': ritaform, 'students': name, 'offenses': ritaoffenses}
    return render(request, 'accounts/ritaoffense_form.html', context)

@login_required(login_url='login')
def ritaupdateOffense(request, pk):

    ritaoffense = RitaOffense.objects.get(id=pk)
    ritaform =  RitaOffenseForm(instance=ritaoffense)
    
    if request.method == 'POST':
        ritaform = RitaOffenseForm(request.POST, instance=ritaoffense)
        if ritaform.is_valid():
            ritaform.save()
            return redirect('rita')

    context = {'ritaform': ritaform}
    return render(request, 'accounts/ritaoffense_form.html', context)

@login_required(login_url='login')
def ritadeleteOffense(request, pk):
    ritaoffense = RitaOffense.objects.get(id=pk)
    if request.method == "POST":
        ritaoffense.delete()
        return redirect('rita')
    context = {'item': ritaoffense}
    return render(request, 'accounts/ritadelete.html', context)

#rose------------------------------------------------------------------------------------
@login_required(login_url='login')
def rose(request):
    roseoffenses = RoseOffense.objects.all()
    rosestudents = RoseStudent.objects.all()

    total_students = rosestudents.count()
    total_offenses = roseoffenses.count()
    minor = roseoffenses.filter(category='Minor').count()
    major = roseoffenses.filter(category='Major').count()

    context = {'offenses' :roseoffenses, 'students': rosestudents,
    'total_offenses': total_offenses, 'minor': minor, 'major': major,}

    return render(request, 'accounts/rose.html', context)

@login_required(login_url='login')
def roseprofile(request, pk_test):
    rosestudents = RoseStudent.objects.get(id=pk_test)

    roseoffenses = rosestudents.roseoffense_set.all()
    offense_count = roseoffenses.count()

    context = {'students': rosestudents, 'offenses': roseoffenses, "offense_count": offense_count,}
    return render(request, 'accounts/roseprofile.html', context)

@login_required(login_url='login')
def rosecreateOffense(request, pk):
    
    name = RoseStudent.objects.get(id=pk)
    roseoffenses = name.roseoffense_set.all()
    
    roseform = RoseOffenseForm(initial={'name': name})
    if request.method == 'POST':
        roseform = RoseOffenseForm(request.POST)
        if roseform.is_valid():
            roseform.save()
            return redirect('rose')

    context = {'roseform': roseform, 'students': name, 'offenses': roseoffenses}
    return render(request, 'accounts/roseoffense_form.html', context)

@login_required(login_url='login')
def roseupdateOffense(request, pk):

    roseoffense = RoseOffense.objects.get(id=pk)
    roseform =  RoseOffenseForm(instance=roseoffense)
    
    if request.method == 'POST':
        roseform = RoseOffenseForm(request.POST, instance=roseoffense)
        if roseform.is_valid():
            roseform.save()
            return redirect('rose')

    context = {'roseform': roseform}
    return render(request, 'accounts/roseoffense_form.html', context)

@login_required(login_url='login')
def rosedeleteOffense(request, pk):
    roseoffense = RoseOffense.objects.get(id=pk)
    if request.method == "POST":
        roseoffense.delete()
        return redirect('rose')
    context = {'item': roseoffense}
    return render(request, 'accounts/rosedelete.html', context)

#teresa------------------------------------------------------------------------------------
@login_required(login_url='login')
def teresa(request):
    teresaoffenses = TeresaOffense.objects.all()
    teresastudents = TeresaStudent.objects.all()

    total_students = teresastudents.count()
    total_offenses = teresaoffenses.count()
    minor = teresaoffenses.filter(category='Minor').count()
    major = teresaoffenses.filter(category='Major').count()

    context = {'offenses' :teresaoffenses, 'students': teresastudents,
    'total_offenses': total_offenses, 'minor': minor, 'major': major,}

    return render(request, 'accounts/teresa.html', context)

@login_required(login_url='login')
def teresaprofile(request, pk_test):
    teresastudents = TeresaStudent.objects.get(id=pk_test)

    teresaoffenses = teresastudents.teresaoffense_set.all()
    offense_count = teresaoffenses.count()

    context = {'students': teresastudents, 'offenses': teresaoffenses, "offense_count": offense_count,}
    return render(request, 'accounts/teresaprofile.html', context)

@login_required(login_url='login')
def teresacreateOffense(request, pk):
    
    name = TeresaStudent.objects.get(id=pk)
    teresaoffenses = name.teresaoffense_set.all()
    
    teresaform = TeresaOffenseForm(initial={'name': name})
    if request.method == 'POST':
        teresaform = TeresaOffenseForm(request.POST)
        if teresaform.is_valid():
            teresaform.save()
            return redirect('/')

    context = {'teresaform': teresaform, 'students': name, 'offenses': teresaoffenses}
    return render(request, 'accounts/teresaoffense_form.html', context)

@login_required(login_url='login')
def teresaupdateOffense(request, pk):

    teresaoffense = TeresaOffense.objects.get(id=pk)
    teresaform =  TeresaOffenseForm(instance=teresaoffense)
    
    if request.method == 'POST':
        teresaform = TeresaOffenseForm(request.POST, instance=teresaoffense)
        if teresaform.is_valid():
            teresaform.save()
            return redirect('/')

    context = {'teresaform': teresaform}
    return render(request, 'accounts/teresaoffense_form.html', context)

@login_required(login_url='login')
def teresadeleteOffense(request, pk):
    teresaoffense = TeresaOffense.objects.get(id=pk)
    if request.method == "POST":
        teresaoffense.delete()
        return redirect('/')
    context = {'item': teresaoffense}
    return render(request, 'accounts/teresadelete.html', context)






#original code (the foundation)

#@login_required(login_url='login')
#def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders' :orders, 'customers': customers, 
    'total_orders': total_orders, 'delivered': delivered, 'pending': pending}

    return render(request, 'accounts/dashboard.html', context)



#@login_required(login_url='login')
#def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset = orders)
    orders = myFilter.qs

    context = {'customer': customer, 'orders': orders, "order_count": order_count, 'myFilter': myFilter}
    return render(request, 'accounts/customer.html', context)    

#@login_required(login_url='login')
#def createOrder(request, pk):
    customer = Customer.objects.get(id=pk)

    form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

#@login_required(login_url='login')
#def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

#@login_required(login_url='login')
#def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
