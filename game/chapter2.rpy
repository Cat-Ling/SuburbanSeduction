# This file will contain the consolidated content for Chapter 2.

label c2_day1:
    scene bg_bedroom_morning with fade
    m "The morning light filtered through the blinds. It was the first time in what felt like forever that I had woken up next to Sarah. I turned to look at her, a smile on my face, but she was already awake, sitting on the edge of the bed, scrolling through her phone."

    if sarah_discontent >= 2:
        m "The air in the room was thick with the unspoken tension from last night. My stupid joke had fallen flat, and a wall had gone up between us. She hadn't said anything about it this morning, but her silence was louder than words."

        s "Morning." She said without looking up from her phone. Her voice was flat, neutral.

        m "Morning." I replied, my own voice hesitant. "Sleep okay?"

        s "Fine." She tapped at the screen a few more times before finally putting the phone down and heading to the closet.

        m "I watched her go, a knot of guilt tightening in my stomach. I had been so happy she was home, and I had ruined it with one dumb comment."

        menu:
            "About last night... I'm sorry. It was a stupid joke.":
                $ sarah_discontent -= 2
                $ update_love_score(1) # A small bonus for good communication
                m "I got out of bed and walked over to her. 'Hey,' I said softly. 'About last night... I'm sorry. It was a stupid joke. I was just so happy to see you, and I was being an idiot.'"
                s "She stopped rummaging through her clothes and turned to face me. Her expression softened. 'I know. It just... it wasn't what I needed to hear right then. I was exhausted, and it felt...' she trailed off."
                m "'I know. I'm sorry.' I said, pulling her into a hug. She relaxed in my arms. 'I'm just glad you're home.'"
                s "'Me too.' she murmured into my chest. The tension seemed to melt away."

            "You seem distant. Is everything alright?":
                $ sarah_discontent -= 1
                m "I sat up in bed. 'You seem distant. Is everything alright?' I asked, trying to keep my tone gentle."
                s "She sighed, her shoulders slumping. 'I'm fine. Just tired. The trip was a lot.' She didn't look at me. 'Don't read too much into it.'"
                m "I wasn't convinced, but I let it go. Pushing her would only make things worse. But the distance remained."

            "(Internal) Just give her space. It'll blow over.":
                $ decrease_mark_awareness(-1)
                m "I decided to let it go. Bringing it up would only make it a bigger deal. She was probably just tired and stressed. It would be back to normal in a day or two. I just had to be patient."
                m "I got up and started getting ready for the day, the silence between us stretching on."

    else:
        m "She was already awake, sitting on the edge of the bed, scrolling through her phone. But when she heard me stir, she turned and gave me a warm, sleepy smile."
        s "Morning, handsome." She said, her voice soft and a little husky.
        m "Morning, beautiful." I replied, reaching out to stroke her hair. "Welcome home."
        s "It's good to be home." She leaned in and kissed me, a long, sweet kiss that made me forget all about her trip.

        m "As she was getting ready for work, I noticed she seemed a little preoccupied, her mind already on the day ahead."

        menu:
            "You seem a little quiet. Everything okay?":
                m "I came up behind her as she was doing her makeup. 'You seem a little quiet. Everything okay?'"
                s "She met my eyes in the mirror and smiled. 'Yeah, just thinking about work. I have a big debrief meeting this morning.' She turned and gave me a quick peck on the lips. 'But I'm fine. Really.'"
                m "I smiled back. 'Okay. Just wanted to make sure.'"

            "Want me to make you some coffee?":
                m "'Want me to make you some coffee?' I asked, leaning against the doorframe."
                s "Her face lit up. 'Oh, would you? You're the best.' She blew me a kiss. 'I'll be down in a few minutes.'"
                m "I went downstairs, happy to be back in our familiar routine."

            "(Internal) She's probably just tired from the trip.":
                $ decrease_mark_awareness(-1)
                m "I watched her for a moment, a wave of love washing over me. She was probably just tired from the trip and thinking about work. I didn't need to overanalyze everything. I just needed to be here for her."

    m "Life was slowly returning to normal. Or at least, a new version of it. I couldn't shake the feeling that something had shifted, something I couldn't quite put my finger on. But for now, she was here, and that was enough."

