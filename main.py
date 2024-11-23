# libraries
import pandas as pd
import numpy as np
from loguru import logger
import yaml
import uuid

# code
from src.functions.helpers import load_log_configs
from src.classes.ship import ship


def main():
    print("Hello from container-opti!")

    bays = 2
    tiers = 3
    rows = 4
    s1 = ship(bays, rows, tiers)
    print(s1.space)
    smb2 = s1.space.sum(axis=(0,2))
    print(smb2[s1.tiers_above:])
    print(smb2[:s1.tiers_below])
    print(s1.tiers_below, s1.tiers_above)
    s1.balance_ship()



if __name__ == "__main__":
    main()
