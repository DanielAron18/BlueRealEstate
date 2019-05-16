from django.shortcuts import render, get_object_or_404
from agent.models import Agent


# Create your views here.
def agent_profile(request, id):
    return render(request, './user/agent_profile.html', {
        'AgentProfile': get_object_or_404(Agent, pk=id)
    })