label c2_day2:
    scene bg_kitchen_morning with fade
    m "The next morning, the house was filled with the familiar aroma of coffee and toast. The awkwardness of the previous night had mostly dissipated, replaced by the comfortable rhythm of our shared routine. Sarah was already dressed, a sleek navy blue dress that meant business, but she was smiling as she buttered a piece of toast for me."

    s "Here you go, honey." She slid the plate across the counter. "A little peace offering for being a grump yesterday."

    m "You weren't a grump." I smiled, taking a bite. "You were tired. I get it."

    s "Still. I missed you, and I was so wrapped up in my own head." She sighed, leaning against the counter. "This new role... it's a lot. I feel like I'm constantly trying to prove myself."

    m "You don't have to prove anything to me." I reached for her hand. "You're brilliant. And you're going to be amazing."

    s "Thanks, [mc_name]." She squeezed my hand, her smile a little brighter this time. "I'm just glad you're here to keep me grounded."

    m "Always." I finished my toast, a comfortable silence settling between us. It felt... normal. Like us. But as she gathered her things, her phone buzzed again. She glanced at it, a quick, almost reflexive action, and a faint smile touched her lips before she tucked it into her purse."

    m "I saw it, of course. A fleeting expression, but it was there. A little secret smile that wasn't for me. I chose to ignore it. It was probably just a funny cat video, or a message from one of her friends. Nothing to worry about."
    $ decrease_mark_awareness(-1)

    scene bg_hardware_store_day with fade
    m "The day at the hardware store was a welcome distraction. I was busy, helping customers, restocking shelves, the familiar scent of sawdust and paint a comforting backdrop to my thoughts."

    d "So, the conquering hero has returned, eh?" David's voice boomed from behind me as I was helping a customer with a particularly stubborn bolt.

    m "Something like that." I chuckled, turning to face him. "She's back, and already buried in work."

    d "That's the way it goes, my friend." David leaned in, his voice dropping to a conspiratorial whisper. "Just make sure she's not too buried, if you know what I mean. A man has needs, after all."

    m "I know what you mean, David." I said, a little more sharply than I intended. "And we're fine."

    d "Hey, just looking out for you, buddy." David held up his hands in mock surrender. "You're a good guy, [mc_name]. You deserve to be happy."

    m "I am happy." I said, the words tasting a little hollow, even to my own ears.

    d "Good. That's good." David nodded, then went back to his own work, leaving me with a strange, unsettled feeling.

    scene bg_home_evening with dissolve
    m "I came home to an empty house. Sarah had texted earlier, a quick, 'Working late, don't wait up!' that had become her new mantra. I made myself dinner, a sad-looking sandwich that I ate over the sink, then tried to lose myself in a video game."

    m "But even the familiar thrill of virtual combat couldn't distract me from the silence. I found myself pausing the game, listening for the sound of her car, the key in the lock. But there was nothing."

    m "Around 10 PM, she finally walked in, looking like a soldier returning from a long, hard-fought battle."

    s "I'm so tired, I could sleep for a week." She sighed, dropping her briefcase and collapsing onto the couch.

    m "Rough day?" I asked, sitting down beside her and rubbing her shoulders.

    s "The roughest. We had a major setback with the campaign. A focus group hated the new slogan. Mr. Henderson was... not pleased."

    m "I'm sorry, babe." I said, my heart aching for her. "That sounds awful."

    s "It was." She leaned her head on my shoulder. "But we'll fix it. We have to. I'm flying back to New York next week, a few days earlier than planned, to meet with the team and brainstorm new ideas."

    m "Earlier?" The words slipped out before I could stop them. "But you just got back."

    s "I know." She looked at me, her eyes pleading for understanding. "But this is important, [mc_name]. It's my career. My future."

    menu:
        "Of course, I understand. We'll make it work.":
            m "I took a deep breath, pushing down the wave of disappointment. 'Of course, I understand. We'll make it work.' I said, forcing a smile. 'Whatever you need.'"
            s "Her face flooded with relief. 'Thank you. I knew you'd understand.' She kissed me, a quick, grateful peck. 'I love you.'"
            $ decrease_mark_awareness(-2) # A significant decrease, as Mark is actively suppressing his own feelings to support her.
            $ sarah_discontent -= 1 # Her discontent decreases as she feels supported.

        "This is getting to be a lot, Sarah.":
            m "I sighed, the words tumbling out before I could stop them. 'This is getting to be a lot, Sarah. You're never home. And now you're leaving again?'"
            s "Her face fell, a look of hurt and disappointment in her eyes. 'I thought you supported me, [mc_name]. This is my dream. I can't believe you're making this about you.'"
            m "'I do support you! I just... miss you.' I said, my voice small."
            s "'I miss you too! But this is important!' She stood up, her voice rising. 'I can't do this without your support. I really can't.'"
            $ sarah_discontent += 3 # A significant increase in discontent.
            $ update_love_score(-5) # A major hit to the love score.

        "Is Mr. Henderson going to be there?":
            m "A thought, sharp and unwelcome, pierced through my disappointment. 'Is Mr. Henderson going to be there?' I asked, my voice tight."
            s "She stared at me, her eyes wide with disbelief. 'What? What does that have to do with anything?'"
            m "'I don't know. It just seems like he's always there, doesn't it?'"
            s "'He's my boss, [mc_name]! Of course he's there! I can't believe you're implying...' She shook her head, her voice trembling with a mix of anger and hurt. 'I'm going to bed. I'm too tired for this.'"
            $ sarah_discontent += 5 # A massive increase in discontent.
            $ update_love_score(-10) # A catastrophic hit to the love score.

