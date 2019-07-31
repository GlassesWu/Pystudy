def num_convert(input_num):
    """
    数值转换函数，将浮点型数字与整型数字作对应转换，非数值类型输入转换失败提示错误
    """
    try:
        if '.' in input_num:
            output_num = float(input_num)
        else:
            output_num = int(input_num)
    except:
        print('请输入数字！')
    else:
        return output_num


def operator_check(input_operator):
    """
    操作符检查函数，对输入的操作符进行检查，不在输入范围内提示错误
    """
    if input_operator in ['+', '-', '*', '/', '//', '%', '**']:
        pass
    else:
        input_operator = 1
        print('操作符有误，请输入以下操作符之一：加+ 减- 乘* 除/ 整除// 取余% 幂**')
    return input_operator


def calculate(input_num1, input_operator, input_num2):
    """
    计算函数，做相应计算
    1.操作符我不知道还有没有能绕过检查函数的，再加提示吧
    2.关于计算，这七种计算方式我也不知道会不会算不出结果，所以同样加一层异常判断吧
    """
    try:
        if input_operator == '+':
            result = input_num1 + input_num2
        elif input_operator == '-':
            result = input_num1 - input_num2
        elif input_operator == '*':
            result = input_num1 * input_num2
        elif input_operator == '/':
            result = input_num1 / input_num2
        elif input_operator == '//':
            result = input_num1 // input_num2
        elif input_operator == '%':
            result = input_num1 % input_num2
        elif input_operator == '**':
            result = input_num1 ** input_num2
        else:
            result = '操作符不存在！'
        print('计算结果：'+str(num1)+' '+str(operator)+' '+str(num2)+' '+'='+' '+str(result))
    except:
        print('无法得出计算结果')
    else:
        pass


num1 = num_convert(input('请输入第一个操作数：'))
# 判断num1的类型，不正确就一直循环
while not isinstance(num1, (int, float)):
    num1 = num_convert(input('请输入第一个操作数：'))
operator = operator_check(input('请输入以下操作符之一：加+ 减- 乘* 除/ 整除// 取余% 幂**'))
# 判断操作符的类型，不正确就一直循环
while isinstance(operator, int):
    operator = operator_check(input('请输入以下操作符之一：加+ 减- 乘* 除/ 整除// 取余% 幂**'))
num2 = num_convert(input('请输入第二个操作数：'))
# 判断num2的类型，不正确就一直循环
while not isinstance(num2, (int, float)):
    num2 = num_convert(input('请输入第二个操作数：'))
calculate(num1, operator, num2)
