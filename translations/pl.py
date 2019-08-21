#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains the result sentences and intents for the English version
of the Say it again skill.
"""

# Result sentences
RESULT_SAY_SORRY = "Przepraszam, nie pamiętam co powiedziałem"
RESULT_TEXT_SORRY = "Przepraszam, nie pamiętam co powiedziałeś"
RESULT_TEXT = "Usłyszałem \"{0}\" z prawdopodobieństwem {1}."
RESULT_TEXT_NOTHING = "Przepraszam, nic nie słyszałem"
RESULT_INTENT_SORRY = "Przepraszam, nie pamiętam ostatniej akcji"

# Intents
INTENT_SAY_IT_AGAIN = "hermes/intent/kblachowicz:SayItAgain"
INTENT_WHAT_DID_I_SAY = "hermes/intent/kblachowicz:WhatDidISay"
INTENT_REPEAT_ACTION = "hermes/intent/kblachowicz:RepeatAction"