import os

dirname=os.path.dirname(__file__)

BG_FILENAME=os.getenv('BG_FILENAME') or 'background.png'
BG_FILE_PATH=os.path.join(dirname, 'assets', BG_FILENAME)

GOAL_FILENAME=os.getenv('GOAL_FILENAME') or 'goal.png'
GOAL_FILE_PATH=os.path.join(dirname, 'assets', GOAL_FILENAME)

STARIE_FILENAME=os.getenv('STARIE_FILENAME') or 'starie.png'
STARIE_FILE_PATH=os.path.join(dirname, 'assets', STARIE_FILENAME)

SPIKE_FILENAME=os.getenv('SPIKE_FILENAME') or 'spike.png'
SPIKE_FILE_PATH=os.path.join(dirname, 'assets', SPIKE_FILENAME)