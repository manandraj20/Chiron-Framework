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


    # Visit a parse tree produced by tlangParser#statement_list.
    def visitStatement_list(self, ctx:tlangParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#declaration_list.
    def visitDeclaration_list(self, ctx:tlangParser.Declaration_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#strict_ilist.
    def visitStrict_ilist(self, ctx:tlangParser.Strict_ilistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#declaration.
    def visitDeclaration(self, ctx:tlangParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#instruction.
    def visitInstruction(self, ctx:tlangParser.InstructionContext):
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


    # Visit a parse tree produced by tlangParser#array.
    def visitArray(self, ctx:tlangParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#assignment.
    def visitAssignment(self, ctx:tlangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#printStatement.
    def visitPrintStatement(self, ctx:tlangParser.PrintStatementContext):
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


    # Visit a parse tree produced by tlangParser#returnStatement.
    def visitReturnStatement(self, ctx:tlangParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#binExpr.
    def visitBinExpr(self, ctx:tlangParser.BinExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#unaryExpr.
    def visitUnaryExpr(self, ctx:tlangParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#valueExpr.
    def visitValueExpr(self, ctx:tlangParser.ValueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#notExpr.
    def visitNotExpr(self, ctx:tlangParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#addExpr.
    def visitAddExpr(self, ctx:tlangParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#mulExpr.
    def visitMulExpr(self, ctx:tlangParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#penExpr.
    def visitPenExpr(self, ctx:tlangParser.PenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#assignExpr.
    def visitAssignExpr(self, ctx:tlangParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#parenExpr.
    def visitParenExpr(self, ctx:tlangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#logExpr.
    def visitLogExpr(self, ctx:tlangParser.LogExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#classDeclaration.
    def visitClassDeclaration(self, ctx:tlangParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#classBody.
    def visitClassBody(self, ctx:tlangParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#classAttributeDeclaration.
    def visitClassAttributeDeclaration(self, ctx:tlangParser.ClassAttributeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#objectInstantiation.
    def visitObjectInstantiation(self, ctx:tlangParser.ObjectInstantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#dataLocationAccess.
    def visitDataLocationAccess(self, ctx:tlangParser.DataLocationAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#baseVar.
    def visitBaseVar(self, ctx:tlangParser.BaseVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#lvalue.
    def visitLvalue(self, ctx:tlangParser.LvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#functionCall.
    def visitFunctionCall(self, ctx:tlangParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#methodCaller.
    def visitMethodCaller(self, ctx:tlangParser.MethodCallerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:tlangParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#parameters.
    def visitParameters(self, ctx:tlangParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#arguments.
    def visitArguments(self, ctx:tlangParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#comment.
    def visitComment(self, ctx:tlangParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#logicOp.
    def visitLogicOp(self, ctx:tlangParser.LogicOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#binCondOp.
    def visitBinCondOp(self, ctx:tlangParser.BinCondOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#value.
    def visitValue(self, ctx:tlangParser.ValueContext):
        return self.visitChildren(ctx)



del tlangParser