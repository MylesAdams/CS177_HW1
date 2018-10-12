#!/usr/bin/env python3

import math

CipherTextOne = 'KHAQWVTACPFVCMGCECVCRCTVVQUGGJQYKVYQTMUVJGHKTUVVJKPIAQWJCXGQPAQWTJCPFUKUCPQPYQTMKPIECV'

CipherTextTwo = 'qsgxsogubouuoxztqdatoxgukzlbaquowpqjapolnalaholhsgwutanolhkpsgpzxxggbgbolhgqqolhoqpmkbdqzxrgbajadxknukwqamtdglkzhszlbgwsgwawnjoqsoqptghpsalholhbkjlmzqhglgwattdvzpqappsgsabhkqoqplgxrloxgtdpqwaohsqglgbkzqalbjaphkolhqkhofgqsgsgbhgskhamtkjjoqsoqpsgaboqjkztbqjopqoqpgtuwkzlbalbtkkrziolsgwuaxgjoqspzxsaizyytgbgeiwgppoklqsaqpsgxkztblkqsgtimzwpqolhkzqtazhsolhalbjsglpsgsabhkqoqpsgabbkjlalbjaphkolhqkmgholahaoloqjapfgwdiwkfkrolhqkuolbqsaqqsgsgbhgskhsabzlwkttgboqpgtualbjapolqsgaxqkuxwajtolhajadmgpobgpattqsopqsgwgjaphglgwattdawobhgkwuzwwkjolqsgjadjsgwgfgwpsgjalqgbqkpglbqsgsgbhgskhqkalbapqsgbkzmtgbzipktbogwpjgwgatjadphgqqolhzialbjatrolhkuuqkkqsgwiawqpkuqsghwkzlbatoxgpkklxangqkqsgxklxtzpoklqsaqoqjapafgwdbouuoxztqhangolbggb'

CipherTextThree = 'HAFWKFTKFBTEQUUWEXSTXEDFAFBTCSPGFXGUFAFKFHAFPKFBHJXSTFKCVHABHHAFKFVBSWXSFUFEHBUCYF'


def SplitTextIntoChunks(Text: str, ChunkSize: int) -> [int]:
    Chunks = []

    for i in range(0, math.ceil(len(Text) / ChunkSize)):
        Chunks.append(list(Text[i * ChunkSize : (i + 1) * ChunkSize]))

    return Chunks


def FindLetterIndices(Text: str, Letter: str) -> [int]:
    return [i for i, Char in enumerate(Text) if Char == Letter]


# Shifted right by 11
# IFYOUTRYANDTAKEACATAPARTTOSEEHOWITWORKSTHEFIRSTTHINGYOUHAVEONYOURHANDSISANONWORKINGCAT
def Task2A(CipherText: str) -> None:
    for i in range(0, 26):
        print('Shifted by', i)
        for char in CipherTextOne:
            print(chr(((ord(char) + i) % 26) + 65), end='')
        print()


def Task2B(CipherText: str) -> None:
    CommonLetters = {}
    for Char in CipherText:
        if Char in CommonLetters:
            CommonLetters[Char] += 1
        else:
            CommonLetters[Char] = 1

    for LetterTuple in sorted(CommonLetters.items(), key=lambda x: x[1], reverse=True):
        print(LetterTuple[0], LetterTuple[1], sep=' : ')

    print()

    CipherTextChunks = SplitTextIntoChunks(CipherText, 80)
    PlainTextChunks = SplitTextIntoChunks('_' * len(CipherText), 80)

    for CipherTextChunk, PlainTextChunk in zip(CipherTextChunks, PlainTextChunks):
        print(''.join(CipherTextChunk))
        print(''.join(PlainTextChunk))

    print()

    while(True):
        CTLetter: str = input('CT Letter: ')[0]
        PTLetter: str = input('PT Letter: ')[0]

        if (CTLetter == '!' or PTLetter == '!'):
            break

        for CipherTextChunk, PlainTextChunk in zip(CipherTextChunks, PlainTextChunks):
            LetterIndices = FindLetterIndices(CipherTextChunk, CTLetter)

            for Index in LetterIndices:
                PlainTextChunk[Index] = PTLetter

            print(''.join(CipherTextChunk))
            print(''.join(PlainTextChunk))
            print()

# Problem 2B
# g : 77
# q : 63
# a : 59
# o : 52
# l : 51
# k : 48
# s : 46
# b : 42
# p : 41
# h : 38
# t : 31
# w : 30
# z : 26
# j : 26
# x : 19
# u : 18
# d : 12
# m : 8
# i : 8
# n : 6
# r : 5
# f : 5
# y : 2
# v : 1
# e : 1

# --------

# a -> a
# b -> d
# c -> ?q
# d -> y
# e -> x
# f -> v
# g -> e
# h -> g
# i -> p
# j -> w
# k -> o
# l -> n
# m -> b
# n -> m
# o -> i
# p -> s
# q -> t
# r -> k
# s -> h
# t -> l
# u -> f
# v -> j
# w -> r
# x -> c
# y -> z
# z -> u


if __name__ == "__main__":
    print('Problem 2A')
    #Task2A(CipherTextOne)

    print('\nProblem 2B')
    Task2B(CipherTextTwo)

    Task2B(CipherTextThree)
