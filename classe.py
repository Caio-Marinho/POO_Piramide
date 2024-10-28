class Piramide:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.atual = 1  # Índice atual para iterar sobre a pirâmide

    def __iter__(self):
        self.atual = 1  # Reseta o índice para reiniciar a iteração
        return self

    def __next__(self):
        if self.atual <= self.tamanho:  # Verifica se ainda há níveis na pirâmide
            espaco = self.repetir(' ', self.tamanho - self.atual)  # Ajusta a quantidade de espaços
            caracter = self.repetir(str(self.atual), 2 * self.atual - 1)  # Gera o caractere com o número adequado
            self.atual += 1  # Avança para o próximo nível
            return espaco + caracter  # Retorna a linha da pirâmide
        else:
            raise StopIteration  # Levanta StopIteration quando todos os níveis forem gerados

    @staticmethod
    def repetir(texto, n):
        resultado = ''
        for item in range(1, n + 1):
            resultado += texto
        return resultado
