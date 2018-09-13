class Settings():
    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5

        # alien settings
        self.alien_speed_factor = 5
        self.alien_drop_speed = 5
        self.alien_points = 50

        # alien moving direction. '1' to the right, '-1' to the left
        self.fleet_direction = 1
