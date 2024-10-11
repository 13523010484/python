import code
import sys

# 设置提示符  模拟在工具终端的使用效果  具体输入 print([1,2])  可以打印出具体值
sys.ps1 = 'C> '
sys.ps2 = '... '

# 创建交互式 shell
shell = code.InteractiveConsole(locals())
shell.interact()