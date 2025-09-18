label after_reaction_to_david_observation:
    m "David's words about seeing Sarah with Mr. Henderson at lunch barely registered. Sarah had clients, of course she had clients. It was probably just a misunderstanding, or David being his usual dramatic self."

    m "My mind was more on the leaky faucet in the bathroom and what we were going to have for dinner. Sarah and I were good. Always had been, always would be."

    menu:
        "Brush it off and focus on home life.":
            m "No point dwelling on something so trivial. Sarah would tell me if there was anything important."
            call decrease_mark_awareness(-1) # Mark chooses to be less aware, triggering love_score drop
            call update_love_score(-0.5) # Additional subtle love_score decrease for dismissing a potential cue
            jump after_brush_off
        "Make a mental note to ask Sarah about her day, casually.":
            m "I'll just ask her about her day, like I always do. No big deal."
            # mark_awareness does not decrease here, as Mark is being more aware
            call update_love_score(1) # Subtle love_score increase for making an effort to connect
            jump after_casual_inquiry

label after_brush_off:
    m "When I got home, Sarah was already there, humming softly as she watered her favorite basil plant. The scent of fresh herbs mingled with the faint aroma of something delicious cooking on the stove. She looked up, her smile warm and genuine."
    s "Hey, honey! You're home early."
    m "Just finished up at the store. What's for dinner? Smells amazing!"
    s "Your favorite, chicken parmesan. I had a pretty good day at work, got a lot done. Mr. Henderson was in a good mood, which always helps."
    m "That's great, babe." I kissed her forehead, the thought of David's comment completely forgotten. Our life was simple, happy. That's all that mattered."
    jump continue_normal_evening

label after_casual_inquiry:
    m "When I got home, Sarah was already there, humming softly as she watered her favorite basil plant. The scent of fresh herbs mingled with the faint aroma of something delicious cooking on the stove. She looked up, her smile warm and genuine."
    s "Hey, honey! You're home early."
    m "Just finished up at the store. How was your day, babe? Anything interesting happen?"
    s "Oh, you know, the usual. Lots of emails, a few calls. Had lunch with Mr. Henderson, actually. We were finalizing the details for the new ad campaign. He was surprisingly agreeable today."
    m "That's good to hear." I smiled, genuinely pleased for her. It was just a normal work lunch, exactly as I'd expected. David really did make a mountain out of a molehill."
    s "Yeah, it was productive. And now, I'm making your favorite, chicken parmesan!"
    m "You're the best!" I pulled her into a hug, feeling a wave of contentment. Our life was simple, happy. That's all that mattered."
    jump continue_normal_evening

label continue_normal_evening:
    m "The rest of the evening unfolded in a comfortable rhythm. We ate dinner, sharing stories from our day, laughing at Sarah's recounting of Mr. Henderson's peculiar demands for ad copy. Later, we curled up on the couch, watching a documentary about ancient civilizations, Sarah occasionally dozing off on my shoulder."
    m "As I carried her to bed, her head nestled against my chest, I felt a profound sense of peace. This was our life. Simple, loving, and utterly content. David's comment was a distant, forgotten whisper."
    s "I love you, [mc_name]." She mumbled, half-asleep, as I tucked her in."
    m "I love you too, Sarah. More than anything."
    call chapter1_day2 # Call the next part of the story