label c2_day3:
    scene bg_bedroom_morning with fade
    if sarah_discontent >= 5:
        m "The morning was a landscape of ice. Sarah had slept on the very edge of the bed, her back to me, a rigid line of rejection. I hadn't slept much at all, my mind replaying my stupid, jealous question over and over. The silence in the room was a physical weight, pressing down on me."
        m "She was already up and dressed when I opened my eyes, moving with a clipped, efficient anger. She didn't look at me, didn't even acknowledge my existence. It was like I was a ghost in our own bedroom."
        s "I've called a taxi. It'll be here in twenty minutes." Her voice was cold, devoid of any emotion. "I've packed my things. I'll be at the airport early."
        m "Sarah, can we please talk about this?" I pleaded, sitting up.
        s "There's nothing to talk about, [mc_name]." She finally looked at me, her eyes hard. "You made your feelings perfectly clear last night. You don't trust me. After everything... that's what you think of me."
        m "That's not true! I was just... upset. I didn't mean it."
        s "It doesn't matter what you meant. You said it. And I heard it." She turned away, picking up her suitcase. "I have to go. I have a job to do."
        m "Her footsteps were heavy on the stairs. I heard the front door open and close. And then... silence. A silence that felt final, absolute. I had screwed up. Royally."
        $ update_love_score(-5) # The lingering effect of the fight.
    elif sarah_discontent >= 2:
        m "The morning was tense. We moved around each other like two strangers, the ghost of last night's argument hanging between us. She was quiet, her replies to my attempts at conversation clipped and monosyllabic. I knew she was hurt, and I felt a fresh wave of guilt."
        m "As she was getting ready to leave, I tried one more time."
        m "Sarah, I'm sorry about last night. I was out of line. I'm just... having a hard time with all the changes."
        s "I know." She sighed, her shoulders slumping. "I am too. It's a lot, for both of us. But we can't fight like that, [mc_name]. We have to be a team."
        m "I know. You're right." I pulled her into a hug, and after a moment, she relaxed in my arms. "I love you. We'll get through this."
        s "I love you too." She said, her voice muffled against my chest. "I have to go. I'll call you from New York."
        m "The hug had helped, but the tension hadn't completely disappeared. It was a temporary truce, not a resolution."
        $ sarah_discontent -= 1
    else:
        m "The morning was quiet, but not tense. We moved around each other with a gentle understanding. We were both feeling the strain of the upcoming trip, the distance that was about to open up between us again. But there was no anger, just a quiet sadness."
        m "I'll miss you." I said, as she was about to leave.
        s "I'll miss you too." She came over and gave me a long, deep kiss. "It'll be over before you know it. And then we can have a proper vacation, just the two of us. No work, no laptops. I promise."
        m "I'll hold you to that." I smiled, feeling a little better. "Be safe."
        s "Always." She smiled back, a genuine, loving smile. "I love you."
        m "I love you more."

    scene bg_hardware_store_day with fade
    m "The day was a blur. I couldn't focus on work. My conversation with Sarah, whether it was the icy silence, the strained truce, or the bittersweet farewell, kept replaying in my mind. I felt a growing sense of dread, a feeling that things were spiraling out of my control."

    d "You look like you've seen a ghost, [mc_name]." David said, his usual cheerful tone softened with concern. "Everything okay with Sarah?"

    m "She left for New York this morning." I said, my voice flat.

    d "Ah. That explains it." David nodded sympathetically. "Long-distance is tough, man. My cousin, his wife's a pilot. They barely see each other. It's rough."

    m "Yeah. It is." I agreed, the words feeling heavy in my mouth.

    scene bg_home_evening with dissolve
    m "The house was a tomb. The silence was a physical presence, a constant reminder of her absence. I didn't even bother with dinner. I just sat on the couch, staring at the blank TV screen, the hours ticking by."

    m "I thought about calling her, but what would I say? If we had fought, would she even answer? If we hadn't, what was the point of bothering her when she was so busy?"

    menu:
        "Call her. I need to hear her voice, no matter what.":
            m "I picked up the phone, my thumb hovering over her name. I had to try. I pressed the call button, my heart pounding."
            if sarah_discontent >= 5:
                s "(on phone, voice cold) What do you want, [mc_name]?"
                m "I... I just wanted to see if you got there okay."
                s "(on phone) I'm fine. I'm in a meeting. I have to go."
                m "The line went dead. The rejection was a physical blow. I had pushed her away, and now she was gone."
                $ update_love_score(-3)
            else:
                s "(on phone, tired) Hey, honey. I'm in the middle of something right now, can I call you back later?"
                m "Yeah, of course. Just... wanted to hear your voice."
                s "(on phone) I know. I'll call you tonight. I promise."
                m "The call was short, but it was something. A tiny thread of connection in the vast, empty space between us."

        "Send a text: 'Thinking of you. Hope you're having a good day.'":
            m "I decided a text was safer. Less intrusive. I typed out the words, my fingers fumbling. It felt inadequate, but it was better than nothing."
            m "A few minutes later, my phone buzzed. A single, noncommittal reply: 'Thx.'"
            m "I stared at the screen, a fresh wave of loneliness washing over me. It was like talking to a stranger."
            $ update_love_score(-1)

        "Do nothing. Give her space.":
            m "I put my phone down. She needed space. I needed to respect that. Pushing her would only make things worse. I had to trust that she would call when she was ready."
            m "But as the night wore on, and the silence stretched into an eternity, I began to wonder if she ever would."
            $ decrease_mark_awareness(-1)

