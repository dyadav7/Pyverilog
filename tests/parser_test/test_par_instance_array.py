from __future__ import absolute_import
from __future__ import print_function
import os
import sys
from pyverilog.vparser.parser import VerilogCodeParser

try:
    from StringIO import StringIO
except:
    from io import StringIO

codedir = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))) + '/verilogcode/'

expected = """\
Source:  (at 1)
  Description:  (at 1)
    Module: TOP, None (at 1)
      Ioport:  (at 3)
        Input: VAL, False (at 3)
          Width:  (at 3)
            IntConst: 3 (at 3)
            IntConst: 0 (at 3)
      Ioport:  (at 4)
        Input: in0, False (at 4)
          Width:  (at 4)
            IntConst: 3 (at 4)
            IntConst: 0 (at 4)
      Ioport:  (at 4)
        Input: in1, False (at 4)
          Width:  (at 4)
            IntConst: 3 (at 4)
            IntConst: 0 (at 4)
      Ioport:  (at 4)
        Input: in2, False (at 4)
          Width:  (at 4)
            IntConst: 3 (at 4)
            IntConst: 0 (at 4)
      Ioport:  (at 5)
        Input: in3, False (at 5)
      Ioport:  (at 5)
        Input: in4, False (at 5)
      Ioport:  (at 5)
        Input: in5, False (at 5)
      Ioport:  (at 6)
        Output: LED0, False (at 6)
          Width:  (at 6)
            IntConst: 3 (at 6)
            IntConst: 0 (at 6)
      Ioport:  (at 6)
        Output: LED1, False (at 6)
          Width:  (at 6)
            IntConst: 3 (at 6)
            IntConst: 0 (at 6)
      Ioport:  (at 6)
        Output: LED2, False (at 6)
          Width:  (at 6)
            IntConst: 3 (at 6)
            IntConst: 0 (at 6)
      Ioport:  (at 6)
        Output: LED3, False (at 6)
          Width:  (at 6)
            IntConst: 3 (at 6)
            IntConst: 0 (at 6)
      Ioport:  (at 7)
        Output: LED4, False (at 7)
      Ioport:  (at 7)
        Output: LED5, False (at 7)
      Decl:  (at 10)
        Instance: SUB, inst_sub0 (at 10)
          ParamArg: MODE (at 11)
            IntConst: 0 (at 11)
          PortArg: None (at 12)
            Pointer:  (at 12)
              Identifier: VAL (at 12)
              IntConst: 0 (at 12)
          PortArg: None (at 12)
            Pointer:  (at 12)
              Identifier: LED0 (at 12)
              IntConst: 0 (at 12)
        Instance: SUB, inst_sub1 (at 10)
          ParamArg: MODE (at 11)
            IntConst: 0 (at 11)
          PortArg: None (at 13)
            Pointer:  (at 13)
              Identifier: VAL (at 13)
              IntConst: 1 (at 13)
          PortArg: None (at 13)
            Pointer:  (at 13)
              Identifier: LED0 (at 13)
              IntConst: 1 (at 13)
        Instance: SUB, inst_sub2 (at 10)
          ParamArg: MODE (at 11)
            IntConst: 0 (at 11)
          PortArg: None (at 14)
            Pointer:  (at 14)
              Identifier: VAL (at 14)
              IntConst: 2 (at 14)
          PortArg: None (at 14)
            Pointer:  (at 14)
              Identifier: LED0 (at 14)
              IntConst: 2 (at 14)
        Instance: SUB, inst_sub3 (at 10)
          ParamArg: MODE (at 11)
            IntConst: 0 (at 11)
          PortArg: None (at 15)
            Pointer:  (at 15)
              Identifier: VAL (at 15)
              IntConst: 3 (at 15)
          PortArg: None (at 15)
            Pointer:  (at 15)
              Identifier: LED0 (at 15)
              IntConst: 3 (at 15)
      Decl:  (at 17)
        Instance: SUB, inst_sub4 (at 17)
          Width:  (at 19)
            IntConst: 3 (at 19)
            IntConst: 0 (at 19)
          ParamArg: MODE (at 18)
            IntConst: 0 (at 18)
          PortArg: None (at 19)
            Identifier: VAL (at 19)
          PortArg: None (at 19)
            Identifier: LED1 (at 19)
        Instance: SUB, inst_sub5 (at 17)
          Width:  (at 20)
            IntConst: 3 (at 20)
            IntConst: 0 (at 20)
          ParamArg: MODE (at 18)
            IntConst: 0 (at 18)
          PortArg: None (at 20)
            Identifier: VAL (at 20)
          PortArg: None (at 20)
            Identifier: LED2 (at 20)
      Decl:  (at 22)
        Instance: and, U0 (at 22)
          Width:  (at 22)
            IntConst: 3 (at 22)
            IntConst: 0 (at 22)
          PortArg: None (at 22)
            Identifier: LED3 (at 22)
          PortArg: None (at 22)
            Identifier: in0 (at 22)
          PortArg: None (at 22)
            Identifier: in1 (at 22)
          PortArg: None (at 22)
            Identifier: in2 (at 22)
      Decl:  (at 23)
        Instance: and,  (at 23)
          PortArg: None (at 23)
            Identifier: LED4 (at 23)
          PortArg: None (at 23)
            Identifier: in3 (at 23)
          PortArg: None (at 23)
            Identifier: in4 (at 23)
          PortArg: None (at 23)
            Identifier: in5 (at 23)
        Instance: and,  (at 23)
          PortArg: None (at 23)
            Identifier: LED5 (at 23)
          PortArg: None (at 23)
            Identifier: in3 (at 23)
          PortArg: None (at 23)
            Identifier: in4 (at 23)
          PortArg: None (at 23)
            Identifier: in5 (at 23)
    Module: SUB, None (at 26)
      Decl:  (at 28)
        Parameter: MODE, False (at 28)
          Rvalue:  (at 28)
            IntConst: 0 (at 28)
      Ioport:  (at 31)
        Input: VAL, False (at 31)
      Ioport:  (at 32)
        Output: LED, False (at 32)
      Assign:  (at 34)
        Lvalue:  (at 34)
          Identifier: LED (at 34)
        Rvalue:  (at 34)
          And:  (at 34)
            Unot:  (at 34)
              Identifier: VAL (at 34)
            Identifier: MODE (at 34)
"""


def test():
    filelist = [codedir + 'instance_array.v']
    output = 'preprocess.out'
    include = None
    define = None

    parser = VerilogCodeParser(filelist,
                               preprocess_include=include,
                               preprocess_define=define)
    ast = parser.parse()
    directives = parser.get_directives()

    output = StringIO()
    ast.show(buf=output)

    for lineno, directive in directives:
        output.write('Line %d : %s' % (lineno, directive))

    rslt = output.getvalue()

    print(rslt)
    assert(expected == rslt)


if __name__ == '__main__':
    test()
