class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, sw_settings):
        """Initialize statistics."""
        self.ai_settings = sw_settings
        self.reset_stats()
        self.game_active = False
        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 0

