# Generated from tlang.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tlangParser import tlangParser
else:
    from tlangParser import tlangParser

# This class defines a complete generic visitor for a parse tree produced by tlangParser.

class tlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by tlangParser#start.
    def visitStart(self, ctx:tlangParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#instruction_list.
    def visitInstruction_list(self, ctx:tlangParser.Instruction_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#strict_ilist.
    def visitStrict_ilist(self, ctx:tlangParser.Strict_ilistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#instruction.
    def visitInstruction(self, ctx:tlangParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#struct_definition.
    def visitStruct_definition(self, ctx:tlangParser.Struct_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#declaration_list.
    def visitDeclaration_list(self, ctx:tlangParser.Declaration_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#declaration.
    def visitDeclaration(self, ctx:tlangParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#assignment_list.
    def visitAssignment_list(self, ctx:tlangParser.Assignment_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#array_declaration.
    def visitArray_declaration(self, ctx:tlangParser.Array_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#variable_declaration.
    def visitVariable_declaration(self, ctx:tlangParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#data_type.
    def visitData_type(self, ctx:tlangParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#custom.
    def visitCustom(self, ctx:tlangParser.CustomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#conditional.
    def visitConditional(self, ctx:tlangParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#ifConditional.
    def visitIfConditional(self, ctx:tlangParser.IfConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#ifElseConditional.
    def visitIfElseConditional(self, ctx:tlangParser.IfElseConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#loop.
    def visitLoop(self, ctx:tlangParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#gotoCommand.
    def visitGotoCommand(self, ctx:tlangParser.GotoCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#assignment.
    def visitAssignment(self, ctx:tlangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#varAssignment.
    def visitVarAssignment(self, ctx:tlangParser.VarAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#memberAssignment.
    def visitMemberAssignment(self, ctx:tlangParser.MemberAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#arrayMemberAssignment.
    def visitArrayMemberAssignment(self, ctx:tlangParser.ArrayMemberAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#arrayAssignment.
    def visitArrayAssignment(self, ctx:tlangParser.ArrayAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#moveCommand.
    def visitMoveCommand(self, ctx:tlangParser.MoveCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#moveOp.
    def visitMoveOp(self, ctx:tlangParser.MoveOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#penCommand.
    def visitPenCommand(self, ctx:tlangParser.PenCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#pauseCommand.
    def visitPauseCommand(self, ctx:tlangParser.PauseCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#unaryExpr.
    def visitUnaryExpr(self, ctx:tlangParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#valueExpr.
    def visitValueExpr(self, ctx:tlangParser.ValueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#addExpr.
    def visitAddExpr(self, ctx:tlangParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#mulExpr.
    def visitMulExpr(self, ctx:tlangParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#parenExpr.
    def visitParenExpr(self, ctx:tlangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#multiplicative.
    def visitMultiplicative(self, ctx:tlangParser.MultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#additive.
    def visitAdditive(self, ctx:tlangParser.AdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#unaryArithOp.
    def visitUnaryArithOp(self, ctx:tlangParser.UnaryArithOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#condition.
    def visitCondition(self, ctx:tlangParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#binCondOp.
    def visitBinCondOp(self, ctx:tlangParser.BinCondOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#logicOp.
    def visitLogicOp(self, ctx:tlangParser.LogicOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#value.
    def visitValue(self, ctx:tlangParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#member.
    def visitMember(self, ctx:tlangParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#array_member.
    def visitArray_member(self, ctx:tlangParser.Array_memberContext):
        return self.visitChildren(ctx)



del tlangParser