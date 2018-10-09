#!/usr/bin/env python3

CipherTextOne = 'KHAQWVTACPFVCMGCECVCRCTVVQUGGJQYKVYQTMUVJGHKTUVVJKPIAQWJCXGQPAQWTJCPFUKUCPQPYQTMKPIECV'

CipherTextTwo = 'qsgxsogubouuoxztqdatoxgukzlbaquowpqjapolnalaholhsgwutanolhkpsgpzxxggbgbolhgqqolhoqpmkbdqzxrgbajadxknukwqamtdglkzhszlbgwsgwawnjoqsoqptghpsalholhbkjlmzqhglgwattdvzpqappsgsabhkqoqplgxrloxgtdpqwaohsqglgbkzqalbjaphkolhqkhofgqsgsgbhgskhamtkjjoqsoqpsgaboqjkztbqjopqoqpgtuwkzlbalbtkkrziolsgwuaxgjoqspzxsaizyytgbgeiwgppoklqsaqpsgxkztblkqsgtimzwpqolhkzqtazhsolhalbjsglpsgsabhkqoqpsgabbkjlalbjaphkolhqkmgholahaoloqjapfgwdiwkfkrolhqkuolbqsaqqsgsgbhgskhsabzlwkttgboqpgtualbjapolqsgaxqkuxwajtolhajadmgpobgpattqsopqsgwgjaphglgwattdawobhgkwuzwwkjolqsgjadjsgwgfgwpsgjalqgbqkpglbqsgsgbhgskhqkalbapqsgbkzmtgbzipktbogwpjgwgatjadphgqqolhzialbjatrolhkuuqkkqsgwiawqpkuqsghwkzlbatoxgpkklxangqkqsgxklxtzpoklqsaqoqjapafgwdbouuoxztqhangolbggb'

CipherTextThree = 'HAFWKFTKFBTEQUUWEXSTXEDFAFBTCSPGFXGUFAFKFHAFPKFBHJXSTFKCVHABHHAFKFVBSWXSFUFEHBUCYF'

# Shifted right by 11
# IFYOUTRYANDTAKEACATAPARTTOSEEHOWITWORKSTHEFIRSTTHINGYOUHAVEONYOURHANDSISANONWORKINGCAT
def Task2A():
    for i in range(0, 26):
        print('Shifted by', i)
        for char in CipherTextOne:
            print(chr(((ord(char) + i) % 26) + 65), end='')
        print()


Task2A()
