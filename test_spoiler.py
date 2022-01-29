from spoiler import spoilerize_buffer, spoilerize_irc


def test_spoilerize_buffer():
    msg1 = 'This message has no spoilers.'
    msg2 = 'This message has no spoilers.'
    assert spoilerize_buffer(..., ..., ..., msg1) == msg2

    msg1 = ('The answer to life, the universe, and everything '
            'is <spoiler>42</spoiler>.')
    msg2 = ('The answer to life, the universe, and everything '
            'is \x0314,1442\x03.')
    assert spoilerize_buffer(..., ..., ..., msg1) == msg2

    msg1 = ('<spoiler 3>Darth Vader</spoiler> is <spoiler blue>'
            'Luke</spoiler>\'s father.')
    msg2 = ('\x0303,03Darth Vader\x03 is \x0302,02Luke\x03\'s '
            'father.')
    assert spoilerize_buffer(..., ..., ..., msg1) == msg2


def test_spoilerize_irc():
    msg1 = 'PRIVMSG #foo :This message has no spoilers.'
    msg2 = 'PRIVMSG #foo :This message has no spoilers.'
    assert spoilerize_irc(..., ..., ..., msg1) == msg2
    # TODO: use something other than None? 0? empty string? ellipsis? _ (nah)?

    msg1 = ('PRIVMSG #lug :The answer to life, the universe, and everything '
            'is <spoiler>42</spoiler>.')
    msg2 = ('PRIVMSG #lug :The answer to life, the universe, and everything '
            'is \x0314,1442\x03.')
    assert spoilerize_irc(..., ..., ..., msg1) == msg2

    msg1 = ('PRIVMSG #lug :<spoiler 3>Darth Vader</spoiler> is <spoiler blue>'
            'Luke</spoiler>\'s father.')
    msg2 = ('PRIVMSG #lug :\x0303,03Darth Vader\x03 is \x0302,02Luke\x03\'s '
            'father.')
    assert spoilerize_irc(..., ..., ..., msg1) == msg2
