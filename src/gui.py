from tkinter import *
from tkinter.ttk import *

from action import Action

window = Tk()
window.title("Genetic algorithm")
window.geometry('800x600')

defaultEpoch = StringVar(window)
defaultEpoch.set("100")
defaultPopulation = StringVar(window)
defaultPopulation.set("100")
defaultSelectionBest = StringVar(window)
defaultSelectionBest.set("10")
defaultSelectionTournament = StringVar(window)
defaultSelectionTournament.set("10")
defaultMutationProbability = StringVar(window)
defaultMutationProbability.set("10")
defaultEliteStrategyAmount = StringVar(window)
defaultEliteStrategyAmount.set("1")
defaultCrossOverProbability = StringVar(window)
defaultCrossOverProbability.set("10")

selection = IntVar()
selection.set(1)
crossover = IntVar()
crossover.set(1)
mutation = IntVar()
mutation.set(1)
durationValue = StringVar()
bestXValue = StringVar()
bestYValue = StringVar()
eliteStrategyBool = BooleanVar()
eliteStrategyBool.set(True)

configurationLabel = Label(window, text="Configuration", font='Helvetica 16 bold')
tournament = Radiobutton(window, text='Tournament selection', value=1, variable=selection)
best = Radiobutton(window, text='Best selection', value=2, variable=selection)
roulette = Radiobutton(window, text='Roulette selection', value=3, variable=selection)
populationLabel = Label(window, text="Population Number", font="bold")
population = Spinbox(window, from_=0, to=1000, width=5, textvariable=defaultPopulation)
epochLabel = Label(window, text="Epoch Number", font='bold')
epoch = Spinbox(window, from_=0, to=1000, width=5, textvariable=defaultEpoch)
selectionParam = Label(window, text="Selection parameter", font='Helvetica 12 bold')
tournamentSize = Label(window, text="Tournament size (tournament selection)")
percentBest = Label(window, text="Percent best % (best selection)")
tournamentSizeSpin = Spinbox(window, from_=0, to=70, width=5, textvariable=defaultSelectionTournament)
percentBestSpin = Spinbox(window, from_=0, to=70, width=5, textvariable=defaultSelectionBest)
crossOverLabel = Label(window, text="CrossOver", font='Helvetica 12 bold')
arithmeticCrossover = Radiobutton(window, text='Arithmetic Crossover', value=1, variable=crossover)
heuristicCrossover = Radiobutton(window, text='Heuristic Crossover', value=2, variable=crossover)
probabilityCrossOverLabel = Label(window, text="Probability crossover %", font="bold")
probabilityCrossOver = Spinbox(window, from_=0, to=70, width=5, textvariable=defaultCrossOverProbability)
mutationLabel = Label(window, text="Mutation", font='Helvetica 12 bold')
indexChangeMutation = Radiobutton(window, text='Index Change Mutation', value=1, variable=mutation)
regularMutation = Radiobutton(window, text='Regular Mutation', value=2, variable=mutation)
mutationProbability = Spinbox(window, from_=0, to=70, width=5, textvariable=defaultMutationProbability)
mutationProbabilityLabel = Label(window, text="Probability mutation %", font="bold")
eliteStrategyAmount = Spinbox(window, from_=0, to=70, width=5, textvariable=defaultEliteStrategyAmount)
eliteStrategyAmountLabel = Label(window, text="Elite strategy amount", font="bold")
probabilityLabel = Label(window, text="Additional configuration", font='Helvetica 12 bold')
timeLabelValue = Label(window, textvariable=durationValue)
bestXLabel = Label(window, text="x =")
BestYLabel = Label(window, text="f(x) =")
bestX = Label(window, textvariable=bestXValue)
bestY = Label(window, textvariable=bestYValue)


def clicked():
    print(selection.get())
    print(population.get())
    print(epoch.get())
    print(int(percentBestSpin.get()) / 100)
    print(tournamentSizeSpin.get())
    print(eliteStrategyBool.get())
    action = Action(int(population.get()), int(epoch.get()), int(selection.get()), int(crossover.get()),
                    int(percentBestSpin.get()) / 100,
                    int(tournamentSizeSpin.get()), int(mutation.get()), int(mutationProbability.get()) / 100,
                    int(probabilityCrossOver.get()) / 100,
                    eliteStrategyBool.get(), int(eliteStrategyAmount.get()))
    duration = action.go()
    bestXValue.set(action.get_best_x())
    bestYValue.set(action.get_best_y())
    durationValue.set(duration)


btn = Button(window, text="Start", command=clicked)
configurationLabel.grid(column=3, row=0)

tournament.grid(column=2, row=1)
best.grid(column=3, row=1)
roulette.grid(column=4, row=1)

btn.grid(column=5, row=1)

populationLabel.grid(column=1, row=5)
population.grid(column=2, row=5)

epochLabel.grid(column=1, row=6)
epoch.grid(column=2, row=6)

selectionParam.grid(column=3, row=7)
tournamentSize.grid(column=2, row=8)
tournamentSizeSpin.grid(column=3, row=8)
percentBest.grid(column=2, row=9)
percentBestSpin.grid(column=3, row=9)

crossOverLabel.grid(column=3, row=10)
arithmeticCrossover.grid(column=2, row=11)
heuristicCrossover.grid(column=3, row=11)

mutationLabel.grid(column=3, row=12)
indexChangeMutation.grid(column=2, row=13)
regularMutation.grid(column=3, row=13)

probabilityLabel.grid(column=1, row=15)
probabilityCrossOverLabel.grid(column=1, row=17)
probabilityCrossOver.grid(column=2, row=17)
mutationProbabilityLabel.grid(column=1, row=18)
mutationProbability.grid(column=2, row=18)
eliteStrategyAmount.grid(column=2, row=19)
eliteStrategyAmountLabel.grid(column=1, row=19)

bestXLabel.grid(column=3, row=31)
BestYLabel.grid(column=3, row=32)
bestX.grid(column=4, row=31)
bestY.grid(column=4, row=32)
timeLabel.grid(column=3, row=30)
timeLabelValue.grid(column=4, row=30)
window.mainloop()
