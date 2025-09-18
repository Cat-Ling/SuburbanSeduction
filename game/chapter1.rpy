# This file will contain the consolidated content for Chapter 1.

label day1:
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

label day2:
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

label day3:
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

label day4:
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

    s "You have no idea." She sighed, a deep, weary sound. "Mr. Henderson is being particularly demanding. He wants everything perfect. I swear, he nitpicks every single word."

    m "Sounds stressful." I rubbed her back, trying to soothe her.

    s "It is. But it'll be worth it if we land this account." She pulled away, heading for the kitchen. "Did you eat?"

    m "Yeah, had the lasagna. It was delicious." I watched her as she poured herself a glass of water, then pulled out her laptop. "You're not going to work more, are you?"

    s "Just a few more things to review. I can't afford to mess this up." Her eyes were already glued to the screen, a focused intensity I admired, but also, tonight, found a little distant.

    m "I watched her, hunched over her laptop, the soft glow illuminating her face. She was beautiful, brilliant, and dedicated. And she was mine. This was just a busy period. It would pass. Everything would go back to normal soon. It had to."
    call decrease_mark_awareness(-1) # Mark dismisses another cue about her increasing preoccupation
    call update_love_score(-1) # Subtle decrease as their connection is strained by her work focus

label day5:
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

label day6:
    scene bg_hardware_store with fade # Assuming a hardware store background
    m "The day of Sarah's big presentation felt strangely long. Every tick of the clock seemed to stretch, and I found myself constantly checking my phone, half-expecting an update from her. I knew she didn't need my reassurance, but I couldn't help but feel a little anxious for her."

    d "Still got that faraway look, [mc_name]?" David's voice cut through my thoughts as I was restocking a shelf of garden tools. "Big day for the missus, huh?"

    m "Yeah, her big presentation is today." I smiled, a genuine one this time. "She's going to nail it."

    d "Atta boy! That's the spirit." David grinned, then lowered his voice conspiratorially. "Heard Mr. Henderson is a tough cookie. Hope she brought her A-game."

    m "Sarah always brings her A-game, David." I said, a touch of pride in my voice. "She's the best."

    d "No doubt, no doubt." David held up his hands in surrender, then went back to organizing a display of power drills. His comments, while sometimes a little intrusive, were always well-meaning. Just David being David."

    m "The rest of the workday passed in a blur. My thoughts were with Sarah, imagining her in the boardroom, confidently presenting her ideas. I knew she was brilliant, and I had no doubt she would impress everyone."

    scene bg_home_evening with dissolve # Assuming a home evening background
    m "I got home a little earlier than usual, wanting to make sure everything was perfect for her return. I tidied up the living room, put on some soft jazz, and even chilled a bottle of her favorite white wine."

    m "Around six, I heard her key in the lock. The door opened, and Sarah walked in, a wide, triumphant smile on her face. Her eyes sparkled with excitement, and she practically radiated relief."

    s "I did it, [mc_name]!" She practically shouted, dropping her bag and rushing into my arms. "It went perfectly! They loved it!"

    m "I knew you would, babe!" I hugged her tightly, lifting her off her feet and spinning her around. "I'm so proud of you!"

    s "Mr. Henderson was beaming! He said it was the best presentation he'd seen all year. He even hinted at a promotion!" She pulled back, her hands cupping my face, her eyes shining.

    m "A promotion? That's incredible, Sarah!" I kissed her, a long, passionate kiss that spoke volumes of my pride and love.

    s "And it's all thanks to you, for being so supportive." She leaned her forehead against mine. "You're the best husband a girl could ask for."

    m "You deserve all the credit, babe. You worked your ass off for this." I smiled, feeling a profound sense of happiness. This was our life. Supporting each other, celebrating each other's successes. It was perfect."
    call update_love_score(5) # Significant increase due to shared success and strong bond

    m "We spent the rest of the evening celebrating. We ordered takeout, drank the chilled wine, and talked for hours about her presentation, her future at the company, and all the exciting possibilities. Her phone remained forgotten in her bag, her attention solely on me, on us."

    m "As we finally drifted off to sleep, intertwined in each other's arms, I felt a deep, abiding contentment. Sarah was happy, I was happy. Our love was strong, unshakeable. Nothing could come between us."

