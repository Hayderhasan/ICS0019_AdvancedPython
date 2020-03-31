from appJar import gui
import importlib

quadraticGui = importlib.import_module("quadratic-equation-haalsa.quadratic-equation-solver")

values = {
    # the values to be entered
    "a": 0,
    "b": 0,
    "c": 0
}

roots = {
    # the results of calculation, if available
    "rootOne": 0.0,
    "rootTwo": 0.0
}

# creating the labels
def guiShow(app):
    app.addLabelEntry("a")
    app.addLabelEntry("b")
    app.addLabelEntry("c")

    app.addLabelEntry("rootOne")
    app.addLabelEntry("rootTwo")
    app.addButtons(["Calculate", "Stop"], buttonToCalc)

# showing the calculated result
def displayResult(app, result):
    app.setEntry("rootOne", result["rootOne"])
    app.setEntry("rootTwo", result["rootTwo"])

def showValue(app):
    solution = quadraticGui.solveQuadraticEquation(values["a"], values["b"], values["c"])
    if solution == "This equation has no solution":
        roots["rootOne"] = "imaginary"
        roots["rootTwo"] = "imaginary"
    else:
        roots["rootOne"] = solution[0]
        roots["rootTwo"] = solution[1]
    displayResult(app, roots)

# button clicking logic
def buttonToCalc(buttonClicked):
    global values
    if buttonClicked == "Stop":
        app.stop()
    if buttonClicked == "Calculate":
        values["a"] = int(app.getEntry("a"))
        values["b"] = int(app.getEntry("b"))
        values["c"] = int(app.getEntry("c"))
        showValue(app)

def init():
    global app
    app = gui()
    guiShow(app=app)
    app.go()

if __name__ == "__main__":
    init()
