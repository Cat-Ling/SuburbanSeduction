# This file will contain the next part of the story.
# The story will continue from here after chapter1_day2.rpy finishes.

label chapter1_day3:
    scene bg_livingroom with fade # Assuming a living room background
    m "The workday dragged on, a blur of invoices and customer queries. My mind, however, kept drifting back to Sarah. Her smile that morning, the way she'd tucked her hair behind her ear as she talked about her presentation. I couldn't wait to get home."

    m "As I unlocked the front door, the scent of something delicious wafted from the kitchen. Sarah was already home, a rare treat on a weekday. Usually, her work kept her later than mine."

    s "Hey, stranger!" Sarah called out from the kitchen, her voice cheerful. "Rough day?"

    m "Long day, but much better now that I'm home." I walked into the kitchen, dropping my keys on the counter and wrapping my arms around her waist, resting my chin on her shoulder. She leaned back into my embrace, a soft sigh escaping her lips.

    s "Mmm, that's nice." She turned slightly, pressing a kiss to my cheek. "Dinner's almost ready. I made your favorite lasagna."

    m "You're the best, you know that?" I tightened my hug, inhaling the familiar scent of her shampoo and the delicious aroma of the food.

    s "Only for you, [mc_name]." She chuckled, a warm, genuine sound. "So, how was your day at the hardware store? Any exciting plumbing emergencies?"

    m "Just the usual. Old Mr. Henderson came in, complaining about a leaky faucet. Said he'd tried everything, but it was still dripping. I gave him some tips, hopefully, he can fix it." I paused, then added, "Speaking of Mr. Henderson, how was your lunch with him yesterday? You mentioned it this morning."

    s "Oh, that." Sarah turned off the stove, then faced me, her hands resting on my chest. "It was fine. Productive, actually. He's really keen on this new marketing push. We went over the campaign strategy, the ad copy... he's very particular, but I think we're finally on the same page."

    m "That's good. Sounds like a big project." I looked into her eyes, searching for... I wasn't sure what. Just reassurance, I suppose. Her gaze was clear, open. No hesitation.
    call decrease_mark_awareness(-1) # Mark chooses to dismiss his own subtle anxieties
    call update_love_score(-1) # Subtle decrease for not fully engaging with his own fleeting doubt

    s "It is. And it's going to mean a few late nights, probably. But if it goes well, it could really boost my career." She squeezed my hands. "You don't mind, do you?"

    m "Of course not, babe. I'm proud of you. Just don't overdo it, okay?" I kissed her forehead. "And make sure you eat properly. I can always bring you dinner if you're stuck at the office."

    s "You're too sweet." She smiled, a genuine, loving smile that chased away any lingering, unspoken doubts. "I'll be fine. I'm a big girl."

    m "We spent the rest of the evening in comfortable domesticity. Dinner was delicious, followed by our usual ritual of watching a movie on the couch, Sarah curled up against me. Her phone lay forgotten on the coffee table, a silent testament to her presence and focus on us."

    m "As I drifted off to sleep, her head nestled on my chest, I felt a profound sense of peace. This was our life. Simple, loving, and utterly content. The fleeting thought of David's comment, or Sarah's work emails, seemed utterly ridiculous now. We were solid."

    call chapter1_day4 # Call the next part of the story
    return