label c2_day4:
    scene bg_bedroom_morning with fade
    m "I woke up with a dull headache, the ghost of yesterday's turmoil clinging to me like a shroud. The empty space beside me in the bed felt vast, a cold expanse that echoed the emptiness in my chest. Sarah was gone, and I was alone with my thoughts, a dangerous combination."

    if sarah_discontent >= 5:
        m "My heart ached with the memory of her cold fury. 'You don't trust me.' Her words were a brand on my soul. I had let my jealousy, my insecurity, get the better of me, and I had pushed her away. Maybe for good."
    elif sarah_discontent >= 2:
        m "The memory of our strained goodbye was a bitter pill. We had patched things up, but it was a flimsy bandage on a deep wound. The distance between us wasn't just physical anymore. It was emotional, a chasm that seemed to be growing wider with every passing day."
    else:
        m "I missed her. It was a simple, profound ache. I replayed our last kiss, her promise of a vacation, a desperate mantra against the encroaching loneliness. But even that couldn't fill the void she had left behind."

    scene bg_hardware_store_day with fade
    m "Work was a welcome distraction, a familiar routine in a world that felt increasingly chaotic. I threw myself into my tasks, organizing shelves, helping customers, the physical labor a soothing balm for my troubled mind."

    d "You're a man possessed today, [mc_name]!" David exclaimed, watching me haul a stack of lumber. "Trying to build a fortress around your broken heart?"

    m "Just keeping busy, David." I grunted, the words more true than I wanted to admit.

    d "I hear you, man." He nodded, his usual smirk replaced by a look of genuine sympathy. "Hey, a bunch of us are going out for a beer after work. You should come. Get your mind off things."

    m "I don't know, David. I'm not really in the mood."

    d "That's why you should come! A couple of beers, a few laughs. It'll do you good. Don't just sit at home moping."

    scene bg_home_evening with dissolve
    m "I ended up taking David's advice. The bar was loud, crowded, and smelled of stale beer and fried food. It was the last place I wanted to be, but it was better than the crushing silence of an empty house."

    m "I had a few beers, listened to my coworkers' stories about their wives, their kids, their weekend plans. It was a glimpse into a world of normal, happy lives, a world that suddenly felt very far from my own. I felt like an outsider, a tourist in the land of contentment."

    m "I came home late, the alcohol doing little to numb the ache in my chest. The house was dark, silent. I checked my phone, a desperate, foolish hope flaring in my chest. Nothing. Not a call, not a text. Not even a 'Thx.'"

    m "The loneliness was a physical weight, pressing down on me, making it hard to breathe. I felt a surge of anger, at Sarah, at her job, at Mr. Henderson, at the whole damn world. But most of all, I was angry at myself. For being weak, for being jealous, for pushing her away."

    menu:
        "Pour a whiskey and lose myself in the bottom of the glass.":
            m "I went to the kitchen and poured myself a generous glass of whiskey. The amber liquid burned as it went down, a welcome fire in the cold emptiness of my soul. I drank another, and another, until the edges of my pain began to blur, the world softening into a hazy, manageable fog."
            $ update_love_score(-2)
            $ sarah_discontent += 1 # My drinking will only make things worse when she finds out.

        "Go for a long, punishing run.":
            m "I changed into my running clothes, the need for physical exertion a primal scream in my body. I ran until my lungs burned and my legs ached, the physical pain a welcome distraction from the emotional turmoil. I ran until I was too exhausted to think, too tired to feel anything but the rhythmic pounding of my feet on the pavement."

        "Look at old photos of us, trying to remember the good times.":
            m "I pulled out our old photo albums, the pages filled with images of a happier time. Our wedding, our honeymoon, our first Christmas together. We were so young, so in love, so blissfully unaware of the cracks that were beginning to form in our perfect world. The photos were a sweet, painful reminder of everything I was in danger of losing."
            $ update_love_score(1) # A small increase, as I'm focusing on the good times.

