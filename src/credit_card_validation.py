
cards = [
            {
                'type': 'maestro',
                'patterns': [5018, 502, 503, 506, 56, 58, 639, 6220, 67],
                'length': [12, 13, 14, 15, 16, 17, 18, 19],
                'cvvLength': [3],
                'luhn': True
            }, {
                'type': 'forbrugsforeningen',
                'patterns': [600],
                'length': [16],
                'cvvLength': [3],
                'luhn': True
            }, {
                'type': 'dankort',
                'patterns': [5019],
                'length': [16],
                'cvvLength': [3],
                'luhn': True
            }, {
                'type': 'visa',
                'patterns': [4],
                'length': [13, 16],
                'cvvLength': [3],
                'luhn': True
            }, {
                'type': 'mastercard',
                'patterns': [51, 52, 53, 54, 55, 22, 23, 24, 25, 26, 27],
                'length': [16],
                'cvvLength': [3],
                'luhn': True
            }, {
                'type': 'amex',
                'patterns': [34, 37],
                'length': [15],
                'cvvLength': [3, 4],
                'luhn': True
            }, {
                'type': 'dinersclub',
                'patterns': [30, 36, 38, 39],
                'length': [14],
                'cvvLength': [3],
                'luhn': True
            }, {
                'type': 'discover',
                'patterns': [60, 64, 65, 622],
                'length': [16],
                'cvvLength': [3],
                'luhn': True
            }, {
                'type': 'unionpay',
                'patterns': [62, 88],
                'length': [16, 17, 18, 19],
                'cvvLength': [3],
                'luhn': False
            }, {
                'type': 'jcb',
                'patterns': [35],
                'length': [16],
                'cvvLength': [3],
                'luhn': True
            }
        ]