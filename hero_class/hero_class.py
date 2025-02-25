from random import randint, choice


class Hero:
    def __init__(self, name: str, health: int, max_health: int, shield: int):
        """Initializes the attributes of the Hero parent class.

        Args:
            name (str): The name of the hero.
            health (int): The current health points.
            max_health (int): The maximum possible health points.
            shield (int): The amount of shield points that reduce incoming damage.
        """
        self.name: str = name
        self.health: int = health
        self._max_health: int = max_health
        self.shield: int = shield

    def attack(self, target: "Hero", damage: int) -> int:
        """Inflicts damage on the target, considering its shield.

        Args:
            target (Hero): The character receiving the attack.
            damage(int): The base damage before shield reduction.

        Returns:
            int: The target's updated health after taking damage.

        Note:
            The method prints a message about attacking process,
            including the inflicted damage and the target's updated health.
        """
        damage = max(damage - target.shield, 0)
        target.health = max(target.health - damage, 0)
        print(f"\n{self.name} attacks {target.name}, inflicting damage: {damage} DMG.")
        print(f"{target.name}'s current health after attack: {target.health} HP.")
        return target.health

    def is_death(self) -> bool:
        """Checks if the character is dead.

        Returns:
            bool: True if the health is 0 or lower, otherwise False.
        """
        return self.health <= 0


class Warrior(Hero):
    def __init__(self, strength=10):
        """Initializes a Warrior character with inherited default attributes from the Hero class and a custom strength.

        Args:
            strength (int): The strength of the Warrior, default is 10. It affects special attack and defence power.

        Sets the following inherited attributes from the Hero class for the Warrior instance:
            name (str): "Warrior".
            health (int): 100.
            max_health (int): 100.
            shield (int): 10.

        Note:
            max_shield (int): The maximum value of shield, this attribute is not passed as an argument.
        """
        super().__init__(name="Warrior", health=100, max_health=100, shield=10)
        self.strength: int = strength
        self._max_shield: int = self.strength + self.shield

    def attack(self, target: "Hero", damage: int) -> int:
        """Resets the Warrior's shield to the default value before the attack."""
        self.shield = 10
        return super().attack(target, damage)

    def bleeding(self, target: "Mage", damage: int) -> int:
        """Inflicts damage to the target (Mage), considering its shield and the attacker's (Warrior) strength.

        Args:
            target (Mage): The character receiving the attack.
            damage (int): The base damage before applying the attacker's strength and the target's shield reduction.

        Returns:
            int: The target's remaining health after taking damage.

        Note:
            The method prints a message about attacking process,
            including the inflicted damage and the target's updated health.
        """
        self.shield = 10
        damage = max((self.strength + damage) - target.shield, 0)
        target.health = max(target.health - damage, 0)
        print(f"\n{self.name} uses a bleeding attack, inflicting damage: {damage} DMG.")
        print(f"{target.name}'s current health after attack: {target.health} HP.")
        return target.health

    def get_shield(self) -> int:
        """Increases the shield by the strength value.

        Returns:
            int: The updated shield value.

        Note:
            The method prints a message about the shield increase process.
        """
        self.shield = self._max_shield
        print(f"\n{self.name} increases his shield, current shield: {self.shield} DEF.")
        return self.shield


class Mage(Hero):
    def __init__(self, intellect=10):
        """Initializes a Mage character with inherited default attributes from the Hero class and custom intellect.

        Args:
            intellect (int): The intellect of the Mage, default is 10. It affects special attack and heal power.

        Sets the following inherited attributes from the Hero class for the Mage instance:
            name (str): "Mage".
            health (int): 80.
            max_health (int): 80.
            shield (int): 5.
        """
        super().__init__(name="Mage", health=80, max_health=80, shield=5)
        self.intellect: int = intellect

    def fire_ball(self, target: "Warrior", damage: int) -> int:
        """Inflicts the damage to the target (Warrior), considering its shield and attacker's (Mage) intellect.

        Args:
            target (Warrior): The character receiving the attack.
            damage (int): The base damage before applying the attacker's intellect and the target's shield reduction.

        Returns:
            int: The target's remaining health after taking damage.

        Note:
            The method prints a message about attacking process,
            including the inflicted damage and the target's updated health.
        """
        damage = max((self.intellect + damage) - target.shield, 0)
        target.health = max(target.health - damage, 0)
        print(f"\n{self.name} uses the fire ball, inflicting damage: {damage} DMG.")
        print(f"{target.name} has {damage} damage. Now {target.name}'s health is {target.health}.")
        return target.health

    def heal(self, heal: int) -> int:
        """Increases the character's health by the given heal value and intellect value.

        Args:
        heal (int): The base heal value.

        Returns:
            int: The updated character's health.

        Note:
            The method prints a message about the healing process.
        """
        heal = self.intellect + heal
        actual_heal = min(heal, self._max_health - self.health)
        self.health += actual_heal
        print(f"\n{self.name} heals itself by {actual_heal} points, current health: {self.health} HP.")
        return self.health


if __name__ == "__main__":
    warrior = Warrior()
    mage = Mage()
    value = randint(10, 15)

    warrior_actions = [lambda: warrior.attack(mage, value),
                       lambda: warrior.bleeding(mage, value),
                       lambda: warrior.get_shield()]

    mage_actions = [lambda: mage.attack(warrior, value),
                    lambda: mage.fire_ball(warrior, value),
                    lambda: mage.heal(value)]

    while not warrior.is_death():
        warrior_move = choice(warrior_actions)()
        if mage.is_death():
            break
        mage_move = choice(mage_actions)()

    print(f"\n{mage.name if mage.is_death() else warrior.name} was died.")