label day7:
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

label day8:
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

label day9:
    scene bg_bedroom_morning with fade # Assuming a bedroom morning background
    m "The news of Sarah's upcoming New York trips settled over me like a fine dust. Not heavy, not suffocating, but present. I tried to shake it off. This was good news, great news even. Her career was soaring. And I was her biggest fan."

    m "Sarah, oblivious to my internal monologue, was already buzzing with plans for the weekend. 'We should do something fun, [mc_name]! A proper date night. We haven't had one in ages, with all this presentation madness.'"

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

    call day10 # Call the next part of the story

label after_adventurous_suggestion:
    m "Saturday night was a whirlwind of delicious food, lively conversation, and shared laughter. The Italian place was everything we hoped for, and Sarah was radiant, her excitement about her new role infectious."

    m "She talked animatedly about her plans for the national campaign, the challenges, the people she'd be working with. I listened, fascinated, asking questions, genuinely engaged in her world. Her phone remained in her purse, forgotten."

    m "Later, as we walked home, hand in hand, the city lights twinkling around us, I felt a profound sense of connection. This was us. Navigating new adventures, together."

    m "As we drifted off to sleep, intertwined in each other's arms, I felt a deep, abiding contentment. Sarah was happy, I was happy. Our love was strong, unshakeable. This new chapter, with all its changes, would only make us stronger."

    call day10 # Call the next part of the story

label day10:
    scene bg_home_day with fade # Assuming a general home background
    m "The week leading up to Sarah's first New York trip was a strange mix of excitement and subtle tension. Sarah was buzzing, her energy infectious as she finalized presentations, packed her bags, and coordinated with her team. I, on the other hand, found myself feeling a quiet apprehension."

    m "Every evening, after I got home from the hardware store, I'd find her either on a video call, or hunched over her laptop, a focused frown on her face. Dinner became a quick affair, often eaten in silence as she typed away, or punctuated by her sudden exclamations about a new idea or a problem solved."

    m "I tried to be supportive, to match her enthusiasm. I'd ask about her day, about the campaign, about Mr. Henderson. She'd answer, but her eyes would be glued to the screen, her answers brief and distracted."
    s "Mmm, that sounds tempting, [mc_name], but I really need to get through this. I'm so close to finishing this section. Maybe tomorrow?" She gave me an apologetic look, but her fingers were already hovering over the keyboard.
            call update_love_score(-2) # More significant decrease. Mark's need for connection is unmet, and Sarah's focus is clearly elsewhere.
            $ sarah_discontent += 1 # Sarah feels a tiny bit of pressure/guilt, subtly increasing her discontent.
            # mark_awareness does not change here, as it cannot increase.
            jump after_relaxing_evening_suggestion

label after_offer_to_help:
    m "I retreated to the living room, feeling a little useless. I wanted to help, to be part of her world, but it felt like she was in a different orbit entirely. I tried to tell myself it was just the intensity of the new project, that it would pass."

    m "The house was filled with the quiet hum of her laptop, punctuated by the occasional click of her mouse. It was a new kind of quiet, one that felt less peaceful and more... empty."

    call day11 # Call the next part of the story

label after_relaxing_evening_suggestion:
    m "I sighed, a quiet sound that went unheard. I understood, intellectually, that this was important for her career. But emotionally, it stung a little. I missed our easy evenings, our shared laughter, the simple comfort of her undivided attention."

    m "I ended up making myself dinner and watching TV alone. The silence in the house felt heavy, amplified by the knowledge that she was just in the next room, but miles away in her own world of corporate strategy and national campaigns."

    call day11 # Call the next part of the story

