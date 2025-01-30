import random

class Generate:
    def nine_aleatory(self) -> str: 
            nove_digitos = ''
            for i in range(9):
                nove_digitos += str(random.randint(0, 9))
            return nove_digitos
    
    def generate_cpf(self) -> str    :
        nine_digit = self.nine_aleatory()

        def digit_iterator(digitos: str, contador: int) -> int:
            res = 0
            for digito in digitos:
                res += (int(digito) * contador)
                contador -= 1
            return int(res)
        
        def digit_calculation(iter: int) -> str:
            iter = (iter * 10) % 11
            digito = 0 if iter > 9 else iter
            return str(digito)
        
        def fist_digit(cpf: str) -> str:
            nine_digit = cpf[:9]
            countdown_timer = 10
            res = digit_iterator(nine_digit, countdown_timer)
            return digit_calculation(res)
        
        def second_digit(cpf: str) -> str:
            ten_digit = cpf[:9] + fist_digit(cpf)
            countdown_timer = 11
            res = digit_iterator(ten_digit, countdown_timer)
            return digit_calculation(res)
        
        cpf: str = f'{nine_digit[:3]}-{nine_digit[3:6]}-{nine_digit[6:9]}.{fist_digit(nine_digit)}{second_digit(nine_digit)}'
        return cpf
        


if __name__ == '__main__':
    
    a = Generate()
    
    print(a.generate_cpf())