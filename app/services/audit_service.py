import time
import random
import logging

logger = logging.getLogger(__name__)


def enviar_auditoria(simulation_id: int):
    try:
        delay = random.uniform(1, 3)
        time.sleep(delay)

        if random.random() < 0.1:
            raise Exception("Error en el servicio externo de scoring")
        logger.info(f"Auditoria exitosa para simulacion {simulation_id}!")
    except Exception as e:
        logger.error(
            f"Fallo la simulacion de la auditoria {simualtion_id}: {e}"
        )

    print(f"Auditoria exitosa para la simulacion {simulation_id}!")