label day11:
    scene bg_bedroom_morning with fade # Assuming a bedroom morning background
    m "The morning of Sarah's trip to New York felt different. The air was charged with a quiet anticipation, a mix of her excitement and my own subtle apprehension. She was up even earlier than usual, moving with a focused energy as she double-checked her packing list."

    s "Did I remember my charger?" She muttered to herself, rummaging through her carry-on. "And my presentation notes? Oh, and that new power bank Mr. Henderson recommended."

    m "I've got the chargers, babe." I said, holding up a handful of cords. "And your notes are right here." I handed them to her, trying to catch her eye, but her gaze was already flitting to her watch."

    s "Thanks, [mc_name]. You're a lifesaver." She gave me a quick, distracted kiss on the cheek. "I really need to get going. Traffic to the airport is going to be a nightmare."

    m "I know." I followed her to the front door, feeling a familiar pang of loneliness already setting in. "Call me when you land, okay?"

    s "Of course!" She smiled, a genuine, bright smile, but her eyes were already looking past me, towards the waiting car. "Love you!"

    m "Love you too, Sarah!" I called after her, watching her get into the taxi. The car pulled away, and the street, usually bustling with morning activity, felt suddenly empty. The house felt even emptier."

    m "I spent the rest of the morning in a strange limbo. The silence was deafening. I tried to distract myself with chores, but my mind kept drifting to Sarah, already miles away, embarking on her new adventure. I was proud of her, truly. But a part of me, a selfish, needy part, just wanted her here."

    m "The day dragged on. I went to work, but my heart wasn't in it. David's usual banter seemed louder, more intrusive. The customers' questions felt more demanding. I just wanted the day to be over, so I could hear Sarah's voice, even if it was just for a few minutes."

    scene bg_home_evening with dissolve # Assuming a home evening background
    m "My phone finally buzzed around 6 PM. A text from Sarah: 'Landed safely! Crazy day already. Talk soon! Love you!'"

    m "A wave of relief washed over me, followed by a familiar ache. She was safe. She was busy. And I was here, alone. It was just for a few days, I reminded myself. Just a few days. We would make it work. We always did."

    call day12

label day12:
    scene bg_home_day with fade # Assuming a general home background
    m "The first day of Sarah's New York trip felt incredibly long. The house, usually filled with her vibrant energy, was eerily quiet. Every shadow seemed to stretch, every creak of the floorboards amplified in her absence."

    m "I went to work, but my mind was constantly drifting. I found myself checking my phone every few minutes, hoping for a call, a text, anything more substantial than the brief 'Landed safely!' she'd sent last night."

    d "Missing the missus already, huh?" David asked, leaning against the counter, a knowing smirk on his face. "It's only been a day, [mc_name]."

    m "Just checking in." I shrugged, trying to appear nonchalant. "She's got a big meeting today."

    d "Big city, big meetings." David chuckled. "Don't worry, she'll be back before you know it. Probably with a fancy New York accent and a new appreciation for our little town."

    m "I forced a laugh, but David's words, meant to be reassuring, only amplified my unease. New York. It was a world away from our quiet suburban life. Would she still appreciate our little town after experiencing the hustle and bustle of the big city?"

    scene bg_home_evening with dissolve # Assuming a home evening background
    m "The evening was the hardest. I made myself dinner, but it tasted bland. I tried to watch TV, but my attention kept wandering. I just wanted to hear her voice."

    m "Around 8 PM, my phone rang. It was Sarah! My heart leaped. "Hey, babe! How was your first day?"

    s "(on phone) Hey, honey! It was insane! So much to do, so many people to meet. I'm completely exhausted." Her voice was a little muffled, and I could hear background noise, like she was in a busy place."

    m "Sounds intense. Are you okay?"

    s "(on phone) Yeah, just tired. Listen, I'm actually on my way to a client dinner right now. Mr. Henderson insisted. I just wanted to call quickly before I lost signal."

    m "Oh. A client dinner. Right." My voice felt flat, even to my own ears. "Well, have fun. Don't work too hard."

    s "(on phone) I won't. I miss you already. Talk soon, okay? I'll try to call you tomorrow, but it might be late. Love you!"

    m "Love you too, Sarah." The line went dead. I stared at my phone, the silence in the room pressing in on me. A client dinner. With Mr. Henderson. Of course. It was part of her job. But still...

    m "I tried to push away the tiny, unwelcome tendrils of doubt. She was busy. She was working. This was what she wanted. And I supported her. I had to. But the evening felt long, and the bed felt incredibly empty."

    call day13

