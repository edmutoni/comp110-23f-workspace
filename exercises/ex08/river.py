"""File to define River class."""

__author__ = "930690385"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Initializing the river attributes."""

    day: int
    bears: list
    fish: list
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking the ages of fish and bears."""
        new_fish_list: list[Fish] = []
        new_bears_list: list[Bear] = []
        for f in self.fish:
            if f.age <= 3:
                new_fish_list.append(f)
        for b in self.bears:
            if b.age <= 5:
                new_bears_list.append(b)
        self.fish = new_fish_list
        self.bears = new_bears_list
        return None

    def remove_fish(self, amount: int):
        """Removing the old fish from the river."""
        f: int = 0
        while f < amount:
            self.fish.pop(f)
            f = f + 1
    
    def remove_bears(self, amount: int):
        """Removing the old bears from the river."""
        b: int = 0
        while b < amount:
            self.bears.pop(b)
            b = b + 1

    def bears_eating(self):
        """Adding to the hunger_score for bears if there is fish to eat, and removing the eaten fish."""
        for b in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                b.eat(3)
        return None
    
    def check_hunger(self):
        """Checking the hunger score of the bears and then removing the starving bears from the river."""
        new_bears_list2: list[Bear] = []
        for b in self.bears:
            if b.hunger_score >= 0:
                new_bears_list2.append(b)
        self.bears = new_bears_list2
        return None
        
    def repopulate_fish(self):
        """Adding the baby fish."""
        baby_fish: list[Fish] = []
        for f in range(0, (len(self.fish) // 2) * 4):
            baby_fish.append(Fish())
        self.fish = self.fish + baby_fish
        return None
    
    def repopulate_bears(self):
        """Adding the baby bears."""
        baby_bears: list[Bear] = []
        for b in range(0, len(self.bears) // 2):
            baby_bears.append(Bear())
        self.bears = self.bears + baby_bears
        return None
    
    def view_river(self):
        """Viewing the bear and fish pop of the river, as well as the day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
    
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Simulates a river week by calling the one_river_day method 7 times."""
        day: int = 0
        while day < 7:
            self.one_river_day()
            day = day + 1