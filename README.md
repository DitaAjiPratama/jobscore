# JobScore
Python Script for check your profession value.

## Usage

import the script

    import jobscore

prepare your list.

    history = [
        {
            'year'   : 2015,
            'salary' : 2200000.00,
            'based'  : {
                'gold' : 474773.00,
                'umr'  : 2700000.00
            }
        },
        {
            'year'   : 2016,
            'salary' : 3300000.00,
            'based'  : {
                'gold' : 568643.00,
                'umr'  : 3100000.00
            }
        },
        {
            'year'   : 2018,
            'salary' : 4000000.00,
            'based'  : {
                'gold' : 567498.00,
                'umr'  : 3648036.00
            }
        },
        {
            'year'   : 2019,
            'salary' : 8000000.00,
            'based'  : {
                'gold' : 758000.00,
                'umr'  : 3900000.00
            }
        }
    ]

define a number formating (optional).

    def formating(i):
        return "{:,.2f}".format(i)

to get a percent of the changes comparison in your profession value.

    data = {
        'from'  : 2018,
        'to'    : 2019,
        'based' : 'gold'
    }

    result = formating( jobscore.compare(history, data) )
    print(f'{result}%')

to get a salary increase proposal based on your last profession value.

    data = {
        'percent' : 20, # increase you expected
        'from'    : 2019,
        'based'   : {
            'type'  : 'gold',
            'value' : 1073235.00 # current based value
        }
    }
    
    result = formating( jobscore.proposal(history, data) )
    print(f'Rp {result}')