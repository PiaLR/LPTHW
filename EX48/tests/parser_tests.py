from nose.tools import *
from ex48.parser import *
from ex48 import lexicon

def test_verb():
    result = lexicon.scan("go north")
    sentence = parse_sentence(result)
    assert_equal(sentence.verb, 'go')
    assert_raises(ParserError, parse_verb, 'noun')
    wrong_result = lexicon.scan("x south")
    assert_raises(ParserError, parse_sentence, wrong_result)

def test_subject():
    result = lexicon.scan("bear go north")
    sentence = parse_sentence(result)
    assert_equal(sentence.subject, 'bear')
    assert_raises(ParserError, parse_verb, 'verb')
    wrong_result = lexicon.scan("go go go")
    assert_raises(ParserError, parse_sentence, wrong_result)

def test_object():
    result = lexicon.scan("bear go north")
    sentence = parse_sentence(result)
    assert_equal(sentence.object, 'north')
    assert_raises(ParserError, parse_verb, 'subj')
    wrong_result = lexicon.scan("bear go x")
    assert_raises(ParserError, parse_sentence, wrong_result)
