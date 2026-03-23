"""
Story Game GM - D&D-like Game Master Assistant
Main module for managing game state and mechanics
"""

import random
from typing import List, Dict, Any


class DiceRoller:
    """Utility class for dice rolling mechanics"""
    
    @staticmethod
    def roll_dice(num_dice: int, sides: int) -> int:
        """Roll multiple dice and return the total"""
        return sum(random.randint(1, sides) for _ in range(num_dice))
    
    @staticmethod
    def roll_d20() -> int:
        """Roll a standard 20-sided die"""
        return random.randint(1, 20)


class Player:
    """Represents a player character"""
    
    def __init__(self, name: str, hp: int, level: int):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.level = level
        self.inventory: List[str] = []
    
    def take_damage(self, damage: int) -> None:
        """Apply damage to player"""
        self.hp = max(0, self.hp - damage)
    
    def heal(self, amount: int) -> None:
        """Heal player"""
        self.hp = min(self.max_hp, self.hp + amount)
    
    def is_alive(self) -> bool:
        """Check if player is still alive"""
        return self.hp > 0


class Combat:
    """Handles combat resolution between entities"""
    
    @staticmethod
    def resolve_attack(attacker_level: int, defender_level: int) -> bool:
        """Resolve a combat attack - return True if hit"""
        attack_roll = DiceRoller.roll_d20()
        difficulty = 10 + defender_level
        return attack_roll + attacker_level > difficulty


def main():
    """Main entry point"""
    print("Story Game GM initialized")
    
    # Test dice roller
    print(f"D20 roll: {DiceRoller.roll_d20()}")
    print(f"2d6 roll: {DiceRoller.roll_dice(2, 6)}")


if __name__ == "__main__":
    main()