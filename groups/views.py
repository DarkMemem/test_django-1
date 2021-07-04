from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import UpdateView

from .models import Group
from .forms import GroupCreateForm


def get_groups(request):
    groups = Group.objects.all()

    # extra_context = {'groups': Group.objects.all()}

    return render(request, 'groups/list.html', {'groups': groups})


def create_group(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request,
        'groups/create.html',
        context={'form': form}
    )


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
            # 'group': group,
            # 'students': group.students.all(),
            'students': group.students.select_related('group', 'headed_group').all()
        }
    )


def delete_group(request, pk):
    pass


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'

    pk_url_kwarg = 'ppk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.select_related('group', 'headed_group').all()

        return context
