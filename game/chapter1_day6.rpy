# This file will contain the next part of the story.
# The story will continue from here after chapter1_day5.rpy finishes.

label chapter1_day6:
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

    call chapter1_day7 # Call the next part of the story
    return