# Before
Ask the player for their name they would like to use for this session before continuing to start session.



# Start Session

Create a new game session using the following format.

| Input | Steps | Output |
|------|-------|--------|
| Player name <br> Optional starting context | Initialize session <br> Roll base player stats using the [dice roller](../tools/dice_roller.md) and the process in [player stats](../context/player_stats.md) <br> Provide list of races from [player races](../context/player_races.md) and set race as chosen by player <br> Provide list of classes from [player classes](../context/player_classes.md) and set class as chosen by player <br> Save the previously gathered information to [player memory](../memory/player_memory.md) <br> Begin narrative scene immediately| Active session + starter character sheet |

## Rules

1. Generate the six core stats first.
2. Start with a short narrative hook so the session can begin immediately.

## Starter Character Sheet

| Field | Value |
|------|-------|
| Name | _______ |
| Class | _______ |
| Race | _______ |
| Strength (STR) | _______ |
| Dexterity (DEX) | _______ |
| Constitution (CON) | _______ |
| Intelligence (INT) | _______ |
| Wisdom (WIS) | _______ |
| Charisma (CHA) | _______ |

## Example Output

**Session Start:**
The player wakes in an unfamiliar roadside camp just before dawn. Their gear is scattered, their memory is incomplete, and danger is already nearby.

**Character State:**
- Class: Chosen normally
- Race: Chosen normally
- Stats: Generated normally
- Session: Active
