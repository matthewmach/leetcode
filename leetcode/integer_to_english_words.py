class Solution:
    def numberToWords(self, num: int) -> str:
        def helper(n):
            if n == 0:
                return ""
            digits = {
                1:"One",
                2:"Two",
                3:"Three",
                4:"Four",
                5:"Five",
                6:"Six",
                7:"Seven",
                8:"Eight",
                9:"Nine",
            }
            teens = {
                
                11:"Eleven",
                12:"Twelve",
                13:"Thirteen",
                14:"Fourteen",
                15:"Fifteen",
                16:"Sixteen",
                17:"Seventeen",
                18:"Eighteen",
                19:"Nineteen",
            }
            tens = {
                10:"Ten",
                20:"Twenty",
                30:"Thirty",
                40:"Forty",
                50:"Fifty",
                60:"Sixty",
                70:"Seventy",
                80:"Eighty",
                90:"Ninety",
                100:"Hundred",
            }
            out = ""
            if n // 100 > 0:
                out = digits[n // 100] + " " + tens[100]
                n = n % 100
            if n < 20 and n > 10:
                if out:
                    out = out + " "
                out = out + teens[n]
                n = 0

            if n - n % 10 > 0:
                if out:
                    out = out + " "
                out = out + tens[n - n % 10] 
            if n % 10 > 0:
                if out:
                    out = out + " "
                out = out + digits[n % 10]
            return out 
        
        thousands = {
            0:"",
            1:" Thousand",
            2:" Million",
            3:" Billion",
            4:" Trillion",
        }

        thousands_count = 0
        out = ""
        if num == 0:
            return "Zero"

        while num > 0:

            print (out)
            thousand = num % 1000
            if thousand != 0:
                if out:
                    out = " " + out
                out = helper(thousand )+ thousands[thousands_count]  + out        
            thousands_count += 1
            num = num // 1000
        return out