label c2_day5:
    scene bg_bedroom_morning with fade
    m "I woke up feeling drained, a hollowed-out feeling in the pit of my stomach. The house was unnervingly quiet, each tick of the clock a hammer blow against the silence. Another day without Sarah stretched before me, a vast, empty expanse."

    scene bg_hardware_store_day with fade
    m "Work was a slog. I moved through the motions, a robot in a flannel shirt. I answered questions, stocked shelves, and rang up customers, my mind a million miles away. I felt disconnected, a ghost in my own life."

    d "You're looking rough, buddy." David said, his voice unusually gentle. "You need to talk?"

    m "I'm fine." I lied, the word tasting like ash in my mouth. "Just tired."

    d "If you say so." David didn't push, for which I was grateful. "But hey, I saw something on my wife's social media this morning. A picture from some fancy New York restaurant. Sarah was in it, with her boss and some other work people. Looked like they were having a good time."

    m "Oh. That's... nice." I said, my voice barely a whisper. A picture. She hadn't sent it to me.

    scene bg_home_evening with dissolve
    m "The evening was a carbon copy of the last: a silent house, a tasteless dinner, and the crushing weight of loneliness. I was just about to give up and go to bed when my phone buzzed. A message from Sarah."

    m "My heart leaped, a flicker of hope in the darkness. I opened the message. It was a photo. A group of people, smiling and laughing around a table laden with food and wine. Sarah was in the center, radiant, a glass of champagne in her hand. And next to her, his arm draped casually over the back of her chair, was Mr. Henderson."

    m "The photo was a punch to the gut. It wasn't just the arm, it was the easy intimacy of the gesture, the way she was leaning into him, the way they were both smiling, sharing a private joke in a crowded room. They looked... like a couple."

    m "My hands were shaking. My blood ran cold. This wasn't just a work dinner. This was something else. Something I didn't want to admit, didn't want to see. But there it was, in living color, a snapshot of my wife, my life, slipping away."

    menu:
        "Reply: 'Looks like fun! Glad you're having a good time.'":
            $ day5_choice = 1
            m "I typed out the words, my fingers stiff and clumsy. It was a lie, a brave front, a desperate attempt to pretend that everything was okay. To be the supportive, trusting husband she wanted me to be. But the words felt like poison in my mouth."
            $ decrease_mark_awareness(-3) # A massive decrease in awareness, as Mark is actively choosing to ignore a major red flag.
            $ update_love_score(-5) # The emotional toll of suppressing his feelings is immense.

        "Reply: 'Who's the guy with his arm around you?'":
            $ day5_choice = 2
            m "My jealousy, hot and sharp, overrode everything else. I had to know. I had to hear her explanation. My thumbs flew across the screen, the question a digital accusation."
            $ sarah_discontent += 5 # A direct confrontation, causing a huge spike in discontent.
            $ update_love_score(-10) # A catastrophic hit to their relationship.

        "Don't reply. Just stare at the photo until the screen goes dark.":
            $ day5_choice = 3
            m "I couldn't reply. I couldn't think. I just stared at the photo, the image burning itself into my brain. Her smile. His arm. The two of them, together. The silence in the house was deafening, broken only by the frantic, panicked beating of my own heart."
            $ update_love_score(-3) # The emotional damage is significant.

