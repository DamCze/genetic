from selections.tournament_selection import TournamentSelection
from selections.best_selection import BestSelection
from selections.roulette_wheel_selection import RouletteWheelSelection

ITournamentSelection = "TournamentSelection"
IBestSelection = 'BestSelection'
IRouletteWheelSelection = 'RouletteWheelSelection'

__all__ = ['TournamentSelection', 'BestSelection', 'RouletteWheelSelection', 'ITournamentSelection', 'IBestSelection',
           'IRouletteWheelSelection']
