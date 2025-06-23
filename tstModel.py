from model.modello import Model

mymodel = Model()
mymodel.buildGraph(1996, "circle")
print(mymodel.getGraphDetails())
mymodel.getPesiMaggiori()