label c2_day6:
    scene bg_bedroom_morning with fade
    m "Sleep offered no escape. The image of the photo was burned onto the inside of my eyelids. I woke up feeling like I hadn't slept at all, a cold dread coiling in my stomach."

    if day5_choice == 1: # Supportive reply
        m "My phone buzzed. A reply from Sarah: 'Thanks, honey! It was fun, but I miss you! Can't wait to be home.' Her words were sweet, reassuring. But they did little to quell the storm in my heart. Was I being paranoid? Or was I just a fool?"
        $ sarah_discontent -= 1
    elif day5_choice == 2: # Confrontational reply
        m "My phone buzzed. A reply from Sarah: 'That's my boss, [mc_name]. You know that. I can't believe you're starting this again. I'm trying to work, and I don't have time for your jealousy.' The words were like a slap in the face. I had pushed her even further away."
        $ sarah_discontent += 2
        $ update_love_score(-5)
    else: # No reply
        m "My phone buzzed. A message from Sarah: 'Are you okay? You didn't reply to my photo. Is something wrong?' Her concern, whether genuine or feigned, only twisted the knife in my gut. What could I possibly say?"

    scene bg_hardware_store_day with fade
    m "The hardware store was a special kind of hell today. Every customer seemed to be a happy couple, holding hands, laughing, picking out paint colors for their new life together. It was a constant, brutal reminder of everything I was losing."

    d "Whoa, you look like death warmed over, buddy." David said, his eyes wide. "Seriously, what's going on? You can talk to me, you know."

    m "It's nothing, David." I muttered, turning away. "Just... tired."

    d "You've been 'just tired' for a week, [mc_name]. This is more than that. Is it Sarah? Is she okay?"

    m "She's fine." I said, my voice tight. "She's having a great time in New York."

    d "Okay, okay." David backed off, but I could feel his worried gaze on me for the rest of the day.

    scene bg_home_evening with dissolve
    m "The evening was a long, slow descent into a personal hell. The silence of the house was a canvas, and my mind painted it with a thousand different scenarios, each one more painful than the last. Sarah and Henderson, laughing together, drinking together, maybe even... I couldn't let myself go there. But the thought was a poison, seeping into every corner of my mind."

    m "I needed a distraction. Something, anything, to stop the endless loop of doubt and jealousy."

    menu:
        "Call David and take him up on his offer to talk.":
            $ day7_choice = 1
            m "I picked up the phone and called David. 'Hey, man. You still up for that beer?'"
            d "(on phone) [mc_name]! Yeah, of course! Meet me at O'Malley's in twenty?"
            m "I'll be there."
            # This choice will lead to a scene in the next day where David gives his perspective.

        "Start going through Sarah's things, looking for... something.":
            $ day7_choice = 2
            m "A dark, ugly thought began to form in my mind. I could look. I could go through her things. Her drawers, her closet, her laptop. Maybe I'd find something. An old letter, a diary, anything to explain what was happening. It was a monstrous violation of her privacy. But I was desperate."
            $ update_love_score(-10) # A massive hit for this violation of trust.
            # This will lead to a scene where Mark finds something... or nothing.

        "Sit in the dark and do nothing, letting the pain wash over me.":
            $ day7_choice = 3
            m "I couldn't move. I just sat there, in the dark, the silence a roaring in my ears. The pain was a physical thing, a crushing weight on my chest. I let it wash over me, drowning in a sea of my own misery."
            $ decrease_mark_awareness(-2)

label c2_day8:
    if day7_choice == 1: # Confronted Sarah
        scene bg_home_evening with fade
        m "My heart was a leaden weight in my chest. I had to call her. I had to know. I dialed her number, my hand trembling."
        s "(on phone, clipped) What do you want, [mc_name]?"
        m "The necklace, Sarah. David told me about the necklace."
        s "(on phone) ...What? You were talking to David about me? About us?"
        m "He's my friend, Sarah! I'm allowed to talk to my friends!"
        s "(on phone) Not about this! This is between us! And for the record, the necklace was a team gift. A thank you for all the hard work on the campaign. Not that it's any of your business."
        m "A team gift? That's not what David said."
        s "(on phone) I don't care what David said! I can't believe you're listening to gossip instead of trusting me! I have to go. I have a meeting."
        m "Sarah, wait-"
        m "The line went dead. The silence that followed was a crushing weight. I had accused her, and she had denied it. But her denial felt... thin. Rehearsed. And now she was angry. Angrier than I had ever heard her."
        $ sarah_discontent += 10
        $ update_love_score(-20)
    elif day7_choice == 2: # Waited to think
        scene bg_home_evening with fade
        m "The day passed in a haze of suspicion and doubt. I couldn't eat, I couldn't sleep. The image of the necklace, the note from 'H', was burned into my mind. I had to know the truth. But I was terrified of what that truth might be."
        m "I spent the evening pacing the house like a caged animal, my mind a whirlwind of unanswered questions. Was she cheating on me? Was I going crazy? Was our entire marriage a lie?"
        m "I needed to do something. I couldn't just sit here and let this eat me alive."
    else: # Researched Henderson
        scene bg_home_evening with fade
        m "I spent hours online, a digital voyeur in the life of a man I had never met. Richard Henderson. CEO of a major marketing firm. Divorced, two kids in college. A public profile filled with photos of charity galas, exotic vacations, and a string of beautiful women on his arm. He was everything I wasn't: rich, powerful, successful."
        m "And he was my wife's boss. The man who gave her expensive gifts, who took her on business trips, who had his arm around her in that photo. The more I learned about him, the more my suspicion grew into a monstrous, all-consuming certainty."
        m "I was losing her. To him. To a world I could never be a part of."
        $ update_love_score(-5)

    m "The night offered no answers, only more questions. I was at a crossroads, a precipice. And I had to decide which way to fall."
    menu:
        "I need to get out of here. Go for a drive.":
            $ day8_choice = 1
            m "I grabbed my keys and headed for the door. I just had to get out of this house, away from the silence and the memories. I drove for hours, with no destination in mind, the road a blur of headlights and darkness."
        "I'm calling her. I don't care what she said.":
            $ day8_choice = 2
            m "I picked up the phone again, my thumb hovering over her name. I didn't care if she was in a meeting. I didn't care if she was angry. I needed to talk to her. I needed to hear her voice."
        "I'll just go to bed. Maybe tomorrow will be better.":
            $ day8_choice = 3
            m "I trudged upstairs to our empty bedroom. I crawled into bed, the sheets cold against my skin. I closed my eyes, praying for sleep, for a temporary escape from the nightmare my life had become."
            $ decrease_mark_awareness(-1)

