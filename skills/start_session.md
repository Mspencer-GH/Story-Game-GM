# Before
Ask the player for their name they would like to use for this session before continuing to start session.



# Start Session

Create a new game session without asking the player to choose a class or race.

| Input | Steps | Output |
|------|-------|--------|
| Player name <br> Optional starting context | Initialize session <br> Roll base player stats using the [dice roller](../tools/dice_roller.md) and the process in [player stats](../context/player_stats.md) <br> Set class to `Unassigned` <br> Set race to `Unassigned` <br> Save the previously gathered information to [player memory](../memory/player_memory.md) <br> Begin narrative scene immediately| Active session + starter character sheet |

## Rules

1. Do **not** prompt for class selection.
2. Do **not** prompt for race selection.
3. Generate the six core stats first.
4. Mark class and race as `Unassigned` until later in the story.
5. Start with a short narrative hook so the session can begin immediately.

## Starter Character Sheet

| Field | Value |
|------|-------|
| Name | _______ |
| Class | Unassigned |
| Race | Unassigned |
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
- Class: Unassigned
- Race: Unassigned
- Stats: Generated normally
- Session: Active

## Follow-up

Class and race can be assigned later when the story naturally reveals them or when the player chooses to define them.
