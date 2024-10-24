import random
import time
import tqdm
import os
from colorama import Fore, init

from errors import ChanceError


class GoodLuck:
    def __init__(self, chance: float = 0.5, load_time: float = 5.0) -> None:
        if chance <= 0 or chance >= 1:
            raise ChanceError

        self.load_time: float = load_time
        self.chance: float = chance

    def try_(self) -> None:
        """Сделать попытку"""
        os.system("clear")
        init(autoreset=True)
        print(Fore.LIGHTYELLOW_EX + "ЗАГРУЖАЕМ ТВОЮ УДАЧУ...")

        for _ in tqdm.tqdm(iterable=range(7777), ascii=True, ncols=69):
            time.sleep(round(self.load_time / 7777, 5))

        if random.random() > self.chance:
            print(Fore.LIGHTRED_EX + "ПРОИГРАЛ ЛОШАРА")
            return
        print(Fore.LIGHTGREEN_EX + "Ты выиграл")
