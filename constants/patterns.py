from enum import StrEnum

PROFILE_MAIN_VALIDATOR = r"^Раса:.+#нет_войне.$"


class CommonPatterns(StrEnum):
    RACE = r"Раса:\s(?P<race>.+)"
    NICKNAME = r"Ник:\s(\[.+?\])?(?P<nickname>.+)"
    GUILD_NAME = r"Ник:\s\[(?P<guild_name>.+?)\]"
    USER_ID = r"Идентификатор:\s(?P<user_id>\d+)"
    CHARACTER_LVL = r"Уровень:\s(?P<character_lvl>\d+)"
    PARAGON_LVL = r"Уровень:\s\d+?\((?P<paragon_lvl>\d+)"


class StatsPatterns(StrEnum):
    MAX_HP = r"Здоровье:\s\d+?/(?P<max_hp>\d+)"
    BASIC_ATTACK = r"Атака:\s(?P<basic_attack>\d+)"
    EXTRA_ATTACK = r"Атака:\s\d+?\s\(\+(?P<extra_attack>\d+)"
    BASIC_ARMOR = r"Защита:\s(?P<basic_armor>\d+)"
    EXTRA_ARMOR = r"Защита:\s\d+?\s\(\+(?P<extra_armor>\d+)"
    BASIC_DODGE = r"Уворот:\s(?P<basic_dodge>\d+)"
    EXTRA_DODGE = r"Уворот:\s\d+?%\s\(\+(?P<extra_dodge>[\d.]+?)%"
    BASIC_CRIT = r"Крит:\s(?P<basic_crit>\d+)"
    EXTRA_CRIT = r"Крит:\s\d+?%\s\(\+(?P<extra_crit>[\d\.]+?)%"
    BASIC_ACCURACY = r"Точность:\s(?P<basic_accuracy>\d+)"
    EXTRA_ACCURACY = r"Точность:\s\d+?%\s\(\+(?P<extra_accuracy>[\d\.]+?)%"


class ResourcePatterns(StrEnum):
    CHARACTER_EXP = r"🌕Опыт:\s(?P<character_exp>[\d\s]+)"
    ADENA = r"🏵Аден:\s(?P<adena>[\d\s]+)"


RACE_SYMBOL = r"(?P<race_symbol>.+)(Basilaris|Aquilla|Castitas)"
