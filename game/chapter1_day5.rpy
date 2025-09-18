# This file will contain the next part of the story.
# The story will continue from here after chapter1_day4.rpy finishes.

label chapter1_day5:
    scene bg_kitchen with fade # Assuming a kitchen background
    m "The next morning, Sarah was up even earlier than usual. I found her in the kitchen, already dressed for work, a whirlwind of efficiency as she made herself a quick smoothie."

    s "Morning, sleepyhead!" She greeted me with a bright smile, a quick peck on the lips. "Sorry if I woke you. Just trying to get a head start on the day. Big meeting with Mr. Henderson this afternoon."

    m "No worries, babe." I yawned, pouring myself a cup of coffee. "You're always so energetic in the mornings. I don't know how you do it."

    s "Adrenaline, mostly." She laughed, a light, airy sound. "And the thought of finally getting this presentation over with. It's been consuming my life for the past week."

    m "I know." I reached for her hand, giving it a gentle squeeze. "You've been working so hard. Make sure you take a break today, okay? Don't burn yourself out."

    s "I will, I promise." She squeezed my hand back, her eyes warm and sincere. "You're always looking out for me, [mc_name]. I love that about you."

    m "I love you too, Sarah." I meant it. Every word. Her dedication, her passion for her work, her unwavering affection for me – it was all part of the woman I fell in love with."

    m "As she gathered her things, I noticed a new, sleek-looking pen clipped to her blazer. It was a nice pen, silver with a subtle engraving. Probably a corporate gift, I thought. Her company was always giving out branded merchandise."

    m "She was about to head out the door when I called after her. "Hey, what's with the fancy new pen?"

    s "Oh, this?" She glanced down at it, a faint blush rising on her cheeks. "Mr. Henderson gave it to me yesterday. Said it was a good luck charm for the presentation. It's a Montblanc, I think. Pretty fancy, huh?"

    m "Wow, a Montblanc? That's quite a gift." I raised an eyebrow, a playful smirk on my face. "He must really want this presentation to go well."

    s "Tell me about it." She rolled her eyes, but there was a hint of amusement in her voice. "He's a bit over the top sometimes, but he means well. Anyway, gotta run! Wish me luck!"

    m "Good luck, babe! You'll crush it!" I called after her as she hurried out the door, blowing me a kiss.

    m "I stood there for a moment, the scent of her perfume lingering in the air. A Montblanc pen. A good luck charm from Mr. Henderson. It was a nice gesture, I supposed. A bit extravagant, maybe, but harmless. Just a client trying to motivate his team. Nothing to worry about. Sarah was just being Sarah, dedicated and charming. And I loved her for it."
    call decrease_mark_awareness(-1) # Mark dismisses the subtle cue of an extravagant gift
    call update_love_score(-1) # Subtle decrease as Mark overlooks a potential, albeit innocent, shift in dynamic

    call chapter1_day6 # Call the next part of the story
    return