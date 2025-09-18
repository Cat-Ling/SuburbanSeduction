# This file will contain the next part of the story.
# The story will continue from here after chapter1_day8.rpy finishes.

label chapter1_day9:
    scene bg_bedroom_morning with fade # Assuming a bedroom morning background
    m "The news of Sarah's upcoming New York trips settled over me like a fine dust. Not heavy, not suffocating, but present. I tried to shake it off. This was good news, great news even. Her career was soaring. And I was her biggest fan."

    m "Sarah, oblivious to my internal monologue, was already buzzing with plans for the weekend. "We should do something fun, [mc_name]! A proper date night. We haven't had one in ages, with all this presentation madness."

    menu:
        "Suggest a quiet night in, just the two of us.":
            m "That sounds perfect, babe. How about I cook your favorite, and we just relax, watch a movie?"
            s "Oh, that sounds lovely!" Sarah smiled, a genuine, appreciative smile. "A quiet night in sounds exactly what I need. Just you and me."
            call update_love_score(-1) # A very subtle, almost imperceptible decrease. It's not a bad choice, but it's not actively engaging with her new, more dynamic life.
            jump after_quiet_night_suggestion
        "Suggest something more adventurous, to celebrate her new role.":
            m "How about we try that new Italian place downtown? The one with the amazing reviews. A proper celebration for your new role!"
            s "Oh, [mc_name], that's a fantastic idea!" Her eyes lit up. "I've been dying to try that place! You're the best!"
            call update_love_score(1) # A very subtle, almost imperceptible increase. Actively engaging with her new life.
            jump after_adventurous_suggestion

label after_quiet_night_suggestion:
    m "We spent Saturday evening in comfortable silence, the aroma of my homemade pasta filling the kitchen. Sarah seemed relaxed, but I noticed her glancing at her phone a few times, even though she quickly put it away. She was tired, I told myself. Just tired."

    m "Later, curled up on the couch, watching a rom-com, I felt her drift off to sleep beside me. I pulled a blanket over her, kissing her forehead. She was here, with me. That's all that mattered."

    m "But as I lay awake, listening to her soft breathing, a tiny thought, like a persistent mosquito, buzzed in the back of my mind. Was a quiet night in truly what she needed, or was it just what *I* needed?"
    call decrease_mark_awareness(-1) # Mark's subtle lack of awareness of Sarah's true needs

    call chapter1_day10 # Call the next part of the story
    return

label after_adventurous_suggestion:
    m "Saturday night was a whirlwind of delicious food, lively conversation, and shared laughter. The Italian place was everything we hoped for, and Sarah was radiant, her excitement about her new role infectious."

    m "She talked animatedly about her plans for the national campaign, the challenges, the people she'd be working with. I listened, fascinated, asking questions, genuinely engaged in her world. Her phone remained in her purse, forgotten."

    m "Later, as we walked home, hand in hand, the city lights twinkling around us, I felt a profound sense of connection. This was us. Navigating new adventures, together."

    m "As we drifted off to sleep, intertwined in each other's arms, I felt a deep, abiding contentment. Sarah was happy, I was happy. Our love was strong, unshakeable. This new chapter, with all its changes, would only make us stronger."

    call chapter1_day10 # Call the next part of the story
    return