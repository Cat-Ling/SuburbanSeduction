# This file will contain the next part of the story.
# The story will continue from here after chapter1_day6.rpy finishes.

label chapter1_day7:
    scene bg_hardware_store_day with fade # Assuming a hardware store background during the day
    m "The morning after Sarah's triumph, I woke up feeling refreshed and proud. Her success felt like my own, a shared victory. As I drove to the hardware store, I found myself humming, a lightness in my step."

    m "My day started with the usual rhythm of bolts, lumber, and paint swatches. Mr. Henderson, the one from Sarah's office, even popped in. He was looking for some specialized sealant for his home office, and we chatted briefly."

    h "Morning, Mark!" Mr. Henderson greeted me with a hearty handshake. "Heard about Sarah's presentation yesterday. Absolutely brilliant! She really knocked it out of the park. We're all very impressed."

    m "Thanks, Mr. Henderson. I knew she would." I beamed, a genuine smile spreading across my face. "She worked really hard on it."

    h "She certainly did. And it paid off. We're looking at some exciting new opportunities for her. More responsibility, bigger projects. She's a real asset to the team." He winked. "Keep an eye on her, Mark. She's going places."

    m "I will." I chuckled, feeling a surge of pride. "She deserves it."
    call decrease_mark_awareness(-1) # Mark dismisses the subtle cue about Sarah's rising status and potential changes

    m "Mr. Henderson left with his sealant, and I went back to my work, a warm glow in my chest. Sarah was going places. And I was right there with her, cheering her on."

    d "Big talk about the wife, huh?" David appeared beside me, wiping grease from his hands with a rag. "Mr. Henderson seems to be quite the fan."

    m "He is. Sarah did a fantastic job on her presentation yesterday." I explained, feeling no need to hide my pride.

    d "Good for her. Always knew she was a go-getter." David nodded, then added, "Just make sure she doesn't forget about the little people, eh? All that corporate ladder climbing can change a person."

    m "Sarah would never change, David." I said, a touch of defensiveness in my voice. "She's not like that."
    call decrease_mark_awareness(-1) # Mark dismisses David's well-meaning warning
    call update_love_score(-1) # Subtle decrease as Mark dismisses a potential strain on their relationship

    d "Just saying, [mc_name]. Just saying." David shrugged, then went back to his task. His words, as usual, were easily dismissed. Sarah was Sarah. And she loved me."

    m "The rest of the workday was uneventful. My thoughts kept returning to Sarah and her potential promotion. More responsibility, bigger projects. It was exciting, but also... a little daunting. Our lives were so comfortable, so predictable. Would this change things?"
    call update_love_score(-1) # Subtle decrease as Mark acknowledges a nascent strain, even if he pushes it away

    m "I pushed the thought away. Change was good. Growth was good. And we would navigate it together. We always did."

    scene bg_home_evening with dissolve # Assuming a home evening background
    m "When I got home, Sarah was already there, humming softly as she prepared dinner. She looked up, her eyes bright."

    s "Hey, honey! Guess what? Mr. Henderson officially offered me the lead on the new national campaign! It's a huge step up!"

    m "That's amazing, babe! I knew you'd get it!" I hugged her tightly, genuinely thrilled for her. "When do you start?"

    s "Next week! It's going to be a lot of work, even more travel, but it's exactly what I've been working towards." She beamed, her excitement infectious.

    m "I'm so proud of you, Sarah." I kissed her forehead, a tiny, almost imperceptible flicker of something akin to apprehension stirring within me. More travel. That was new. But it was for her career. And I supported her, completely."
    call decrease_mark_awareness(-1) # Mark dismisses his own apprehension about the travel
    call update_love_score(-1) # Subtle decrease as Mark rationalizes away a potential strain on their time together

    m "We spent the evening talking about her new role, the challenges, and the opportunities. Her enthusiasm was contagious, and soon, my apprehension was replaced by shared excitement. This was a new chapter for us, a new adventure. And we would face it together."

    call chapter1_day8 # Call the next part of the story
    return