from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Group
from .forms import GroupCreateForm


def get_groups(request):
    groups = Group.objects.all()

    return render(request, 'groups/list.html', {'groups': groups})


def create_group(request):
    pass


def update_group(request, pk):
    group = get_object_or_404(Group, id=pk)

    if request.method == 'POST':
        form = GroupCreateForm(request.POST, instance=group)

        if form.is_valid():
            group = form.save()
            print(f'Group has been saved: {group}')
            return HttpResponseRedirect(reverse('groups:list'))
    else:
        form = GroupCreateForm(
            instance=group
        )

    return render(request, 'groups/update.html', context={
            'form': form,
            'group': group,
            # 'students': group.students.all(),
            'students': group.students.select_related('headed_group').all()
        }
    )


def delete_group(request, pk):
    pass
