# Story Generation Prompt for Gemini

## Core Requirements:

*   **Format:** Ren'Py game script (`.rpy` files), text-only.
*   **Interactivity:** Choices are for the *player* to make within the Ren'Py game. I (Gemini) will write the script with these choices embedded, not make the choices myself.
*   **Genre/Pacing:** Slow burn netorare. **Crucially, it is NOT netorare from the start.** The story begins with a genuinely loving couple in a stable, normal relationship. Conflicts should be *small, subtle, and realistic* initially, slowly and gradually escalating over time.
## Protagonists:

*   Mark (male lead, POV character) and Sarah (his wife). They are a normie husband and wife, acting normally in a loving relationship with normal jobs.

## Supporting Characters:

*   David: Mark's colleague at the hardware store. A well-meaning but somewhat gossipy individual who tends to over-interpret situations.
*   **POV:** Exclusively from Mark's perspective ("us"). He makes all the decisions that shape the narrative.
*   **Harem:** Explicitly removed. This is a story focused on the core couple and the very slow and subtle external influences.

## Game Mechanics (Internal to Script):

*   **Love Score:** `love_score` variable, defaults to 200. It can *only* decrease. Once it goes down, the new value becomes the effective "max" for that path (it won't go back up).
*   **Mark's Awareness:** `mark_awareness` variable. Starts at 0 (oblivious). Choices will increase or decrease this, reflecting whether Mark is observant of subtle cues or chooses to ignore them.
*   **Sarah's Discontent:** `sarah_discontent` variable. Starts at 0 (content). Choices and events will increase this, reflecting Sarah's growing dissatisfaction or discomfort.

## Narrative Style & Content:

*   **Start:** Begin with a normal day, husband and wife in a loving relationship, normal jobs, and daily interactions.
*   **Conflict Escalation:** Small conflicts should *very slowly* become bigger conflicts. Avoid immediate red flags or dramatic events early on. Focus on the erosion of trust, subtle changes in behavior, and misinterpretations.
*   **Mark's Role:** Mark's decisions should reflect his personality – he can be a smart, observant guy who picks up on subtle cues, or he can be oblivious, dismissing potential issues as harmless.
*   **Length:** The story should be long and slow, aiming for a substantial narrative. (The 1 million word limit is understood as a general directive for length, not a literal target for every response).
*   **Detail:** Explain scenes in detail, including daily life, internal monologues, and eventually, sex scenes (when they naturally arise from the slow burn and narrative progression).
*   **Realism:** Characters and their reactions should be realistic.
*   **Depth:** Occasionally, allow for Mark to access Sarah's phone, chats, emails, etc., to add depth and potential for discovery/misinterpretation.

## Current Story State (as of last interaction):

The story has begun, establishing Mark and Sarah as a genuinely loving couple. The narrative has progressed through several days, subtly introducing minor shifts in their routine and Mark's perception, without any overt conflict or wrongdoing from Sarah.

Key events and developments:
*   **Initial Interaction:** Mark's colleague, David, subtly mentions seeing Sarah with Mr. Henderson at lunch. Mark initially dismisses this.
*   **Sarah's Increasing Workload:** Sarah's new role leading a national campaign has led to increased work hours, late nights, and upcoming travel to New York.
*   **Mark's Rationalizations:** Mark consistently rationalizes Sarah's preoccupation and absence as normal work-related dedication, reinforcing his trust and love for her.
*   **Subtle Cues and Mark's Awareness:** Minor events, such as Sarah's phone glances, the Montblanc pen from Mr. Henderson, and David's well-meaning warnings, have been introduced. Mark's tendency to dismiss these cues has subtly impacted his `mark_awareness` and `love_score`.
*   **Variable Changes Implemented:** The game mechanics for `love_score` (which can only decrease, with a dynamic `max_love_score` ceiling) and `mark_awareness` (which can only decrease, impacting `love_score`) have been integrated into the narrative choices and events.
*   **Multi-file Structure:** The story is now split across multiple `.rpy` files for better organization (e.g., `chapter1_intro.rpy`, `chapter1_day1.rpy`, `chapter1_day2.rpy`, etc.).

The story is currently set to continue from `label chapter1_day14:` in `chapter1_day14.rpy`.
