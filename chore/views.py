from django.shortcuts import render
from .models import ChoreGroup, Chore
from django.shortcuts import redirect

def choregroupList(request):
    print('debug choregroupList')
    print(request)
    choregroups = ChoreGroup.objects.all().filter(author=request.user).order_by('-choregroup_name')
    return render(request, 'chore/index.html', {'choregroups':choregroups })

def choregroupCreate(request):
    print('debug choreGroupCreate')


    if request.method == 'POST':
        print(request.POST['choregroup_name'])
        print(request.POST['description'])
        print(request.POST)
        newchoreGroup = ChoreGroup.objects.create(
            choregroup_name=request.POST['choregroup_name'],
            description=request.POST['description'],
            author=request.user
        )
        print('new choregroupid:', newchoreGroup.id)
        for formName in request.POST:
            print('ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ',formName, request.POST[formName])
            if formName.startswith('chore_name'):
                choreNumber=formName.split("_")[2]
                sequenceField= 'chore_sequence_' + choreNumber
                Chore.objects.create(
                    chore_name=request.POST[formName],
                    sequence=request.POST[sequenceField],
                    choregroup=newchoreGroup
                )
        return redirect('choregroup_list')
    else:
        return render(request, 'chore/choregroup_create.html')


def choregroupUpdate(request, pk):
    print('debug choreGroupUpdate', pk)
    if request.method == 'POST':
        #update the choregroup
        choregroup = ChoreGroup.objects.get(pk=pk)
        choregroup.choregroup_name = request.POST['choregroup_name']
        choregroup.description = request.POST['description']
        choregroup.save()

        for formField in request.POST:
            #update (or delete) existing chores
            if formField.startswith('chore_name'):
                choreId=formField.split("_")[2]
                chore = Chore.objects.get(pk=choreId)
                chore.chore_name=request.POST[formField]
                sequence='chore_sequence_' + choreId
                chore.sequence=request.POST[sequence]
                if request.POST[formField] == '':
                    chore.delete()
                else:
                    chore.save()
            #TODO add new chores
            if formField.startswith('newchore_name'):
                newChoreId=formField.split("_")[2]
                sequenceField='newchore_sequence_' + newChoreId
                print('ddddddd',sequenceField)
                newChore = Chore(chore_name=request.POST[formField], sequence=request.POST[sequenceField],choregroup=choregroup)
                newChore.save()
                chore.chore_name=request.POST[formField]

        return redirect('choregroup_list')
    else:
        choregroup = ChoreGroup.objects.all().values('choregroup_name','description','Chore__chore_name','Chore__id','Chore__sequence').filter(pk=pk).order_by('-Chore__sequence')
        # choregroup = Chore.objects.all().values('chore_name','sequence','choregroup__choregroup_name','choregroup__description').filter(pk=pk)
        # print(choregroup.description)
        print(choregroup.query)
        for ddd in choregroup:
            print(ddd)
            print(ddd['choregroup_name'])
            print(ddd['description'])
            print(ddd['Chore__chore_name'],ddd['Chore__id'],ddd['Chore__sequence'])
        return render(request, 'chore/choregroup_update.html', {'choregroup':choregroup } )

def choregroupDelete(request,pk):
    ChoreGroup.objects.filter(pk=pk).delete()
    print('debug choreGroupDelete', pk)
    return redirect('choregroup_list')
