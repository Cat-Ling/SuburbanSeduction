# This file will contain the next part of the story.
# The story will continue from here after chapter1_day1.rpy finishes.

label chapter1_day2:
    scene bg_bedroom with fade # Assuming a bedroom background exists
    m "The morning after David's comment was, thankfully, uneventful. Sarah stirred beside me, her soft breathing a comforting rhythm against my ear. I loved these quiet mornings, the world still asleep, just the two of us."

    s "Morning, sleepyhead." Sarah's voice was a gentle murmur as she stretched, her hand finding mine under the covers.

    m "Morning, beautiful." I squeezed her hand, a warmth spreading through me. This was it. This was happiness.

    scene bg_kitchen with dissolve # Assuming a kitchen background
    m "We moved through our morning routine with the practiced ease of a couple who knew each other intimately. Coffee brewed, toast popped, and the morning news droned softly from the living room."

    s "I have a big presentation coming up next week," Sarah said, stirring sugar into her coffee. "Mr. Henderson wants to really push the new campaign. It's a lot of work, but it could be a huge win for the company."

    m "That's great, babe! I know you'll nail it. You always do." I smiled, genuinely proud of her ambition and talent.

    s "Thanks, honey." She smiled back, a quick, bright flash before her gaze drifted to her phone. She was scrolling through something, a faint, almost imperceptible frown creasing her brow for a moment before it smoothed away.

    m "Everything alright?" I asked, not out of suspicion, but simple concern.

    s "Hmm? Oh, yeah, just a work email. Nothing important." She dismissed it with a wave of her hand, but I noticed she didn't put the phone down immediately. She continued to glance at it periodically throughout breakfast, though she was still engaged in our conversation.

    m "Probably just the usual office drama," I thought, taking a bite of my toast. "Sarah gets so invested in her projects. It's one of the things I love about her."
    call decrease_mark_awareness(-1) # Mark chooses to dismiss the subtle cue
    call update_love_score(-1) # Subtle decrease for overlooking a potential, albeit innocent, shift

    m "The rest of the morning passed without incident. We kissed goodbye at the door, a lingering, affectionate kiss that left me feeling warm and secure."

    m "Another normal day. Another day with my amazing wife. Life was good."

    call chapter1_day3 # Call the next part of the story
    return