import re
class Validation:
    def validate_cpf(self, cpf: str) -> str    :
        CPF = cpf.replace('.', '').replace('-', '')

        def validate_input(valor: str) -> bool: # Verifica se o valor é uma string
            if not isinstance(valor, str):
                return False
            padrao = r'^\d{11}$' # Define o padrão de regex para exatamente 11 dígitos
            if re.match(padrao, valor): # Verifica se o valor corresponde ao padrão
                return True
            return False

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
        
        if validate_input(CPF):
            cpf_calculation: str = f'{CPF[:9]}{fist_digit(CPF)}{second_digit(CPF)}'

            if CPF == cpf_calculation:
                return f'O CPF: {cpf} é válido.'     
               
            return f'O CPF: {CPF} é Inválido!'    
        
        return f'O CPF: {CPF} está incorreto!'                