label c2_day9:
    if day8_choice == 1: # Went for a drive
        scene bg_bedroom_morning with fade
        m "I woke up on the couch, a crick in my neck and the faint smell of gasoline on my clothes. The drive had done little to clear my head. It had only delayed the inevitable confrontation with my own thoughts. The suspicion was still there, a cold, hard knot in my stomach."
    elif day8_choice == 2: # Called Sarah again
        scene bg_home_evening with fade
        m "She didn't pick up. I called again. And again. And again. Each ring was a fresh wave of panic, each unanswered call a confirmation of my worst fears. She was ignoring me. She was with him. I knew it. I threw my phone against the wall, a satisfying crunch as the screen shattered. And then, I just sat there, in the dark, the silence a deafening roar."
        $ update_love_score(-10)
        $ sarah_discontent += 5
    else: # Went to bed
        scene bg_bedroom_morning with fade
        m "Sleep was not an escape. It was a descent into a fever dream of paranoia and fear. I dreamt of Sarah and Henderson, their faces contorted in mocking laughter. I dreamt of the necklace, a silver serpent coiled around her throat. I woke up in a cold sweat, my heart pounding, the line between dream and reality blurred and indistinct."

    scene bg_hardware_store_day with fade
    m "I was a zombie at work. I moved in a fog, my mind a million miles away. I barely registered David's concerned glances, his hesitant questions. The world had faded to a dull, monochrome gray."

    scene bg_home_evening with dissolve
    m "The evening was a repeat of the last. A lonely dinner, a silent house, and the suffocating weight of my own thoughts. I was scrolling through my phone, a masochistic ritual of checking her social media, when I saw it. An email notification. From a travel agency."

    m "My blood ran cold. I opened the email. It was a flight confirmation. For two people. To a private resort in the Caribbean. For next month. And the names on the tickets... Mr. and Mrs. Henderson."

    m "I stared at the screen, the words blurring through a haze of disbelief and rage. It wasn't a work trip. It was a vacation. A romantic getaway. For my wife... and her boss. The proof I had been so desperately searching for, and so terrified to find, was right here, in black and white."

    m "The world tilted on its axis. The floor seemed to drop out from under me. Everything I thought I knew, everything I believed in, was a lie. My wife, my Sarah, the love of my life... was cheating on me."

    menu:
        "Forward the email to Sarah with a single question: 'What is this?'":
            $ day9_choice = 1
            m "My fingers were numb, but I managed to type out the words. It was a declaration of war. The end of everything."
            $ sarah_discontent += 20
            $ update_love_score(-50)
        "Delete the email and pretend I never saw it.":
            $ day9_choice = 2
            m "I couldn't do it. I couldn't confront her. Not yet. It was too much, too soon. I deleted the email, the evidence of her betrayal. But the knowledge remained, a poison in my veins."
            $ decrease_mark_awareness(-10)
            $ update_love_score(-20)
        "Call a lawyer.":
            $ day9_choice = 3
            m "This was it. The end. There was no coming back from this. I looked up the number for a divorce lawyer, my heart a cold, dead thing in my chest."

