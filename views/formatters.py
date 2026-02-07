import re
from typing import Optional
from datetime import timedelta

from database import models
from constants.patterns import RACE_SYMBOL


class UserProfileFormatter:
    @staticmethod
    def format(
        profile: models.UserProfile,
        old_profile: Optional[models.UserProfile] = None
    ) -> str:        
        race = re.search(RACE_SYMBOL, profile.race).group("race_symbol")
        lines = [
            f"{race} [{profile.guild_name}]{profile.nickname}",
            f"🏅: {profile.character_lvl}({profile.paragon_lvl})",
            "",
            (
                f"❤️: {profile.max_hp}  <b>•</b>  ⚔️: {profile.attack}"
                f"  <b>•</b>  🛡: {profile.armor}"
            ),
            (
                f"💨 : {profile.dodge}%  <b>•</b>  🎯: {profile.crit}%"
                f"  <b>•</b>  ⏳: {profile.crit}%"
            )
        ]

        if old_profile:
            time_diff = profile.updated_at - old_profile.updated_at
            exp_diff = profile.character_exp - old_profile.character_exp
            adena_diff = profile.adena - old_profile.adena

            duration_str = UserProfileFormatter._format_duration(time_diff)

            diff_line = f"\n+{exp_diff:,}🌕 +{adena_diff:,}🏵  {duration_str}"
            lines.append(diff_line)

        return "\n".join(lines)

    @staticmethod
    def _format_duration(td: timedelta) -> str:
        total_seconds = int(td.total_seconds())
        total_seconds = max(0, total_seconds)

        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        parts = []
        if hours > 0:
            parts.append(f"{hours}час.")
        if minutes > 0:
            parts.append(f"{minutes}мин.")
        if seconds > 0 or not parts:
            parts.append(f"{seconds}сек.")
            
        return " ".join(parts)
