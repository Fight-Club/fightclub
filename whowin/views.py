from django.views.generic import ListView, DetailView, TemplateView
from whowin.forms import FighterSelectForm
from whowin.models import Fight, Fighter
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class FightView(FormView):
    
    fight = None
    template_name = 'whowin/match.html'

    def get_success_url(self): 
        return reverse('home') 
    

    def get_form(self, form_class):
        self.fight = get_object_or_404(Fight, pk=self.kwargs['id'])
        choices = [(self.fight.member1.id, self.fight.member1.name),
                   (self.fight.member2.id, self.fight.member2.name)]
        kwargs = super(FightView, self).get_form_kwargs()
        kwargs.update({"choices": choices})
        form = FighterSelectForm(**kwargs)
        return form

    def form_valid(self, form):
        winner = Fighter.objects.get(id=form.cleaned_data['who_would_win_in_a_fight_between'])
        self.fight.rankupdate(winner)
        return super(FightView, self).form_valid(form)
	

class TopTenView(ListView):
    queryset = Fighter.objects.order_by('rank')[:10]
    context_object_name = 'fighter_list'
    template_name = 'whowin/topten.html'


class BottomTenView(ListView):
    queryset = Fighter.objects.order_by('-rank')[:10]
    context_object_name = 'fighter_list'
    template_name = 'whowin/bottomten.html'


class FighterDetailView(DetailView):
    model = Fighter
    template_name = 'whowin/fighterdetail.html'


class FighterListView(ListView):
    template_name = 'whowin/fighterlist.html'
    context_object_name = 'all_fighters'
    queryset = Fighter.objects.order_by('name')

class AboutView(TemplateView):
    template_name = 'whowin/about.html'

def stats_view(request):
    total = 0
    all_fighters = Fighter.objects.all()
    for member in all_fighters:
        total += member.fightswon
        total += member.fightslost
    total = total/2

    return render_to_response('whowin/stats.html', {'total': total})

def home_view(request):
    next = Fight.objects.order_by('?')[0]
    return HttpResponseRedirect(reverse('fight', kwargs={'id': next.pk}))