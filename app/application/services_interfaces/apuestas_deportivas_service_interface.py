from abc import ABC, abstractmethod

from app.domain.models.apuestas_deportivas import ApuestasDeportivas


class ApuestasDeportivasServiceInterface(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def login_happy_path(self, apuestas_deportivas: ApuestasDeportivas):
        return apuestas_deportivas

    @abstractmethod
    def visualizar_torneos(self, apuestas_deportivas: ApuestasDeportivas):
        return apuestas_deportivas

    @abstractmethod
    def visualizar_promociones_pro(self, apuestas_deportivas: ApuestasDeportivas):
        return apuestas_deportivas

    @abstractmethod
    def col_promociones(self, apuestas_deportivas: ApuestasDeportivas):
        return apuestas_deportivas

    @abstractmethod
    def visualizar_promocion_winner_de_winners(self, apuestas_deportivas: ApuestasDeportivas):
     return apuestas_deportivas

    @abstractmethod
    def visualizar_depositos_col(self, apuestas_deportivas: ApuestasDeportivas):
        return apuestas_deportivas

    @abstractmethod
    def visualizar_depositos_ad(self, apuestas_deportivas: ApuestasDeportivas):
        return apuestas_deportivas