from collections import namedtuple

Mode = namedtuple('Mode', 'background text border light_border hover edit')

DARKMODE = Mode('rgb(43, 46, 51)', 'rgb(235, 235, 235)', 'rgb(29, 29, 29)', 'rgb(49, 49, 49)',
                'rgb(50, 54, 60)', 'rgb(42, 45, 50)')

LIGHTMODE = Mode('rgb(235, 235, 235)', 'rgb(62, 65, 73)', 'rgb(215, 215, 215)', 'rgb(207, 207, 207)',
                 'rgb(222, 222, 222)', 'rgb(230, 230, 230)')
