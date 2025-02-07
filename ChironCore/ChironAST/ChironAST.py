#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Abstract syntax tree for ChironLang

class AST(object):
    pass


# --Instruction Classes-----------------------------------------------

class Instruction(AST):
    pass

# --Assignment Classes-----------------------------------------------


class AssignmentCommand(Instruction):
    pass


class VarAssignmentCommand(AssignmentCommand):
    def __init__(self, leftvar, rexpr):
        self.lvar = leftvar
        self.rexpr = rexpr

    def __str__(self):
        return self.lvar.__str__() + " = " + self.rexpr.__str__()


class MemberAssignmentCommand(AssignmentCommand):
    def __init__(self, member, expr):
        self.member = member
        self.expr = expr

    def __str__(self):
        return self.member.__str__() + " = " + self.expr.__str__()

class ArrayMemberAssignmentCommand(AssignmentCommand):
    def __init__(self, arrayMember, rexpr):
        self.lvar = arrayMember
        self.rexpr = rexpr

    def __str__(self):
        return self.lvar.__str__() + " = " + self.rexpr.__str__()


class ArrayAssignmentCommand(AssignmentCommand):
    def __init__(self, lvar, expr_list):
        self.lvar = lvar
        self.rexpr = expr_list

    def __str__(self):
        return self.lvar.__str__() + " = " + self.rexpr.__str__()


class Custom(Instruction):
    def __init__(self, var):
        self.var = var

    def __str__(self):
        return "struct " + self.var.__str__()


class Data_type(Instruction):
    def __init__(self, dtype):
        self.dtype = dtype

    def __str__(self):
        return self.dtype.__str__()


class VarDeclarationCommand(Instruction):
    def __init__(self, dtype, var):
        self.var = var
        self.dtype = dtype

    def __str__(self):
        return self.dtype.__str__() + " " + self.var.__str__()


class Array_declarationCommand(Instruction):
    def __init__(self, dtype, var, sizeExpr):
        self.var = var
        self.dtype = dtype
        self.size = sizeExpr

    def __str__(self):
        return self.dtype.__str__() + " " + self.var.__str__() + "[" + self.size.__str__() + "]"


class ConditionCommand(Instruction):
    def __init__(self, condition):
        self.cond = condition

    def __str__(self):
        return self.cond.__str__()

# Not Implemented Yet.


class AssertCommand(Instruction):
    def __init__(self, condition):
        self.cond = condition

    def __str__(self):
        return self.cond.__str__()


class MoveCommand(Instruction):
    def __init__(self, motion, expr):
        self.direction = motion
        self.expr = expr

    def __str__(self):
        return self.direction + " " + self.expr.__str__()


class PenCommand(Instruction):
    def __init__(self, penstat):
        self.status = penstat

    def __str__(self):
        return self.status


class GotoCommand(Instruction):
    def __init__(self, x, y):
        self.xcor = x
        self.ycor = y

    def __str__(self):
        return "goto " + str(self.xcor) + " " + str(self.ycor)


class NoOpCommand(Instruction):
    def __init__(self):
        pass

    def __str__(self):
        return "NOP"


class PauseCommand(Instruction):
    def __init__(self):
        pass

    def __str__(self):
        return "pause"


class Expression(AST):
    pass


# --Arithmetic Expressions--------------------------------------------

class ArithExpr(Expression):
    pass


class BinArithOp(ArithExpr):
    def __init__(self, expr1, expr2, opsymbol):
        self.lexpr = expr1
        self.rexpr = expr2
        self.symbol = opsymbol

    def __str__(self):
        return "(" + self.lexpr.__str__() + " " + self.symbol + " " + self.rexpr.__str__() + ")"


class UnaryArithOp(ArithExpr):
    def __init__(self, expr1, opsymbol):
        self.expr = expr1
        self.symbol = opsymbol

    def __str__(self):
        return self.symbol + self.expr.__str__()


class UMinus(UnaryArithOp):
    def __init__(self, lexpr):
        super().__init__(lexpr, "-")


class Sum(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "+")


class Diff(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "-")


class Mult(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "*")


class Div(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "/")


class ExpressionList(AST):
    def __init__(self, expr_list):
        self.expr_list = expr_list

    def __str__(self):
        return "[" + ', '.join([str(x) for x in self.expr_list]) + "]"
    
# --Boolean Expressions-----------------------------------------------

class BoolExpr(Expression):
    pass


class BinCondOp(BoolExpr):
    def __init__(self, expr1, expr2, opsymbol):
        self.lexpr = expr1
        self.rexpr = expr2
        self.symbol = opsymbol

    def __str__(self):
        return "(" + self.lexpr.__str__() + ' ' + self.symbol + ' ' + self.rexpr.__str__() + ")"


class AND(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "and")


class OR(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "or")


class LT(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "<")


class GT(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, ">")


class LTE(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "<=")


class GTE(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, ">=")


class EQ(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "==")


class NEQ(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "!=")


class NOT(BoolExpr):
    def __init__(self, uexpr):
        self.expr = uexpr
        self.symbol = "not"

    def __str__(self):
        return self.symbol + self.expr.__str__()


class PenStatus(BoolExpr):
    def __init__(self):
        pass

    def __str__(self):
        return "pendown?"


class BoolTrue(BoolExpr):
    def __init__(self):
        pass

    def __str__(self):
        return "True"


class BoolFalse(BoolExpr):
    def __init__(self):
        pass

    def __str__(self):
        return "False"


class Value(Expression):
    pass


class ArrayMember(Value):
    def __init__(self, var, index):
        self.var = var
        self.idx = index

    def __str__(self):
        return self.var.__str__() + "[" + self.idx.__str__() + "]"


class Num(Value):
    def __init__(self, v):
        self.val = int(v)

    def __str__(self):
        return str(self.val)


class Var(Value):
    def __init__(self, vname):
        self.varname = vname

    def __str__(self):
        return self.varname
