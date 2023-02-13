from core.config import constants
from app.application.repositories_interfaces.apuestas_deportivas_repository_interface import ApuestasDeportivasRepositoryInterface
from app.domain.models.apuestas_deportivas import ApuestasDeportivas


class ApuestasDeportivasRepository(ApuestasDeportivasRepositoryInterface):

    def visualizar_depositos_col(self, apuestas_deportivas: ApuestasDeportivas):
        pass

    def __init__(self):
        super().__init__()

    def login_happy_path(self, apuestas_deportivas: ApuestasDeportivas):

        """ Todo lo que tenga que ver con base de datos de preferencia
        tambien otras cosas que no sean como funciona la prueba
        - Atte HOT DOG CODER """


        return  apuestas_deportivas

    def visualizar_torneos(self, apuestas_deportivas: ApuestasDeportivas):

        """ Todo lo que tenga que ver con visualización de promoción
        - Atte HOT DOG CODER """


        return apuestas_deportivas

    def visualizar_promociones_pro(self, apuestas_deportivas: ApuestasDeportivas):
        return  apuestas_deportivas

    def col_promociones(self, apuestas_deportivas: ApuestasDeportivas):
        return apuestas_deportivas

    def visualizar_promocion_winner_de_winners(self, apuestas_deportivas: ApuestasDeportivas):
        return apuestas_deportivas

    def visualizar_depositos_ad(self, apuestas_deportivas: ApuestasDeportivas):
        return apuestas_deportivas

