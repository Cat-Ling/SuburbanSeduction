# This file will contain the next part of the story.
# The story will continue from here after chapter1_day7.rpy finishes.

label chapter1_day8:
    scene bg_bedroom_morning with fade # Assuming a bedroom morning background
    m "The alarm blared at 6:00 AM, an hour earlier than our usual. Sarah groaned beside me, but was already reaching for her phone, her fingers flying across the screen even before her eyes were fully open."

    s "Morning, early bird." She mumbled, not looking up. "Just checking emails. National campaign, you know. It's already buzzing."

    m "I know." I stretched, feeling the familiar ache in my back from a long day of lifting boxes. "You got a big day today?"

    s "Every day is a big day now, honey." She finally looked at me, a tired but determined smile on her face. "First official day leading the national team. Lots of calls, lots of planning. I probably won't be home until late."

    m "I figured." I swung my legs out of bed. "I'll make sure dinner's ready when you get back, no matter how late."

    s "You're the best." She blew me a kiss, then was out of bed and into the bathroom, the shower starting almost immediately."
    call decrease_mark_awareness(-1) # Mark dismisses Sarah's early morning preoccupation as normal determination
    call update_love_score(-1) # Subtle decrease as their morning routine becomes more rushed and less connected

    scene bg_kitchen_morning with dissolve # Assuming a kitchen morning background
    m "Breakfast was a rushed affair. Sarah, still glued to her phone, ate a piece of toast standing up, occasionally muttering to herself about marketing strategies and budget allocations. I made us both coffee, but hers was half-finished by the time she grabbed her briefcase."

    s "Gotta run!" She called out, already at the door. "Love you!"

    m "Love you too!" I called back, the door already closing behind her. The house felt suddenly quiet, the usual morning bustle replaced by an unfamiliar stillness. It was just 6:45 AM."

    scene bg_hardware_store_day with fade # Assuming a hardware store background during the day
    m "My day at the hardware store was, as usual, a steady stream of customers. Mrs. Rodriguez needed advice on repotting her prize-winning orchids, young Timmy from down the street wanted help finding a specific type of screw for his skateboard, and a new contractor was looking to buy a bulk order of lumber."

    m "I spent an hour in the back, meticulously organizing the new shipment of power tools, making sure every wrench and drill bit was in its proper place. It was satisfying work, tangible and straightforward. No abstract marketing campaigns or demanding clients, just honest work and happy customers."

    d "Still holding down the fort, [mc_name]?" David sauntered over, leaning against a display of hammers. "Sarah still burning the candle at both ends?"

    m "She's got a big new role, David. National campaign." I said, trying to keep the pride in my voice from sounding defensive. "It's a lot of work."

    d "National, huh? Fancy. Just make sure she doesn't forget where she came from." He winked, then walked off, whistling a tuneless melody.

    m "David's comments, as always, were a little annoying, but harmless. Sarah would never forget where she came from. She was grounded, real. This new job was just a testament to her talent, not a change in her character."
    call decrease_mark_awareness(-1) # Mark dismisses David's subtle warning about Sarah changing
    call update_love_score(-1) # Subtle decrease as Mark rationalizes away a potential strain on their relationship

    scene bg_home_evening with dissolve # Assuming a home evening background
    m "I got home around five, the house still empty. I started dinner, a simple pasta dish, and put on some music. The quiet was nice, at first. A chance to unwind. But as the hours ticked by, it started to feel... empty."

    m "I ate dinner alone, watching an old movie. Sarah's usual spot at the table remained vacant. Her presence, usually so vibrant and comforting, was noticeably absent. I missed her laughter, her stories about her day, even her occasional complaints about her boss."
    call update_love_score(-1) # Subtle decrease as Mark feels the strain of her prolonged absence

    m "Around 9:30 PM, I heard her car. The familiar sound brought a wave of relief. She walked in, looking exhausted but still managing a tired smile."

    s "Hey, honey." She dropped her bag with a thud. "Long day. Just finished a conference call with the West Coast team."

    m "I know. Dinner's ready." I gestured to the table. "I saved you some."

    s "You're a lifesaver." She sat down, picking at her food. "This campaign is going to be huge, [mc_name]. But it's a beast. I'm going to be traveling a lot more, too. Starting next month, I'll be in New York for a few days every other week."

    m "New York?" I tried to keep my voice even. "That's... a lot of travel."

    s "I know. But it's necessary. Face-to-face meetings, building relationships. It's part of the job." She looked at me, her eyes searching. "You okay with that?"

    m "Of course, babe. I support you, always." I reached across the table and took her hand, squeezing it reassuringly. "It's a big opportunity. We'll make it work. We always do."

    m "I smiled, but a tiny knot formed in my stomach. New York. Every other week. It was a lot. But she was so excited, so passionate. And I loved her. I would always support her. Even if it meant a little less of her at home. It was just a phase. It had to be."
    call decrease_mark_awareness(-1) # Mark dismisses his own apprehension about the travel
    call update_love_score(-1) # Subtle decrease as Mark rationalizes away a potential strain on their time together

    call chapter1_day9 # Call the next part of the story
    return