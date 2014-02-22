from django.views.generic import ListView
from whowin.forms import FighterSelectForm
from whowin.models import Fight, Fighter
from django.views.generic.edit import FormView


class FightView(FormView):

    fight = None
    template_name = 'whowin/match.html'
    success_url = '/results/'

    def get_form(self, form_class):
        self.fight = Fight.objects.order_by('?')[0]
        choices = [(self.fight.member1.id, self.fight.member1.name),
                   (self.fight.member2.id, self.fight.member2.name)]
        kwargs = super(FightView, self).get_form_kwargs()
        kwargs.update({"choices": choices})
        form = FighterSelectForm(**kwargs)
        return form

    def form_valid(self, form):
        winner = Fighter.objects.get(id=form.cleaned_data['fighter_choices'])
        self.fight.rankupdate(winner)
        print("Fighter winner: {}".format(winner.name))
        return super(FightView, self).form_valid(form)
	

class RankResultsView(ListView):
	queryset = Fighter.objects.order_by('-rating')
	context_object_name = 'fighter_list'
	template_name = 'whowin/results.html'

