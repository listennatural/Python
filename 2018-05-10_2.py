import decimal
"""
企业发放的奖金根据利润提成。利润 (p) ：
    低于或等于 10 万元时，奖金可提 10%；
    高于 10 万元，低于 20 万元时，低于 10 万元的部分按 10%提成，高于 10万元的部分，可提成 7.5%；
    20 万到 40 万之间时，高于 20 万元的部分，可提成 5%；
    40 万到 60 万之间时，高于 40 万元的部分，可提成 3%；
    60 万到 100 万之间时，高于 60 万元的部分，可提成 1.5%，
    高于 100 万元时，超过 100 万元的部分按 1%提成，
    从键盘输入当月利润 p ，求应发放奖金总数？
"""
p = input('请输入当前月利润(万)')

try:
    p = decimal.Decimal(p)
    if p - 10 > 0:
        if p - 20 > 0:
            if p - 40 > 0:
                if p - 60 > 0:
                    if p - 100 > 0:
                        bonus = (p - 100) * decimal.Decimal('0.001') + decimal.Decimal('3.950')
                    else:
                        bonus = (p - 60) * decimal.Decimal('0.015') + decimal.Decimal('3.350')
                else:
                    bonus = (p - 40) * decimal.Decimal('0.03') + decimal.Decimal('2.750')
            else:
                bonus = (p - 20) * decimal.Decimal('0.05') + decimal.Decimal('1.750')
        else:
            bonus = (p - 10) * decimal.Decimal('0.075') + 1
    else:
        bonus = p * decimal.Decimal('0.1')

    print('奖金为：', bonus, '万')
except decimal.InvalidOperation:
    print('请输入正确的月利润!!!')