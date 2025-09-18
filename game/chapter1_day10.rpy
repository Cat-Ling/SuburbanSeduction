# This file will contain the next part of the story.
# The story will continue from here after chapter1_day9.rpy finishes.

label chapter1_day10:
    scene bg_home_day with fade # Assuming a general home background
    m "The week leading up to Sarah's first New York trip was a strange mix of excitement and subtle tension. Sarah was buzzing, her energy infectious as she finalized presentations, packed her bags, and coordinated with her team. I, on the other hand, found myself feeling a quiet apprehension."

    m "Every evening, after I got home from the hardware store, I'd find her either on a video call, or hunched over her laptop, a focused frown on her face. Dinner became a quick affair, often eaten in silence as she typed away, or punctuated by her sudden exclamations about a new idea or a problem solved."

    m "I tried to be supportive, to match her enthusiasm. I'd ask about her day, about the campaign, about Mr. Henderson. She'd answer, sometimes with a distracted air, sometimes with a burst of detailed explanation that left me feeling a little lost in the corporate jargon."

    menu:
        "Offer to help her pack or prepare for the trip.":
            m "Hey, babe, anything I can do to help? Need me to iron your shirts, or go over your presentation with you?"
            s "Oh, that's sweet of you, [mc_name], but I've got it. Everything's under control. You just relax." She smiled, a quick, reassuring flash, but didn't look up from her laptop. "I appreciate the offer, though."
            call update_love_score(-1) # Subtle decrease. Mark's effort is appreciated, but Sarah's focus means the connection isn't fully made.
            # mark_awareness does not change here, as it cannot increase.
            jump after_offer_to_help
        "Suggest a relaxing evening together, away from work.":
            m "You've been working non-stop, babe. How about we just order some takeout tonight and watch a movie? No work talk, just us."
            s "Mmm, that sounds tempting, [mc_name], but I really need to get through this. I'm so close to finishing this section. Maybe tomorrow?" She gave me an apologetic look, but her fingers were already hovering over the keyboard.
            call update_love_score(-2) # More significant decrease. Mark's need for connection is unmet, and Sarah's focus is clearly elsewhere.
            $ sarah_discontent += 1 # Sarah feels a tiny bit of pressure/guilt, subtly increasing her discontent.
            # mark_awareness does not change here, as it cannot increase.
            jump after_relaxing_evening_suggestion

label after_offer_to_help:
    m "I retreated to the living room, feeling a little useless. I wanted to help, to be part of her world, but it felt like she was in a different orbit entirely. I tried to tell myself it was just the intensity of the new project, that it would pass."

    m "The house was filled with the quiet hum of her laptop, punctuated by the occasional click of her mouse. It was a new kind of quiet, one that felt less peaceful and more... empty."

    call chapter1_day11 # Call the next part of the story
    return

label after_relaxing_evening_suggestion:
    m "I sighed, a quiet sound that went unheard. I understood, intellectually, that this was important for her career. But emotionally, it stung a little. I missed our easy evenings, our shared laughter, the simple comfort of her undivided attention."

    m "I ended up making myself dinner and watching TV alone. The silence in the house felt heavy, amplified by the knowledge that she was just in the next room, but miles away in her own world of corporate strategy and national campaigns."

    call chapter1_day11 # Call the next part of the story
    return