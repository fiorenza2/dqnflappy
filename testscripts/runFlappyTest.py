from ple.games.flappybird import FlappyBird
from ple import PLE
from DQNAgent import *

# #===============================DEBUG BEGIN============================##
# import sys
# sys.path.append("pycharm-debug-py3k.egg")
# import pydevd
#
# pydevd.settrace('127.0.0.1', port=5678, stdoutToServer=True,
# stderrToServer=True)
# #================================DEBUG END=============================##

game = FlappyBird()
p = PLE(game, fps=30, display_screen=True, frame_skip=2, force_fps=False)
p.init()

flappy_agent = DQNAgent(p.getActionSet(), frame_stack=4)

flappy_tester = Tester(p, flappy_agent, 84)
flappy_tester.load_model('models/last_trained_model.pth')
flappy_agent.eps = 0.01

flappy_tester.run_experiment(100000)



