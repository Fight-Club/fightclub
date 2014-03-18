from django.views.generic import ListView, DetailView, TemplateView
from whowin.forms import FighterSelectForm
from whowin.models import Fight, Fighter
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from random import randint


class FightView(FormView):

    fight = None
    template_name = 'whowin/match.html'

    def get_success_url(self):
        return reverse('home')

    def get_form(self, form_class):

        if self.kwargs['f1'] == self.kwargs['f2']:
            self.template_name = '404.html'

        a = Fighter.objects.get(id=self.kwargs['f1'])
        b = Fighter.objects.get(id=self.kwargs['f2'])
        if self.request.user.is_authenticated():
            self.fight = Fight(member1=a, member2=b, member1_start_rank=a.rank,
                               member2_start_rank=b.rank, member1_start_rating=a.rating,
                               member2_start_rating=b.rating, user=self.request.user)
        else:
            self.fight = Fight(member1=a, member2=b, member1_start_rank=a.rank,
                               member2_start_rank=b.rank, member1_start_rating=a.rating,
                               member2_start_rating=b.rating, user=None)

        choices = [(self.fight.member1.id, self.fight.member1.name),
                   (self.fight.member2.id, self.fight.member2.name)]
        kwargs = super(FightView, self).get_form_kwargs()
        kwargs.update({"choices": choices})
        form = FighterSelectForm(**kwargs)
        return form

    def form_valid(self, form):
        win = Fighter.objects.get(
            id=form.cleaned_data['who_would_win_in_a_fight_between'])

        if win == self.fight.member1:
            lose = self.fight.member2
        else:
            lose = self.fight.member1
        self.fight.rankupdate(win)
        self.fight.member1_end_rating = self.fight.member1.rating
        self.fight.member2_end_rating = self.fight.member2.rating
        self.fight.winner = win
        self.fight.loser = lose
        self.fight.save()

        fighterlist = list(Fighter.objects.order_by('-rating', 'name'))
        for fighter in fighterlist:
            r = fighterlist.index(fighter)
            r += 1
            fighter.rank = r
            fighter.save()
        self.fight.member1_end_rank = self.fight.member1.rank
        self.fight.member2_end_rank = self.fight.member2.rank
        self.fight.save()

        return super(FightView, self).form_valid(form)


class TopTenView(ListView):
    queryset = Fighter.objects.order_by('-rating')[:10]
    context_object_name = 'fighter_list'
    template_name = 'whowin/topten.html'


class BottomTenView(ListView):
    queryset = Fighter.objects.order_by('rating')[:10]
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


class StatsView(TemplateView):
    template_name = 'whowin/stats.html'

    def get_context_data(self, **kwargs):
        all_fighters = Fighter.objects.all()
        total = 0
        for member in all_fighters:
            total += member.fightswon
            num = Fighter.objects.count()
        context = super(StatsView, self).get_context_data(**kwargs)
        context['total'] = total
        context['numfighters'] = num
        return context


def home_view(request):
    last = Fighter.objects.count() - 1
    index1 = randint(0, last)
    index2 = randint(0, last - 1)
    if index2 == index1:
        index2 = last
    fi1 = Fighter.objects.all()[index1]
    fi2 = Fighter.objects.all()[index2]

    return HttpResponseRedirect(reverse('fight', kwargs={'f1': fi1.id,
                                                         'f2': fi2.id
                                                         }))
class UserStatsView(ListView):
    template_name = 'whowin/fighterlist.html'
    context_object_name = 'all_fighters'
    queryset = Fight.objects.filter(user=self.request.user)