label day13:
    scene bg_hardware_store_day with fade # Assuming a hardware store background during the day
    m "The second day of Sarah's trip felt even longer than the first. The initial novelty of having the house to myself had worn off, replaced by a dull ache of absence. Work was a distraction, but even there, her absence was felt."

    d "Still no word from the big city?" David asked, as I was helping a customer load a bag of topsoil into his truck. He always seemed to know when I was thinking about Sarah.

    m "She texted last night. Busy with client dinners." I said, trying to sound casual, but the words felt hollow.

    d "Client dinners, huh?" David raised an eyebrow, a familiar glint in his eye. "Sounds glamorous. Hope she's not working too hard."

    m "She loves her job, David." I said, a little more sharply than I intended. "It's important to her."

    d "Hey, easy there, tiger." David held up his hands in mock surrender. "Just making conversation. You're a little on edge, [mc_name]. Missing her already?"

    m "Of course I am." I sighed, leaning against the counter. "It's just... weird. Not having her around."

    d "Yeah, I get it. My wife went to visit her sister for a week once. House felt like a tomb. You just gotta find ways to keep busy." David offered, surprisingly empathetic.

    m "I nodded, appreciating his attempt at comfort. He was right. I needed to keep busy. But what? The evenings stretched out before me, long and empty."

    scene bg_home_evening with dissolve # Assuming a home evening background
    m "I got home, and the silence hit me harder than usual. I tried to cook, but my heart wasn't in it. The food tasted like ash. I tried to watch TV, but every show seemed to remind me of something Sarah and I would watch together."

    m "Around 9 PM, my phone buzzed. A video call from Sarah! My spirits lifted immediately. I answered, eager to see her face."

    s "(on video call) Hey, honey! Sorry I couldn't call earlier. It's been a crazy day!"

    m "No worries, babe. Just good to see your face." Her face filled the screen, looking a little tired, but still beautiful. She was in a hotel room, the background a blur of generic art."

    s "(on video call) Just got back from a dinner with Mr. Henderson and some potential investors. It went really well! We're making great progress."

    m "That's great, Sarah! I knew you'd crush it." I smiled, genuinely happy for her success, even as a tiny part of me wished she was here.

    s "(on video call) I miss you, [mc_name]. It's weird being here without you. The bed feels huge." She pouted playfully.

    m "I miss you too, babe. More than you know. The house is too quiet without you." I tried to keep my voice light, but a hint of longing crept in.

    s "(on video call) I know. Just a few more days. I'll be home before you know it. I promise to make it up to you. Big time." She winked, and I felt a blush creep up my neck.

    m "I'll hold you to that." I chuckled. "Get some rest, okay? You sound exhausted."

    s "(on video call) I will. You too. Love you!"

    m "Love you more!" I said, as she blew a kiss and the call ended. The screen went dark, and the silence returned, heavier this time. She missed me. That was good. But she was still so far away."

    m "I spent the next hour just staring at the ceiling, replaying our conversation. She missed me. She really did. But the client dinners, the investors, Mr. Henderson... it all felt so far removed from our life here. I pushed the thoughts away. She was coming home soon. That's all that mattered."

    call day14

label day14:
    scene bg_home_evening with fade
    m "Another day gone. The routine of work, eat, and sleep felt hollow without Sarah. I found myself wandering through the house, picking up her things, smelling her perfume on a scarf she'd left behind. It only made the ache of her absence worse."

    m "I sat on the couch, scrolling aimlessly through my phone. I thought about what she'd said on the video call - the hotel, the investors, Mr. Henderson. It all felt so distant, a world away from our quiet life here."

    m "On a whim, I typed the name of her hotel into a search engine. The website was slick and professional, with pictures of luxurious rooms and a rooftop bar overlooking the city. And then I saw it: a 'Live View' link. A webcam showing the hotel lobby."

    m "My heart started to beat a little faster. I could just... take a look. It wasn't about spying. It was about feeling closer to her, seeing a part of her world while she was away. A digital window into her life right now."

    m "But another part of me felt a pang of guilt. Was this what it had come to? Checking up on her like a suspicious teenager? She trusted me. Shouldn't I trust her?"

    menu:
        "Look at the webcam. I just want to feel close to her.":
            $ update_love_score(-1)
            m "I clicked the link. The video feed was surprisingly clear. I could see people coming and going, the bellhops, the reception desk. I scanned the faces, hoping for a glimpse of Sarah. But she wasn't there."

            m "I watched for a few minutes, a strange mix of disappointment and relief washing over me. Then, I saw a familiar figure. Mr. Henderson. He was talking to a group of people, laughing. He looked confident, at ease in this high-powered world. Sarah was nowhere in sight."

            m "I closed the browser, feeling a little foolish. What had I expected? To see her waving at the camera? Still, the image of Henderson lingered in my mind. He was a part of her life now, in a way I wasn't."
            $ sarah_discontent += 0 # No change, as this is all in Mark's head.

        "This is a bad idea. I trust her.":
            $ decrease_mark_awareness(-1) # This will also decrease love_score by 0.5
            m "I closed the browser. This was a line I didn't want to cross. It felt... wrong. A violation of the trust we had built over so many years. She was working hard for us, for our future. The least I could do was believe in her."

            m "I felt a sense of calm settle over me. I had made the right choice. Our relationship was stronger than a momentary pang of loneliness. I would wait for her to call, and I would tell her how much I loved her. No doubts, no suspicions."
            $ sarah_discontent += 0 # No change.

    m "I went to bed, the empty space beside me feeling larger than ever. The trip was almost over. Just a few more days. I just had to hold on."

    call day15

