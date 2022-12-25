class FourDigitConvter:
    regex = '[0-9]{1}'

    def to_python(self,value):
        return int(value)

    def to_url(self,value):
        return f'{value:1d}'