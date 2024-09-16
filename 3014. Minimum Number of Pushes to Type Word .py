class Solution:
    def minimumPushes(self, word: str) -> int:
        word_length=len(word)
        full_length=word_length//8
        remaining_char=word_length%8
        total_pushes=0
        print(full_length,remaining_char)
        for i in range(1,full_length+1):
            total_pushes+=i*8
            print(i,i*8)
        total_pushes+=(full_length+1)*remaining_char
        return total_pushes