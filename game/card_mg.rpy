screen CardScreen:
    grid 4 3:
        align (.5, .5)
        spacing 20
        for card in card_list:
            button:
                xsize 240
                ysize 320
                if card ["value"] != 'empty':
                    if card ["chosen"]:
                        if card ["value"] == 'R':
                            background '#ff0000'
                        if card ["value"] == 'G':
                            background '#1aff00'
                        if card ["value"] == 'B':
                            background '#0084ff'
                        if card ["value"] == 'Y':
                            background '#ffff00'
                        if card ["value"] == 'W':                               #цвета у двух карт должны быть разными
                            #background '#ffffff'
                            if current_wild == 'R':
                                background '#ff0000'
                            if current_wild == 'G':
                                background '#1aff00'
                            if current_wild == 'B':
                                background '#0084ff'
                            if current_wild == 'Y':
                                background '#ffff00'

                    else:
                        background '#fac984'
                action If ((not card ["chosen"] and can_click), [SetDict (card, "chosen", True), Return (card)] ) #нажатие на карту



label CardGame:
    python:
        turns=10
        open_cards = []
        current_wild = 'R'
        can_click = True
        card_values = ['R','R','G','G','Y','Y','B','B','W','W','W']
        card_list = []
        renpy.random.shuffle (card_values)
        card_values.append('empty')
        for i in range (0, len (card_values)):
            if card_values [i] == 'empty':
                card_list.append ({"value": card_values[i], "chosen": True})
            else:
                card_list.append ({"value": card_values[i], "chosen": False})

    show screen CardScreen
   
    label .game_cycle:
        $can_click = True
        if len(open_cards) <2:
            $card = ui.interact()
            if card["value"] == 'W':
                $rand = renpy.random.randint(1,4)
                if rand == 1:
                    $current_wild = 'R'
                if rand == 2:
                    $current_wild = 'G'
                if rand == 3:
                    $current_wild = 'Y'
                if rand == 4:
                    $current_wild = 'B' 
            $open_cards.append(card)
            jump .game_cycle
        $can_click = False
        $renpy.pause (0.3, hard = True)
        if len(open_cards) == 2:
            python:
                if open_cards [0] ["value"] == open_cards [1] ["value"] and open_cards [0] ["value"] != 'W':
                    open_cards [0] ["value"] = 'empty'
                    open_cards [1] ["value"] = 'empty'
                open_cards [0] ["chosen"] = False
                open_cards [1] ["chosen"] = False
                open_cards.clear()
        #здесь будет условие завершения игры
        jump .game_cycle
    #hide screen CardScreen


