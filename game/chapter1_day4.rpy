# This file will contain the next part of the story.
# The story will continue from here after chapter1_day3.rpy finishes.

label chapter1_day4:
    scene bg_hardware_store with fade # Assuming a hardware store background
    m "The next day at the hardware store was typical. I helped Mrs. Gable find the right shade of paint for her guest bathroom, advised a young couple on the best sealant for their new deck, and spent a good hour untangling a display of garden hoses."

    d "Hey, [mc_name]!" David clapped me on the shoulder, making me jump. "You look like you're in a trance. Thinking about Sarah, are we?"

    m "Just thinking about dinner, David." I chuckled, trying to sound casual. "Long day."

    d "Tell me about it." He leaned against a stack of paint cans. "Saw Sarah's car still in the office parking lot when I drove by a little while ago. Must be burning the midnight oil for that big presentation, huh?"

    m "Yeah, she's really dedicated to her work." I felt a familiar pang of pride, mixed with a tiny, almost imperceptible flicker of... something else. Concern? Loneliness? I pushed it away.

    d "Dedicated, alright. Hope she's not overdoing it. You know how those corporate types are, always pushing for more." David shook his head, then wandered off to help a customer.

    m "David's words lingered. Sarah working late. It wasn't unusual, especially with a big project. But a part of me, a very small, quiet part, wished she was home, curled up on the couch with me."
    call decrease_mark_awareness(-1) # Mark dismisses David's subtle warning
    call update_love_score(-1) # Subtle decrease as Mark rationalizes away a potential concern

    scene bg_livingroom with fade
    m "When I finally got home, the house was quiet. Too quiet. Sarah's car wasn't in the driveway. I checked my phone. A text from her: 'Running late, babe. Dinner in the fridge. Love you!'"

    m "I heated up the lasagna, eating alone at the kitchen table. It tasted good, but somehow, it wasn't the same without her across from me, sharing stories about our day. I found myself glancing at the clock more often than usual."
    call update_love_score(-1) # Subtle decrease as Mark feels the strain of her absence

    m "Around nine, I heard her car pull into the driveway. A few minutes later, the front door opened, and Sarah walked in, her briefcase in one hand, her shoulders slumped slightly."

    s "Hey, honey." She offered a tired smile, dropping her bag by the door. "Sorry I'm so late. That presentation is really eating up my time."

    m "It's okay, babe. I figured." I went over and gave her a hug, feeling the tension in her shoulders. "Rough day?"

    s "You have no idea." She sighed, leaning into my embrace. "Mr. Henderson is being particularly demanding. He wants everything perfect. I swear, he nitpicks every single word."

    m "Sounds stressful." I rubbed her back, trying to soothe her.

    s "It is. But it'll be worth it if we land this account." She pulled away, heading for the kitchen. "Did you eat?"

    m "Yeah, had the lasagna. It was delicious." I watched her as she poured herself a glass of water, then pulled out her laptop. "You're not going to work more, are you?"

    s "Just a few more things to review. I can't afford to mess this up." Her eyes were already glued to the screen, a focused intensity I admired, but also, tonight, found a little distant.

    m "I watched her, hunched over her laptop, the soft glow illuminating her face. She was beautiful, brilliant, and dedicated. And she was mine. This was just a busy period. It would pass. Everything would go back to normal soon. It had to."
    call decrease_mark_awareness(-1) # Mark dismisses another cue about her increasing preoccupation
    call update_love_score(-1) # Subtle decrease as their connection is strained by her work focus

    call chapter1_day5 # Call the next part of the story
    return