label c2_day10:
    if day9_choice == 1: # Confronted Sarah
        scene bg_home_evening with fade
        m "The reply came almost instantly. 'It's not what it looks like, [mc_name]. It's a work thing. A incentive trip for top performers. My name is on there because I'm the lead on the campaign. It's for Mr. and Mrs. Henderson.' The explanation was plausible. But was it true? Or was it just another lie?"
        menu:
            "I don't believe you.":
                $ day10_choice = 1
                m "I typed back, my fingers trembling with rage. 'I don't believe you. This is over, Sarah.' The words, once sent, could never be taken back. Our marriage was a casualty of a war I had just declared."
                $ sarah_discontent += 20
                $ love_score = 0
            "We need to talk. When you get back.":
                $ day10_choice = 2
                m "I took a deep breath, trying to calm the storm inside me. 'We need to talk. When you get back.' It was a temporary ceasefire, a delay of the inevitable."
                $ sarah_discontent += 5
    elif day9_choice == 2: # Deleted the email
        scene bg_home_evening with fade
        m "I spent the day in a self-imposed prison of silence and suspicion. I didn't talk to anyone, didn't answer my phone. The knowledge of the email was a cancer, eating away at me from the inside. I was a ghost in my own life, haunting the rooms of a house that no longer felt like a home."
        menu:
            "Continue to say nothing. Let her think everything is fine.":
                $ day10_choice = 3
                m "I would play the part of the loving husband. I would smile, I would pretend, I would let her believe her lies were working. And I would wait for the perfect moment to watch it all burn down."
                $ decrease_mark_awareness(-5)
            "Send her a simple 'I love you' text.":
                $ day10_choice = 4
                m "Maybe I was wrong. Maybe there was an explanation. I sent the text, a desperate plea for reassurance, a test. Her reply would tell me everything I needed to know."
                $ update_love_score(5) # A last grasp at hope.
    else: # Called a lawyer
        scene bg_lawyer_office with fade
        m "The lawyer's office was a sterile, impersonal space. The lawyer, a man with a kind face and sad eyes, listened patiently as I told him my story. He gave me a pamphlet on divorce proceedings, a roadmap to the end of my world. I left his office feeling numb, a strange sense of calm settling over me. The decision had been made. There was no going back."
        $ love_score = 1 # The last flicker of love, extinguished.
        menu:
            "Wait for her to get back to tell her in person.":
                $ day10_choice = 5
                m "She deserved that much. To hear it from me, face to face. To see the wreckage of what she had destroyed. I would wait. The calm in my heart was the stillness of a battlefield after the slaughter."
            "Send her a text: 'We need to talk when you get back. I've spoken to a lawyer.'":
                $ day10_choice = 6
                m "I typed the message without emotion. It was a courtesy. A final, formal severing of our ties. The response was immediate, a flurry of question marks and panicked denials. I turned my phone off."
                $ sarah_discontent += 30

    call c2_day11

label c2_day11:
    scene bg_bedroom_morning with fade
    m "The morning light felt different today. It wasn't the gentle start to a new day, but a harsh, interrogating glare. The events of yesterday had cast a long, dark shadow that the sun couldn't erase. My path was chosen, for better or for worse."

    if day10_choice == 1: # Declared it's over
        m "I woke up with a hollow feeling in my chest. I had done it. I had ended my marriage with a text message. There was no reply from Sarah. Just a crushing, absolute silence. It was a silence that spoke volumes, a confirmation of her guilt."
        m "I spent the day in a daze, a ghost haunting the ruins of my life. The world outside my window seemed to move on, oblivious to the fact that mine had just ended."

    elif day10_choice == 2: # We need to talk
        m "The day was a long, slow torture of anticipation. Every buzz of my phone made my heart leap, my stomach clench. Sarah finally replied in the afternoon, a single, terse message: 'I'll be home in two days. We'll talk then.' Two more days. Two more days of this purgatory."

    elif day10_choice == 3: # Pretend everything is fine
        m "I woke up and sent her a text: 'Good morning, beautiful. Hope you have a great day!' The words felt like acid on my tongue. She replied with a stream of heart emojis and 'I love yous'. It was a sickeningly sweet performance, and I was playing my part perfectly. The loving husband. The unsuspecting fool. But I knew the truth. And the waiting was a delicious, private torment."
        $ update_love_score(-5) # The toll of the deception.
        $ decrease_mark_awareness(-2)

    elif day10_choice == 4: # Sent 'I love you'
        m "I waited all morning for a reply. It finally came around noon. 'I love you too, honey. So much.' The words should have been a comfort, a reassurance. But they felt hollow, a lie. Was she just saying what I wanted to hear? Or was I so lost in my own paranoia that I couldn't see the truth?"
        if sarah_discontent >= 10:
            m "The reply felt forced, an obligation. It did nothing to soothe the gnawing doubt in my gut. It only made it worse."
            $ update_love_score(-3)
        else:
            m "For a moment, a tiny flicker of hope ignited in my chest. Maybe I was wrong. Maybe I had overreacted. But the image of the email, of her and Henderson, was a ghost that refused to be banished."
            $ update_love_score(2)

    elif day10_choice == 5: # Wait to tell her in person
        m "I felt a strange sense of calm. The decision was made. The storm was over. Now, there was only the grim, quiet aftermath. I spent the day in a detached haze, making plans for a future that didn't include her. I looked at apartments online, my heart a cold, dead thing in my chest."

    elif day10_choice == 6: # Told her about the lawyer
        m "I had turned my phone off last night. I turned it on this morning to a barrage of notifications. Dozens of missed calls from Sarah. A flood of frantic texts. 'What are you talking about? A lawyer? [mc_name], please call me! This is a misunderstanding!' I read them all, a strange mix of sadness and vindication washing over me. It was too late for explanations. It was too late for us."
        $ sarah_discontent += 10

    m "The day ended as it began, in a state of quiet desperation. The future was a blank page, and I had no idea what to write on it."
    call c2_day12
