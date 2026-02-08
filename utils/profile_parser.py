import re
from typing import Any

from database.models import UserProfile
from constants.patterns import (
    StatsPatterns,
    CommonPatterns,
    ResourcePatterns,
)


class ProfileParser:
    def __init__(self, text: str):
        self.text = text

    def _extract(self, pattern: str, group_name: str) -> Any:
        match = re.search(pattern, self.text, re.IGNORECASE)
        if not match:
            return None
        val = match.group(group_name).strip()

        if re.match(r"^[\d\s]+$", val):
            val = val.replace(" ", "")

        if val.isdigit():
            return int(val)
        try:
            return float(val)
        except ValueError:
            return val

    def parse(self) -> UserProfile:
        total_atk = self._extract(
            StatsPatterns.BASIC_ATTACK, "basic_attack"
        ) + self._extract(StatsPatterns.EXTRA_ATTACK, "extra_attack")
        total_arm = self._extract(
            StatsPatterns.BASIC_ARMOR, "basic_armor"
        ) + self._extract(StatsPatterns.EXTRA_ARMOR, "extra_armor")
        total_dodge = self._extract(
            StatsPatterns.BASIC_DODGE, "basic_dodge"
        ) + self._extract(StatsPatterns.EXTRA_DODGE, "extra_dodge")
        total_crit = self._extract(
            StatsPatterns.BASIC_CRIT, "basic_crit"
        ) + self._extract(StatsPatterns.EXTRA_CRIT, "extra_crit")

        total_acc = self._extract(
            StatsPatterns.BASIC_ACCURACY, "basic_accuracy"
        ) + self._extract(StatsPatterns.EXTRA_ACCURACY, "extra_accuracy")

        return UserProfile(
            user_id=self._extract(CommonPatterns.USER_ID, "user_id"),
            race=self._extract(CommonPatterns.RACE, "race"),
            nickname=self._extract(CommonPatterns.NICKNAME, "nickname"),
            guild_name=self._extract(CommonPatterns.GUILD_NAME, "guild_name"),
            character_lvl=self._extract(CommonPatterns.CHARACTER_LVL, "character_lvl"),
            paragon_lvl=self._extract(CommonPatterns.PARAGON_LVL, "paragon_lvl"),
            max_hp=self._extract(StatsPatterns.MAX_HP, "max_hp"),
            attack=total_atk,
            armor=total_arm,
            dodge=total_dodge,
            crit=total_crit,
            accuracy=total_acc,
            character_exp=self._extract(
                ResourcePatterns.CHARACTER_EXP, "character_exp"
            ),
            adena=self._extract(ResourcePatterns.ADENA, "adena"),
        )
