###
# Copyright (c) 2016, kongr45gpen
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import local.AOL


class AOL(callbacks.Plugin):
    """Adds an AOL command to send messages in AOL format"""

    def aol(self, irc, msg, args, text):
        """text

        Format a message based on AOL standards
        """
        formatted = local.AOL.aol(text)

        irc.reply(formatted, prefixNick = False)
    aol = wrap(aol, ['text'])

Class = AOL


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
