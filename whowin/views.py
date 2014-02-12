from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from whowin.forms import FighterSelectForm
from whowin.models import Fight, Fighter
from django.views.generic.edit import FormView


def random_fight(request):
    fight = Fight.objects.order_by('?')[0]
    return HttpResponseRedirect(reverse('fight_view', kwargs={"fight_id": str(fight.id)}))


class FightView(FormView):
    template_name = 'whowin/match.html'
    success_url = '/results/'

    def get_form(self, form_class):
        fight = Fight.objects.order_by('?')[0]
        choices = [(fight.member1.id, fight.member1.name),
                   (fight.member2.id, fight.member2.name)]
        kwargs = super(FightView, self).get_form_kwargs()
        kwargs.update({"choices": choices})
        form = FighterSelectForm(**kwargs)
        return form

    def form_valid(self, form):
        selected = Fighter.objects.get(id=form.cleaned_data['fighter_choices'])
        selected.rating += 100  # Use any logic to change rating here
        selected.save()
        print("Fighter selected: {}".format(selected.name))
        return super(FightView, self).form_valid(form)
	

class RankResultsView(ListView):
	queryset = Fighter.objects.order_by('-rating')
	context_object_name = 'fighter_list'
	template_name = 'whowin/results.html'

