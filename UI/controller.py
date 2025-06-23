import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDyear(self):
        years = self._model.getYears()
        for a in years:
            self._view.ddyear.options.append(ft.dropdown.Option(a))
        self._view.update_page()

    def fillDDShape(self):
        shape = self._model.getShape()
        for s in shape:
            self._view.ddshape.options.append(ft.dropdown.Option(s))
        self._view.update_page()

    def handle_graph(self, e):
        self._view.txt_result1.controls.clear()
        if self._view.ddyear.value is None or self._view.ddshape.value is None:
            self._view.create_alert("Attenzione: selezionare anno e shape!")
        year = int(self._view.ddyear.value)
        shape = self._view.ddshape.value
        self._model.buildGraph(year, shape)
        numNodi, numArchi = self._model.getGraphDetails()
        self._view.txt_result1.controls.append(ft.Text(f"Numero di vertici: {numNodi}"))
        self._view.txt_result1.controls.append(ft.Text(f"Numero di archi: {numArchi}"))
        self._view.update_page()

    def handle_path(self, e):
        pass
