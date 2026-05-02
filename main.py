from agents.analysis_agent import run as a
from agents.optimize_agent import run as o
from agents.review_agent import run as r

def run_all(code):
    return {"analysis":a(code),"optimize":o(code),"review":r(code)}
