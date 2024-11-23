# libraries
import pandas as pd
import numpy as np
from loguru import logger
import yaml
import uuid

# code
from src.functions.helpers import load_log_configs


log_configs = load_log_configs()
logger.add(**log_configs)


# classes
class ship():
    
    def __init__(self, max_bay: int = 20, max_row: int = 16, max_tier: int =  15, balance_tolerance: float = 5):
        self.id = uuid.uuid4()
        self.balance_tolerance = balance_tolerance
        self.max_bay = max_bay
        self.max_row = max_row
        self.max_tier = max_tier
        self.gross_capacity = max_bay * max_row * max_tier
        logger.info(f"Ship {self.id} created with {self.gross_capacity} gross capacity.")
        self.space = self._get_container_space()
        self.tiers_below, self.tiers_above = self._get_below_deck_tiers(max_tier=self.max_tier)

    def _get_below_deck_tiers(self, max_tier, perc_below: float = 0.6):
        """
        get how many tiers should be below deck and how many above
        """
        tier_below = int(np.ceil(max_tier*perc_below))
        logger.info(f"Number of tiers below deck = {tier_below}")
        return tier_below, (max_tier-tier_below)
    
    def _get_container_space(self):
        """
        get the container space/grid of binary values; 0 is empty 1 is filled
        """
        return np.ones(self.gross_capacity).reshape(self.max_bay, self.max_tier, self.max_row)
        # return np.zeros(self.gross_capacity).reshape(self.max_bay, self.max_tier, self.max_row)

    def balance_bays(self):
        """
        check if front and back weights are balanced
        """
        sum_bays = self.space.sum(axis=(1,2))
        mid_bay = self.max_bay // 2
        self.front_half_wt = sum_bays[:mid_bay].sum()
        self.back_half_wt = sum_bays[mid_bay:].sum()
        logger.info(f"Front ship wt = {self.front_half_wt}")
        logger.info(f"Back ship wt = {self.back_half_wt}")
        assert np.abs(self.back_half_wt - self.front_half_wt) <= self.balance_tolerance
        logger.info("Bays balanced!")

    def balance_tiers(self):
        """
        check if top and bottom weights are balanced
        """
        sum_tiers = self.space.sum(axis=(0,2))
        self.top_half_wt = sum_tiers[:self.tiers_above].sum()
        self.bottom_half_wt = sum_tiers[self.tiers_below:].sum()
        logger.info(f"Top ship wt = {self.top_half_wt}")
        logger.info(f"Bottom ship wt = {self.bottom_half_wt}")
        assert np.abs(self.top_half_wt - self.bottom_half_wt) <= self.balance_tolerance
        logger.info("Tiers balanced!")

    def balance_rows(self):
        """
        check if right and left weights are balanced
        """
        sum_rows = self.space.sum(axis=(0,1))
        mid_row = self.max_row // 2
        self.right_half_wt = sum_rows[:mid_row].sum()
        self.left_half_wt = sum_rows[mid_row:].sum()
        logger.info(f"Top ship wt = {self.right_half_wt}")
        logger.info(f"Bottom ship wt = {self.left_half_wt}")
        assert np.abs(self.right_half_wt - self.left_half_wt) <= self.balance_tolerance
        logger.info("Rows balanced!")

    def balance_ship(self):
        """
        """
        self.balance_bays()
        self.balance_tiers()
        self.balance_rows()
        logger.info("Ship balanced!")