label day15:
    scene bg_home_evening with fade
    m "The final day of Sarah's trip. I woke up with a sense of anticipation I hadn't felt all week. She was coming home. The thought was a warm glow in my chest."

    m "I spent the day in a flurry of activity. I cleaned the house until it sparkled, bought fresh flowers for the table, and started preparing her favorite meal. I wanted everything to be perfect for her return."

    m "Finally, I heard her key in the lock. The door opened, and there she was. She looked tired, but her smile was as bright as ever. She dropped her bags and ran into my arms."

    s "I'm home!" she whispered into my shoulder, and I held her tight, breathing in the familiar scent of her hair.

    m "I missed you so much." I said, my voice thick with emotion.

    s "I missed you too. You have no idea." She pulled back, her eyes shining. "The house looks amazing! And is that... my favorite pasta?"

    m "Only the best for my returning hero." I grinned, leading her to the dining table.

    m "We ate and talked, and for a while, everything felt normal again. She told me about the meetings, the presentations, the endless stream of people. She mentioned Mr. Henderson a few times, always in a professional context, praising his leadership and guidance."

    m "Then, as she was telling me about a particularly difficult client, her phone, which was on the table, buzzed with a notification. She glanced at it, her expression unreadable for a moment, before quickly turning her attention back to me."

    menu:
        "Who was that?":
            $ update_love_score(-1)
            $ sarah_discontent += 1
            s "Oh, it's just... work stuff. Mr. Henderson sending over some final notes on the campaign." She said, her voice a little tight. "It can wait."
            m "I nodded, but a small seed of doubt had been planted. Why did she seem so hesitant to tell me? It was probably nothing, just work stress. But I couldn't shake the feeling that something was off."

        "You must be exhausted. Don't worry about work.":
            $ decrease_mark_awareness(-1) # love_score decreases by 0.5
            m "I reached across the table and took her hand. 'Hey, you're home now. Work can wait. I'm just happy to have you back.' I said, giving her my most reassuring smile."
            s "Her shoulders relaxed, and she smiled back, a genuine, warm smile this time. 'You're right. I'm sorry. It's just... hard to switch off sometimes.' She squeezed my hand. 'Thank you.'"
            m "I felt a wave of love for her. She was just tired, that's all. I was being silly to even think anything else."

        "Making a joke: 'Is that your secret lover?'":
            $ update_love_score(-2)
            $ sarah_discontent += 2
            m "I chuckled, trying to sound playful. 'Is that your secret lover? Can't bear to be apart from you for even one evening?'"
            s "She stared at me for a moment, her smile frozen on her face. Then she forced a laugh, but it didn't reach her eyes. 'Don't be silly, [mc_name]. It's just work.' She picked up her phone and put it in her purse. 'I'm going to go get changed. I'm exhausted.'"
            m "The atmosphere had suddenly turned chilly. I had meant it as a joke, a way to poke fun at the interruption, but it had clearly landed wrong. The rest of the evening was quiet, a strange tension hanging between us."

    m "Later that night, as we lay in bed, I held her close. She felt a little distant, but I told myself it was just the exhaustion from the trip. She was home. That's all that mattered. For now."

    call c2_day1
