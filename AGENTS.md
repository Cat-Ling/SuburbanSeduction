# Agent Instructions

This document provides instructions for an agent (e.g., Jules) to continue the "Suburban Seduction" story.

## Task: Continue Story Development

The primary task is to continue the Ren'Py story "Suburban Seduction".

## Story Context and Guidelines:

Refer to the `story.md` file located in the `Suburban Seduction` directory for all detailed instructions regarding:
*   **Format:** Ren'Py game script (`.rpy` files), text-only.
*   **Interactivity:** Choices are for the *player* to make.
*   **Genre/Pacing:** Slow burn netorare, starting with a loving couple, small conflicts escalating slowly.
## Protagonists:

*   Player-named male lead (default "Mark") and Sarah.

## Supporting Characters:

*   David: Mark's colleague at the hardware store. A well-meaning but somewhat gossipy individual who tends to over-interpret situations.
*   **POV:** Exclusively the player-named MC's.
*   **Harem:** Removed.
*   **Game Mechanics:** `love_score`, `mark_awareness`, `sarah_discontent` variables.
*   **Narrative Style:** Long, detailed scenes (including sex scenes when appropriate), realistic characters, daily interactions, occasional access to Sarah's private communications.

## Current Project Setup:

*   Ren'Py SDK 8.4.1 is installed in `/mnt/external_hdd/gemini-cii/renpy/`.
*   The game project structure has been set up in `/mnt/external_hdd/gemini-cii/Suburban Seduction/` as follows:
    ```
    Suburban Seduction/
    ├── game/
    │   ├── chapter1_intro.rpy
    │   ├── chapter1_day1.rpy
    │   ├── chapter1_day2.rpy
    │   ├── options.rpy
    │   ├── screens.rpy
    │   └── images/
    ```
*   Project initialization is typically done via the Ren'Py graphical launcher. As this is a CLI environment, the basic project structure has been created manually.

## Ren'Py Feature Implementation Guide:

Ren'Py scripts (`.rpy` files) are primarily composed of statements and Python blocks.

**Key Concepts:**

1.  **Characters:**
    *   Defined using `define character_name = Character("Display Name")`.
    *   Dialogue: `character_name "Dialogue text."`

2.  **Scenes and Images:**
    *   `scene` statement: Changes background image (e.g., `scene bg room`). Images go in `game/images/`.
    *   `show` and `hide` statements: Display/hide character sprites or other images (e.g., `show sarah happy`).

3.  **Labels and Jumps:**
    *   `label label_name:`: Defines a point in the script.
    *   `jump label_name`: Transfers control to a label for branching.
    *   `call label_name`: Transfers control to a label, and returns to the calling point when the called label finishes.

4.  **Menus and Choices:**
    *   `menu:` statement: Presents player choices.
    *   Each choice has text and associated code/jump.

5.  **Variables and Python Integration:**
    *   `default variable_name = initial_value`: Defines game variables.
    *   `$ python_statement`: Executes single-line Python.
    *   `init python:` block: Executes Python once at game start.
    *   `python:` block: Executes Python during the game.
    *   Variables in dialogue: `m "My love score is [love_score]."`.

6.  **Music and Sound:**
    *   `play music "audio/track.ogg"`: Plays background music.
    *   `play sound "audio/sfx.ogg"`: Plays sound effects.

**To implement new features:**
*   Create new `.rpy` files for new story segments (e.g., `chapter1_day2.rpy`, `chapter1_day3.rpy`).
*   Call these new files from the end of the previous `.rpy` file using `call new_file_label`.
*   Add dialogue, scenes, and choices to the new `.rpy` files.
*   Define new characters, add backgrounds/sprites (in `game/images/`).
*   Use `$` statements or `python:` blocks to modify `love_score`, `mark_awareness`, and `sarah_discontent` based on player choices.
*   Create new labels and use `jump` for navigation within a single `.rpy` file.

## Current Story State (as of last interaction):

*   The story is split across multiple `.rpy` files in the `game/` directory.
*   `chapter1_intro.rpy` handles the game's start and asks for the player-character's name.
*   `chapter1_day1.rpy` contains the initial story segment, focusing on a normal, loving interaction between the MC and Sarah, with David's comment being genuinely dismissed or casually inquired about, without immediate suspicion.
*   The story is currently set to continue in `chapter1_day14.rpy` from the `label chapter1_day14:`.

## Action Plan for Agent:

To continue the story, follow these steps:

1.  **Understand Context:**
    *   **Read `story.md`:** This file contains the overarching narrative guidelines, core requirements, game mechanics, and a summary of the story's progression so far. It is the primary source of truth for the story's direction.
    *   **Read the last `.rpy` file:** Identify the current continuation point (the `label` specified in the `Current Story State` section of `AGENTS.md`). This provides the immediate narrative context.

2.  **Write New Story Segment:**
    *   **Create a new `.rpy` file:** If the current `.rpy` file is concluding a logical segment, create a new `.rpy` file (e.g., `chapter1_day15.rpy`) for the next part of the story.
    *   **Write detailed scenes:** Focus on realistic, detailed interactions and dialogue, including internal monologues for the player-character.
    *   **Adhere to Mechanics:** Subtly integrate changes to `love_score`, `mark_awareness`, and `sarah_discontent` variables based on player choices and narrative events. Remember:
        *   `love_score` can only decrease.
        *   `mark_awareness` can only decrease.
        *   `sarah_discontent` can only increase.
        *   Refer to the `update_love_score` and `decrease_mark_awareness` functions in `chapter1_intro.rpy` for how to modify these variables.
    *   **Maintain Pacing:** Ensure the slow burn, subtle conflict escalation, and loving couple dynamic are maintained. Sarah remains innocent and genuinely loving for a long time.
    *   **Call Next Segment:** At the end of the current `.rpy` file, add a `call` statement to the `label` in the next `.rpy` file (e.g., `call chapter1_day15`).

3.  **Update `AGENTS.md`:**
    *   After writing a new `.rpy` file and setting up the `call` statement, update the `Current Story State` section in `AGENTS.md` to reflect the new continuation point (the `label` in the newly created `.rpy` file). This is crucial for seamless handover.